#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from runtime import active_session, checkpoint, coordinator, hook_payload, save_session, workspace


def control_context(state, control: Path) -> str:
    reasons = "; ".join(
        reason
        for item in state.get("route_history", [])
        for reason in item.get("reasons", [])
    )
    return """[DOMANGCHA CODEX CONTROL]
task_id={task_id} route={route}
reasons={reasons}
control=python3 \"{control}\"

The lifecycle hook already selected the canonical route. Use the DOMANGCHA skill workflow, record progress, run relevant validation, and call the exact control command with `complete` before claiming completion. Do not create another router. Destructive or irreversible work still requires explicit user approval.
""".format(task_id=state["task_id"], route=state["route"], reasons=reasons, control=control)


def main() -> int:
    payload = hook_payload()
    prompt = str(payload.get("prompt", "")).strip()
    if not prompt:
        return 0
    root = workspace(payload)
    session_id = str(payload.get("session_id", "unknown"))
    control = Path(__file__).with_name("control.py").resolve()
    existing = active_session(root, session_id)
    if existing and not existing.get("completed"):
        try:
            persisted = checkpoint(root, existing["task_id"])
        except Exception:
            persisted = {}
        if persisted.get("status") not in {"COMPLETED", "FAILED", "ABORTED"}:
            persisted.setdefault("decisions", []).append({"kind": "user_followup", "prompt": prompt[:1000]})
            coordinator(root).checkpoints.write(existing["task_id"], persisted)
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": control_context(persisted, control),
                }
            }, ensure_ascii=False))
            return 0
    try:
        state = coordinator(root).start(prompt)
    except Exception as exc:
        print(json.dumps({"systemMessage": "DOMANGCHA degraded: %s" % exc}))
        return 0
    session = {
        "task_id": state.task_id,
        "route": state.route.value,
        "continuations": 0,
        "mutation_observed": False,
        "validation_observed": False,
        "review_observed": False,
    }
    save_session(root, session_id, session)
    context = control_context(state.to_dict(), control)
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
