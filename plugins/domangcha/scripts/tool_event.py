#!/usr/bin/env python3
from __future__ import annotations

import json
import re

from runtime import active_session, hook_payload, save_session, workspace


VALIDATION = re.compile(r"(^|\s)(test|pytest|unittest|jest|vitest|lint|typecheck|tsc|build|cargo test|go test)(\s|$)", re.I)


def succeeded(response) -> bool:
    if isinstance(response, dict):
        code = response.get("exit_code", response.get("exitCode"))
        return code in (None, 0)
    return "error" not in str(response).lower()


def main() -> int:
    payload = hook_payload()
    root = workspace(payload)
    session_id = str(payload.get("session_id", "unknown"))
    session = active_session(root, session_id)
    if not session:
        return 0
    event = payload.get("hook_event_name")
    if event == "SubagentStop":
        session["review_observed"] = True
        save_session(root, session_id, session)
        print("{}")
        return 0
    tool = str(payload.get("tool_name", ""))
    tool_input = payload.get("tool_input") or {}
    command = str(tool_input.get("command") or tool_input.get("cmd") or "")
    if tool in {"apply_patch", "Edit", "Write"}:
        session["mutation_observed"] = True
    if tool == "Bash" and VALIDATION.search(command) and succeeded(payload.get("tool_response")):
        session["validation_observed"] = True
        session.setdefault("validation_commands", []).append(command[:500])
    save_session(root, session_id, session)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
