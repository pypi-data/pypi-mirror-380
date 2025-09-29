"""Workflow-aware service context utilities."""
from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING
from uuid import uuid4

from temporalio import workflow

from ..constants import WORKFLOW_ID_PREFIX
from ..context import ServiceContext

if TYPE_CHECKING:  # pragma: no cover - for static analysis only
    from ..service import CloudService, UnknownTaskError
    from .queue import TaskQueueRuntime


class WorkflowServiceContext(ServiceContext):
    """Service context that proxies actions via workflow activities."""

    def __init__(
        self,
        service: "CloudService",
        runtime: "TaskQueueRuntime",
        *,
        metadata: Optional[dict[str, Any]] = None,
    ) -> None:
        self._runtime = runtime
        super().__init__(
            service,
            metadata=metadata,
            action_handler=self._execute_action,
            call_handler=self._call_service,
            emit_handler=self._emit_event,
        )

    async def _execute_action(self, name: str, *args: Any, **kwargs: Any) -> Any:
        activity_name = self._runtime.activity_name(self.service.name, name)
        payload = {
            "args": args,
            "kwargs": kwargs,
        }
        result = await workflow.execute_activity(
            activity_name,
            payload,
            schedule_to_close_timeout=self._runtime.config.activity_timeout,
            start_to_close_timeout=self._runtime.config.activity_timeout,
        )
        return result

    async def execute_child_task(self, name: str, payload: Any, **kwargs: Any) -> Any:
        """Start a child workflow for a task and wait for the result."""
        service_name, task_name, workflow_name = self._resolve_target(name)
        options = self._compose_child_options(service_name, task_name, kwargs)
        return await workflow.execute_child_workflow(
            workflow_name,
            payload,
            **options,
        )

    async def start_child_task(
        self,
        name: str,
        payload: Any,
        **kwargs: Any,
    ) -> workflow.ChildWorkflowHandle[Any, Any]:
        """Start a child workflow for a task and return its handle."""
        service_name, task_name, workflow_name = self._resolve_target(name)
        options = self._compose_child_options(service_name, task_name, kwargs)
        return await workflow.start_child_workflow(
            workflow_name,
            payload,
            **options,
        )

    async def _call_service(self, target: str, payload: Any) -> Any:
        return await self.execute_child_task(target, payload)

    async def _emit_event(self, topic: str, payload: Any) -> None:
        event_bus = self._runtime.event_bus
        if event_bus is None:
            raise NotImplementedError("EventBus is not configured for this runtime.")
        await event_bus.publish(topic, payload, metadata=dict(self.metadata))

    def _resolve_target(self, name: str) -> tuple[str, str, str]:
        service_name, task_name = self._parse_target(name)
        routed_service = self._map_service_name(service_name)
        if routed_service == self.service.name and task_name not in self.service.tasks:
            from ..service import UnknownTaskError

            raise UnknownTaskError(f"Task '{task_name}' is not registered.")
        workflow_name = self._runtime.workflow_name(routed_service, task_name)
        return routed_service, task_name, workflow_name

    def _parse_target(self, raw: str) -> tuple[str, str]:
        if "." in raw:
            service_name, task_name = raw.split(".", 1)
            return service_name, task_name
        return self.service.name, raw

    def _map_service_name(self, requested: str) -> str:
        from ..router import RouterStartupError, get_router_client

        try:
            router = get_router_client()
        except RouterStartupError as exc:  # pragma: no cover - should be ready
            raise RuntimeError(
                "Router client is not ready for workflow call resolution."
            ) from exc
        return router.resolve_service(requested)

    def _compose_child_options(
        self,
        service_name: str,
        task_name: str,
        options: dict[str, Any],
    ) -> dict[str, Any]:
        merged = dict(options)
        if "task_queue" not in merged and service_name != self.service.name:
            merged["task_queue"] = f"{service_name}-queue"
        if "id" not in merged:
            merged["id"] = f"{WORKFLOW_ID_PREFIX}-{service_name}-{task_name}-{uuid4()}"
        return merged
