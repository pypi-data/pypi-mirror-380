"""Message protocol implementation for NatsWork."""

import json
import re
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional, Type, Union

from pydantic import BaseModel, Field, field_serializer, field_validator


class BaseMessage(BaseModel):
    """Base message structure for all NatsWork messages."""

    job_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="UUID for job identification")
    job_class: str = Field(..., description="Fully qualified job class name")
    queue: str = Field(..., description="Target queue name")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    version: str = Field(default="1.0", description="Protocol version")

    @field_validator("job_id")
    @classmethod
    def validate_job_id(cls, v: str) -> str:
        """Validate UUID format."""
        try:
            uuid.UUID(v)
        except ValueError:
            raise ValueError(f"Invalid job_id format: {v}")
        return v

    @field_validator("queue")
    @classmethod
    def validate_queue(cls, v: str) -> str:
        """Validate queue naming conventions."""
        if not re.match(r"^[a-zA-Z0-9_-]+$", v):
            raise ValueError(f"Invalid queue name: {v}")
        return v

    @field_validator("job_class")
    @classmethod
    def validate_job_class(cls, v: str) -> str:
        """Validate job class name format."""
        # Allow both Python (module.Class) and Ruby (Module::Class) formats
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_.:]*$", v):
            raise ValueError(f"Invalid job class format: {v}")
        return v

    @field_serializer('created_at')
    def serialize_created_at(self, dt: datetime) -> str:
        """Serialize datetime to ISO8601 with Z suffix."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")


class JobMessage(BaseMessage):
    """Job dispatch message."""

    arguments: Union[List[Any], Dict[str, Any]] = Field(default_factory=list)
    options: Dict[str, Any] = Field(default_factory=dict)
    retry_count: int = Field(default=0)
    max_retries: int = Field(default=3)
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional job metadata")


class ResultMessage(BaseModel):
    """Job result message."""

    job_id: str
    status: Literal["success", "error", "retry"]
    result: Optional[Any] = None
    error: Optional[Dict[str, str]] = None
    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    processing_time: float = Field(description="Execution time in seconds")
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @field_validator("job_id")
    @classmethod
    def validate_job_id(cls, v: str) -> str:
        """Validate UUID format."""
        try:
            uuid.UUID(v)
        except ValueError:
            raise ValueError(f"Invalid job_id format: {v}")
        return v

    @field_serializer('completed_at')
    def serialize_completed_at(self, dt: datetime) -> str:
        """Serialize datetime to ISO8601 with Z suffix."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")


class ControlMessage(BaseModel):
    """Control message for job management."""

    type: Literal["cancel", "pause", "resume", "status"]
    job_id: Optional[str] = None
    queue: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @field_serializer('timestamp')
    def serialize_timestamp(self, dt: datetime) -> str:
        """Serialize datetime to ISO8601 with Z suffix."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")


class MessageBuilder:
    """Builder for creating NatsWork messages."""

    @staticmethod
    def build_job_message(
        job_class: str,
        queue: str,
        arguments: Union[List, Dict] = None,
        options: Dict = None,
        job_id: str = None,
        metadata: Dict = None,
    ) -> JobMessage:
        """Build a job dispatch message."""
        return JobMessage(
            job_id=job_id or str(uuid.uuid4()),
            job_class=job_class,
            queue=queue,
            arguments=arguments or [],
            options=options or {},
            metadata=metadata or {},
        )

    @staticmethod
    def build_result_message(
        job_id: str,
        status: str,
        result: Any = None,
        error: Exception = None,
        processing_time: float = 0.0,
        metadata: Dict = None,
    ) -> ResultMessage:
        """Build a job result message."""
        error_dict = None
        if error:
            error_dict = {
                "class": error.__class__.__name__,
                "message": str(error),
                "args": str(error.args) if error.args else "",
            }

        return ResultMessage(
            job_id=job_id,
            status=status,
            result=result,
            error=error_dict,
            processing_time=processing_time,
            metadata=metadata or {},
        )

    @staticmethod
    def build_control_message(
        message_type: str, job_id: str = None, queue: str = None, metadata: Dict = None
    ) -> ControlMessage:
        """Build a control message."""
        return ControlMessage(type=message_type, job_id=job_id, queue=queue, metadata=metadata or {})


class NatsWorkEncoder(json.JSONEncoder):
    """Custom JSON encoder for NatsWork message types."""

    def default(self, obj):
        if isinstance(obj, datetime):
            # Ensure UTC timezone and format as ISO8601 with Z suffix
            if obj.tzinfo is None:
                obj = obj.replace(tzinfo=timezone.utc)
            return obj.isoformat().replace("+00:00", "Z")
        elif isinstance(obj, (BaseMessage, ResultMessage, ControlMessage)):
            return obj.model_dump()
        elif isinstance(obj, Exception):
            # Handle exceptions - use first arg as message if it exists
            if obj.args:
                message = str(obj.args[0])
            else:
                message = str(obj)
            return {"class": obj.__class__.__name__, "message": message, "args": str(obj.args) if obj.args else ""}
        return super().default(obj)


class MessageSerializer:
    """Message serialization and deserialization."""

    @classmethod
    def serialize(cls, message: Union[BaseMessage, ResultMessage, ControlMessage]) -> bytes:
        """Serialize message to JSON bytes."""
        # Use model_dump_json for proper Pydantic serialization
        json_str = message.model_dump_json()
        return json_str.encode("utf-8")

    @classmethod
    def deserialize(cls, data: bytes, message_type: Type[BaseModel]) -> BaseModel:
        """Deserialize JSON bytes to message object."""
        json_str = data.decode("utf-8")
        dict_data = json.loads(json_str)

        # Handle datetime strings
        for field in ["created_at", "completed_at", "timestamp"]:
            if field in dict_data and isinstance(dict_data[field], str):
                # Parse ISO8601 datetime string
                dt_str = dict_data[field].rstrip("Z")
                if "+" not in dt_str and "T" in dt_str:
                    dt_str += "+00:00"
                dict_data[field] = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

        return message_type.model_validate(dict_data)

    @classmethod
    def to_json_string(cls, message: Union[BaseMessage, ResultMessage, ControlMessage]) -> str:
        """Convert message to JSON string."""
        return message.model_dump_json()

    @classmethod
    def from_json_string(cls, json_str: str, message_type: Type[BaseModel]) -> BaseModel:
        """Create message from JSON string."""
        return cls.deserialize(json_str.encode("utf-8"), message_type)


class ProtocolValidator:
    """Protocol validation utilities."""

    @staticmethod
    def validate_job_id(job_id: str) -> bool:
        """Validate UUID format."""
        try:
            uuid.UUID(job_id)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_queue_name(queue: str) -> bool:
        """Validate queue naming conventions."""
        return bool(re.match(r"^[a-zA-Z0-9_-]+$", queue))

    @staticmethod
    def validate_job_class(job_class: str) -> bool:
        """Validate job class name format."""
        # Allow both Python (module.Class) and Ruby (Module::Class) formats
        return bool(re.match(r"^[a-zA-Z_][a-zA-Z0-9_.:]*$", job_class))


class VersionHandler:
    """Message version handling."""

    SUPPORTED_VERSIONS = ["1.0", "1.1"]
    CURRENT_VERSION = "1.0"

    @classmethod
    def is_supported(cls, version: str) -> bool:
        """Check if version is supported."""
        return version in cls.SUPPORTED_VERSIONS

    @classmethod
    def upgrade_message(cls, message_dict: Dict, from_version: str, to_version: str = None) -> Dict:
        """Upgrade message format between versions."""
        to_version = to_version or cls.CURRENT_VERSION

        if from_version == to_version:
            return message_dict

        # Version migration logic would go here
        # For now, just update the version field
        message_dict["version"] = to_version
        return message_dict


# Error classes
class MessageError(Exception):
    """Base class for message-related errors."""

    pass


class SerializationError(MessageError):
    """Raised when message serialization fails."""

    pass


class ValidationError(MessageError):
    """Raised when message validation fails."""

    pass


class ProtocolError(MessageError):
    """Raised when protocol compatibility issues occur."""

    pass
