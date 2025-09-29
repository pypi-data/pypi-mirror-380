"""CloudTools SDK for building services on top of Temporal."""

from .client import ServiceClient, ServiceClientConfig
from .constants import WORKFLOW_ID_PREFIX
from .context import ServiceContext
from .eventbus import EventBusSettings, ServiceEventBus
from .logging_utils import capture_service_logs, temporary_log_file
from .router import (
    DuplicateServiceRegistrationError,
    RouterStartupError,
    ServiceRegistrationError,
)
from .runtime import ServiceRuntime
from .runtime.queue import QueueRuntimeConfig, TaskQueueRuntime
from .service import (
    CloudService,
    CloudServiceError,
    DuplicateRegistrationError,
    RuntimeNotConfiguredError,
    ExposureMetadata,
    UnknownActionError,
    UnknownTaskError,
)

__all__ = [
    "CloudService",
    "ServiceContext",
    "ServiceRuntime",
    "TaskQueueRuntime",
    "QueueRuntimeConfig",
    "ServiceEventBus",
    "EventBusSettings",
    "ServiceClient",
    "ServiceClientConfig",
    "CloudServiceError",
    "RuntimeNotConfiguredError",
    "DuplicateRegistrationError",
    "UnknownActionError",
    "UnknownTaskError",
    "ExposureMetadata",
    "RouterStartupError",
    "ServiceRegistrationError",
    "DuplicateServiceRegistrationError",
    "WORKFLOW_ID_PREFIX",
    "temporary_log_file",
    "capture_service_logs",
    "__version__",
]

__version__ = "0.1.0"
