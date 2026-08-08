from __future__ import annotations

from concurrent.futures import ALL_COMPLETED, FIRST_COMPLETED, ThreadPoolExecutor, TimeoutError, wait
from dataclasses import dataclass
import json
from pathlib import Path
import time
from typing import Any, Callable, Dict, List, Optional

from .contracts import EdgeSpec, GraphState, Idempotency, NodeSpec, NodeType, RunStatus


class GraphDefinitionError(ValueError):
    pass


class ApprovalRequired(RuntimeError):
    pass


@dataclass
class GraphDefinition:
    id: str
    version: str
    start: str
    nodes: List[NodeSpec]
    edges: List[EdgeSpec]

    @classmethod
    def from_path(cls, path: Path) -> "GraphDefinition":
        data = json.loads(path.read_text(encoding="utf-8"))
        nodes = [NodeSpec(
            id=item["id"],
            type=NodeType(item["type"]),
            timeout_seconds=item.get("timeout_seconds", 300),
            max_attempts=item.get("max_attempts", 1),
            idempotency=Idempotency(item.get("idempotency", "PURE")),
            required_capabilities=item.get("required_capabilities", []),
            input_fields=item.get("input_fields", []),
            input_schema=item.get("input_schema", {}),
            output_schema=item.get("output_schema", {}),
            failure_destination=item.get("failure_destination"),
            fallback_destination=item.get("fallback_destination"),
            optional=item.get("optional", False),
            metadata=item.get("metadata", {}),
        ) for item in data["nodes"]]
        edges = [EdgeSpec(**item) for item in data["edges"]]
        graph = cls(data["id"], data["version"], data["start"], nodes, edges)
        graph.validate()
        return graph

    def validate(self) -> None:
        ids = {node.id for node in self.nodes}
        if len(ids) != len(self.nodes) or self.start not in ids:
            raise GraphDefinitionError("invalid or duplicate node IDs")
        for edge in self.edges:
            if edge.source not in ids or edge.target not in ids:
                raise GraphDefinitionError("edge references unknown node")
        reachable = {self.start}
        changed = True
        while changed:
            changed = False
            for edge in self.edges:
                if edge.source in reachable and edge.target not in reachable:
                    reachable.add(edge.target)
                    changed = True
        if reachable != ids:
            raise GraphDefinitionError("unreachable nodes: " + ",".join(sorted(ids - reachable)))
        if not any(not any(edge.source == node.id for edge in self.edges) for node in self.nodes):
            raise GraphDefinitionError("graph has no terminal node")


class GraphExecutor:
    def __init__(self, handlers: Dict[str, Callable[[GraphState, NodeSpec], Dict[str, Any]]], events=None):
        self.handlers = handlers
        self.events = events

    def run(self, graph: GraphDefinition, state: GraphState, checkpoint=None) -> GraphState:
        graph.validate()
        nodes = {node.id: node for node in graph.nodes}
        state.graph_id, state.graph_version = graph.id, graph.version
        state.current_node = state.current_node or graph.start
        state.status = RunStatus.RUNNING
        run_started = time.monotonic()
        while state.current_node:
            if time.monotonic() - run_started >= state.budget.wall_seconds:
                state.status = RunStatus.BUDGET_EXHAUSTED
                state.errors.append({"terminal": True, "error": "wall time budget exhausted"})
                self._save(checkpoint, state)
                return state
            node = nodes[state.current_node]
            if node.type == NodeType.HUMAN_GATE and state.approvals.get(node.id, {}).get("status") == "REJECTED":
                state.status = RunStatus.ABORTED
                self._emit("approval_received", state, node, approved=False)
                self._save(checkpoint, state)
                return state
            if node.type == NodeType.HUMAN_GATE and not self._approved(state, node.id):
                state.status = RunStatus.WAITING_FOR_APPROVAL
                self._emit("approval_requested", state, node)
                self._save(checkpoint, state)
                return state
            self._emit("node_started", state, node, attempt=state.attempt_counts.get(node.id, 0) + 1)
            try:
                result = {"outcome": "approved"} if node.type == NodeType.HUMAN_GATE else self._execute_node(state, node)
            except Exception as exc:
                state.errors.append({"node": node.id, "terminal": True, "error": str(exc)})
                self._emit("node_failed", state, node, error=str(exc))
                destination = node.fallback_destination or node.failure_destination
                if destination:
                    state.current_node = destination
                    self._save(checkpoint, state)
                    continue
                if state.status != RunStatus.BUDGET_EXHAUSTED:
                    state.status = RunStatus.FAILED
                if self.events:
                    self.events.emit("graph_failed", task_id=state.task_id, graph_id=state.graph_id, error=str(exc))
                self._save(checkpoint, state)
                return state
            state.node_results[node.id] = result
            state.completed_nodes.append(node.id)
            self._emit("node_completed", state, node)
            try:
                state.current_node = self._next(graph, node.id, result)
            except GraphDefinitionError as exc:
                state.errors.append({"node": node.id, "terminal": True, "error": str(exc)})
                state.status = RunStatus.FAILED
                if self.events:
                    self.events.emit("graph_failed", task_id=state.task_id, graph_id=state.graph_id, error=str(exc))
                self._save(checkpoint, state)
                return state
            self._save(checkpoint, state)
        state.status = RunStatus.COMPLETED
        if self.events:
            self.events.emit("graph_completed", task_id=state.task_id, graph_id=state.graph_id)
        self._save(checkpoint, state)
        return state

    def _emit(self, event, state, node, **fields):
        if self.events:
            self.events.emit(event, task_id=state.task_id, graph_id=state.graph_id, node_id=node.id, **fields)

    def _execute_node(self, state: GraphState, node: NodeSpec) -> Dict[str, Any]:
        handler = self.handlers.get(node.id) or self.handlers.get(node.type.value)
        if not handler:
            raise GraphDefinitionError("missing handler for " + node.id)
        bucket = {
            NodeType.LLM: "model_calls",
            NodeType.AGENT: "agent_calls",
            NodeType.TOOL: "tool_calls",
        }.get(node.type)
        if bucket:
            used = state.usage.get(bucket, 0)
            if used >= getattr(state.budget, bucket):
                state.status = RunStatus.BUDGET_EXHAUSTED
                raise RuntimeError(bucket + " budget exhausted")
            state.usage[bucket] = used + 1
        attempts = state.attempt_counts.get(node.id, 0)
        last_error = None
        while attempts < node.max_attempts:
            attempts += 1
            state.attempt_counts[node.id] = attempts
            try:
                result = self._call(handler, state, node)
                if not isinstance(result, dict):
                    raise TypeError("node output must be an object")
                self._validate_schema(result, node.output_schema, "output")
                return result
            except Exception as exc:
                last_error = exc
                state.errors.append({"node": node.id, "attempt": attempts, "error": str(exc)})
                if node.idempotency == Idempotency.NON_IDEMPOTENT:
                    break
                if state.usage.get("retries", 0) >= state.budget.retries:
                    state.status = RunStatus.BUDGET_EXHAUSTED
                    raise
                state.usage["retries"] = state.usage.get("retries", 0) + 1
        raise last_error or RuntimeError("node failed")

    @staticmethod
    def _call(handler, state, node):
        pool = ThreadPoolExecutor(max_workers=1)
        source = state.to_dict()
        fields = node.input_fields or ["task_id", "artifacts"]
        context = {key: source.get(key) for key in fields}
        GraphExecutor._validate_schema(context, node.input_schema, "input")
        future = pool.submit(handler, context, node)
        try:
            return future.result(timeout=node.timeout_seconds)
        except TimeoutError:
            future.cancel()
            raise TimeoutError("node timed out: " + node.id)
        finally:
            pool.shutdown(wait=False)

    @staticmethod
    def _validate_schema(value: Dict[str, Any], schema: Dict[str, Any], label: str) -> None:
        if not schema:
            return
        for key in schema.get("required", []):
            if key not in value:
                raise ValueError("%s schema missing key: %s" % (label, key))
        types = {"string": str, "integer": int, "number": (int, float), "boolean": bool, "object": dict, "array": list}
        for key, spec in schema.get("properties", {}).items():
            expected = types.get(spec.get("type"))
            if key in value and expected and not isinstance(value[key], expected):
                raise ValueError("%s schema type mismatch: %s" % (label, key))

    @staticmethod
    def execute_wave(
        branches: Dict[str, Callable[[], Any]],
        strategy: str = "ALL",
        max_concurrency: int = 4,
        timeout_seconds: int = 300,
        quorum: Optional[int] = None,
        required_branches: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Execute a bounded dynamic fan-out with explicit join semantics."""
        if not branches or max_concurrency < 1:
            raise ValueError("wave requires branches and positive concurrency")
        results, errors = {}, {}
        pool = ThreadPoolExecutor(max_workers=min(max_concurrency, len(branches)))
        futures = {pool.submit(fn): name for name, fn in branches.items()}
        if strategy == "ANY":
            deadline = time.monotonic() + timeout_seconds
            done, pending = set(), set(futures)
            while pending and not results:
                remaining = max(0, deadline - time.monotonic())
                newly_done, pending = wait(pending, timeout=remaining, return_when=FIRST_COMPLETED)
                done.update(newly_done)
                for future in newly_done:
                    name = futures[future]
                    try:
                        results[name] = future.result()
                    except Exception as exc:
                        errors[name] = str(exc)
                if remaining <= 0:
                    break
        else:
            done, pending = wait(futures, timeout=timeout_seconds, return_when=ALL_COMPLETED)
        for future in done:
            name = futures[future]
            if name in results or name in errors:
                continue
            try:
                results[name] = future.result()
            except Exception as exc:
                errors[name] = str(exc)
        required_names = set(required_branches) if required_branches is not None else set(branches)
        required = quorum or len(required_names)
        success = {
            "ALL": required_names.issubset(results),
            "ANY": bool(results),
            "QUORUM": len(results) >= required,
            "BEST_EFFORT": bool(results),
        }.get(strategy)
        if success is None:
            pool.shutdown(wait=False)
            raise ValueError("unknown join strategy")
        for future in pending:
            future.cancel()
            errors[futures[future]] = "timeout_or_cancelled"
        pool.shutdown(wait=False)
        return {"ok": success, "results": results, "errors": errors, "strategy": strategy}

    @staticmethod
    def _approved(state: GraphState, node_id: str) -> bool:
        return state.approvals.get(node_id, {}).get("status") == "APPROVED"

    @staticmethod
    def _next(graph: GraphDefinition, source: str, result: Dict[str, Any]) -> Optional[str]:
        edges = sorted((x for x in graph.edges if x.source == source), key=lambda x: -x.priority)
        for edge in edges:
            if edge.guard == "always" or result.get("outcome") == edge.guard:
                return edge.target
        if edges:
            raise GraphDefinitionError("no edge guard matched for " + source)
        return None

    @staticmethod
    def _save(checkpoint, state: GraphState) -> None:
        if checkpoint:
            checkpoint.write(state.task_id, state.to_dict())
