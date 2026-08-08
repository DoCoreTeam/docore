# /ceo-ralph — Forced Loop Mode

기존 명령 이름을 유지하는 LOOP adapter다. `/ceo-ralph "업무"`는 canonical TaskRouter에서 최소 route를 LOOP로 설정한다.

```text
PLAN → EXECUTE → VALIDATE → ACT
                     ├─ success → COMPLETE
                     ├─ failure → bounded retry
                     └─ complexity discovered → GRAPH escalation
```

## 상태와 호환성

- `.ralph/PROMPT.md`, `.ralph/fix_plan.md`, `.ralph/decisions/`, `.ralph/status.json` UX를 유지한다.
- canonical checkpoint는 `.domangcha/checkpoints/`에 저장한다.
- `status.json.exit_signal`만으로 완료할 수 없다. fix plan, tests, evaluator, gate evidence를 engine/hook이 검증한다.
- 기존 status 파일은 없는 필드에 기본값을 적용하여 읽는다.

## 종료 조건

- explicit completion criteria
- max iterations
- retry budget
- no-progress detection
- repeated-error fingerprint
- tests/validator evidence
- independent reviewer evidence when code was meaningfully changed

## 중단과 승인

- circuit breaker 또는 budget exhaustion은 typed failure로 종료한다.
- destructive, irreversible, security-sensitive action 발견 시 질문 금지 규칙보다 HUMAN_GATE가 우선한다.
- interactive runtime은 승인을 요청하고, Codex Cloud/비대화형 runtime은 `WAITING_FOR_APPROVAL` checkpoint를 남긴다.

## 명령

- `/ceo-ralph status`: checkpoint와 legacy status 조회
- `/ceo-ralph reset`: active execution만 종료하고 기존 artifacts/decisions는 archive한다.
- reset은 사용자 변경사항을 자동 stash하거나 삭제하지 않는다.
