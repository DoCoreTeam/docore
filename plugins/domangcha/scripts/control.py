#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from runtime import checkpoint, find_session_for_task, read_json, update_checkpoint, write_json


def evidence(root: Path, task_id: str):
    session_path = find_session_for_task(root, task_id)
    return session_path, read_json(session_path) if session_path else {}


def main() -> int:
    parser = argparse.ArgumentParser(description="DOMANGCHA Codex control plane")
    parser.add_argument("action", choices=("status", "resume", "progress", "complete"))
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--message")
    parser.add_argument("--summary")
    parser.add_argument("--review")
    args = parser.parse_args()
    root = Path(args.workspace).resolve()
    state = checkpoint(root, args.task_id)
    session_path, session = evidence(root, args.task_id)
    if args.action in {"status", "resume"}:
        print(json.dumps({"state": state, "codex": session}, ensure_ascii=False, indent=2))
        return 0
    now = datetime.now(timezone.utc).isoformat()
    if args.action == "progress":
        if not args.message:
            parser.error("progress requires --message")
        state.setdefault("decisions", []).append({"at": now, "kind": "progress", "message": args.message})
        update_checkpoint(root, args.task_id, state)
        print(json.dumps({"ok": True, "task_id": args.task_id}))
        return 0
    if not args.summary:
        parser.error("complete requires --summary")
    route = state.get("route", "DIRECT")
    missing = []
    if session.get("mutation_observed") and not session.get("validation_observed"):
        missing.append("successful validation command")
    if route == "GRAPH" and session.get("mutation_observed") and not (session.get("review_observed") or args.review):
        missing.append("independent review evidence")
    if missing:
        print(json.dumps({"ok": False, "missing": missing}, ensure_ascii=False))
        return 2
    state["status"] = "COMPLETED"
    state["updated_at"] = now
    state.setdefault("artifacts", {})["completion_evidence"] = {
        "summary": args.summary,
        "review": args.review,
        "validation_commands": session.get("validation_commands", []),
    }
    update_checkpoint(root, args.task_id, state)
    session["completed"] = True
    if session_path:
        write_json(session_path, session)
    print(json.dumps({"ok": True, "task_id": args.task_id, "status": "COMPLETED"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
