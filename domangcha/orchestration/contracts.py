from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class Route(str, Enum):
    DIRECT = "DIRECT"
    LOOP = "LOOP"
    GRAPH = "GRAPH"


class RunStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    WAITING_FOR_APPROVAL = "WAITING_FOR_APPROVAL"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


class NodeType(str, Enum):
    DETERMINISTIC = "DETERMINISTIC"
    LLM = "LLM"
    AGENT = "AGENT"
    TOOL = "TOOL"
    VALIDATOR = "VALIDATOR"
    HUMAN_GATE = "HUMAN_GATE"
    JOIN = "JOIN"


class Idempotency(str, Enum):
    PURE = "PURE"
    IDEMPOTENT = "IDEMPOTENT"
    NON_IDEMPOTENT = "NON_IDEMPOTENT"


class JoinStrategy(str, Enum):
    ALL = "ALL"
    ANY = "ANY"
    QUORUM = "QUORUM"
    BEST_EFFORT = "BEST_EFFORT"


@dataclass
class Budget:
    model_calls: int = 12
    agent_calls: int = 12
    tool_calls: int = 80
    retries: int = 6
    parallel_branches: int = 4
    wall_seconds: int = 3600
    token_budget: Optional[int] = None


@dataclass
class RuntimeCapabilities:
    runtime: str = "UNKNOWN"
    interactive_approval: bool = False
    background_execution: bool = False
    subagents: bool = False
    hooks: bool = False
    shell: bool = True
    network: bool = False
    browser: bool = False
    checkpointing: bool = True
    parallelism: int = 1
    workspace_write: bool = True


@dataclass
class RouteDecision:
    route: Route
    score: int
    reasons: List[str]
    approval_required: bool = False
    ambiguous: bool = False
    proposed_route: Optional[Route] = None


@dataclass
class NodeSpec:
    id: str
    type: NodeType
    timeout_seconds: int = 300
    max_attempts: int = 1
    idempotency: Idempotency = Idempotency.PURE
    required_capabilities: List[str] = field(default_factory=list)
    input_fields: List[str] = field(default_factory=list)
    input_schema: Dict[str, Any] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)
    failure_destination: Optional[str] = None
    fallback_destination: Optional[str] = None
    optional: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EdgeSpec:
    source: str
    target: str
    guard: str = "always"
    priority: int = 0
    failure_behavior: str = "FAIL"


@dataclass
class GraphState:
    task_id: str
    request: str
    normalized_intent: Dict[str, Any]
    route: Route
    graph_id: str = ""
    graph_version: str = "1"
    current_node: Optional[str] = None
    status: RunStatus = RunStatus.PENDING
    artifacts: Dict[str, str] = field(default_factory=dict)
    node_results: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    errors: List[Dict[str, Any]] = field(default_factory=list)
    attempt_counts: Dict[str, int] = field(default_factory=dict)
    approvals: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    decisions: List[Dict[str, Any]] = field(default_factory=list)
    route_history: List[Dict[str, Any]] = field(default_factory=list)
    completed_nodes: List[str] = field(default_factory=list)
    pending_nodes: List[str] = field(default_factory=list)
    budget: Budget = field(default_factory=Budget)
    usage: Dict[str, int] = field(default_factory=dict)
    started_at: str = ""
    updated_at: str = ""
    checkpoint_version: int = 1

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GraphState":
        values = dict(data)
        values["route"] = Route(values["route"])
        values["status"] = RunStatus(values.get("status", "PENDING"))
        values["budget"] = Budget(**values.get("budget", {}))
        allowed = set(cls.__dataclass_fields__)
        return cls(**{key: value for key, value in values.items() if key in allowed})
