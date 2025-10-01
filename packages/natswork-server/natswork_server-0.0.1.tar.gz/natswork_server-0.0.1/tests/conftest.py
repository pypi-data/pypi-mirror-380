"""Pytest configuration and fixtures for natswork-server tests."""

import asyncio

import pytest

# Pytest configuration
pytest_plugins = ["pytest_asyncio"]


@pytest.fixture(scope="session")
def event_loop():
    """Create an event loop for the test session."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def nats_url() -> str:
    """NATS server URL for testing."""
    return "nats://localhost:4222"


@pytest.fixture
def sample_job():
    """Sample job class for testing."""
    from natswork_server.job import job

    @job(queue="test", retries=2, timeout=10)
    class TestJob:
        def perform(self, x, y):
            return x + y

    return TestJob
