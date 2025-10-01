import logging
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from .job import Job, JobConfig
    from .metrics import MetricsCollector
    from .worker_pool import JobExecution

logger = logging.getLogger(__name__)


class JobMiddleware:

    async def before_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig'):
        pass

    async def after_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', result: Any):
        pass

    async def on_error(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', error: Exception):
        pass

    def wrap(self, next_executor: Callable, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig'):
        async def wrapper():
            try:
                await self.before_execute(job_instance, execution, config)
                result = await next_executor()
                await self.after_execute(job_instance, execution, config, result)
                return result
            except Exception as e:
                await self.on_error(job_instance, execution, config, e)
                raise

        return wrapper


class LoggingMiddleware(JobMiddleware):

    async def before_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig'):
        logger.info(
            "Starting job execution",
            extra={
                "job_id": execution.job_id,
                "job_class": execution.job_class_name,
                "worker_id": execution.worker_id,
                "queue": execution.job_message.queue,
                "retry_count": execution.retry_count
            }
        )

    async def after_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', result: Any):
        logger.info(
            "Job execution completed",
            extra={
                "job_id": execution.job_id,
                "execution_time": execution.get_execution_time(),
                "result_type": type(result).__name__
            }
        )

    async def on_error(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', error: Exception):
        logger.error(
            "Job execution failed",
            extra={
                "job_id": execution.job_id,
                "error_type": type(error).__name__,
                "error_message": str(error),
                "execution_time": execution.get_execution_time()
            },
            exc_info=True
        )


class MetricsMiddleware(JobMiddleware):

    def __init__(self, metrics_collector: 'MetricsCollector'):
        self.metrics = metrics_collector

    async def before_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig'):
        self.metrics.increment_counter("jobs.started", {
            "job_class": execution.job_class_name,
            "queue": execution.job_message.queue
        })

    async def after_execute(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', result: Any):
        self.metrics.increment_counter("jobs.completed", {
            "job_class": execution.job_class_name,
            "queue": execution.job_message.queue
        })

        self.metrics.record_histogram("jobs.execution_time",
            execution.get_execution_time(), {
                "job_class": execution.job_class_name,
                "queue": execution.job_message.queue
            }
        )

    async def on_error(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', error: Exception):
        self.metrics.increment_counter("jobs.failed", {
            "job_class": execution.job_class_name,
            "queue": execution.job_message.queue,
            "error_type": type(error).__name__
        })


class RetryMiddleware(JobMiddleware):

    async def on_error(self, job_instance: 'Job', execution: 'JobExecution', config: 'JobConfig', error: Exception):
        should_retry = (
            execution.retry_count < config.retries and
            job_instance.should_retry(error, execution.retry_count)
        )

        if should_retry:
            if hasattr(job_instance, 'context') and job_instance.context:
                job_instance.context.add_metadata("last_error", str(error))
                job_instance.context.add_metadata("retry_scheduled", True)

            logger.info(
                f"Job {execution.job_id} will be retried (attempt {execution.retry_count + 1}/{config.retries})"
            )
        else:
            logger.error(
                f"Job {execution.job_id} failed permanently after {execution.retry_count} retries"
            )
