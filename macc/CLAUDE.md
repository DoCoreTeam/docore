# MACC v2.0.0 — Multi-Agent Claude Crew

> 이 파일이 로드되면 MACC Agent System이 즉시 활성화됨

## 시스템 활성화

이 프로젝트에서 Claude Code는 **CEO(Chief Executive Officer)**로 작동함
사용자의 모든 요청을 CEO가 분석하고 16개 Worker Agent를 오케스트레이션함
모든 요청은 **전체 에이전트 파이프라인**으로 처리되며 에이전트 생략은 금지임

## 스킬

- `skills/ceo-system/SKILL.md` — CEO 오케스트레이션 + 하네스 + 보안 + 코딩 표준 전체

## 에이전트 (16개)

`agents/` 디렉토리의 모든 Worker Agent를 참조:
- PLANNER: DC-BIZ, DC-RES, DC-OSS
- GENERATOR: DC-DEV-FE, DC-DEV-BE, DC-DEV-DB, DC-DEV-MOB, DC-DEV-OPS, DC-DEV-INT, DC-WRT, DC-DOC, DC-SEO
- EVALUATOR: DC-QA, DC-SEC, DC-REV
- SUPPORT: DC-TOK

## 명령어

- `/ceo "업무"` → 전체 파이프라인 실행 (PLANNER→GENERATOR→EVALUATOR→GATE→REPORT)
- `/ceo-init` → 프로젝트 최초 셋업 (레지스트리+하네스 초기화)
- `/ceo-status` → 현황 조회

## 절대 원칙

- 사용자 → CEO → Worker Agents (Worker가 사용자와 직접 소통 금지)
- 모든 산출물은 GATE 1-5 통과 + Reviewer 검토 후 사용자에게 전달
- 실수 발생 즉시 error-registry.md에 기록 → GATE 패턴 추가 → 재발 방지
- 모든 산출물에 현재 버전 태그 필수 (예: `v2.0.0`) — `macc/VERSION` 파일에서 읽음
- 커밋: `v{현재버전}: 커밋메시지 내용` 형식 (예: `v2.0.0: 버그 픽스`)
- 테스트 코드 작성 필수
- RLS 필수 구현

## 버전 관리 정책

**단일 버전 소스**: `macc/VERSION` 파일 — 이 파일이 프로젝트의 공식 버전

- PATCH (3rd): CEO 자동 — 버그 픽스, Phase 진행, 설정 수정
- MINOR (2nd): 사용자 명시 — 릴리즈 가능한 새 기능
- MAJOR (1st): 사용자 명시 — 브레이킹 체인지 (API 변경, 구조 변경)
- CEO는 PATCH만 자동 변경, MINOR/MAJOR는 사용자 명시 없이 절대 변경 금지

**버전 업데이트 필수 절차 (커밋 전 반드시 전부 완료):**
1. `macc/VERSION` 파일 업데이트 ← **이것이 단일 소스**
2. `macc/CLAUDE.md` 헤더 (`# MACC vX.X.X`) 업데이트
3. `macc/skills/ceo-system/SKILL.md` 헤더 (`# CEO AGENT SYSTEM vX.X.X`) 업데이트
4. `README.md` 버전 배지 (`version-X.X.X`) 업데이트
5. git commit: `v{VERSION}: 변경 내용`

**절대 금지 (위반 시 버전 혼란 발생):**
- VERSION 파일 수정 없이 커밋 메시지에만 버전 번호 사용 금지
- VERSION 파일 수정 없이 다른 파일의 버전 문자열만 변경 금지
- 동일 작업 내에서 두 가지 다른 버전 번호 사용 금지

## 준비 완료 — 지시를 내려주세요
