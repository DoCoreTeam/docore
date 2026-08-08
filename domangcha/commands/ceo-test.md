# /ceo-test — 테스트 오케스트레이터 / Test Orchestrator

Canonical TaskRouter에 validation intent를 전달한다. Deterministic test는 DIRECT, 반복 수정은 LOOP, 병렬 검증은 GRAPH다.

**EN** — Runs the full testing suite: TDD enforcement, unit/integration tests, E2E browser tests, and QA flows. Combines ECC, gstack, and DC-QA agent.

**KO** — TDD 강제 → 단위/통합 테스트 → E2E 브라우저 테스트 → QA 플로우까지 전체 테스트 스위트를 실행합니다. ECC, gstack, DC-QA 에이전트를 결합합니다.

## 사용법 / Usage

```
/ceo-test              → 전체 테스트 스위트 / Full test suite
/ceo-test --tdd        → TDD 워크플로우 강제 / Enforce TDD workflow
/ceo-test --e2e        → E2E + QA 집중 / E2E + QA focus
/ceo-test --coverage   → 커버리지 분석 포함 / Include coverage analysis
/ceo-test --lang go    → 언어별 테스트 (go/rust/cpp/flutter/kotlin) / Language-specific
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: TDD 강제 (TDD Enforcement)
- ECC `/tdd` → RED(테스트 먼저) → GREEN(구현) → REFACTOR 사이클 확인
- 언어별 라우팅: `/go-test` / `/rust-test` / `/cpp-test` / `/flutter-test` / `/kotlin-test`

### STEP 2: 테스트 실행 (Test Execution)
- ECC `/test` → 단위 + 통합 테스트 실행
- gstack `/test` → gstack 테스트 워크플로우

### STEP 3: 커버리지 분석 (Coverage Analysis)
- ECC `/test-coverage` → 80% 미만 구간 식별 및 보고

### STEP 4: 브라우저 검증 + E2E + QA
- **Claude-in-Chrome 확장 (기본)** → `mcp__claude-in-chrome__*`로 실화면 QA (렌더·인터랙션·콘솔/네트워크·스크린샷)
- ECC `/e2e` → Playwright E2E — **폴백**: Chrome 확장 미가용 / 헤드리스 CI / CI에 박제할 회귀 스위트일 때만
- DC-QA 에이전트 → 기능/품질 종합 검증
- 우선순위 근거: `skills/ceo-standards/SKILL.md` "브라우저 검증 정책" [BV-1]/[BV-2]

## 결과 보고 / Output

```
[CEO-TEST REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 단위/통합 (Unit/Integration): PASS / FAIL — <커버리지>%
🌐 E2E:                         PASS / FAIL — <시나리오 수>
🖥️  QA (Browser):               PASS / FAIL — <스크린샷 첨부>
📊 전체 커버리지 (Coverage):     <X>% (목표: 80%+)
🚦 최종 판정 (Verdict):          ✅ ALL PASS / ❌ FAILURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[실패 테스트 목록]
[커버리지 부족 구간]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/tdd` | ECC | TDD 워크플로우 강제 |
| `/test` | ECC | 테스트 실행 |
| `/test-coverage` | ECC | 커버리지 분석 |
| `mcp__claude-in-chrome__*` | Claude-in-Chrome | **실화면 브라우저 검증 (기본)** |
| `/e2e` | ECC | Playwright E2E (폴백 — CI/헤드리스) |
| `/go-test` `/rust-test` `/cpp-test` etc. | ECC | 언어별 TDD |
| `/test` | gstack | gstack 테스트 |
| DC-QA | DOMANGCHA | QA 전문 에이전트 |
