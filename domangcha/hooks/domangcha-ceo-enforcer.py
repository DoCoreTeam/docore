#!/usr/bin/env python3
"""Claude UserPromptSubmit adapter for the canonical DOMANGCHA router."""
from __future__ import annotations

import json
import os
import re
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
            break
        if (root / "engine.py").exists() and (root / "orchestration").is_dir():
            sys.path.insert(0, str(root.parent))
            break
    else:
        raise RuntimeError("DOMANGCHA engine is not installed")
    from domangcha.engine import route_request
    from domangcha.orchestration.status import StatusReporter
    return route_request, StatusReporter


REPORTING_CONTRACT = """진행 상황 보고 규칙 (기본 활성 · 끄려면 사용자가 명시적으로 요청):
1. 응답 시작에 위 라우트 카드를 그대로 보여준다. 사용자가 "지금 무엇을 왜 하는지"를 먼저 알게 한다.
2. LOOP: 매 반복마다 `{loop_example}` 형태로 회차·예산·진전을 보고하고,
   이번 회차에서 실제로 달라진 것 한 줄을 덧붙인다. 같은 자리를 도는 중이면 그렇다고 말한다.
3. GRAPH: 노드 진행(완료 ✅ · 진행 ⏳ · 대기 ⏸)을 보고하고, 병렬 브랜치는 시작할 때 목록을,
   끝날 때 `{wave_example}` 형태로 성공/실패와 join 전략을 보여준다.
4. 30초 이상 걸리는 단계는 침묵하지 않는다. 시작·중간·끝을 짧게 알린다.
5. HUMAN_GATE 앞에서는 무엇을·왜 승인받아야 하는지 사람의 말로 설명한 뒤 멈춘다.
6. 톤: 사용자의 언어로, 친절하고 간결하게. 전문용어에는 짧은 풀이를 붙이고, 실패는 감추지 말고
   있는 그대로 + 다음 조치를 함께 말한다.
7. 카드 문법은 `python3 <engine.py> route|status --format card` 출력과 동일하게 유지한다.
   상세 상태가 필요하면 `engine.py status <task_id>`를 실행해 그 카드를 보여준다."""

CEO_COMMAND = re.compile(r"^\s*/ceo\b", re.IGNORECASE)

YIELD_MESSAGE = """[DOMANGCHA] 이 프로젝트는 프로젝트 루프로 운영됩니다 (.loop/ 감지).
전역 라우터는 물러나고 프로젝트 규정인 LOOP.md 가 우선합니다.
지시 기록과 다음 행동은 프로젝트 훅(scripts/loop.mjs)이 이어서 출력합니다.
하네스가 필요하면 /ceo 로 시작하세요 — 그때는 이 라우터가 다시 맡습니다."""

ESCALATION_NOTICE = """[DOMANGCHA] /ceo 로 프로젝트 루프에서 하네스로 올라갑니다.
이번 요청에 한해 아래 라우트를 따르고, 끝나면 LOOP.md 로 돌아갑니다.
결과는 loop pass 또는 loop plan revise 로 프로젝트 플랜에 반영하세요."""

LOOP_EXAMPLE = "🔁 LOOP 3/12 ▓▓░░░░░░░░ 25% · 재시도 여유 5 · 정체 0/3 · 예산 model 5/12"
WAVE_EXAMPLE = "🌿 병렬 3 브랜치 · join=ALL · ✅ be | ✅ fe | ❌ sec"


def _message(result: dict, card: str) -> str:
    return """[DOMANGCHA ADAPTIVE ROUTER]
{card}

route={route} score={score} approval_required={approval}

{contract}

Use the canonical route. DIRECT has no planner graph, recursive loop, mandatory DOC, or agent fan-out.
LOOP uses bounded PLAN→EXECUTE→VALIDATE→ACT with checkpointing.
GRAPH uses typed nodes and deterministic edges; destructive effects require HUMAN_GATE.
Do not use legacy SMALL/MEDIUM/FULL-PIPELINE prose to override this decision.
""".format(
        card=card,
        route=result["route"],
        score=result["score"],
        approval=str(result["approval_required"]).lower(),
        contract=REPORTING_CONTRACT.format(loop_example=LOOP_EXAMPLE, wave_example=WAVE_EXAMPLE),
    )


def _project_loop_root() -> Path | None:
    """A project running the v3 lightweight loop owns its own protocol."""
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
    if (root / ".loop").is_dir() and (root / "scripts" / "loop.mjs").exists():
        return root
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        prompt = payload.get("prompt", "")
        if not prompt:
            return 0
        loop_root = _project_loop_root()
        escalating = loop_root is not None
        if escalating and not CEO_COMMAND.match(prompt):
            print(YIELD_MESSAGE)
            return 0
        route_request, reporter = _load_engine()
        result = route_request(prompt)
        if escalating:
            print(ESCALATION_NOTICE)
        print(_message(result, reporter().route_card(result)))
        return 0
    except Exception as exc:
        print("[DOMANGCHA ROUTER DEGRADED] %s. Use the safest applicable route." % exc)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
