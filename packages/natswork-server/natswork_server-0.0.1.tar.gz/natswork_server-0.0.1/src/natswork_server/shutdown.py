"""Graceful shutdown handling for NatsWork."""

import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .worker_pool import WorkerPoolManager

logger = logging.getLogger(__name__)


class GracefulShutdownHandler:
    """Handles graceful shutdown of worker system"""

    def __init__(self, worker_pool_manager: 'WorkerPoolManager'):
        self.worker_pool_manager = worker_pool_manager
        self._shutdown_initiated = False
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    def setup_signal_handlers(self, loop: asyncio.AbstractEventLoop):
        """Setup signal handlers for graceful shutdown"""
        self._loop = loop

        for sig in [signal.SIGTERM, signal.SIGINT]:
            try:
                loop.add_signal_handler(sig, lambda s=sig: self._signal_handler(s))
            except NotImplementedError:
                signal.signal(sig, lambda signum, frame: self._sync_signal_handler(signum))

    def _signal_handler(self, signum):
        """Handle shutdown signal (async loop version)"""
        if self._shutdown_initiated:
            logger.warning("Shutdown already initiated, ignoring signal")
            return

        self._shutdown_initiated = True
        logger.info(f"Received signal {signum}, initiating graceful shutdown...")

        if self._loop:
            self._loop.create_task(self._async_shutdown())

    def _sync_signal_handler(self, signum):
        """Handle shutdown signal (sync version for Windows)"""
        if self._shutdown_initiated:
            logger.warning("Shutdown already initiated, ignoring signal")
            return

        self._shutdown_initiated = True
        logger.info(f"Received signal {signum}, initiating graceful shutdown...")

        if self._loop and self._loop.is_running():
            self._loop.create_task(self._async_shutdown())

    async def _async_shutdown(self):
        """Perform async shutdown operations"""
        try:
            await asyncio.wait_for(
                self.worker_pool_manager.shutdown(),
                timeout=60
            )
            logger.info("Graceful shutdown completed")
        except asyncio.TimeoutError:
            logger.error("Shutdown timeout, forcing exit")
        finally:
            if self._loop and self._loop.is_running():
                self._loop.stop()
