"""Message protocol implementation for NatsWork server."""

# Re-export all message types from client for consistency
from natswork_client.messages import (
    BaseMessage,
    ControlMessage,
    JobMessage,
    MessageBuilder,
    MessageError,
    MessageSerializer,
    NatsWorkEncoder,
    ProtocolError,
    ProtocolValidator,
    ResultMessage,
    SerializationError,
    ValidationError,
    VersionHandler,
)

__all__ = [
    "BaseMessage",
    "JobMessage",
    "ResultMessage",
    "ControlMessage",
    "MessageBuilder",
    "MessageSerializer",
    "NatsWorkEncoder",
    "ProtocolValidator",
    "VersionHandler",
    "MessageError",
    "SerializationError",
    "ValidationError",
    "ProtocolError",
]
