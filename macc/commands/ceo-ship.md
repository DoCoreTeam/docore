# /ceo-ship — 배포 오케스트레이터 / Ship Orchestrator

**EN** — Full ship pipeline: quality gate → review → build → deploy. Combines gstack, ECC, and DC-DEV-OPS agent for a safe, verified release.

**KO** — 품질 게이트 → 리뷰 → 빌드 → 배포 전체 파이프라인. gstack, ECC, DC-DEV-OPS 에이전트를 결합하여 안전하고 검증된 릴리즈를 보장합니다.

## 사용법 / Usage

```
/ceo-ship              → 전체 배포 파이프라인 / Full ship pipeline
/ceo-ship --canary     → 카나리 배포 / Canary release
/ceo-ship --dry-run    → 실제 배포 없이 검증만 / Validate without deploying
/ceo-ship --hotfix     → 핫픽스 빠른 배포 / Hotfix fast-track
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 품질 검증 (Quality Validation)
- ECC `/quality-gate` → 5개 게이트 통과 확인
- ECC `/test-coverage` → 80% 커버리지 확인
- ECC `/security-review` → 보안 취약점 최종 스캔

### STEP 2: 코드 리뷰 (Code Review)
- gstack `/review` → 배포 전 최종 코드 검토
- DC-REV 에이전트 → PASS 판정 확인

### STEP 3: 빌드 검증 (Build Verification)
- ECC `/build-fix` → 빌드 오류 사전 감지 및 수정
- DC-DEV-OPS 에이전트 → CI/CD 파이프라인 상태 확인

### STEP 4: 배포 (Deploy)
- gstack `/ship` → 전체 배포 워크플로우 실행
- `--canary` 옵션 시 → gstack `/canary`
- gstack `/land-and-deploy` → 변경사항 랜딩 + 배포
- ECC `/pipeline` → CI/CD 파이프라인 트리거

### STEP 5: 배포 후 검증 (Post-Deploy Verification)
- gstack `/qa` → 배포된 서비스 브라우저 QA
- DC-QA 에이전트 → 프로덕션 기능 검증

## 결과 보고 / Output

```
[CEO-SHIP REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 품질 게이트 (Quality Gate): PASS
✅ 코드 리뷰 (Code Review):   PASS
✅ 빌드 (Build):              PASS
🚀 배포 (Deploy):             SUCCESS — <환경>
🖥️  배포 후 QA (Post-Deploy): PASS / FAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏷️  버전 (Version): v{VERSION} (macc/VERSION 파일 기준)
🔗 배포 URL: <url>
📋 커밋: <commit hash>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/quality-gate` | ECC | 품질 게이트 |
| `/test-coverage` | ECC | 커버리지 확인 |
| `/security-review` | ECC | 보안 최종 스캔 |
| `/build-fix` | ECC | 빌드 오류 수정 |
| `/pipeline` | ECC | CI/CD 트리거 |
| `/ship` | gstack | 전체 배포 |
| `/canary` | gstack | 카나리 배포 |
| `/land-and-deploy` | gstack | 랜딩 + 배포 |
| `/review` | gstack | 배포 전 리뷰 |
| `/qa` | gstack | 배포 후 QA |
| DC-DEV-OPS | MACC | DevOps 전문 에이전트 |
| DC-REV | MACC | 최종 리뷰 에이전트 |
| DC-QA | MACC | QA 전문 에이전트 |
