"""NatsWork worker implementation."""

import asyncio
import logging
import time
from typing import List

from .job import JobRegistry
from .messages import JobMessage, MessageBuilder
from .nats_client import JetStreamClient, NatsConnectionManager, StreamManager
from .shutdown import GracefulShutdownHandler
from .worker_pool import WorkerPoolManager

logger = logging.getLogger(__name__)


class Worker:
    """NatsWork worker for processing jobs."""

    def __init__(
        self,
        queues: List[str] = None,
        concurrency: int = 10,
        nats_url: str = "nats://localhost:4222"
    ):
        """Initialize worker.

        Args:
            queues: List of queue names to process
            concurrency: Number of concurrent jobs
            nats_url: NATS server URL
        """
        self.queues = queues or ["default"]
        self.concurrency = concurrency
        self.nats_url = nats_url
        self._running = False
        self._connection_manager = None
        self._worker_pool_manager = None
        self._shutdown_handler = None
        self._tasks = []

    async def start(self) -> None:
        """Start the worker."""
        if self._running:
            return

        self._connection_manager = NatsConnectionManager(servers=[self.nats_url])
        await self._connection_manager.connect()

        js_client = JetStreamClient(self._connection_manager)
        stream_manager = StreamManager(js_client)

        for queue in self.queues:
            await stream_manager.ensure_job_stream(queue)

        self._worker_pool_manager = WorkerPoolManager(self._connection_manager)

        for queue in self.queues:
            await self._worker_pool_manager.start_pool(queue, self.concurrency)

        self._shutdown_handler = GracefulShutdownHandler(self._worker_pool_manager)
        self._shutdown_handler.setup_signal_handlers(asyncio.get_event_loop())

        self._running = True
        logger.info(f"Worker started for queues: {self.queues}")

    async def stop(self) -> None:
        """Stop the worker."""
        if not self._running:
            return

        self._running = False

        if self._worker_pool_manager:
            await self._worker_pool_manager.shutdown()

        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks.clear()

        if self._connection_manager:
            await self._connection_manager.disconnect()

        logger.info("Worker stopped")

    async def process_job(self, job_message: JobMessage) -> dict:
        """Process a single job.

        Args:
            job_message: Job message to process

        Returns:
            Result dictionary
        """
        job_class = JobRegistry.get_job_class(job_message.job_class)

        if not job_class:
            raise ValueError(f"Unknown job class: {job_message.job_class}")

        job_instance = job_class(
            job_id=job_message.job_id,
            arguments=job_message.arguments
        )

        start_time = time.time()

        try:
            job_instance.before_perform()

            if isinstance(job_message.arguments, dict):
                result = await job_instance.perform(**job_message.arguments)
            else:
                result = await job_instance.perform(*job_message.arguments)

            job_instance.after_perform(result)

            processing_time = time.time() - start_time

            return MessageBuilder.build_result_message(
                job_id=job_message.job_id,
                status="success",
                result=result,
                processing_time=processing_time
            ).model_dump()

        except Exception as e:
            job_instance.on_failure(e)
            processing_time = time.time() - start_time

            return MessageBuilder.build_result_message(
                job_id=job_message.job_id,
                status="error",
                error=e,
                processing_time=processing_time
            ).model_dump()

    def get_stats(self):
        """Get worker statistics"""
        if self._worker_pool_manager:
            return self._worker_pool_manager.get_stats()
        return {}
