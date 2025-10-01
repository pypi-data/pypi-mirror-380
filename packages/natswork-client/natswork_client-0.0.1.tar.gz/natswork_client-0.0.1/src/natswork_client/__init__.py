"""NatsWork Client - Job dispatching and result handling for distributed job processing."""

__version__ = "0.1.0"
__author__ = "NatsWork Contributors"
__email__ = "natswork@tesote.com"

from .async_support import AsyncJobDispatcher, natswork_client
from .client import (
    ConfigurableClient,
    NatsWorkClient,
    get_default_client,
    perform_async,
    perform_sync,
)
from .config import ClientConfig
from .dispatcher import JobDispatcher
from .exceptions import (
    ClientConnectionError,
    ClientError,
    ClientTimeoutError,
    ConnectionError,
    JobDispatchError,
    JobExecutionError,
    NatsWorkError,
    ResultHandlingError,
    TimeoutError,
)
from .job import (
    Job,
    JobConfig,
    JobContext,
    JobDiscovery,
    JobRegistry,
    QueueConfig,
    QueueManager,
    job,
)
from .messages import (
    JobMessage,
    MessageBuilder,
    MessageSerializer,
    ResultMessage,
)
from .result_handler import JobResult
from .status_tracker import JobStatus, JobStatusInfo

__all__ = [
    "NatsWorkClient",
    "ConfigurableClient",
    "perform_async",
    "perform_sync",
    "get_default_client",
    "Job",
    "JobConfig",
    "JobContext",
    "JobDiscovery",
    "JobRegistry",
    "QueueConfig",
    "QueueManager",
    "job",
    "NatsWorkError",
    "ConnectionError",
    "TimeoutError",
    "JobExecutionError",
    "ClientError",
    "ClientConnectionError",
    "ClientTimeoutError",
    "JobDispatchError",
    "ResultHandlingError",
    "JobMessage",
    "ResultMessage",
    "MessageBuilder",
    "MessageSerializer",
    "ClientConfig",
    "JobResult",
    "JobStatus",
    "JobStatusInfo",
    "JobDispatcher",
    "natswork_client",
    "AsyncJobDispatcher",
]
