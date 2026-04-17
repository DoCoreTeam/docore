# /ceo-security — 보안 오케스트레이터 / Security Orchestrator

**EN** — Full security audit pipeline: OWASP scan → secrets → auth → rate limiting → penetration. Combines ECC's security suite with gstack and DC-SEC agent.

**KO** — OWASP 스캔 → 시크릿 → 인증 → 레이트 리미팅 → 침투 테스트 전체 보안 파이프라인. ECC 보안 스위트 + gstack + DC-SEC 에이전트를 결합합니다.

## 사용법 / Usage

```
/ceo-security              → 전체 보안 감사 / Full security audit
/ceo-security --owasp      → OWASP Top 10만 / OWASP Top 10 only
/ceo-security --secrets    → 시크릿 노출만 / Secrets exposure only
/ceo-security --auth       → 인증/인가만 / Auth/authz only
/ceo-security --api        → API 보안만 / API security only
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 시크릿 스캔 (Secrets Scan)
- DC-SEC 에이전트 → API 키, 비밀번호, 토큰 하드코딩 탐지
- ECC `security-scan` 스킬 → 자동화 스캔

### STEP 2: OWASP Top 10 (OWASP Audit)
- ECC `/security-review` → OWASP 전체 체크리스트
  - A01: 접근 제어 취약점
  - A02: 암호화 실패
  - A03: 인젝션 (SQL, XSS, Command)
  - A04: 안전하지 않은 설계
  - A05: 보안 설정 오류
  - A06: 취약한 컴포넌트
  - A07: 인증 및 세션 관리 실패
  - A08: 소프트웨어/데이터 무결성
  - A09: 보안 로깅/모니터링 실패
  - A10: SSRF

### STEP 3: 인증/인가 검토 (Auth Review)
- DC-SEC 에이전트 → JWT 설정, RLS 구현, 권한 체계 검토

### STEP 4: API 보안 (API Security)
- ECC `/security-review` → 레이트 리미팅, 입력 검증, CORS 설정 확인

### STEP 5: 보안 취약점 수정 (Fix)
- CRITICAL 발견 시 → 즉시 중단 + 수정 계획 수립
- DC-DEV-BE, DC-DEV-FE 에이전트 → 취약점 수정 실행

## 결과 보고 / Output

```
[CEO-SECURITY REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔑 시크릿 노출 (Secrets):    CLEAN / <N>건 발견
🛡️  OWASP Top 10:            PASS / FAIL — <이슈>
🔐 인증/인가 (Auth):          PASS / FAIL
🌐 API 보안 (API):            PASS / FAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 CRITICAL: <목록>
⚠️  HIGH:     <목록>
ℹ️  MEDIUM:   <목록>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚦 최종 판정: ✅ SECURE / 🔴 BLOCKED (CRITICAL 발견)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **CRITICAL 발견 시 즉시 중단** — 수정 전까지 배포 불가
> Stop immediately on CRITICAL — no deploy until fixed

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/security-review` | ECC | OWASP + API 보안 |
| `security-scan` | ECC skill | 자동 스캔 |
| `security-bounty-hunter` | ECC skill | 버그 바운티 스타일 탐색 |
| DC-SEC | MACC | 보안 전문 에이전트 |
| DC-DEV-BE | MACC | 백엔드 취약점 수정 |
| DC-DEV-FE | MACC | 프론트엔드 취약점 수정 |
