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

## 진행 보고 (기본 활성)

`engine.py route|status`는 기본으로 사람이 읽는 카드를 출력한다(`--format json`으로 원시 상태, `--lang en`으로 영어).
Claude `UserPromptSubmit` 훅이 같은 카드와 보고 규칙을 자동 주입한다.

```text
🚂 DOMANGCHA · GRAPH 🧭 (score 10)
├ 이유: hard graph invariant: parallel
├ 계획: 타입 노드 그래프 · 병렬 브랜치 · join · 체크포인트
└ 다음: 노드별·브랜치별 진행 상태를 보고합니다
```

- 응답 시작에 라우트 카드를 보여준다. 사용자가 "지금 무엇을 왜 하는지"를 먼저 알게 한다.
- LOOP는 매 반복마다 `🔁 LOOP n/N · 재시도 여유 · 정체 · 예산`과 이번 회차의 실제 변화 1줄을 보고한다.
- GRAPH는 노드 진행(완료 ✅ · 진행 ⏳ · 대기 ⏸)과 병렬 브랜치(`🌿 병렬 n 브랜치 · join=ALL`)를 보고한다.
- HUMAN_GATE 앞에서는 무엇을·왜 승인받는지 사람의 말로 설명한 뒤 멈춘다.
- 긴 단계에서 침묵하지 않는다. 실패는 감추지 않고 다음 조치와 함께 말한다.

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
