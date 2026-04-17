# /ceo-init — 프로젝트 최초 셋업

새 프로젝트에 CEO 시스템을 처음 세팅할 때 사용

## 실행 순서

### Step 1: gstack 스킬 확인
- https://github.com/garrytan/gstack 스킬 설치 여부 확인
- 미설치 시 설치 → 이미 설치되었으면 패스

### Step 2: 레지스트리 초기화
아래 파일들을 `~/.claude/` 에 생성 (없으면):
- `error-registry.md` — 실수 기록 + 방어 규칙
- `skill-registry.md` — 학습된 스킬 패턴
- `project-registry.md` — 프로젝트 등록부
- `decision-log.md` — 의사결정 기록

### Step 3: 하네스 장치 전체 구축
DC-DEV-OPS를 통해 아래 7개를 전부 구축:
1. pre-commit hook — error-registry 금지 패턴 자동 스캔
2. lint 규칙 — 프로젝트 컨벤션 린터 강제
3. 아키텍처 테스트 — 의존성 방향/레이어 분리 테스트
4. commit-msg hook — 버전 태그 + Conventional Commits 강제
5. CI/CD 게이트 — GATE 1-5 자동 실행
6. CODEOWNERS — 파일/디렉토리 보호
7. gc.sh — error-registry 기반 방어 규칙 자동 생성

### Step 4: 사업 분류
DC-BIZ 호출하여 초기 프로젝트 분류

### Step 5: 프로젝트 등록
project-registry.md에 초기 PROJECT 항목 생성

### Step 6: 에이전트 파일 확인
.claude/agents/ 디렉토리에 모든 Worker 에이전트 파일 존재 확인
미존재 시 생성

### Step 7: 초기화 보고

```
[CEO SYSTEM INITIALIZED] v1.0.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ERROR-REGISTRY : N건
SKILL-REGISTRY : N건
DECISION-LOG   : N건
ACTIVE PROJECTS: N개
MODEL TIERS    : Opus(설계·보안·검토) / Sonnet(개발·분석) / Haiku(리서치·문서·QA)
DEV WORKERS    : FE / BE / DB / MOB / OPS / INT (병렬)
SPECIAL WORKERS: BIZ(사업판단) / OSS(자원탐색) / TOK(토큰관리)
GATE           : 1-5 가동
HARNESS        : ①~⑦ 구축 완료
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
준비 완료. 지시를 내려주세요.
```
