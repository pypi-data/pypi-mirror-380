"""Unit tests for Job base class."""

from abc import ABC

import pytest

from natswork_client.job import Job, job


@job(queue="test")
class ConcreteJob(Job):
    """Concrete job implementation for testing."""

    def perform(self, *args, **kwargs):
        return f"performed with args={args}, kwargs={kwargs}"


class TestJob:
    """Test cases for Job base class."""

    def test_job_is_abstract(self):
        """Test that Job is an abstract base class."""
        assert issubclass(Job, ABC)

        with pytest.raises(TypeError):
            Job()

    def test_concrete_job_implementation(self):
        """Test concrete job implementation."""
        job_instance = ConcreteJob()

        # Check class attributes
        assert ConcreteJob.queue == "test"
        assert ConcreteJob.retries == 3
        assert ConcreteJob.timeout == 300

        result = job_instance.perform("arg1", "arg2", key="value")
        assert result == "performed with args=('arg1', 'arg2'), kwargs={'key': 'value'}"

    def test_custom_job_attributes(self):
        """Test job with custom attributes."""
        @job(queue="custom", retries=5, timeout=60)
        class CustomJob(Job):
            def perform(self, *args, **kwargs):
                return "custom"

        # Check class attributes
        assert CustomJob.queue == "custom"
        assert CustomJob.retries == 5
        assert CustomJob.timeout == 60

        # Check instance works
        job_instance = CustomJob()
        assert job_instance.perform() == "custom"
