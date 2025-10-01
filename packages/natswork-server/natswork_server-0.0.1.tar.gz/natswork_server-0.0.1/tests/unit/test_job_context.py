from datetime import datetime, timedelta, timezone

from natswork_server.job_context import JobContext


def test_job_context_initialization():
    now = datetime.now(timezone.utc)
    context = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=now,
        started_at=now
    )

    assert context.job_id == "test-123"
    assert context.worker_id == "worker-1"
    assert context.queue == "default"
    assert context.retry_count == 0
    assert context.metadata == {}


def test_add_metadata():
    context = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=datetime.now(timezone.utc),
        started_at=datetime.now(timezone.utc)
    )

    context.add_metadata("key1", "value1")
    context.add_metadata("key2", 42)

    assert context.metadata["key1"] == "value1"
    assert context.metadata["key2"] == 42


def test_get_metadata():
    context = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=datetime.now(timezone.utc),
        started_at=datetime.now(timezone.utc)
    )

    context.add_metadata("test_key", "test_value")

    assert context.get_metadata("test_key") == "test_value"
    assert context.get_metadata("missing_key") is None
    assert context.get_metadata("missing_key", "default") == "default"


def test_get_execution_time():
    past = datetime.now(timezone.utc) - timedelta(seconds=5)
    context = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=past,
        started_at=past
    )

    execution_time = context.get_execution_time()
    assert execution_time >= 5.0
    assert execution_time < 6.0


def test_is_retry():
    context_first = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=0,
        created_at=datetime.now(timezone.utc),
        started_at=datetime.now(timezone.utc)
    )

    context_retry = JobContext(
        job_id="test-123",
        worker_id="worker-1",
        queue="default",
        retry_count=2,
        created_at=datetime.now(timezone.utc),
        started_at=datetime.now(timezone.utc)
    )

    assert not context_first.is_retry()
    assert context_retry.is_retry()
