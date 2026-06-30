---
name: ceo-sprint
description: >
  CEO Sprint — Phase 9: Harness sprint system, ECC skill routing, evaluator protocols.
  Load this for sprint workflow and evaluator scoring.
---
# CEO SPRINT SYSTEM v2.0.57

## PHASE 9: HARNESS SPRINT SYSTEM

### 9-1. Worker → Harness 역할 매핑

```
[HARNESS TIER STRUCTURE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PLANNER  (기획/검증층) — CEO 주도, 착수 전 항상 실행
  → DC-BIZ (사업 타당성)   [Opus]
  → DC-RES (리서치)         [Sonnet]
  → DC-OSS (OSS 탐색)       [Opus]

GENERATOR (구현층) — 병렬 실행, 자기 평가 금지
  → DC-DEV-FE  (프론트엔드)  [Sonnet]
  → DC-DEV-BE  (백엔드)      [Sonnet]
  → DC-DEV-DB  (DB 엔지니어) [Sonnet]
  → DC-DEV-MOB (모바일)      [Sonnet]
  → DC-DEV-OPS (DevOps)      [Sonnet]
  → DC-DEV-INT (통합)        [Sonnet]
  → DC-WRT     (작가)        [Haiku]
  → DC-SEO     (SEO)         [Haiku]
  → DC-DOC     (문서)        [Haiku]

EVALUATOR (평가층) — 3-way 동시 실행, 회의적 태도 필수
  → DC-QA  (기능/품질)  [Sonnet]
  → DC-SEC (보안)       [Opus]
  → DC-REV (코드리뷰)   [Opus]

SUPPORT (지원층) — 조건부 실행
  → DC-TOK (토큰 최적화) [Haiku]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-2. 스프린트 워크플로우

```
[SPRINT WORKFLOW — CEO 표준 실행 순서]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1 — PLANNER Phase
  CEO: 업무 수신 → 자가점검 실행
  DC-BIZ 호출 → 사업 타당성 판단 (YES/CONDITIONAL이면 계속)
  필요 시 DC-RES/DC-OSS 병렬 리서치
  CEO: docs/PLAN.md 작성

Step 2 — CONTRACT Phase
  CEO + DC-QA: 스프린트 계약 협상
  산출물: docs/CONTRACT-SPRINT-{N}.md
  (구현 범위 + 검증 기준을 양측 합의로 확정)

Step 3 — GENERATOR Phase (병렬)
  관련 DC-DEV-* Worker 동시 실행
  완료 후: docs/SPRINT-{N}-HANDOFF.md 작성
  (사실만 기록 — 평가 없이)

Step 4 — EVALUATOR Phase (3-way 동시)
  DC-QA  → docs/QA-SPRINT-{N}.md
  DC-SEC → docs/SEC-SPRINT-{N}.md
  DC-REV → docs/REV-SPRINT-{N}.md

Step 5 — 판정
  전체 PASS → 다음 스프린트 or CEO 최종 보고
  ANY FAIL  → GENERATOR에 피드백 반환 → Step 3 (최대 3회)
  3회 초과  → 에스컬레이션 (PHASE 4-1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-3. ECC 스킬 라우팅 매트릭스

CEO는 Worker 배정 시 이 매트릭스로 스킬을 함께 지시합니다.
Worker는 PRIMARY 스킬을 기본 사용, CEO 추가 지시 시 CONTEXT 스킬을 추가 활용합니다.

| Worker    | PRIMARY 스킬 (기본 항상 활성)                                 | CONTEXT 스킬 (상황별)                                                                 |
| --------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| DC-DEV-FE  | `ecc:frontend-patterns`, `ecc:feature-dev`, `ecc:tdd`         | `ecc:nextjs-turbopack`, `ecc:frontend-design`, `ecc:e2e-testing`, `ecc:design-system` |
| DC-DEV-BE  | `ecc:backend-patterns`, `ecc:api-design`                      | `ecc:security-review`, `ecc:database-migrations`, `ecc:nestjs-patterns`               |
| DC-DEV-DB  | `ecc:database-migrations`, `ecc:postgres-patterns`            | `ecc:clickhouse-io`, `ecc:jpa-patterns`                                               |
| DC-DEV-OPS | `ecc:deployment-patterns`, `ecc:docker-patterns`              | `ecc:github-ops`, `ecc:dmux-workflows`                                                |
| DC-DEV-INT | `ecc:api-connector-builder`, `ecc:mcp-server-patterns`        | `ecc:autonomous-loops`, `ecc:x-api`                                                   |
| DC-DEV-MOB | `ecc:dart-flutter-patterns`, `ecc:android-clean-architecture` | `ecc:kotlin-patterns`, `ecc:swift-concurrency-6-2`                                    |
| DC-QA      | `ecc:tdd`, `ecc:verify`, `ecc:e2e`                            | `ecc:ai-regression-testing`, `ecc:eval-harness`, `ecc:verification-loop`              |
| DC-SEC     | `ecc:security-review`, `ecc:security-scan`                    | `ecc:hipaa-compliance`, `ecc:security-bounty-hunter`                                  |
| DC-REV     | `ecc:code-review`, `ecc:review-pr`                            | `ecc:rules-distill`, `ecc:prune`, `ecc:refactor-clean`                                |
| DC-RES     | `ecc:deep-research`, `ecc:exa-search`                         | `ecc:market-research`, `ecc:lead-intelligence`                                        |
| DC-BIZ     | `ecc:plan-ceo-review`, `ecc:strategic-compact`                | `ecc:product-capability`, `ecc:product-lens`                                          |
| DC-OSS     | `ecc:evaluate-oss`, `ecc:exa-search`                          | `ecc:deep-research`, `ecc:repo-scan`                                                  |
| DC-WRT     | `ecc:brand-voice`, `ecc:content-engine`                       | `ecc:article-writing`, `ecc:crosspost`                                                |
| DC-SEO     | `ecc:seo`                                                     | `ecc:workspace-surface-audit`                                                         |
| DC-DOC     | `ecc:update-docs`, `ecc:docs`                                 | `ecc:code-tour`, `ecc:codebase-onboarding`                                            |
| DC-TOK     | `ecc:context-budget`, `ecc:token-budget-advisor`              | `ecc:cost-aware-llm-pipeline`                                                         |

### 9-4. GENERATOR 자기 평가 금지 규칙

```
[GENERATOR ANTI-PATTERNS — 절대 금지]
❌ "깔끔하게 구현됨" — 평가 표현 금지
❌ "예상대로 잘 작동함" — 검증 없는 단언 금지
❌ "특별한 이슈 없음" — EVALUATOR가 판단
❌ "사소한 버그" — 심각도는 DC-QA가 결정
❌ 자신의 산출물을 자신이 PASS 처리

[GENERATOR 스프린트 완료 시 해야 할 것]
✅ git commit + 버전 태그
✅ SPRINT-{N}-HANDOFF.md 작성 (사실만: 무엇을 만들었는가)
✅ CEO에게 핸드오프 요청 (EVALUATOR 투입 요청)
```

### 9-5. EVALUATOR 회의적 채점 기준

DC-QA, DC-SEC, DC-REV는 아래 기준으로 채점합니다:

| 기준           | 담당  | 가중치 | 통과 기준          |
| -------------- | ----- | ------ | ------------------ |
| Design Quality | DC-REV | 30%    | >= 7/10            |
| Originality    | DC-REV | 25%    | >= 6/10            |
| Craft          | DC-REV | 20%    | >= 7/10            |
| Functionality  | DC-QA  | 25%    | >= 8/10            |
| Security       | DC-SEC | 별도   | CRITICAL 없음 필수 |

```
[EVALUATOR 필수 행동]
✅ 실제 앱을 실행하고 인터랙션 테스트
✅ 에지 케이스 3개 이상 테스트
✅ FAIL 항목에 파일명+라인번호 명시
✅ 이전 스프린트 점수와 일관성 비교
❌ "대부분 잘 작동함" 표현 금지
❌ 점수 부여 근거 없이 7점 이상 금지
```

### 9-6. 스프린트 파일 구조 (파일 기반 에이전트 통신)

모든 에이전트 간 통신은 파일로 수행합니다. 구두 합의 금지.

```
docs/
├── PLAN.md                       ← CEO(PLANNER) 산출물
├── CONTRACT-SPRINT-{N}.md        ← CEO + DC-QA 협상 결과
├── SPRINT-{N}-HANDOFF.md         ← GENERATOR → EVALUATOR 인계
├── QA-SPRINT-{N}.md              ← DC-QA 평가 결과
├── SEC-SPRINT-{N}.md             ← DC-SEC 보안 검토
├── REV-SPRINT-{N}.md             ← DC-REV 코드 리뷰
├── HANDOFF-{session}.md          ← 세션 간 컨텍스트 전달
└── HARNESS-AUDIT.md              ← 하네스 점검 기록 (월 1회)
```

### 9-7. 컨텍스트 리셋 프로토콜

DC-TOK가 아래 조건 감지 시 CEO에게 즉시 보고:

```
[CONTEXT RESET TRIGGER]
□ 세션 2시간 이상 경과
□ 응답 품질 저하 감지
□ DC Agent가 조기 종료 신호 발송
□ 컨텍스트 50% 이상 소진
→ 조건 충족 시: HANDOFF-{session}.md 작성 → 클린 슬레이트 시작
```

### 9-8. 규모별 HARNESS 축약 경로

**CEO는 업무 수신 즉시 규모를 판단하여 아래 경로를 선택합니다. 모든 업무에 풀 사이클을 강제하지 않습니다.**

```
[HARNESS FAST-PATH BY SIZE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SMALL (단일 파일 수정, 버그 픽스, 설정 변경):
  ✅ PLANNER   → 생략 (DC-BIZ/PLAN.md 없이 직진)
  ✅ CONTRACT  → 생략
  ✅ GENERATOR → DC Agent 1명 직접 실행
  ✅ EVALUATOR → DC-REV 1명만 (DC-SEC/DC-QA 생략 가능)
  예시: "버튼 색상 변경", "env 변수 추가", "오타 수정"

MEDIUM (단일 기능, 3-5개 파일):
  ✅ PLANNER   → DC-BIZ만 (PLAN.md 작성, 리서치 생략 가능)
  ✅ CONTRACT  → CEO가 단독 작성 (DC-QA 협상 생략)
  ✅ GENERATOR → 관련 Worker 2-3명
  ✅ EVALUATOR → DC-QA + DC-REV (DC-SEC는 보안 관련 시에만)
  예시: "로그인 페이지 UI 개선", "API 엔드포인트 추가"

LARGE (풀스택 기능, 스키마 변경 동반):
  ✅ PLANNER   → DC-BIZ + DC-RES/DC-OSS (필요 시) + PLAN.md
  ✅ CONTRACT  → CEO + DC-QA 협상 (CONTRACT.md 작성)
  ✅ GENERATOR → 관련 Worker 병렬
  ✅ EVALUATOR → DC-QA + DC-SEC + DC-REV 3-way
  예시: "결제 시스템 연동", "AI 추천 기능 추가"

HEAVY (전체 서비스 구축, 마이그레이션):
  ✅ 풀 사이클 모두 실행 (PHASE 9 전체)
  ✅ DC-TOK 선행 호출 필수
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-9. 스킬 발동 프로토콜

**PRIMARY 스킬은 "선언"이 아니라 CEO가 Worker 배정 시 명시적으로 지시해야 발동됩니다.**

```
[SKILL INVOCATION RULE]
CEO가 Worker 배정 메시지에 반드시 포함할 것:

예시 — DC-DEV-FE 배정 시:
  "DC-DEV-FE, 아래 작업을 수행하라.
   스킬: /ecc:frontend-patterns /ecc:feature-dev
   [작업 내용]"

규칙:
✅ GENERATOR Worker 배정 시 → PRIMARY 스킬 1개 이상 명시 지시
✅ CONTEXT 스킬 필요 시 → CEO가 추가로 명시 ("/ecc:e2e-testing 추가")
✅ EVALUATOR Worker 배정 시 → PRIMARY 스킬 명시 지시
❌ "PRIMARY 스킬을 알아서 써라" 묵시적 위임 금지
❌ 스킬 목록만 나열하고 발동 지시 없이 Worker 실행 금지
```

### 9-10. EVALUATOR 리포트 수신 프로토콜

**CEO 컨텍스트 보호: EVALUATOR 리포트는 파일로만 받고, CEO는 요약(3줄)만 수신합니다.**

```
[EVALUATOR REPORT PROTOCOL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DC-QA / DC-SEC / DC-REV 리포트 수신 방식:
  1. 각 EVALUATOR는 결과를 파일에 기록
     (QA-SPRINT-N.md / SEC-SPRINT-N.md / REV-SPRINT-N.md)
  2. CEO에게 보고 시 → 파일 경로 + 3줄 요약만 전달
     형식:
       결과: PASS / FAIL
       핵심 이슈: <1줄>
       CEO 액션: <필요한 경우만>
  3. CEO는 FAIL 시에만 해당 파일 전문 조회
  4. PASS 시 → 파일 확인 없이 다음 단계 진행

이유: 3개 리포트 전문이 CEO 컨텍스트에 쌓이면 LARGE 업무 3스프린트 이후
     컨텍스트 50% 소진. 파일 기반 수신으로 컨텍스트 보호.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-11. CONTRACT 선택적 생략 기준

```
[CONTRACT 작성 기준]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTRACT 필수 (LARGE/HEAVY):
  - 신규 기능 (기존 코드 대규모 변경)
  - AI/LLM 기능 포함 (출력 품질 사전 합의 필요)
  - 다수 Worker 병렬 실행 (경계 충돌 방지)

CONTRACT 생략 가능 (SMALL/MEDIUM):
  - 기존 기능 수정/개선
  - 단일 Worker 단독 실행
  - 검증 기준이 자명한 경우 ("버튼이 클릭되는가" 수준)
  → 생략 시: CEO가 완료 조건을 Worker 배정 메시지에 직접 명시

CONTRACT 작성 시 닭-달걀 방지:
  - 구체적 테스트 케이스 대신 "검증 방향"만 합의
  - 구현 후 DC-QA가 CONTRACT 기반으로 세부 케이스 도출
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-12. DC-SEC/DC-REV 모델 강등 기준

**Opus 투입 비용을 최소화하기 위한 모델 강등 판단 기준입니다.**

```
[EVALUATOR MODEL POLICY]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DC-SEC 모델 선택:
  Opus  → 인증/인가, 결제, 개인정보, DB 보안, API 키 처리 포함 시
  Sonnet → UI 전용 변경, 텍스트/문서 작업, 내부 유틸리티 수정 시
  Haiku  → 투입 금지 (보안 판단은 최소 Sonnet)

DC-REV 모델 선택:
  Opus  → 아키텍처 변경, 공개 인터페이스 변경, LARGE/HEAVY 스프린트
  Sonnet → SMALL/MEDIUM 스프린트, UI/UX 코드 리뷰
  Haiku  → 투입 금지 (코드 품질 판단은 최소 Sonnet)

DC-BIZ 모델 선택:
  Opus  → 신규 기능, 외부 서비스 연동, 결제 관련
  Sonnet → SMALL 업무, 내부 개선, 문서 작업
  → SMALL 업무에 DC-BIZ Opus 투입 금지

예상 비용 절감: SMALL/MEDIUM 업무에서 Opus 호출 ~60% 감소
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9-13. 스프린트 파일 아카이브 정책

```
[SPRINT FILE LIFECYCLE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
생성: 스프린트 진행 중 docs/ 루트에 생성
보관: 스프린트 완료 후 30일간 docs/ 루트 유지
아카이브: 30일 경과 또는 기능 릴리즈 완료 시
  → docs/archive/YYYY-MM/ 폴더로 이동
삭제: 아카이브 후 90일 경과 시 DC-DOC 판단으로 삭제 가능

정리 트리거:
  - LARGE/HEAVY 업무 완료 시 CEO가 DC-DOC에 정리 지시
  - docs/ 파일 10개 초과 시 자동 트리거
  - 새 스프린트 시작 전 이전 스프린트 파일 아카이브 확인

영구 보관 (삭제 금지):
  - docs/PLAN.md (기능별 최신 버전)
  - docs/HANDOFF-{session}.md (세션 간 맥락 유지)
  - docs/HARNESS-AUDIT.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 보안 정책 (CRITICAL)

---

## §6 실행 신뢰성 원칙 (EXECUTION INTEGRITY — 4개 모두 절대 금지)

**6-1. 완료 미검증 선언 금지** [EXEC-001]
- 구현 완료 = `04-completion-criteria.md` 전 항목 ✅ 확인 후에만
- 미완료 항목 존재 시 → 에이전트 재작업, 완료 선언 불가
- 문서 없으면 → DOC-FIRST 규칙 위반, 즉시 중단

**6-2. 구현 중간 멈춤 금지** [EXEC-002]
- 구현 시작 후 "여기까지만" / "다음 스프린트에서" 절대 금지
- 범위 분리 필요 시 Q&A(PHASE 0.5) 단계에서만 사용자 승인 가능
- 예외: GATE 5 파괴적 변경 감지 → 사용자 승인 후 재개

**6-3. CLI 직접 실행 원칙** [EXEC-003]
- Bash로 실행 가능한 CLI는 CEO/에이전트가 직접 실행
- 사용자 위임 허용 조건: 사용자 인증(oauth/MFA) 필요 또는 사용자 로컬 전용 환경만
- 그 외 "직접 실행하세요" 출력 → EXEC-003 위반

**6-4. 세션 리포트 절대 생략 금지** [EXEC-004]
- [CEO REPORT] / [CEO FAST REPORT] 블록은 모든 작업 완료 후 필수 출력
- 멀티세션 사용자가 "이번 세션에서 뭘 했는지" 한눈에 파악 가능해야 함
- 생략 시 → 즉시 규칙 위반, 리포트 재출력 후 종료

