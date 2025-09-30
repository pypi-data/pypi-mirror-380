"""Default runtime factory for CloudService."""
from __future__ import annotations

from typing import TYPE_CHECKING

from .queue import TaskQueueRuntime

if TYPE_CHECKING:  # pragma: no cover - for type checking only
    from ..service import CloudService
    from .base import ServiceRuntime


def default_runtime_factory(service: "CloudService") -> "ServiceRuntime":
    """Return the default runtime instance for the given service."""
    return TaskQueueRuntime()
