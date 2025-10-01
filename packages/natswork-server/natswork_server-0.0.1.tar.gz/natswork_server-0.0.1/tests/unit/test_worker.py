"""Unit tests for Worker."""

import pytest

from natswork_server.worker import Worker


class TestWorker:
    """Test cases for Worker."""

    def test_worker_init_defaults(self):
        """Test worker initialization with defaults."""
        worker = Worker()

        assert worker.queues == ["default"]
        assert worker.concurrency == 10
        assert worker.nats_url == "nats://localhost:4222"
        assert worker._running is False

    def test_worker_init_custom(self):
        """Test worker initialization with custom values."""
        worker = Worker(
            queues=["queue1", "queue2"],
            concurrency=20,
            nats_url="nats://example.com:4222"
        )

        assert worker.queues == ["queue1", "queue2"]
        assert worker.concurrency == 20
        assert worker.nats_url == "nats://example.com:4222"

    @pytest.mark.asyncio
    async def test_start_stop(self):
        """Test worker start and stop."""
        worker = Worker(nats_url="nats://localhost:4222")

        await worker.start()
        assert worker._running is True
        assert worker._connection_manager is not None

        await worker.stop()
        assert worker._running is False
