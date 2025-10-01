"""Tests for message protocol implementation."""

import json
import uuid
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError as PydanticValidationError

from natswork_client.messages import (
    BaseMessage,
    ControlMessage,
    JobMessage,
    MessageBuilder,
    MessageSerializer,
    NatsWorkEncoder,
    ProtocolValidator,
    ResultMessage,
    VersionHandler,
)


class TestBaseMessage:
    """Test BaseMessage class."""

    def test_create_base_message(self):
        """Test creating a base message with required fields."""
        msg = BaseMessage(job_class="TestJob", queue="default")
        assert msg.job_class == "TestJob"
        assert msg.queue == "default"
        assert msg.version == "1.0"
        assert ProtocolValidator.validate_job_id(msg.job_id)

    def test_auto_generated_job_id(self):
        """Test that job_id is auto-generated as UUID."""
        msg = BaseMessage(job_class="TestJob", queue="default")
        assert uuid.UUID(msg.job_id)  # Should not raise

    def test_custom_job_id(self):
        """Test providing custom job_id."""
        job_id = str(uuid.uuid4())
        msg = BaseMessage(job_id=job_id, job_class="TestJob", queue="default")
        assert msg.job_id == job_id

    def test_invalid_job_id(self):
        """Test validation of invalid job_id."""
        with pytest.raises(PydanticValidationError) as exc_info:
            BaseMessage(job_id="not-a-uuid", job_class="TestJob", queue="default")
        assert "Invalid job_id format" in str(exc_info.value)

    def test_invalid_queue_name(self):
        """Test validation of invalid queue name."""
        with pytest.raises(PydanticValidationError) as exc_info:
            BaseMessage(job_class="TestJob", queue="invalid queue!")
        assert "Invalid queue name" in str(exc_info.value)

    def test_valid_queue_names(self):
        """Test various valid queue name formats."""
        valid_queues = ["default", "high-priority", "low_priority", "queue123", "QUEUE_1"]
        for queue in valid_queues:
            msg = BaseMessage(job_class="TestJob", queue=queue)
            assert msg.queue == queue

    def test_invalid_job_class(self):
        """Test validation of invalid job class."""
        with pytest.raises(PydanticValidationError) as exc_info:
            BaseMessage(job_class="123Invalid", queue="default")
        assert "Invalid job class format" in str(exc_info.value)

    def test_ruby_style_job_class(self):
        """Test Ruby-style job class names are accepted."""
        msg = BaseMessage(job_class="Module::Class", queue="default")
        assert msg.job_class == "Module::Class"

    def test_python_style_job_class(self):
        """Test Python-style job class names are accepted."""
        msg = BaseMessage(job_class="module.submodule.Class", queue="default")
        assert msg.job_class == "module.submodule.Class"

    def test_datetime_with_timezone(self):
        """Test datetime handling with timezone."""
        msg = BaseMessage(job_class="TestJob", queue="default")
        assert msg.created_at.tzinfo == timezone.utc


class TestJobMessage:
    """Test JobMessage class."""

    def test_create_job_message(self):
        """Test creating a job message."""
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments=["arg1", "arg2"],
            options={"timeout": 30},
        )
        assert msg.arguments == ["arg1", "arg2"]
        assert msg.options == {"timeout": 30}
        assert msg.retry_count == 0
        assert msg.max_retries == 3

    def test_job_message_with_dict_arguments(self):
        """Test job message with dictionary arguments."""
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments={"key": "value", "number": 42},
        )
        assert msg.arguments == {"key": "value", "number": 42}

    def test_job_message_defaults(self):
        """Test job message default values."""
        msg = JobMessage(job_class="TestJob", queue="default")
        assert msg.arguments == []
        assert msg.options == {}
        assert msg.metadata == {}

    def test_job_message_with_metadata(self):
        """Test job message with metadata."""
        metadata = {"user_id": 123, "request_id": "abc"}
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            metadata=metadata,
        )
        assert msg.metadata == metadata


class TestResultMessage:
    """Test ResultMessage class."""

    def test_success_result(self):
        """Test successful result message."""
        job_id = str(uuid.uuid4())
        msg = ResultMessage(
            job_id=job_id,
            status="success",
            result={"data": "result"},
            processing_time=1.5,
        )
        assert msg.job_id == job_id
        assert msg.status == "success"
        assert msg.result == {"data": "result"}
        assert msg.processing_time == 1.5
        assert msg.error is None

    def test_error_result(self):
        """Test error result message."""
        job_id = str(uuid.uuid4())
        error = {"class": "ValueError", "message": "Invalid input", "args": ""}
        msg = ResultMessage(
            job_id=job_id,
            status="error",
            error=error,
            processing_time=0.5,
        )
        assert msg.status == "error"
        assert msg.error == error
        assert msg.result is None

    def test_retry_result(self):
        """Test retry result message."""
        job_id = str(uuid.uuid4())
        msg = ResultMessage(
            job_id=job_id,
            status="retry",
            processing_time=0.1,
        )
        assert msg.status == "retry"

    def test_invalid_status(self):
        """Test invalid status value."""
        with pytest.raises(PydanticValidationError):
            ResultMessage(
                job_id=str(uuid.uuid4()),
                status="invalid",  # type: ignore
                processing_time=0,
            )


class TestControlMessage:
    """Test ControlMessage class."""

    def test_cancel_message(self):
        """Test cancel control message."""
        job_id = str(uuid.uuid4())
        msg = ControlMessage(type="cancel", job_id=job_id)
        assert msg.type == "cancel"
        assert msg.job_id == job_id

    def test_pause_queue_message(self):
        """Test pause queue control message."""
        msg = ControlMessage(type="pause", queue="default")
        assert msg.type == "pause"
        assert msg.queue == "default"

    def test_control_message_with_metadata(self):
        """Test control message with metadata."""
        metadata = {"reason": "maintenance"}
        msg = ControlMessage(type="pause", metadata=metadata)
        assert msg.metadata == metadata


class TestMessageBuilder:
    """Test MessageBuilder class."""

    def test_build_job_message(self):
        """Test building a job message."""
        msg = MessageBuilder.build_job_message(
            job_class="TestJob",
            queue="high",
            arguments=["arg1"],
            options={"retry": True},
        )
        assert isinstance(msg, JobMessage)
        assert msg.job_class == "TestJob"
        assert msg.queue == "high"
        assert msg.arguments == ["arg1"]
        assert msg.options == {"retry": True}

    def test_build_job_message_with_custom_id(self):
        """Test building job message with custom ID."""
        job_id = str(uuid.uuid4())
        msg = MessageBuilder.build_job_message(
            job_class="TestJob",
            queue="default",
            job_id=job_id,
        )
        assert msg.job_id == job_id

    def test_build_result_message_success(self):
        """Test building success result message."""
        job_id = str(uuid.uuid4())
        msg = MessageBuilder.build_result_message(
            job_id=job_id,
            status="success",
            result={"output": "data"},
            processing_time=2.5,
        )
        assert isinstance(msg, ResultMessage)
        assert msg.status == "success"
        assert msg.result == {"output": "data"}
        assert msg.processing_time == 2.5

    def test_build_result_message_with_error(self):
        """Test building result message with exception."""
        job_id = str(uuid.uuid4())
        error = ValueError("Test error")
        msg = MessageBuilder.build_result_message(
            job_id=job_id,
            status="error",
            error=error,
            processing_time=0.5,
        )
        assert msg.status == "error"
        assert msg.error["class"] == "ValueError"
        assert msg.error["message"] == "Test error"

    def test_build_control_message(self):
        """Test building control message."""
        msg = MessageBuilder.build_control_message(
            message_type="cancel",
            job_id="test-123",
        )
        assert isinstance(msg, ControlMessage)
        assert msg.type == "cancel"
        assert msg.job_id == "test-123"


class TestMessageSerializer:
    """Test MessageSerializer class."""

    def test_serialize_job_message(self):
        """Test serializing job message to bytes."""
        msg = JobMessage(job_class="TestJob", queue="default")
        data = MessageSerializer.serialize(msg)
        assert isinstance(data, bytes)

        # Verify it's valid JSON
        json_dict = json.loads(data.decode("utf-8"))
        assert json_dict["job_class"] == "TestJob"
        assert json_dict["queue"] == "default"

    def test_deserialize_job_message(self):
        """Test deserializing bytes to job message."""
        job_id = str(uuid.uuid4())
        json_data = {
            "job_id": job_id,
            "job_class": "TestJob",
            "queue": "default",
            "arguments": ["arg1"],
            "options": {},
            "retry_count": 0,
            "max_retries": 3,
            "metadata": {},
            "created_at": datetime.now(timezone.utc).isoformat() + "Z",
            "version": "1.0",
        }
        data = json.dumps(json_data).encode("utf-8")

        msg = MessageSerializer.deserialize(data, JobMessage)
        assert isinstance(msg, JobMessage)
        assert msg.job_id == job_id
        assert msg.job_class == "TestJob"
        assert msg.arguments == ["arg1"]

    def test_roundtrip_serialization(self):
        """Test serialization roundtrip maintains data integrity."""
        original = JobMessage(
            job_class="TestJob",
            queue="high",
            arguments={"key": "value", "nested": {"data": 123}},
            options={"timeout": 30},
            metadata={"user": "test"},
        )

        # Serialize and deserialize
        serialized = MessageSerializer.serialize(original)
        deserialized = MessageSerializer.deserialize(serialized, JobMessage)

        # Compare key fields
        assert deserialized.job_id == original.job_id
        assert deserialized.job_class == original.job_class
        assert deserialized.queue == original.queue
        assert deserialized.arguments == original.arguments
        assert deserialized.options == original.options
        assert deserialized.metadata == original.metadata

    def test_datetime_serialization(self):
        """Test datetime serialization format."""
        msg = JobMessage(job_class="TestJob", queue="default")
        serialized = MessageSerializer.serialize(msg)
        json_dict = json.loads(serialized.decode("utf-8"))

        # Should end with Z for UTC
        assert json_dict["created_at"].endswith("Z")
        # Should be parseable as ISO format
        datetime.fromisoformat(json_dict["created_at"].replace("Z", "+00:00"))

    def test_json_string_methods(self):
        """Test JSON string conversion methods."""
        msg = JobMessage(job_class="TestJob", queue="default")

        # To JSON string
        json_str = MessageSerializer.to_json_string(msg)
        assert isinstance(json_str, str)

        # From JSON string
        restored = MessageSerializer.from_json_string(json_str, JobMessage)
        assert restored.job_class == msg.job_class
        assert restored.queue == msg.queue


class TestNatsWorkEncoder:
    """Test NatsWorkEncoder class."""

    def test_encode_datetime(self):
        """Test encoding datetime objects."""
        encoder = NatsWorkEncoder()
        dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        result = encoder.default(dt)
        assert result == "2024-01-01T12:00:00Z"

    def test_encode_exception(self):
        """Test encoding exception objects."""
        encoder = NatsWorkEncoder()
        exc = ValueError("Test error", "arg1", "arg2")
        result = encoder.default(exc)
        assert result["class"] == "ValueError"
        assert result["message"] == "Test error"
        assert "arg1" in result["args"]

    def test_encode_message(self):
        """Test encoding message objects."""
        encoder = NatsWorkEncoder()
        msg = JobMessage(job_class="TestJob", queue="default")
        result = encoder.default(msg)
        assert isinstance(result, dict)
        assert result["job_class"] == "TestJob"


class TestProtocolValidator:
    """Test ProtocolValidator class."""

    def test_validate_valid_job_id(self):
        """Test validating valid UUID."""
        job_id = str(uuid.uuid4())
        assert ProtocolValidator.validate_job_id(job_id) is True

    def test_validate_invalid_job_id(self):
        """Test validating invalid UUID."""
        assert ProtocolValidator.validate_job_id("not-a-uuid") is False

    def test_validate_valid_queue_names(self):
        """Test validating valid queue names."""
        valid_names = ["default", "high-priority", "low_priority", "queue123"]
        for name in valid_names:
            assert ProtocolValidator.validate_queue_name(name) is True

    def test_validate_invalid_queue_names(self):
        """Test validating invalid queue names."""
        invalid_names = ["with space", "with@symbol", "with.dot", ""]
        for name in invalid_names:
            assert ProtocolValidator.validate_queue_name(name) is False

    def test_validate_valid_job_classes(self):
        """Test validating valid job class names."""
        valid_classes = [
            "MyJob",
            "module.MyJob",
            "Module::MyJob",
            "deep.nested.module.Job",
            "_PrivateJob",
        ]
        for cls in valid_classes:
            assert ProtocolValidator.validate_job_class(cls) is True

    def test_validate_invalid_job_classes(self):
        """Test validating invalid job class names."""
        invalid_classes = ["123Job", "Job-Name", "Job Name", ""]
        for cls in invalid_classes:
            assert ProtocolValidator.validate_job_class(cls) is False


class TestVersionHandler:
    """Test VersionHandler class."""

    def test_current_version(self):
        """Test current version constant."""
        assert VersionHandler.CURRENT_VERSION == "1.0"

    def test_is_supported(self):
        """Test version support checking."""
        assert VersionHandler.is_supported("1.0") is True
        assert VersionHandler.is_supported("1.1") is True
        assert VersionHandler.is_supported("2.0") is False

    def test_upgrade_message_same_version(self):
        """Test upgrading message with same version."""
        message = {"version": "1.0", "data": "test"}
        result = VersionHandler.upgrade_message(message, "1.0")
        assert result == message

    def test_upgrade_message_different_version(self):
        """Test upgrading message to newer version."""
        message = {"version": "1.0", "data": "test"}
        result = VersionHandler.upgrade_message(message, "1.0", "1.1")
        assert result["version"] == "1.1"
        assert result["data"] == "test"


class TestCrossLanguageCompatibility:
    """Test cross-language protocol compatibility."""

    def test_ruby_style_message_deserialization(self):
        """Test deserializing Ruby-style JSON message."""
        # Simulate a message from Ruby with symbol-like keys
        ruby_json = {
            "job_id": str(uuid.uuid4()),
            "job_class": "MyApp::TestJob",  # Ruby-style class name
            "queue": "default",
            "arguments": ["arg1", "arg2"],
            "options": {"retry": True},
            "retry_count": 0,
            "max_retries": 3,
            "metadata": {},
            "created_at": "2024-01-01T12:00:00Z",  # ISO8601 with Z
            "version": "1.0",
        }
        data = json.dumps(ruby_json).encode("utf-8")

        msg = MessageSerializer.deserialize(data, JobMessage)
        assert msg.job_class == "MyApp::TestJob"
        assert msg.arguments == ["arg1", "arg2"]
        assert msg.options == {"retry": True}

    def test_python_message_ruby_compatible(self):
        """Test Python message is Ruby-compatible."""
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments=["arg1"],
        )

        serialized = MessageSerializer.serialize(msg)
        json_dict = json.loads(serialized.decode("utf-8"))

        # Check Ruby-expected fields exist
        assert "job_id" in json_dict
        assert "job_class" in json_dict
        assert "queue" in json_dict
        assert "created_at" in json_dict
        assert json_dict["created_at"].endswith("Z")  # Ruby expects Z suffix


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_large_message_serialization(self):
        """Test serializing large messages."""
        # Create a large payload
        large_data = {"key": "x" * 10000, "array": list(range(1000))}
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments=large_data,
        )

        serialized = MessageSerializer.serialize(msg)
        deserialized = MessageSerializer.deserialize(serialized, JobMessage)
        assert deserialized.arguments == large_data

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        unicode_data = {
            "emoji": "🚀",
            "chinese": "你好",
            "arabic": "مرحبا",
            "special": "café",
        }
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments=unicode_data,
        )

        serialized = MessageSerializer.serialize(msg)
        deserialized = MessageSerializer.deserialize(serialized, JobMessage)
        assert deserialized.arguments == unicode_data

    def test_none_values(self):
        """Test handling None values in messages."""
        msg = ResultMessage(
            job_id=str(uuid.uuid4()),
            status="success",
            result=None,
            error=None,
            processing_time=0,
        )

        serialized = MessageSerializer.serialize(msg)
        deserialized = MessageSerializer.deserialize(serialized, ResultMessage)
        assert deserialized.result is None
        assert deserialized.error is None

    def test_empty_collections(self):
        """Test handling empty collections."""
        msg = JobMessage(
            job_class="TestJob",
            queue="default",
            arguments=[],
            options={},
            metadata={},
        )

        serialized = MessageSerializer.serialize(msg)
        deserialized = MessageSerializer.deserialize(serialized, JobMessage)
        assert deserialized.arguments == []
        assert deserialized.options == {}
        assert deserialized.metadata == {}
