#!/usr/bin/env python3
from __future__ import annotations

import json

from runtime import active_session, checkpoint, hook_payload, save_session, update_checkpoint, workspace


MAX_CONTINUATIONS = 3


def main() -> int:
    payload = hook_payload()
    root = workspace(payload)
    session_id = str(payload.get("session_id", "unknown"))
    session = active_session(root, session_id)
    if not session:
        print("{}")
        return 0
    try:
        state = checkpoint(root, session["task_id"])
    except Exception:
        print("{}")
        return 0
    if state.get("status") == "COMPLETED" or session.get("completed"):
        print("{}")
        return 0
    if state.get("route") == "DIRECT" and not session.get("mutation_observed"):
        state["status"] = "COMPLETED"
        state.setdefault("artifacts", {})["completion_evidence"] = {"kind": "direct_response"}
        update_checkpoint(root, session["task_id"], state)
        session["completed"] = True
        save_session(root, session_id, session)
        print("{}")
        return 0
    count = int(session.get("continuations", 0))
    if count >= MAX_CONTINUATIONS:
        state["status"] = "FAILED"
        state.setdefault("errors", []).append({"terminal": True, "error": "Codex completion evidence missing after bounded continuations"})
        update_checkpoint(root, session["task_id"], state)
        print(json.dumps({"systemMessage": "DOMANGCHA stopped after bounded continuation attempts; task checkpoint is FAILED."}))
        return 0
    session["continuations"] = count + 1
    save_session(root, session_id, session)
    missing = []
    if session.get("mutation_observed") and not session.get("validation_observed"):
        missing.append("run a successful task-relevant validation command")
    missing.append("call the injected DOMANGCHA control command with `complete --task-id %s --summary ...`" % session["task_id"])
    print(json.dumps({
        "decision": "block",
        "reason": "DOMANGCHA task is not complete: " + "; then ".join(missing) + "."
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
