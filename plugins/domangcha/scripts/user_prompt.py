#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from runtime import active_session, checkpoint, coordinator, hook_payload, reporter, save_session, workspace


REPORTING_CONTRACT = """Status reporting is on by default. Report progress to the user, in the user's language:
- Open the reply with the route card above so the user knows what is running and why.
- LOOP: report `iteration n/N`, remaining retry budget, and the one thing that actually changed this pass.
- GRAPH: report node progress (done / running / waiting) and, for parallel branches, the branch list at
  fan-out and the success/failure plus join strategy at join.
- Do not go silent through long steps; announce start, midpoint, and end briefly.
- Explain in plain language what needs approval and why before pausing at a gate.
- Say failures plainly, together with the next action. Never hide a stalled loop."""


def control_context(state, control: Path, card: str = "") -> str:
    reasons = "; ".join(
        reason
        for item in state.get("route_history", [])
        for reason in item.get("reasons", [])
    )
    return """[DOMANGCHA CODEX CONTROL]
{card}
task_id={task_id} route={route}
reasons={reasons}
control=python3 \"{control}\"

{contract}

The lifecycle hook already selected the canonical route. Use the DOMANGCHA skill workflow, record progress, run relevant validation, and call the exact control command with `complete` before claiming completion. Do not create another router. Destructive or irreversible work still requires explicit user approval.
""".format(
        card=(card + "\n") if card else "",
        task_id=state["task_id"],
        route=state["route"],
        reasons=reasons,
        control=control,
        contract=REPORTING_CONTRACT,
    )


def status_card(root: Path, state: dict) -> str:
    renderer = reporter(root)
    return renderer.graph_card(state) if renderer else ""


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
                    "additionalContext": control_context(persisted, control, status_card(root, persisted)),
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
    renderer = reporter(root)
    card = renderer.route_card({"route": state.route.value, "reasons": [
        reason for item in state.route_history for reason in item.get("reasons", [])
    ]}) if renderer else ""
    context = control_context(state.to_dict(), control, card)
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
