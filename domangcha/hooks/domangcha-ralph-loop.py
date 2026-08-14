#!/usr/bin/env python3
"""
Stop hook — DOMANGCHA Ralph Loop Engine
=========================================
ceo-ralph 자율 루프의 실제 "엔진". 프롬프트 prose가 아니라 기계가 강제한다.

동작:
  .ralph/status.json 을 읽어 루프 계속/종료를 결정한다.
  - active != true           → exit 0  (ralph 루프 중 아님 — 일반 세션, 영향 없음)
  - exit_signal + evidence    → active 내림 + exit 0  (완료)
  - circuit_breaker OPEN       → exit 0  (차단기 작동 — 정상 중단)
  - loop_count >= max_loops    → active 내림 + breaker OPEN + exit 0  (런어웨이 방지 캡)
  - 그 외                      → loop_count++ 기록 후 exit 2  (재진입 강제)

exit 2 = stderr 내용을 모델에 주입하고 종료를 막아 루프를 계속시킨다.
exit 0 = 정상 종료 허용.

안전 가드:
  - active 플래그가 없으면 절대 재진입하지 않음 → 전역 세션에 영향 없음
  - max_loops 하드캡 → 무한 루프 불가
  - exit_signal 은 모델이 완료조건(fix_plan 전체 체크 + GATE 통과)을 충족했을 때 설정
"""
from __future__ import annotations  # Path | None 등 union 힌트를 py3.9에서도 허용

import json
import os
import sys
from pathlib import Path

DEFAULT_MAX_LOOPS = 30
ABSOLUTE_MAX_LOOPS = 100  # status.json의 max_loops가 아무리 커도 이 값을 넘지 못함 (런어웨이 절대 상한)


def _find_status() -> Path | None:
    """CLAUDE_PROJECT_DIR 또는 cwd 기준으로 .ralph/status.json 을 찾는다."""
    root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    candidate = Path(root) / ".ralph" / "status.json"
    if candidate.exists():
        return candidate
    # cwd 폴백
    alt = Path(os.getcwd()) / ".ralph" / "status.json"
    return alt if alt.exists() else None


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def _write_json(path: Path, data: dict) -> None:
    # atomic write: 임시파일에 쓰고 os.replace 로 교체 → 동시쓰기 중 손상 방지
    try:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        os.replace(tmp, path)
    except Exception:
        pass


def _status_reporter():
    """Renderer is optional — a missing engine must never break the loop."""
    roots = (
        Path(__file__).resolve().parents[2],
        Path.home() / ".domangcha",
        Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())),
    )
    for root in roots:
        if (root / "domangcha" / "orchestration" / "status.py").exists():
            sys.path.insert(0, str(root))
            try:
                from domangcha.orchestration.status import StatusReporter

                return StatusReporter()
            except Exception:
                return None
    return None


def _loop_card(st: dict, loop_count: int, max_loops: int) -> str:
    """루프 상태를 사람이 읽는 카드로 렌더링한다."""
    reporter = _status_reporter()
    if reporter is None:
        return "🔁 LOOP %d/%d" % (loop_count, max_loops)
    breaker = st.get("circuit_breaker") if isinstance(st.get("circuit_breaker"), dict) else {}
    gates = " · ".join(
        "%s %s" % (label, st.get(key) or "—")
        for label, key in (("검증", "validation_status"), ("테스트", "tests_status"), ("리뷰", "evaluators_status"))
    )
    extra = ["게이트: " + gates, "차단기: " + (breaker.get("status") or "CLOSED")]
    return reporter.loop_card(
        {
            "status": "RUNNING" if st.get("active") else "PENDING",
            "iteration": loop_count,
            "max_iterations": max_loops,
            "retry_budget": st.get("retry_budget", 0),
            "no_progress_count": st.get("no_progress_count", 0),
            "repeated_error_count": st.get("repeated_error_count", 0),
            "usage": st.get("usage", {}),
            "decisions": [{"error": st["last_error"]}] if st.get("last_error") else [],
        },
        extra=extra,
    )


def _completion_is_valid(status_path: Path, st: dict) -> bool:
    """The model cannot end a loop by setting exit_signal alone."""
    fix_plan = status_path.parent / "fix_plan.md"
    if not fix_plan.exists() or "- [ ]" in fix_plan.read_text():
        return False
    if st.get("validation_status", st.get("gate_status")) not in {"PASS", "PASSED"}:
        return False
    if st.get("requires_tests") and st.get("tests_status") not in {"PASS", "PASSED"}:
        return False
    if st.get("requires_review") and st.get("evaluators_status") not in {"PASS", "PASSED"}:
        return False
    return True


CONTINUE_MSG = """\
[RALPH ENGINE] 루프 미완료 — 계속 진행하세요.

{card}

이번 회차 응답 첫 줄에 위 루프 카드를 그대로 보여주고, 지난 회차 대비 실제로 달라진 것 한 줄을
사용자 언어로 덧붙이세요. 같은 자리를 돌고 있으면 숨기지 말고 그렇다고 말하세요.

1. .ralph/PROMPT.md 와 .ralph/fix_plan.md 를 읽으세요.
2. fix_plan.md 의 미체크([ ]) 항목 중 최우선 1개를 실행하세요.
3. 기술/접근법 선택이 필요하면 멈추지 말고 WEIGHTED DECISION 으로 즉시 결정 →
   .ralph/decisions/DECISION-<날짜>-<주제>.md 에 기록하세요 (LOOP-002/004).
4. 사용자에게 질문하려고 멈추지 마세요 (LOOP-001/003). Circuit Breaker 조건만 중단 허용.
5. 매 루프 끝에 RALPH_STATUS 블록을 출력하고 .ralph/status.json 의 loop 상태를 갱신하세요.

⚠️ 완료 판정: fix_plan.md 전 항목 [x] + route-relevant deterministic validation
   + 필요한 경우 tests/independent review evidence가 있을 때에만
   .ralph/status.json 의 "exit_signal" 을 true 로 설정하세요.
   그 전에는 이 엔진이 계속 루프를 재개합니다. "여기까지만" 금지 [EXEC-002].
"""

CAP_MSG = """\
[RALPH ENGINE] 루프 상한(max_loops={maxl}) 도달 — 안전 종료합니다.

{card}

사용자에게 위 카드와 함께 어디까지 되었고 무엇이 남았는지 친절하게 설명하세요.
fix_plan.md 미완료 항목이 남아 있다면 사용자에게 Circuit Breaker 보고를 출력하세요.
재개하려면 .ralph/status.json 의 loop_count 를 낮추거나 /ceo-ralph reset 하세요.
"""


def main() -> int:
    # Stop hook 입력 (stop_hook_active 등) — 읽되 의존하지 않음
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    status_path = _find_status()
    if status_path is None:
        return 0  # ralph 상태 없음 → 일반 세션, 종료 허용

    st = _read_json(status_path)
    if not st:
        return 0

    # 1) active 가드 — ralph 루프가 실제로 켜져 있을 때만 엔진 작동
    if not st.get("active"):
        return 0

    # 2) 완료 신호 — 모델이 완료조건 충족 시 설정
    if st.get("exit_signal") is True and _completion_is_valid(status_path, st):
        st["active"] = False
        _write_json(status_path, st)
        return 0
    if st.get("exit_signal") is True:
        st["exit_signal"] = False
        st["last_error"] = "exit_signal rejected: completion evidence missing"
        _write_json(status_path, st)

    # 3) Circuit Breaker OPEN → 정상 중단
    breaker = st.get("circuit_breaker", {})
    if isinstance(breaker, dict) and breaker.get("status") == "OPEN":
        return 0

    # 4) 런어웨이 방지 하드캡
    max_loops = int(st.get("max_loops", DEFAULT_MAX_LOOPS) or DEFAULT_MAX_LOOPS)
    max_loops = min(max_loops, ABSOLUTE_MAX_LOOPS)  # status.json 조작으로도 절대 상한 우회 불가
    loop_count = int(st.get("loop_count", 0) or 0)
    if loop_count >= max_loops:
        st["active"] = False
        breaker = breaker if isinstance(breaker, dict) else {}
        breaker["status"] = "OPEN"
        st["circuit_breaker"] = breaker
        _write_json(status_path, st)
        sys.stderr.write(CAP_MSG.format(maxl=max_loops, card=_loop_card(st, loop_count, max_loops)))
        return 0  # 캡 도달은 정상 종료(종료 허용) — 무한루프 차단

    # 5) 그 외 → 루프 카운트 증가 후 재진입 강제
    loop_count += 1
    st["loop_count"] = loop_count
    _write_json(status_path, st)
    sys.stderr.write(CONTINUE_MSG.format(card=_loop_card(st, loop_count, max_loops)))
    return 2  # exit 2 = 종료 막고 모델 재진입


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # 엔진 오류로 세션이 막히면 안 됨 → 안전하게 종료 허용
        sys.exit(0)
