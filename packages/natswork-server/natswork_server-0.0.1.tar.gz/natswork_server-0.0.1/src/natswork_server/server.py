"""NatsWork server implementation."""

import asyncio
import logging
from typing import List

from .nats_client import NatsConnectionManager
from .shutdown import GracefulShutdownHandler
from .worker_pool import WorkerPoolManager

logger = logging.getLogger(__name__)


class NatsWorkServer:
    """NatsWork server for managing workers."""

    def __init__(
        self,
        queues: List[str] = None,
        concurrency: int = 10,
        nats_url: str = "nats://localhost:4222"
    ):
        """Initialize server.

        Args:
            queues: List of queue names to process
            concurrency: Number of concurrent jobs
            nats_url: NATS server URL
        """
        self.queues = queues or ["default"]
        self.concurrency = concurrency
        self.nats_url = nats_url
        self._connection_manager = None
        self._worker_pool_manager = None
        self._shutdown_handler = None
        self._running = False

    async def start(self) -> None:
        """Start the server."""
        if self._running:
            return

        self._connection_manager = NatsConnectionManager(servers=[self.nats_url])
        await self._connection_manager.connect()

        self._worker_pool_manager = WorkerPoolManager(self._connection_manager)

        for queue in self.queues:
            await self._worker_pool_manager.start_pool(queue, self.concurrency)

        self._shutdown_handler = GracefulShutdownHandler(self._worker_pool_manager)
        self._shutdown_handler.setup_signal_handlers(asyncio.get_event_loop())

        self._running = True

        logger.info(f"NatsWorkServer started for queues: {self.queues}")

    async def stop(self) -> None:
        """Stop the server."""
        if not self._running:
            return

        if self._worker_pool_manager:
            await self._worker_pool_manager.shutdown()

        if self._connection_manager:
            await self._connection_manager.disconnect()

        self._running = False
        logger.info("NatsWorkServer stopped")

    def get_stats(self):
        """Get server statistics"""
        if self._worker_pool_manager:
            return self._worker_pool_manager.get_stats()
        return {}
