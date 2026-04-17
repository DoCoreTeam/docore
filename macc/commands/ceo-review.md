# /ceo-review — 코드 리뷰 오케스트레이터 / Code Review Orchestrator

**EN** — Runs all review tools in optimal order: security first, then code quality, then PR-level review. Combines ECC, gstack, and DC-REV agent for maximum coverage.

**KO** — 보안 → 코드 품질 → PR 리뷰 순서로 모든 리뷰 도구를 최적 순서로 실행합니다. ECC, gstack, DC-REV 에이전트를 결합하여 최대 커버리지를 확보합니다.

## 사용법 / Usage

```
/ceo-review              → 현재 변경사항 전체 리뷰 / Review all current changes
/ceo-review 123          → PR #123 리뷰 / Review PR #123
/ceo-review --security   → 보안 집중 리뷰 / Security-focused review only
/ceo-review --quick      → 빠른 리뷰 (핵심만) / Quick review (critical only)
```

## 실행 파이프라인 / Execution Pipeline

CEO가 아래 순서로 모든 도구를 오케스트레이션합니다.
CEO orchestrates all tools in this order:

### STEP 1: 보안 검토 (Security Review)
- ECC `/security-review` → OWASP Top 10, 시크릿 노출, SQL 인젝션, XSS, 인증 취약점
- DC-SEC 에이전트 → 심층 보안 분석 및 위험 등급 산정

### STEP 2: 코드 품질 (Code Quality)
- ECC `/code-review` → 로직, 가독성, 중복, 복잡도
- gstack `/review` → 실용적 관점의 코드 검토
- ECC `/refactor-clean` → 데드코드, 미사용 import 감지

### STEP 3: PR 리뷰 (PR Review, PR 번호 전달 시)
- ECC `/review-pr` → GitHub PR 종합 리뷰
- DC-REV 에이전트 → 최종 합격/거부 판정 (PASS / FAIL)

### STEP 4: 품질 게이트 (Quality Gate)
- ECC `/quality-gate` → 5개 게이트 통과 여부 확인
- ECC `/santa-loop` → 두 리뷰어가 모두 PASS해야 완료 (선택)

## 결과 보고 / Output

```
[CEO-REVIEW REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔒 보안 (Security):   PASS / FAIL — <요약>
📝 코드 품질 (Quality): PASS / FAIL — <요약>
🔍 PR 리뷰 (PR):      PASS / FAIL — <요약>
🚦 최종 판정 (Verdict): ✅ APPROVED / ❌ BLOCKED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CRITICAL 이슈 목록]
[HIGH 이슈 목록]
[권장 수정 사항]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/security-review` | ECC | OWASP 보안 검토 |
| `/code-review` | ECC | 코드 품질 검토 |
| `/review-pr` | ECC | PR 종합 리뷰 |
| `/refactor-clean` | ECC | 데드코드 감지 |
| `/quality-gate` | ECC | 5개 게이트 통과 확인 |
| `/review` | gstack | 실용적 코드 검토 |
| DC-SEC | MACC | 보안 전문 에이전트 |
| DC-REV | MACC | 코드 리뷰 전문 에이전트 |
