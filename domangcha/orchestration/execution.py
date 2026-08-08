from __future__ import annotations

import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .checkpoint import CheckpointStore
from .contracts import GraphState, Route, RunStatus
from .events import EventWriter
from .intent import IntentNormalizer
from .router import TaskRouter


class ExecutionCoordinator:
    """Lifecycle owner shared by CLI, Claude hooks, and Codex adapters."""

    def __init__(self, workspace: Path, events: Optional[EventWriter] = None):
        self.workspace = workspace
        self.checkpoints = CheckpointStore(workspace / ".domangcha" / "checkpoints")
        self.events = events or EventWriter(workspace / ".domangcha" / "events.jsonl")
        self.normalizer = IntentNormalizer()
        self.router = TaskRouter()

    def start(self, request: str, minimum: Optional[Route] = None, task_id: Optional[str] = None) -> GraphState:
        intent = self.normalizer.normalize(request)
        decision = self.router.route(intent, minimum=minimum)
        now = datetime.now(timezone.utc).isoformat()
        state = GraphState(
            task_id=task_id or uuid.uuid4().hex,
            request=request,
            normalized_intent=intent,
            route=decision.route,
            status=RunStatus.PENDING,
            started_at=now,
            updated_at=now,
            route_history=[{"route": decision.route.value, "reasons": decision.reasons, "at": now}],
        )
        self.checkpoints.write(state.task_id, state.to_dict())
        self.events.emit("task_received", task_id=state.task_id)
        self.events.emit("route_selected", task_id=state.task_id, route=decision.route.value, score=decision.score)
        return state

    def escalate(self, state: GraphState, reason: str) -> GraphState:
        decision = self.router.escalate(state.route, reason)
        state.route = decision.route
        state.route_history.append({"route": decision.route.value, "reason": reason})
        self.checkpoints.write(state.task_id, state.to_dict())
        self.events.emit("route_escalated", task_id=state.task_id, route=decision.route.value, reason=reason)
        return state

    def load(self, task_id: str) -> GraphState:
        return GraphState.from_dict(self.checkpoints.read(task_id))

    def approve(self, task_id: str, node_id: str, approved: bool, actor: str = "user") -> dict:
        state = self.checkpoints.read(task_id)
        state.setdefault("approvals", {})[node_id] = {
            "status": "APPROVED" if approved else "REJECTED",
            "actor": actor,
        }
        if not approved:
            state["status"] = RunStatus.ABORTED.value
        self.checkpoints.write(task_id, state)
        self.events.emit("approval_received", task_id=task_id, node_id=node_id, approved=approved)
        return state
