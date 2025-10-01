"""NatsWork job base class and registry."""

import importlib
import inspect
import logging
import pkgutil
import sys
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Type, Union

logger = logging.getLogger(__name__)


@dataclass
class JobConfig:
    """Job configuration metadata."""
    queue: str
    retries: int = 3
    timeout: int = 300
    retry_delay: Union[int, Callable[[int], int], None] = None
    priority: int = 0
    unique: bool = False
    unique_for: int = 3600  # seconds
    dead_letter_queue: Optional[str] = None

    def calculate_retry_delay(self, attempt: int) -> int:
        """Calculate delay for retry attempt."""
        if callable(self.retry_delay):
            return self.retry_delay(attempt)
        elif isinstance(self.retry_delay, int):
            return self.retry_delay
        else:
            # Exponential backoff: 2^attempt seconds
            return min(2 ** attempt, 300)


class JobContext:
    """Context information for job execution."""

    def __init__(self, job_id: str):
        self.job_id = job_id
        self.attempt = 1
        self.metadata = {}


class Job(ABC):
    """Base class for NatsWork jobs."""

    def __init__(self, job_id: str = None, arguments: Union[List, Dict] = None):
        self.job_id = job_id
        self.arguments = arguments or {}
        self.context = JobContext(job_id=job_id) if job_id else None

    @abstractmethod
    async def perform(self, *args, **kwargs) -> Any:
        """Perform the job.

        Override this method to implement job logic.
        Can be async or sync - async is preferred for I/O operations.

        Args:
            *args: Job arguments
            **kwargs: Job keyword arguments

        Returns:
            Job result
        """
        raise NotImplementedError("Jobs must implement the perform method")

    def before_perform(self):
        """Hook called before job execution."""
        pass

    def after_perform(self, result):
        """Hook called after successful job execution."""
        pass

    def on_failure(self, exception):
        """Hook called when job fails."""
        pass

    def should_retry(self, exception, attempt_number):
        """Determine if job should be retried after failure."""
        config = getattr(self.__class__, '_natswork_config', None)
        if not config:
            return False
        return attempt_number < config.retries


class JobRegistry:
    """Central registry for job classes and their metadata."""

    _jobs: Dict[str, Type[Job]] = {}
    _queues: Dict[str, Set[str]] = defaultdict(set)
    _configs: Dict[str, JobConfig] = {}

    @classmethod
    def register(cls, job_class: Type[Job], config: JobConfig = None):
        """Register a job class.

        Args:
            job_class: Job class to register
            config: Job configuration (optional, uses class attribute if available)
        """
        job_name = f"{job_class.__module__}.{job_class.__name__}"

        if config is None:
            config = getattr(job_class, '_natswork_config', None)

        if not config:
            # Create default config from class attributes
            config = JobConfig(
                queue=getattr(job_class, 'queue', 'default'),
                retries=getattr(job_class, 'retries', 3),
                timeout=getattr(job_class, 'timeout', 300)
            )

        cls._jobs[job_name] = job_class
        cls._configs[job_name] = config
        cls._queues[config.queue].add(job_name)

        logger.debug(f"Registered job {job_name} on queue {config.queue}")

    @classmethod
    def get_job_class(cls, job_name: str) -> Optional[Type[Job]]:
        """Retrieve job class by name."""
        return cls._jobs.get(job_name)

    @classmethod
    def get_job_config(cls, job_name: str) -> Optional[JobConfig]:
        """Retrieve job configuration."""
        return cls._configs.get(job_name)

    @classmethod
    def get_queue_jobs(cls, queue_name: str) -> Set[str]:
        """Get all job names for a queue."""
        return cls._queues.get(queue_name, set())

    @classmethod
    def list_all_jobs(cls) -> Dict[str, JobConfig]:
        """List all registered jobs with their configs."""
        return cls._configs.copy()

    @classmethod
    def clear(cls):
        """Clear registry (useful for testing)."""
        cls._jobs.clear()
        cls._queues.clear()
        cls._configs.clear()


def job(
    queue: str = "default",
    retries: int = 3,
    timeout: int = 300,
    retry_delay: Union[int, Callable[[int], int], None] = None,
    **kwargs
):
    """Decorator to mark a class as a NatsWork job.

    Args:
        queue: Target queue name
        retries: Maximum retry attempts
        timeout: Job timeout in seconds
        retry_delay: Delay between retries (seconds or callable)
        **kwargs: Additional configuration options
    """
    def decorator(cls):
        # Set job metadata on class
        cls._natswork_config = JobConfig(
            queue=queue,
            retries=retries,
            timeout=timeout,
            retry_delay=retry_delay,
            **kwargs
        )

        # Also set individual attributes for backward compatibility
        cls.queue = queue
        cls.retries = retries
        cls.timeout = timeout

        # Register the job class
        JobRegistry.register(cls, cls._natswork_config)

        return cls
    return decorator


class JobDiscovery:
    """Automatic job discovery system."""

    @staticmethod
    def discover_from_module(module_name: str):
        """Discover jobs from a specific module."""
        try:
            module = importlib.import_module(module_name)
            JobDiscovery._scan_module(module)
        except ImportError as e:
            logger.warning(f"Could not import module {module_name}: {e}")

    @staticmethod
    def discover_from_package(package_name: str):
        """Discover jobs from all modules in a package."""
        try:
            package = importlib.import_module(package_name)
            if hasattr(package, '__path__'):
                for _finder, name, _ispkg in pkgutil.iter_modules(package.__path__, package_name + "."):
                    JobDiscovery.discover_from_module(name)
        except ImportError as e:
            logger.warning(f"Could not import package {package_name}: {e}")

    @staticmethod
    def _scan_module(module):
        """Scan module for job classes."""
        for name in dir(module):
            obj = getattr(module, name)
            if (
                inspect.isclass(obj) and
                issubclass(obj, Job) and
                obj != Job and
                hasattr(obj, '_natswork_config')
            ):
                # Job is already registered via @job decorator
                logger.debug(f"Found job class {obj.__name__} in {module.__name__}")

    @staticmethod
    def discover_django_jobs():
        """Discover jobs from Django apps."""
        if 'django' in sys.modules:
            from django.apps import apps
            for app_config in apps.get_app_configs():
                JobDiscovery.discover_from_module(f"{app_config.name}.jobs")

    @staticmethod
    def discover_flask_jobs(app=None):
        """Discover jobs from Flask application."""
        # Look in jobs module or jobs package
        JobDiscovery.discover_from_module("jobs")


class QueueConfig:
    """Queue-specific configuration."""

    def __init__(self, name: str):
        self.name = name
        self.concurrency = 10
        self.max_retries = 3
        self.dead_letter_queue = f"{name}.dead"
        self.priority_levels = 3

    def get_subject_name(self) -> str:
        """Get NATS subject for this queue."""
        return f"natswork.jobs.{self.name}"

    def get_result_subject_name(self) -> str:
        """Get NATS subject for job results."""
        return f"natswork.results.{self.name}"


class QueueManager:
    """Manage queue configurations and routing."""

    def __init__(self):
        self._queues: Dict[str, QueueConfig] = {}

    def register_queue(self, name: str, config: QueueConfig = None):
        """Register a queue configuration."""
        if config is None:
            config = QueueConfig(name)
        self._queues[name] = config

    def get_queue_config(self, name: str) -> QueueConfig:
        """Get queue configuration, creating default if needed."""
        if name not in self._queues:
            self.register_queue(name)
        return self._queues[name]
