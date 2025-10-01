"""Unit tests for NatsWorkServer."""

import pytest

from natswork_server.server import NatsWorkServer


class TestNatsWorkServer:
    """Test cases for NatsWorkServer."""

    def test_server_init_defaults(self):
        """Test server initialization with defaults."""
        server = NatsWorkServer()

        assert server.queues == ["default"]
        assert server.concurrency == 10
        assert server.nats_url == "nats://localhost:4222"

    def test_server_init_custom(self):
        """Test server initialization with custom values."""
        server = NatsWorkServer(
            queues=["queue1", "queue2"],
            concurrency=20,
            nats_url="nats://example.com:4222"
        )

        assert server.queues == ["queue1", "queue2"]
        assert server.concurrency == 20
        assert server.nats_url == "nats://example.com:4222"

    @pytest.mark.asyncio
    async def test_start_stop(self):
        """Test server start and stop."""
        server = NatsWorkServer(nats_url="nats://localhost:4222")

        await server.start()
        assert server._running is True
        assert server._connection_manager is not None

        await server.stop()
        assert server._running is False
