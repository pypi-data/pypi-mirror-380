"""Job execution engine for NatsWork."""

import asyncio
import logging
import time
from typing import Callable, Dict, List, Type

from .argument_serializer import ArgumentSerializer
from .error_reporter import JobErrorReporter
from .exceptions import JobExecutionError, JobInstantiationError, JobTimeoutError
from .job import Job, JobConfig, JobRegistry
from .job_context import JobContext
from .middleware import JobMiddleware
from .timeout_handler import TimeoutHandler
from .worker_pool import JobExecution, JobResult

logger = logging.getLogger(__name__)


class JobExecutor:
    """Executes jobs with timeout and error handling"""

    def __init__(self):
        self._middleware_stack: List[JobMiddleware] = []
        self._timeout_handler = TimeoutHandler()
        self._error_reporter = JobErrorReporter()

    def add_middleware(self, middleware: JobMiddleware):
        self._middleware_stack.append(middleware)

    def add_error_handler(self, handler: Callable):
        self._error_reporter.add_error_handler(handler)

    async def execute_job(self, execution: JobExecution) -> JobResult:
        """Execute a job with timeout handling"""
        start_time = time.time()

        try:
            job_class = JobRegistry.get_job_class(execution.job_class_name)

            if not job_class:
                raise JobExecutionError(f"Job class not found: {execution.job_class_name}")

            job_config = JobRegistry.get_job_config(execution.job_class_name)

            job_instance = await self._create_job_instance(execution, job_class)

            result = await self._execute_with_middleware(job_instance, execution, job_config)

            execution_time = time.time() - start_time
            return JobResult.success(result, execution_time)

        except asyncio.TimeoutError:
            execution_time = time.time() - start_time
            error = JobTimeoutError(f"Job timed out after {execution_time:.2f}s")
            await self._error_reporter.report_error(execution, error)
            return JobResult.from_error(error, execution_time)

        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"Job {execution.job_id} failed: {e}", exc_info=True)
            await self._error_reporter.report_error(execution, e)
            return JobResult.from_error(e, execution_time)

    async def _create_job_instance(self, execution: JobExecution, job_class: Type[Job]) -> Job:
        try:
            args, kwargs = ArgumentSerializer.deserialize(execution.job_message.arguments)

            job_instance = job_class(
                job_id=execution.job_id,
                arguments=execution.job_message.arguments
            )

            job_instance.context = JobContext(
                job_id=execution.job_id,
                worker_id=execution.worker_id,
                queue=execution.job_message.queue,
                retry_count=execution.retry_count,
                created_at=execution.job_message.created_at,
                started_at=execution.started_at
            )

            return job_instance

        except Exception as e:
            raise JobInstantiationError(f"Failed to create job instance: {e}")

    async def _execute_with_middleware(self, job_instance: Job, execution: JobExecution, config: JobConfig):
        middleware_chain = self._build_middleware_chain(job_instance, execution, config)
        return await middleware_chain()

    def _build_middleware_chain(self, job_instance: Job, execution: JobExecution, config: JobConfig):
        async def final_executor():
            return await self._execute_job_method(job_instance, execution, config)

        executor = final_executor
        for middleware in reversed(self._middleware_stack):
            executor = middleware.wrap(executor, job_instance, execution, config)

        return executor

    async def _execute_job_method(self, job_instance: Job, execution: JobExecution, config: JobConfig):
        # Always pass arguments as a dict (matches Ruby's hash interface)
        args_dict = self._ensure_dict_arguments(execution.job_message.arguments)

        try:
            await self._call_hook(job_instance.before_perform)
        except Exception as e:
            logger.warning(f"before_perform hook failed: {e}")

        try:
            result = await asyncio.wait_for(
                self._call_perform_method(job_instance, args_dict),
                timeout=config.timeout
            )

            try:
                await self._call_hook(job_instance.after_perform, result)
            except Exception as e:
                logger.warning(f"after_perform hook failed: {e}")

            return result

        except Exception as e:
            try:
                await self._call_hook(job_instance.on_failure, e)
            except Exception as hook_error:
                logger.warning(f"on_failure hook failed: {hook_error}")

            raise e

    def _ensure_dict_arguments(self, arguments):
        """Ensure arguments are always a dict for consistency with Ruby"""
        if isinstance(arguments, dict):
            return arguments
        elif isinstance(arguments, list):
            # Convert list to dict with numeric keys for backward compatibility
            return {str(i): v for i, v in enumerate(arguments)}
        else:
            # Single value
            return {"value": arguments}

    async def _call_perform_method(self, job_instance: Job, args_dict: Dict):
        perform_method = job_instance.perform

        if asyncio.iscoroutinefunction(perform_method):
            return await perform_method(args_dict)
        else:
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, lambda: perform_method(args_dict))

    async def _call_hook(self, hook_method, *args):
        if asyncio.iscoroutinefunction(hook_method):
            await hook_method(*args)
        else:
            hook_method(*args)
