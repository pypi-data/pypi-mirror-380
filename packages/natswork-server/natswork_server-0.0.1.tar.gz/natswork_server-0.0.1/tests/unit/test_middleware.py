import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest

from natswork_server.job import Job, JobConfig
from natswork_server.messages import JobMessage
from natswork_server.middleware import JobMiddleware, LoggingMiddleware, RetryMiddleware
from natswork_server.worker_pool import JobExecution


class SampleJob(Job):
    async def perform(self, *args, **kwargs):
        return "success"

    def should_retry(self, exception, attempt_number):
        return True


@pytest.fixture
def job_instance():
    job_id = str(uuid.uuid4())
    return SampleJob(job_id=job_id, arguments={})


@pytest.fixture
def job_config():
    return JobConfig(queue="default", retries=3, timeout=30)


@pytest.fixture
def job_execution(job_instance):
    job_message = JobMessage(
        job_id=job_instance.job_id,
        job_class="SampleJob",
        arguments={},
        queue="default",
        created_at=datetime.now(timezone.utc)
    )
    return JobExecution(
        job_message=job_message,
        worker_id="worker-1",
        nats_msg=MagicMock()
    )


@pytest.mark.asyncio
async def test_middleware_before_execute(job_instance, job_execution, job_config):
    middleware = JobMiddleware()
    called = False

    original_before = middleware.before_execute
    async def track_call(*args, **kwargs):
        nonlocal called
        called = True
        await original_before(*args, **kwargs)

    middleware.before_execute = track_call

    async def next_executor():
        return "result"

    wrapper = middleware.wrap(next_executor, job_instance, job_execution, job_config)
    result = await wrapper()

    assert called
    assert result == "result"


@pytest.mark.asyncio
async def test_middleware_after_execute(job_instance, job_execution, job_config):
    middleware = JobMiddleware()
    called = False

    original_after = middleware.after_execute
    async def track_call(*args, **kwargs):
        nonlocal called
        called = True
        await original_after(*args, **kwargs)

    middleware.after_execute = track_call

    async def next_executor():
        return "result"

    wrapper = middleware.wrap(next_executor, job_instance, job_execution, job_config)
    result = await wrapper()

    assert called
    assert result == "result"


@pytest.mark.asyncio
async def test_middleware_on_error(job_instance, job_execution, job_config):
    middleware = JobMiddleware()
    error_called = False

    original_error = middleware.on_error
    async def track_call(*args, **kwargs):
        nonlocal error_called
        error_called = True
        await original_error(*args, **kwargs)

    middleware.on_error = track_call

    async def failing_executor():
        raise ValueError("test error")

    wrapper = middleware.wrap(failing_executor, job_instance, job_execution, job_config)

    with pytest.raises(ValueError):
        await wrapper()

    assert error_called


@pytest.mark.asyncio
async def test_logging_middleware(job_instance, job_execution, job_config, caplog):
    middleware = LoggingMiddleware()

    async def next_executor():
        return "success"

    wrapper = middleware.wrap(next_executor, job_instance, job_execution, job_config)
    result = await wrapper()

    assert result == "success"


@pytest.mark.asyncio
async def test_retry_middleware(job_instance, job_execution, job_config):
    from natswork_server.job_context import JobContext

    job_instance.context = JobContext(
        job_id=job_instance.job_id,
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=datetime.now(timezone.utc),
        started_at=datetime.now(timezone.utc)
    )

    middleware = RetryMiddleware()

    async def failing_executor():
        raise ValueError("test error")

    wrapper = middleware.wrap(failing_executor, job_instance, job_execution, job_config)

    with pytest.raises(ValueError):
        await wrapper()

    assert job_instance.context.get_metadata("retry_scheduled") is True
    assert job_instance.context.get_metadata("last_error") == "test error"
