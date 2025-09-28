"""Chaturbate Events API Python package.

This package provides an async Python wrapper for the Chaturbate Events API.

See individual module docstrings and the project README for usage examples and details.
"""

from importlib.metadata import version as get_version

from .client import EventClient
from .config import EventClientConfig
from .models import (
    Event,
    EventType,
    Message,
    RoomSubject,
    Tip,
    User,
)
from .router import EventRouter

__version__ = get_version("chaturbate-events")
__all__ = [
    "Event",
    "EventClient",
    "EventClientConfig",
    "EventRouter",
    "EventType",
    "Message",
    "RoomSubject",
    "Tip",
    "User",
]
