# /ceo-feature — 기능 개발 오케스트레이터 / Feature Development Orchestrator

**EN** — Full feature development lifecycle: plan → TDD → implement → review → ship. The most comprehensive single command for building a new feature end-to-end.

**KO** — 기획 → TDD → 구현 → 리뷰 → 배포 전체 기능 개발 라이프사이클. 새로운 기능을 처음부터 끝까지 빌드하기 위한 가장 포괄적인 단일 커맨드입니다.

## 사용법 / Usage

```
/ceo-feature "기능 설명"   → 전체 기능 개발 라이프사이클 / Full feature lifecycle
/ceo-feature --plan-only   → 기획만 / Plan only
/ceo-feature --no-ship     → 배포 제외 / Skip deployment
/ceo-feature --lang go     → 언어별 TDD / Language-specific TDD
```

## 실행 파이프라인 / Execution Pipeline

이 커맨드는 `/ceo-plan` → `/ceo-test` → 구현 → `/ceo-review` → `/ceo-ship`을 순서대로 실행합니다.
This command runs `/ceo-plan` → `/ceo-test` → implement → `/ceo-review` → `/ceo-ship` in order.

### STEP 1: 기획 (Plan) — `/ceo-plan` 실행
- Q&A로 요구사항 명확화
- DC-BIZ, DC-RES, DC-OSS 에이전트
- `docs/PLAN.md` 생성

### STEP 2: TDD 설정 (TDD Setup) — `/ceo-test --tdd` 실행
- 테스트 먼저 작성 (RED)
- ECC 언어별 테스트 커맨드

### STEP 3: 구현 (Implementation) — 병렬 실행
- DC-DEV-FE, DC-DEV-BE, DC-DEV-DB 에이전트 (해당 항목 병렬)
- ECC `/feature-dev` → 코드베이스 패턴 기반 구현
- ECC `/implement` → 계획 실행
- 테스트 GREEN 통과 확인

### STEP 4: 리뷰 (Review) — `/ceo-review` 실행
- 보안 → 코드 품질 → PR 리뷰
- FAIL 시 최대 3회 재작업

### STEP 5: 배포 (Ship) — `/ceo-ship` 실행
- 품질 게이트 → 빌드 → 배포 → QA

## 결과 보고 / Output

```
[CEO-FEATURE REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 기능명 (Feature): <이름>
📋 기획 (Plan):      ✅ docs/PLAN.md
🧪 TDD:              ✅ <N>개 테스트 통과
💻 구현 (Implement): ✅ <파일 목록>
🔍 리뷰 (Review):    ✅ APPROVED
🚀 배포 (Ship):      ✅ v{VERSION}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏷️  버전: v{VERSION} (macc/VERSION 파일 기준)
📊 커버리지: <X>%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

이 커맨드는 아래 CEO-* 오케스트레이터를 순서대로 호출합니다:
This command calls the following CEO-* orchestrators in order:

| 오케스트레이터 | 역할 |
|---------------|------|
| `/ceo-plan` | 기획 + Q&A + BIZ/RES/OSS |
| `/ceo-test --tdd` | TDD 강제 + 언어별 테스트 |
| `/ceo-review` | 보안 + 코드 품질 + PR 리뷰 |
| `/ceo-ship` | 품질 게이트 + 빌드 + 배포 |

추가 도구:
| 도구 | 출처 | 역할 |
|------|------|------|
| `/feature-dev` | ECC | 코드베이스 기반 구현 |
| `/implement` | ECC | 계획 실행 |
| DC-DEV-FE/BE/DB | MACC | 병렬 구현 에이전트 |
