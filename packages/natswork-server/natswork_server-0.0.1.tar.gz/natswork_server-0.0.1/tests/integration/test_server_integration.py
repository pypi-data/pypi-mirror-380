"""Integration tests for NatsWorkServer."""

import pytest

from natswork_server.server import NatsWorkServer
from natswork_server.worker import Worker


@pytest.mark.integration
class TestNatsWorkServerIntegration:
    """Integration test cases for NatsWorkServer."""

    @pytest.mark.asyncio
    async def test_server_startup(self, nats_url):
        """Test server can start up."""
        server = NatsWorkServer(queues=["test"], nats_url=nats_url)

        await server.start()
        assert server._running is True
        assert server._connection_manager is not None
        assert server._connection_manager._connected is True

        await server.stop()
        assert server._running is False

    @pytest.mark.asyncio
    async def test_job_processing(self, nats_url, sample_job):
        """Test server can process jobs."""
        from natswork_server.job import Job, JobRegistry, job
        from natswork_server.messages import MessageBuilder
        from natswork_server.worker import Worker

        @job(queue="test", retries=3, timeout=60)
        class TestProcessJob(Job):
            async def perform(self, value):
                return f"processed_{value}"

        worker = Worker(queues=["test"], nats_url=nats_url)
        await worker.start()

        job_message = MessageBuilder.build_job_message(
            job_class="test_server_integration.TestProcessJob",
            queue="test",
            arguments={"value": "test123"}
        )

        result = await worker.process_job(job_message)

        assert result["status"] == "success"
        assert result["result"] == "processed_test123"
        assert result["job_id"] == job_message.job_id

        await worker.stop()

        JobRegistry.clear()

    @pytest.mark.asyncio
    async def test_worker_management(self, nats_url):
        """Test worker management."""
        worker = Worker(queues=["test", "other"], concurrency=5, nats_url=nats_url)

        await worker.start()
        assert worker._running is True
        assert worker._connection_manager is not None
        assert len(worker.queues) == 2

        await worker.stop()
        assert worker._running is False
