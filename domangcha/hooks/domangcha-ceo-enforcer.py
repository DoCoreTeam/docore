#!/usr/bin/env python3
"""Claude UserPromptSubmit adapter for the canonical DOMANGCHA router."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def _load_engine():
    candidates = [
        Path(__file__).resolve().parents[2],
        Path.home() / ".domangcha",
        Path.home() / ".claude" / "domangcha",
        Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())),
    ]
    for root in candidates:
        if (root / "domangcha" / "engine.py").exists():
            sys.path.insert(0, str(root))
            from domangcha.engine import route_request
            return route_request
        if (root / "engine.py").exists() and (root / "orchestration").is_dir():
            sys.path.insert(0, str(root.parent))
            from domangcha.engine import route_request
            return route_request
    raise RuntimeError("DOMANGCHA engine is not installed")


def _message(result: dict) -> str:
    return """[DOMANGCHA ADAPTIVE ROUTER]
route={route} score={score} approval_required={approval}
reasons={reasons}

Use the canonical route. DIRECT has no planner graph, recursive loop, mandatory DOC, or agent fan-out.
LOOP uses bounded PLAN→EXECUTE→VALIDATE→ACT with checkpointing.
GRAPH uses typed nodes and deterministic edges; destructive effects require HUMAN_GATE.
Do not use legacy SMALL/MEDIUM/FULL-PIPELINE prose to override this decision.
""".format(
        route=result["route"],
        score=result["score"],
        approval=str(result["approval_required"]).lower(),
        reasons="; ".join(result["reasons"]),
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        prompt = payload.get("prompt", "")
        if not prompt:
            return 0
        print(_message(_load_engine()(prompt)))
        return 0
    except Exception as exc:
        print("[DOMANGCHA ROUTER DEGRADED] %s. Use the safest applicable route." % exc)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
