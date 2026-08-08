from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from .contracts import RunStatus


@dataclass
class LoopState:
    status: RunStatus = RunStatus.PENDING
    iteration: int = 0
    max_iterations: int = 12
    retry_budget: int = 6
    max_wall_seconds: int = 3600
    max_model_calls: int = 12
    max_agent_calls: int = 8
    max_tool_calls: int = 80
    max_tokens: Optional[int] = None
    usage: Dict[str, int] = field(default_factory=dict)
    no_progress_count: int = 0
    repeated_error_count: int = 0
    last_progress_hash: str = ""
    last_error_fingerprint: str = ""
    decisions: List[Dict[str, Any]] = field(default_factory=list)
    result: Optional[Dict[str, Any]] = None


class LoopExecutor:
    """Bounded PLAN → EXECUTE → VALIDATE → ACT executor."""

    def __init__(self, max_no_progress: int = 3, max_same_error: int = 3):
        self.max_no_progress = max_no_progress
        self.max_same_error = max_same_error

    def run(
        self,
        plan: Callable[[LoopState], Dict[str, Any]],
        execute: Callable[[Dict[str, Any]], Dict[str, Any]],
        validate: Callable[[Dict[str, Any]], Dict[str, Any]],
        state: Optional[LoopState] = None,
        on_iteration: Optional[Callable[[LoopState], None]] = None,
    ) -> LoopState:
        state = state or LoopState()
        state.status = RunStatus.RUNNING
        started = time.monotonic()
        while state.iteration < state.max_iterations:
            if time.monotonic() - started >= state.max_wall_seconds:
                state.status = RunStatus.BUDGET_EXHAUSTED
                return state
            state.iteration += 1
            try:
                work = execute(plan(state))
                self._record_usage(state, work.get("_usage", {}))
                if self._budget_exhausted(state):
                    state.status = RunStatus.BUDGET_EXHAUSTED
                    return state
                verdict = validate(work)
                if verdict.get("ok"):
                    state.result = work
                    state.status = RunStatus.COMPLETED
                    if on_iteration:
                        on_iteration(state)
                    return state
                self._track_progress(state, verdict)
            except Exception as exc:  # executor boundary: converted to typed loop state
                state.retry_budget -= 1
                self._track_error(state, exc)
            if on_iteration:
                on_iteration(state)
            if state.retry_budget < 0 or state.no_progress_count >= self.max_no_progress:
                state.status = RunStatus.FAILED
                return state
            if state.repeated_error_count >= self.max_same_error:
                state.status = RunStatus.FAILED
                return state
        state.status = RunStatus.BUDGET_EXHAUSTED
        return state

    @staticmethod
    def _fingerprint(value: Any) -> str:
        return hashlib.sha256(repr(value).encode("utf-8")).hexdigest()[:16]

    def _track_progress(self, state: LoopState, verdict: Dict[str, Any]) -> None:
        fingerprint = self._fingerprint(verdict.get("progress", verdict))
        state.no_progress_count = state.no_progress_count + 1 if fingerprint == state.last_progress_hash else 0
        state.last_progress_hash = fingerprint
        state.decisions.append({"iteration": state.iteration, "verdict": verdict})

    def _track_error(self, state: LoopState, exc: Exception) -> None:
        fingerprint = self._fingerprint((type(exc).__name__, str(exc)))
        state.repeated_error_count = state.repeated_error_count + 1 if fingerprint == state.last_error_fingerprint else 1
        state.last_error_fingerprint = fingerprint
        state.decisions.append({"iteration": state.iteration, "error": str(exc), "fingerprint": fingerprint})

    @staticmethod
    def _record_usage(state: LoopState, usage: Dict[str, int]) -> None:
        for key in ("model_calls", "agent_calls", "tool_calls", "tokens"):
            state.usage[key] = state.usage.get(key, 0) + int(usage.get(key, 0) or 0)

    @staticmethod
    def _budget_exhausted(state: LoopState) -> bool:
        limits = {
            "model_calls": state.max_model_calls,
            "agent_calls": state.max_agent_calls,
            "tool_calls": state.max_tool_calls,
            "tokens": state.max_tokens,
        }
        return any(limit is not None and state.usage.get(key, 0) > limit for key, limit in limits.items())
