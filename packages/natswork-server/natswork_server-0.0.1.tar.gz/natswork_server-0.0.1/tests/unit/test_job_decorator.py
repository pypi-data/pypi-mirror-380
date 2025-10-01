"""Unit tests for job decorator and registry."""

from natswork_server.job import Job, JobRegistry, _job_registry, get_job_class, job


class TestJobDecorator:
    """Test cases for job decorator."""

    def setup_method(self):
        """Clear job registry before each test."""
        JobRegistry.clear()

    def test_job_decorator_default_values(self):
        """Test job decorator with default values."""
        @job()
        class DefaultJob(Job):
            def perform(self):
                return "done"

        assert DefaultJob.queue == "default"
        assert DefaultJob.retries == 3
        assert DefaultJob.timeout == 300
        job_name = f"{DefaultJob.__module__}.DefaultJob"
        assert job_name in _job_registry
        assert _job_registry[job_name] is DefaultJob

    def test_job_decorator_custom_values(self):
        """Test job decorator with custom values."""
        @job(queue="custom", retries=5, timeout=60)
        class CustomJob(Job):
            def perform(self):
                return "custom"

        assert CustomJob.queue == "custom"
        assert CustomJob.retries == 5
        assert CustomJob.timeout == 60
        job_name = f"{CustomJob.__module__}.CustomJob"
        assert job_name in _job_registry

    def test_job_registry_lookup(self):
        """Test job registry lookup."""
        @job(queue="test")
        class RegistryJob(Job):
            def perform(self):
                return "registry"

        # Test successful lookup with short name
        found_class = get_job_class("RegistryJob")
        assert found_class is RegistryJob

        # Test successful lookup with full name
        full_name = f"{RegistryJob.__module__}.RegistryJob"
        found_class2 = get_job_class(full_name)
        assert found_class2 is RegistryJob

        # Test missing lookup
        missing_class = get_job_class("MissingJob")
        assert missing_class is None

    def test_multiple_jobs_registration(self):
        """Test multiple jobs can be registered."""
        @job(queue="queue1")
        class Job1(Job):
            def perform(self):
                return "job1"

        @job(queue="queue2")
        class Job2(Job):
            def perform(self):
                return "job2"

        assert get_job_class("Job1") is Job1
        assert get_job_class("Job2") is Job2
        assert len(_job_registry) == 2
