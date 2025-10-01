"""NatsWork Client exceptions."""


class NatsWorkError(Exception):
    """Base exception for all NatsWork errors."""
    pass


class ConnectionError(NatsWorkError):
    """Raised when connection to NATS fails."""
    pass


class TimeoutError(NatsWorkError):
    """Raised when operation times out."""
    pass


class JobExecutionError(NatsWorkError):
    """Raised when job execution fails."""
    pass


class ClientError(NatsWorkError):
    """Base client error"""
    pass


class ClientConnectionError(ClientError):
    """Connection-related client error"""
    pass


class ClientTimeoutError(ClientError):
    """Client timeout error"""
    pass


class JobDispatchError(ClientError):
    """Job dispatch error"""
    pass


class ResultHandlingError(ClientError):
    """Result handling error"""
    pass
