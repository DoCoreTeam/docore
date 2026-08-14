# /ceo-status — Execution Status

Canonical engine의 DIRECT read-only checkpoint/status adapter다.

```bash
python3 ~/.domangcha/domangcha/engine.py status <task_id> --workspace <project>
```

기본 출력은 사람이 읽는 카드다. 원시 상태는 `--format json`, 영어 카드는 `--lang en`으로 얻는다.

```text
🚂 DOMANGCHA · GRAPH 🧭
├ 이유: hard graph invariant: parallel
├ 계획: 타입 노드 그래프 · 병렬 브랜치 · join · 체크포인트
└ 다음: 노드별·브랜치별 진행 상태를 보고합니다
🧭 GRAPH full_pipeline@1  ▓▓▓▓▓░░░░░ 50% 3/6 노드
├ 완료: intake ✅ · plan ✅ · build ✅
├ 진행: review ⏳ (시도 1)
├ 대기: gate ⏸ · ship ⏸
├ 병렬(build): dc-dev-be ✅ | dc-dev-fe ✅ | dc-sec ❌ · join=ALL
├ 예산: model 4/12 · agent 2/12 · tool 11/80 · retries 0/6
├ 승인 대기: gate 🙋
└ 상태: WAITING_FOR_APPROVAL 🙋
```

보고 항목:

- task ID, route, route history
- current status/node
- completed and pending nodes
- parallel branch results and join strategy
- attempts, budget usage, error fingerprints
- checkpoint version/time
- pending approval
- artifact references

카드를 그대로 사용자에게 보여주고, 필요한 설명은 사용자 언어로 덧붙인다.
Secret values와 untrusted artifact 전문은 출력하지 않는다.
