import json
import os
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ClientConfig:
    servers: List[str] = field(default_factory=lambda: ["nats://localhost:4222"])
    max_reconnect_attempts: int = 10
    reconnect_time_wait: float = 2.0
    connection_timeout: float = 10.0
    request_timeout: float = 30.0
    connection_pool_size: int = 10
    enable_status_tracking: bool = True
    enable_result_callbacks: bool = True
    result_buffer_size: int = 1000

    tls_cert: Optional[str] = None
    tls_key: Optional[str] = None
    tls_ca: Optional[str] = None

    username: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None

    @classmethod
    def from_env(cls) -> 'ClientConfig':
        return cls(
            servers=os.getenv("NATS_SERVERS", "nats://localhost:4222").split(","),
            username=os.getenv("NATS_USERNAME"),
            password=os.getenv("NATS_PASSWORD"),
            token=os.getenv("NATS_TOKEN"),
            tls_cert=os.getenv("NATS_TLS_CERT"),
            tls_key=os.getenv("NATS_TLS_KEY"),
            tls_ca=os.getenv("NATS_TLS_CA")
        )

    @classmethod
    def from_file(cls, config_path: str) -> 'ClientConfig':
        with open(config_path) as f:
            config_data = json.load(f)
        return cls(**config_data)
