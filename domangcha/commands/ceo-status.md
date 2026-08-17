# /ceo-status — Execution Status

Canonical engine의 DIRECT read-only checkpoint/status adapter다.

```bash
python3 ~/.domangcha/domangcha/engine.py status <task_id> --workspace <project>
```

기본 출력은 사람이 읽는 카드다. 원시 상태는 `--format json`, 영어 카드는 `--lang en`으로 얻는다.

DOMANGCHA 저장소에서 실행할 때는 배포 드리프트도 함께 보고한다. 설치본(`~/.domangcha`)은
저장소와 별개로 갱신되므로, 저장소만 고치고 배포하지 않으면 다른 모든 프로젝트는 옛 엔진을 계속 쓴다.
양쪽 VERSION이 같아도 내용이 다를 수 있어 내용 해시로 비교한다. 읽기 전용이고 실패시키지 않는다.

```bash
python3 ~/.domangcha/domangcha/engine.py drift --root <domangcha 저장소>
```

```text
📦 배포 상태 ⚠️
├ 2.3.1 → 2.3.0
├ 오래된 파일: orchestration/validation.py
└ 커밋·푸시 후 install.sh를 다시 실행하면 반영됩니다
```

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
