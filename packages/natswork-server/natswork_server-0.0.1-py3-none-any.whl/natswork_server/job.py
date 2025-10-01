"""NatsWork server-side job extensions."""

from natswork_client.job import (
    Job,
    JobConfig,
    JobContext,
    JobDiscovery,
    JobRegistry,
    QueueConfig,
    QueueManager,
    job,
)

# Re-export all job-related components for server
__all__ = [
    "Job",
    "JobConfig",
    "JobContext",
    "JobDiscovery",
    "JobRegistry",
    "QueueConfig",
    "QueueManager",
    "job",
    "get_job_class",
    "_job_registry",
]

# Backward compatibility
_job_registry = JobRegistry._jobs

def get_job_class(name: str):
    """Get job class by name (backward compatibility).

    Args:
        name: Job class name (can be short or fully qualified)

    Returns:
        Job class or None
    """
    # Try exact match first
    job_class = JobRegistry.get_job_class(name)
    if job_class:
        return job_class

    # Try short name match
    for full_name, cls in JobRegistry._jobs.items():
        if full_name.endswith(f".{name}"):
            return cls

    return None
