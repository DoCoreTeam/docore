#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from domangcha.adapters.runtime import RuntimeDetector
from domangcha.orchestration.contracts import Route
from domangcha.orchestration.intent import IntentNormalizer
from domangcha.orchestration.execution import ExecutionCoordinator
from domangcha.orchestration.router import TaskRouter
from domangcha.orchestration.validation import RepositoryValidator


COMMAND_MINIMUM = {
    "ceo-ralph": Route.LOOP,
    "ceo-debug": Route.LOOP,
    "ceo-security": Route.GRAPH,
    "ceo-ship": Route.GRAPH,
}


def route_request(request: str) -> dict:
    intent = IntentNormalizer().normalize(request)
    minimum = COMMAND_MINIMUM.get(intent.get("explicit_command", ""))
    decision = TaskRouter().route(intent, minimum=minimum)
    runtime = RuntimeDetector().detect()
    return {
        "intent": intent,
        "route": decision.route.value,
        "score": decision.score,
        "reasons": decision.reasons,
        "approval_required": decision.approval_required,
        "ambiguous": decision.ambiguous,
        "runtime": runtime.runtime,
        "capabilities": runtime.__dict__,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="DOMANGCHA adaptive execution engine")
    sub = parser.add_subparsers(dest="command", required=True)
    route = sub.add_parser("route", help="classify a request")
    route.add_argument("request", nargs="?")
    validate = sub.add_parser("validate", help="validate repository invariants")
    validate.add_argument("--root", default=".")
    start = sub.add_parser("start", help="create a resumable execution state")
    start.add_argument("request")
    start.add_argument("--workspace", default=".")
    status = sub.add_parser("status", help="read a checkpoint")
    status.add_argument("task_id")
    status.add_argument("--workspace", default=".")
    approve = sub.add_parser("approve", help="resolve a HUMAN_GATE")
    approve.add_argument("task_id")
    approve.add_argument("node_id")
    approve.add_argument("decision", choices=("approve", "reject"))
    approve.add_argument("--workspace", default=".")
    args = parser.parse_args()
    if args.command == "route":
        request = args.request if args.request is not None else sys.stdin.read()
        print(json.dumps(route_request(request), ensure_ascii=False, indent=2))
        return 0
    if args.command == "start":
        state = ExecutionCoordinator(Path(args.workspace).resolve()).start(args.request)
        print(json.dumps(state.to_dict(), ensure_ascii=False, indent=2))
        return 0
    if args.command == "status":
        coordinator = ExecutionCoordinator(Path(args.workspace).resolve())
        print(json.dumps(coordinator.checkpoints.read(args.task_id), ensure_ascii=False, indent=2))
        return 0
    if args.command == "approve":
        coordinator = ExecutionCoordinator(Path(args.workspace).resolve())
        state = coordinator.approve(args.task_id, args.node_id, args.decision == "approve")
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0
    validator = RepositoryValidator(Path(args.root).resolve())
    errors = validator.validate_manifests() + validator.validate_versions() + validator.validate_graphs()
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
