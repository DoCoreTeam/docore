# /ceo-quality — 품질 오케스트레이터 / Quality Orchestrator

**EN** — Full quality pipeline: health check → coverage → refactor → security → performance. Combines gstack's health tools with ECC's quality suite and DOCORE evaluators.

**KO** — 헬스 체크 → 커버리지 → 리팩터 → 보안 → 성능 전체 품질 파이프라인. gstack 헬스 도구 + ECC 품질 스위트 + MACC 평가자를 결합합니다.

## 사용법 / Usage

```
/ceo-quality              → 전체 품질 파이프라인 / Full quality pipeline
/ceo-quality --health     → 프로젝트 헬스 체크만 / Health check only
/ceo-quality --refactor   → 리팩터 집중 / Refactor focus
/ceo-quality --security   → 보안 집중 / Security focus
/ceo-quality --perf       → 성능 집중 / Performance focus
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 프로젝트 헬스 (Project Health)
- gstack `/health` → 코드 품질, 커버리지, 보안 종합 헬스 체크
- ECC `/quality-gate` → 5개 게이트 상태 확인

### STEP 2: 커버리지 (Coverage)
- ECC `/test-coverage` → 커버리지 분석, 80% 미만 구간 식별

### STEP 3: 리팩터링 (Refactoring)
- ECC `/refactor-clean` → 데드코드 제거, 중복 통합, 미사용 import 정리
- ECC `/rules-distill` → 코드베이스 패턴 추출 및 규칙 정제

### STEP 4: 보안 (Security)
- ECC `/security-review` → OWASP Top 10 전체 스캔
- DC-SEC 에이전트 → 심층 보안 분석

### STEP 5: 성능 (Performance)
- ECC `/perf-check` → 병목, 번들 크기, 쿼리 최적화

### STEP 6: 최종 리뷰 (Final Review)
- ECC `/santa-loop` → 두 리뷰어 모두 PASS 확인
- DC-QA, DC-REV 에이전트 → 종합 품질 판정

## 결과 보고 / Output

```
[CEO-QUALITY REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❤️  헬스 (Health):        <점수>/100
📊 커버리지 (Coverage):   <X>% (목표: 80%+)
🧹 리팩터 (Refactor):     <제거된 코드 수>줄 정리
🔒 보안 (Security):       PASS / <이슈 수>건
⚡ 성능 (Performance):    <개선 항목>
🚦 최종 판정 (Verdict):   ✅ HEALTHY / ⚠️ NEEDS_WORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[남은 이슈 목록]
[권장 개선 사항]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/health` | gstack | 종합 헬스 체크 |
| `/quality-gate` | ECC | 5개 게이트 확인 |
| `/test-coverage` | ECC | 커버리지 분석 |
| `/refactor-clean` | ECC | 데드코드 정리 |
| `/rules-distill` | ECC | 패턴 추출 |
| `/security-review` | ECC | 보안 스캔 |
| `/perf-check` | ECC | 성능 분석 |
| `/santa-loop` | ECC | 이중 리뷰 |
| DC-SEC | MACC | 보안 전문 에이전트 |
| DC-QA | MACC | QA 전문 에이전트 |
| DC-REV | MACC | 리뷰 전문 에이전트 |
