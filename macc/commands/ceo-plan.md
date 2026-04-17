# /ceo-plan — 기획 오케스트레이터 / Plan Orchestrator

**EN** — Full planning pipeline with Q&A: business validation → research → OSS scouting → implementation plan. Combines gstack's Q&A-driven plan with ECC's PRP system and MACC's planning agents.

**KO** — Q&A 기반 전체 기획 파이프라인: 사업 타당성 → 리서치 → 오픈소스 탐색 → 구현 계획. gstack Qgstack Q&A 플랜 + ECC PRP + DOCORE 기획A 플랜 + ECC PRP + MACC 기획 에이전트를 결합합니다.

## 사용법 / Usage

```
/ceo-plan "기능 설명"   → 전체 기획 파이프라인 / Full planning pipeline
/ceo-plan --prd         → PRD 중심 기획 / PRD-focused planning
/ceo-plan --arch        → 아키텍처 중심 기획 / Architecture-focused
/ceo-plan --quick       → 빠른 기획 (소규모) / Quick plan for small tasks
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: Q&A 명확화 (Clarification Q&A)
- gstack `/plan` → 인터랙티브 Q&A로 요구사항 명확화
- ECC `/prp-prd` → 문제 중심 PRD 작성 (선택)
- CEO Q&A 프로토콜 → 기술스택, 플랫폼, 완료 기준, 제약 확인

### STEP 2: 사업 타당성 (Business Validation)
- DC-BIZ 에이전트 → 사업 타당성, ROI, 리스크 판단
- ECC `/spec` → 기술 명세 초안 작성

### STEP 3: 리서치 (Research)
- DC-RES 에이전트 → 기술 리서치, 레퍼런스 수집
- ECC `/evaluate-oss` → 관련 오픈소스 라이브러리 평가

### STEP 4: 오픈소스 탐색 (OSS Scouting)
- DC-OSS 에이전트 → 활용 가능한 라이브러리 Top 3 선정

### STEP 5: 구현 계획 수립 (Implementation Plan)
- ECC `/prp-plan` → 코드베이스 패턴 기반 상세 구현 계획
- ECC `/plan` → 단계별 구현 계획 (사용자 확인 대기)
- gstack `/autoplan` → 컨텍스트 기반 자동 계획 보완

### STEP 6: 산출물 (Deliverables)
- `docs/PLAN.md` — 전체 구현 계획
- `docs/PRD.md` — 제품 요구사항 문서 (선택)
- `docs/TECH-SPEC.md` — 기술 명세

## 결과 보고 / Output

```
[CEO-PLAN REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 기능명 (Feature): <이름>
✅ 사업 타당성 (BIZ): APPROVED / REJECTED — <이유>
🔬 리서치 (Research): <핵심 발견사항>
📦 추천 라이브러리 (OSS): <Top 3>
📝 구현 계획 (Plan): docs/PLAN.md 생성 완료
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Phase 1] <작업 목록>
[Phase 2] <작업 목록>
[예상 리스크] <목록>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/plan` | gstack | Q&A 기반 기획 |
| `/autoplan` | gstack | 자동 계획 보완 |
| `/prp-prd` | ECC | PRD 작성 |
| `/prp-plan` | ECC | 상세 구현 계획 |
| `/plan` | ECC | 단계별 계획 |
| `/spec` | ECC | 기술 명세 |
| `/evaluate-oss` | ECC | 오픈소스 평가 |
| DC-BIZ | MACC | 사업 타당성 에이전트 |
| DC-RES | MACC | 리서치 에이전트 |
| DC-OSS | MACC | 오픈소스 탐색 에이전트 |
