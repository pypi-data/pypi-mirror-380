import asyncio
import logging
from typing import TYPE_CHECKING, Callable, Dict, List

if TYPE_CHECKING:
    from .worker_pool import JobExecution

logger = logging.getLogger(__name__)


class JobErrorReporter:

    def __init__(self):
        self._error_handlers: List[Callable] = []

    def add_error_handler(self, handler: Callable):
        self._error_handlers.append(handler)

    async def report_error(self, execution: 'JobExecution', error: Exception, context: Dict = None):
        error_info = {
            "job_id": execution.job_id,
            "job_class": execution.job_class_name,
            "worker_id": execution.worker_id,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "retry_count": execution.retry_count,
            "execution_time": execution.get_execution_time(),
            "context": context or {}
        }

        for handler in self._error_handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(error_info)
                else:
                    handler(error_info)
            except Exception as e:
                logger.error(f"Error handler failed: {e}")
