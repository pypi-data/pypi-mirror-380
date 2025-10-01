"""Tests for job registry system."""

import asyncio

import pytest

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


class TestJobConfig:
    """Test JobConfig class."""

    def test_default_config(self):
        """Test default job configuration."""
        config = JobConfig(queue="test")
        assert config.queue == "test"
        assert config.retries == 3
        assert config.timeout == 300
        assert config.priority == 0
        assert config.unique is False
        assert config.unique_for == 3600
        assert config.dead_letter_queue is None

    def test_custom_config(self):
        """Test custom job configuration."""
        config = JobConfig(
            queue="custom",
            retries=5,
            timeout=60,
            priority=10,
            unique=True,
            dead_letter_queue="custom.dead"
        )
        assert config.queue == "custom"
        assert config.retries == 5
        assert config.timeout == 60
        assert config.priority == 10
        assert config.unique is True
        assert config.dead_letter_queue == "custom.dead"

    def test_calculate_retry_delay_default(self):
        """Test default exponential backoff."""
        config = JobConfig(queue="test")
        assert config.calculate_retry_delay(1) == 2
        assert config.calculate_retry_delay(2) == 4
        assert config.calculate_retry_delay(3) == 8
        assert config.calculate_retry_delay(10) == 300  # max 300

    def test_calculate_retry_delay_fixed(self):
        """Test fixed retry delay."""
        config = JobConfig(queue="test", retry_delay=10)
        assert config.calculate_retry_delay(1) == 10
        assert config.calculate_retry_delay(5) == 10

    def test_calculate_retry_delay_callable(self):
        """Test callable retry delay."""
        config = JobConfig(
            queue="test",
            retry_delay=lambda attempt: attempt * 5
        )
        assert config.calculate_retry_delay(1) == 5
        assert config.calculate_retry_delay(3) == 15


class TestJobContext:
    """Test JobContext class."""

    def test_job_context_creation(self):
        """Test job context initialization."""
        context = JobContext(job_id="test-123")
        assert context.job_id == "test-123"
        assert context.attempt == 1
        assert context.metadata == {}


class TestJobBase:
    """Test Job base class."""

    def test_job_initialization(self):
        """Test job initialization."""
        class TestJob(Job):
            def perform(self):
                return "result"

        job_instance = TestJob(job_id="test-123", arguments={"key": "value"})
        assert job_instance.job_id == "test-123"
        assert job_instance.arguments == {"key": "value"}
        assert job_instance.context.job_id == "test-123"

    def test_job_hooks(self):
        """Test job lifecycle hooks."""
        class TestJob(Job):
            def perform(self):
                return "result"

        job_instance = TestJob()

        # Hooks should not raise errors
        job_instance.before_perform()
        job_instance.after_perform("result")
        job_instance.on_failure(Exception("test"))

    def test_should_retry_no_config(self):
        """Test should_retry without config."""
        class TestJob(Job):
            def perform(self):
                return "result"

        job_instance = TestJob()
        assert job_instance.should_retry(Exception("test"), 1) is False

    def test_should_retry_with_config(self):
        """Test should_retry with config."""
        @job(retries=3)
        class TestJob(Job):
            def perform(self):
                return "result"

        job_instance = TestJob()
        assert job_instance.should_retry(Exception("test"), 1) is True
        assert job_instance.should_retry(Exception("test"), 2) is True
        assert job_instance.should_retry(Exception("test"), 3) is False
        assert job_instance.should_retry(Exception("test"), 4) is False

    def test_abstract_perform(self):
        """Test that perform must be implemented."""
        class InvalidJob(Job):
            pass

        # Can't instantiate without implementing perform
        with pytest.raises(TypeError):
            InvalidJob()


class TestJobDecorator:
    """Test @job decorator."""

    def setUp(self):
        """Clear registry before each test."""
        JobRegistry.clear()

    def test_basic_decorator(self):
        """Test basic job decorator."""
        self.setUp()

        @job(queue="test_queue")
        class TestJob(Job):
            def perform(self, name):
                return f"Hello {name}"

        # Check class attributes
        assert hasattr(TestJob, '_natswork_config')
        assert TestJob._natswork_config.queue == "test_queue"
        assert TestJob._natswork_config.retries == 3
        assert TestJob._natswork_config.timeout == 300

        # Check backward compatibility attributes
        assert TestJob.queue == "test_queue"
        assert TestJob.retries == 3
        assert TestJob.timeout == 300

    def test_decorator_with_all_options(self):
        """Test decorator with all configuration options."""
        self.setUp()

        @job(
            queue="custom",
            retries=5,
            timeout=60,
            retry_delay=10,
            priority=5,
            unique=True,
            dead_letter_queue="custom.dead"
        )
        class CustomJob(Job):
            def perform(self):
                return "custom"

        config = CustomJob._natswork_config
        assert config.queue == "custom"
        assert config.retries == 5
        assert config.timeout == 60
        assert config.retry_delay == 10
        assert config.priority == 5
        assert config.unique is True
        assert config.dead_letter_queue == "custom.dead"

    def test_decorator_with_callable_retry_delay(self):
        """Test decorator with callable retry delay."""
        self.setUp()

        @job(
            queue="test",
            retry_delay=lambda attempt: attempt * 10
        )
        class RetryJob(Job):
            def perform(self):
                return "retry"

        config = RetryJob._natswork_config
        assert callable(config.retry_delay)
        assert config.calculate_retry_delay(2) == 20


class TestJobRegistry:
    """Test JobRegistry class."""

    def setUp(self):
        """Clear registry before each test."""
        JobRegistry.clear()

    def test_register_job(self):
        """Test job registration."""
        self.setUp()

        @job(queue="test")
        class TestJob(Job):
            def perform(self):
                return "test"

        job_name = f"{TestJob.__module__}.TestJob"

        # Check job is registered
        assert job_name in JobRegistry._jobs
        assert JobRegistry.get_job_class(job_name) == TestJob

        # Check config is stored
        config = JobRegistry.get_job_config(job_name)
        assert config is not None
        assert config.queue == "test"

        # Check queue mapping
        assert job_name in JobRegistry.get_queue_jobs("test")

    def test_register_without_decorator(self):
        """Test registering job without decorator."""
        self.setUp()

        class PlainJob(Job):
            queue = "plain"
            retries = 5
            timeout = 60

            def perform(self):
                return "plain"

        # Register manually
        JobRegistry.register(PlainJob)

        job_name = f"{PlainJob.__module__}.PlainJob"

        # Check registration worked
        assert JobRegistry.get_job_class(job_name) == PlainJob
        config = JobRegistry.get_job_config(job_name)
        assert config.queue == "plain"
        assert config.retries == 5
        assert config.timeout == 60

    def test_list_all_jobs(self):
        """Test listing all registered jobs."""
        self.setUp()

        @job(queue="queue1")
        class Job1(Job):
            def perform(self):
                pass

        @job(queue="queue2")
        class Job2(Job):
            def perform(self):
                pass

        all_jobs = JobRegistry.list_all_jobs()
        assert len(all_jobs) == 2

        for _job_name, config in all_jobs.items():
            assert isinstance(config, JobConfig)

    def test_get_queue_jobs(self):
        """Test getting jobs for a specific queue."""
        self.setUp()

        @job(queue="email")
        class EmailJob1(Job):
            def perform(self):
                pass

        @job(queue="email")
        class EmailJob2(Job):
            def perform(self):
                pass

        @job(queue="sms")
        class SmsJob(Job):
            def perform(self):
                pass

        email_jobs = JobRegistry.get_queue_jobs("email")
        assert len(email_jobs) == 2

        sms_jobs = JobRegistry.get_queue_jobs("sms")
        assert len(sms_jobs) == 1

        # Non-existent queue returns empty set
        assert JobRegistry.get_queue_jobs("nonexistent") == set()

    def test_clear_registry(self):
        """Test clearing the registry."""
        self.setUp()

        @job(queue="test")
        class TestJob(Job):
            def perform(self):
                pass

        assert len(JobRegistry._jobs) > 0

        JobRegistry.clear()

        assert len(JobRegistry._jobs) == 0
        assert len(JobRegistry._configs) == 0
        assert len(JobRegistry._queues) == 0


class TestJobDiscovery:
    """Test JobDiscovery class."""

    def setUp(self):
        """Clear registry before each test."""
        JobRegistry.clear()

    def test_discover_from_module(self):
        """Test discovering jobs from a module."""
        self.setUp()

        # Create a test module with jobs
        import types
        test_module = types.ModuleType("test_jobs")

        # Add a job class to the module
        @job(queue="discovered")
        class DiscoveredJob(Job):
            def perform(self):
                return "discovered"

        test_module.DiscoveredJob = DiscoveredJob

        # Discover from module
        JobDiscovery._scan_module(test_module)

        # Job should be registered
        job_name = f"{DiscoveredJob.__module__}.DiscoveredJob"
        assert JobRegistry.get_job_class(job_name) == DiscoveredJob

    def test_discover_ignores_base_class(self):
        """Test that discovery ignores the base Job class."""
        self.setUp()

        import types
        test_module = types.ModuleType("test_jobs")
        test_module.Job = Job

        # Add a proper job
        @job(queue="test")
        class ProperJob(Job):
            def perform(self):
                pass

        test_module.ProperJob = ProperJob

        initial_count = len(JobRegistry._jobs)
        JobDiscovery._scan_module(test_module)

        # Only ProperJob should be discovered, not Job base class
        assert len(JobRegistry._jobs) == initial_count  # ProperJob already registered by decorator


class TestQueueConfig:
    """Test QueueConfig class."""

    def test_default_queue_config(self):
        """Test default queue configuration."""
        config = QueueConfig("test")
        assert config.name == "test"
        assert config.concurrency == 10
        assert config.max_retries == 3
        assert config.dead_letter_queue == "test.dead"
        assert config.priority_levels == 3

    def test_subject_names(self):
        """Test NATS subject name generation."""
        config = QueueConfig("email")
        assert config.get_subject_name() == "natswork.jobs.email"
        assert config.get_result_subject_name() == "natswork.results.email"


class TestQueueManager:
    """Test QueueManager class."""

    def test_register_queue(self):
        """Test queue registration."""
        manager = QueueManager()

        # Register with default config
        manager.register_queue("test1")
        config1 = manager.get_queue_config("test1")
        assert config1.name == "test1"
        assert config1.concurrency == 10

        # Register with custom config
        custom_config = QueueConfig("test2")
        custom_config.concurrency = 20
        manager.register_queue("test2", custom_config)

        config2 = manager.get_queue_config("test2")
        assert config2.concurrency == 20

    def test_get_queue_config_auto_creates(self):
        """Test that get_queue_config auto-creates missing queues."""
        manager = QueueManager()

        # Queue doesn't exist yet
        assert "new_queue" not in manager._queues

        # Get config auto-creates it
        config = manager.get_queue_config("new_queue")
        assert config.name == "new_queue"
        assert "new_queue" in manager._queues


class TestIntegration:
    """Integration tests for job system."""

    def setUp(self):
        """Clear registry before each test."""
        JobRegistry.clear()

    def test_full_job_lifecycle(self):
        """Test complete job lifecycle."""
        self.setUp()

        # Define a job
        @job(queue="integration", retries=5, timeout=30)
        class IntegrationJob(Job):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.before_called = False
                self.after_called = False
                self.failure_called = False

            def perform(self, x, y):
                return x + y

            def before_perform(self):
                self.before_called = True

            def after_perform(self, result):
                self.after_called = True
                self.result = result

            def on_failure(self, exception):
                self.failure_called = True
                self.exception = exception

        # Create and run job
        job_instance = IntegrationJob(job_id="int-123", arguments=[1, 2])

        # Simulate job execution
        job_instance.before_perform()
        assert job_instance.before_called is True

        result = job_instance.perform(1, 2)
        assert result == 3

        job_instance.after_perform(result)
        assert job_instance.after_called is True
        assert job_instance.result == 3

        # Simulate failure
        exc = Exception("test failure")
        job_instance.on_failure(exc)
        assert job_instance.failure_called is True
        assert job_instance.exception == exc

        # Test retry logic
        assert job_instance.should_retry(exc, 1) is True
        assert job_instance.should_retry(exc, 5) is False

    def test_async_job(self):
        """Test async job execution."""
        self.setUp()

        @job(queue="async")
        class AsyncJob(Job):
            async def perform(self, delay=0.1):
                await asyncio.sleep(delay)
                return "async_result"

        # Create job
        job_instance = AsyncJob()

        # Run async perform
        async def run():
            result = await job_instance.perform(0.01)
            return result

        # Execute
        result = asyncio.run(run())
        assert result == "async_result"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
