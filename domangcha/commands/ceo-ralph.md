# /ceo-ralph — Forced Loop Mode

기존 명령 이름을 유지하는 LOOP adapter다. `/ceo-ralph "업무"`는 canonical TaskRouter에서 최소 route를 LOOP로 설정한다.

```text
PLAN → EXECUTE → VALIDATE → ACT
                     ├─ success → COMPLETE
                     ├─ failure → bounded retry
                     └─ complexity discovered → GRAPH escalation
```

## 루프 상태 보고 (기본 활성)

Stop hook이 매 회차마다 루프 카드를 주입한다. 이 카드를 회차 응답 첫 줄에 그대로 보여주고,
지난 회차 대비 실제로 달라진 것 한 줄을 사용자 언어로 덧붙인다.

```text
🔁 LOOP 5/30  ▓▓░░░░░░░░ 17%
├ 재시도 여유 5 · 정체 0/3 · 반복 오류 0/3
├ 게이트: 검증 FAIL · 테스트 PASS · 리뷰 —
├ 차단기: CLOSED
├ 최근: auth 미들웨어 테스트 2건 실패
└ 상태: RUNNING ⏳
```

같은 자리를 돌고 있으면 숨기지 말고 그렇다고 말한다. 루프 상한 도달 시에도 카드와 함께
어디까지 되었고 무엇이 남았는지 설명한다.

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
