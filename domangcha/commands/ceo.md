# /ceo — Adaptive Execution

`/ceo "업무"`는 DOMANGCHA의 단일 `TaskRouter`를 호출한다. 별도의 CEO router나 고정 FULL PIPELINE을 실행하지 않는다.

## 실행 계약

1. 요청을 `python3 ~/.claude/domangcha/engine.py route "$ARGUMENTS"`로 분류한다.
2. 프로젝트 설치본이 없으면 저장소의 `python3 domangcha/engine.py route "$ARGUMENTS"`를 사용한다.
3. 반환된 route를 따른다.

| Route | 실행 |
|---|---|
| DIRECT | 설명·조회·formatting 또는 trivial isolated change. planner, loop, fan-out, DOC, version bump를 강제하지 않는다. 관련된 최소 검증만 실행한다. |
| LOOP | bounded PLAN → EXECUTE → VALIDATE → ACT. retry/no-progress/budget/checkpoint를 기록한다. 기존 Ralph memory UX를 재사용한다. |
| GRAPH | typed state/node/edge로 실행한다. 병렬 branch, join, fallback, checkpoint, HUMAN_GATE를 코드가 통제한다. |

## 불변 규칙

- LLM 분류는 ambiguous boundary에서 제안만 한다. route invariant는 코드가 결정한다.
- DIRECT가 cross-file dependency 또는 반복 실패를 발견하면 LOOP로 승격한다.
- LOOP가 security, destructive action, independent branches, pause/resume 필요를 발견하면 GRAPH로 승격한다.
- meaningful implementation의 writer는 유일한 reviewer가 될 수 없다.
- commit, push, publish, deploy는 요청에 포함되거나 별도 `/ceo-ship` 권한이 있을 때만 실행한다.
- destructive/irreversible action은 HUMAN_GATE 승인 전 실행하지 않는다.
- route transition과 validation 결과를 structured state에 기록한다.

## 완료

route별 관련 validator가 통과했을 때만 완료를 보고한다. 모든 작업에 동일한 DOC/GATE/agent fan-out을 강제하지 않는다.
