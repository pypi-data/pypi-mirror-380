"""NatsWork client for job dispatching."""

import logging
from typing import Any, Callable, List, Optional, Type

from .config import ClientConfig
from .dispatcher import JobDispatcher
from .job import Job
from .nats_client import NatsConnectionManager
from .result_handler import JobResult, ResultHandler
from .status_tracker import JobStatusInfo, JobStatusTracker

logger = logging.getLogger(__name__)


class NatsWorkClient:
    """Client for dispatching jobs to NatsWork workers."""

    def __init__(self, servers: List[str] = None, **options):
        """Initialize NatsWork client.

        Args:
            servers: List of NATS server URLs
            **options: Additional NATS options
        """
        self.servers = servers or ["nats://localhost:4222"]
        self.options = options
        self._connection_manager = NatsConnectionManager(self.servers)
        self._job_dispatcher = JobDispatcher(self._connection_manager)
        self._result_handler = ResultHandler(self._connection_manager)
        self._status_tracker = JobStatusTracker(self._connection_manager)
        self._connected = False

    async def connect(self):
        """Connect to NATS servers"""
        if self._connected:
            return

        await self._connection_manager.connect()
        await self._result_handler.start()
        await self._job_dispatcher.start()
        self._connected = True
        logger.info("NatsWork client connected")

    async def disconnect(self):
        """Disconnect from NATS servers"""
        if not self._connected:
            return

        await self._job_dispatcher.stop()
        await self._result_handler.stop()
        await self._connection_manager.disconnect()
        self._connected = False
        logger.info("NatsWork client disconnected")

    async def perform_async(self, job_class: Type[Job], *args, **kwargs) -> str:
        """Dispatch job asynchronously (fire-and-forget)

        Args:
            job_class: Job class to execute
            *args, **kwargs: Job arguments

        Returns:
            job_id: UUID of the dispatched job
        """
        if not self._connected:
            await self.connect()

        return await self._job_dispatcher.dispatch_async(job_class, args, kwargs)

    async def perform_sync(self, job_class: Type[Job], *args, timeout: float = 30, **kwargs) -> Any:
        """Dispatch job synchronously (request-reply)

        Args:
            job_class: Job class to execute
            *args, **kwargs: Job arguments
            timeout: Maximum wait time for result

        Returns:
            Job execution result
        """
        if not self._connected:
            await self.connect()

        return await self._job_dispatcher.dispatch_sync(job_class, args, kwargs, timeout)

    async def get_job_status(self, job_id: str) -> Optional[JobStatusInfo]:
        """Get current status of a job"""
        return await self._status_tracker.get_status(job_id)

    def subscribe_to_results(self, callback: Callable[[JobResult], None], job_ids: List[str] = None):
        """Subscribe to job results"""
        self._result_handler.subscribe(callback, job_ids)

    async def wait_for_job(self, job_id: str, timeout: float = None) -> JobResult:
        """Wait for specific job to complete"""
        return await self._result_handler.wait_for_result(job_id, timeout)


_default_client = None


def get_default_client() -> NatsWorkClient:
    """Get default global client instance"""
    global _default_client
    if _default_client is None:
        _default_client = NatsWorkClient()
    return _default_client


async def perform_async(job_class: Type[Job], *args, **kwargs) -> str:
    """Global convenience function for async job dispatch"""
    client = get_default_client()
    return await client.perform_async(job_class, *args, **kwargs)


async def perform_sync(job_class: Type[Job], *args, timeout: float = 30, **kwargs) -> Any:
    """Global convenience function for sync job dispatch"""
    client = get_default_client()
    return await client.perform_sync(job_class, *args, timeout=timeout, **kwargs)


class ConfigurableClient(NatsWorkClient):
    """Client with advanced configuration support"""

    def __init__(self, config: ClientConfig = None):
        if config is None:
            config = ClientConfig.from_env()

        self.config = config

        nats_options = {}

        if config.username and config.password:
            nats_options["user"] = config.username
            nats_options["password"] = config.password
        elif config.token:
            nats_options["token"] = config.token

        super().__init__(servers=config.servers, **nats_options)
