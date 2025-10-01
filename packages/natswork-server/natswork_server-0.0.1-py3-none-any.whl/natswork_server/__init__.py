"""NatsWork Server - Job processing and worker management for distributed job processing."""

__version__ = "0.1.0"
__author__ = "NatsWork Contributors"
__email__ = "natswork@tesote.com"

from .exceptions import (
    JobExecutionError,
    NatsWorkError,
    WorkerError,
)
from .job import Job, JobRegistry, job
from .server import NatsWorkServer
from .worker import Worker

__all__ = [
    "Worker",
    "job",
    "Job",
    "JobRegistry",
    "NatsWorkServer",
    "NatsWorkError",
    "WorkerError",
    "JobExecutionError",
]
