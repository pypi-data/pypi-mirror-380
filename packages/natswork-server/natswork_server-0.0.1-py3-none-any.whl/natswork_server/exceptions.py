"""NatsWork Server exceptions."""


class NatsWorkError(Exception):
    """Base exception for all NatsWork errors."""
    pass


class WorkerError(NatsWorkError):
    """Raised when worker operation fails."""
    pass


class JobExecutionError(NatsWorkError):
    """Raised when job execution fails."""
    pass


class JobInstantiationError(JobExecutionError):
    """Error creating job instance"""
    pass


class JobTimeoutError(JobExecutionError):
    """Job execution timeout"""
    pass


class JobArgumentError(JobExecutionError):
    """Invalid job arguments"""
    pass


class JobMethodError(JobExecutionError):
    """Error calling job method"""
    pass
