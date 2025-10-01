import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, Optional, Set

from .nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


@dataclass
class JobStatusInfo:
    job_id: str
    status: JobStatus
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    retry_count: int = 0
    error: Optional[str] = None
    progress: Dict[str, Any] = field(default_factory=dict)


class JobStatusTracker:

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager
        self._status_cache: Dict[str, JobStatusInfo] = {}
        self._status_subscriptions: Set[str] = set()

    async def get_status(self, job_id: str) -> Optional[JobStatusInfo]:
        if job_id in self._status_cache:
            return self._status_cache[job_id]

        try:
            nc = await self.connection_manager.connect()
            subject = f"natswork.status.{job_id}"

            reply = await nc.request(subject, b"", timeout=5.0)
            status_data = json.loads(reply.data.decode())

            started_at = (
                datetime.fromisoformat(status_data["started_at"]) if status_data.get("started_at") else None
            )
            completed_at = (
                datetime.fromisoformat(status_data["completed_at"]) if status_data.get("completed_at") else None
            )

            status_info = JobStatusInfo(
                job_id=job_id,
                status=JobStatus(status_data["status"]),
                created_at=datetime.fromisoformat(status_data["created_at"]),
                started_at=started_at,
                completed_at=completed_at,
                retry_count=status_data.get("retry_count", 0),
                error=status_data.get("error"),
                progress=status_data.get("progress", {})
            )

            self._status_cache[job_id] = status_info
            return status_info

        except Exception as e:
            logger.warning(f"Could not get status for job {job_id}: {e}")
            return None

    def subscribe_to_status_updates(self, job_id: str, callback: Callable[[JobStatusInfo], None]):
        pass
