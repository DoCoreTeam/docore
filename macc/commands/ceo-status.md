# /ceo-status — 현황 조회

프로젝트와 레지스트리 현재 상태를 보여줌

## 출력 포맷

```
[CEO STATUS]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 프로젝트: <프로젝트명>
🏷️ 현재 버전: <macc/VERSION 파일 읽어서 표시>
📊 상태: PLANNING / ACTIVE / REVIEW / DONE

[레지스트리]
🔴 ERROR-REGISTRY: N건 (최근: <마지막 에러 요약>)
🔧 SKILL-REGISTRY: N건
📋 DECISION-LOG:   N건

[하네스 장치]
✅/⬜ pre-commit hook
✅/⬜ lint 규칙
✅/⬜ 아키텍처 테스트
✅/⬜ commit-msg hook
✅/⬜ CI/CD 게이트
✅/⬜ CODEOWNERS
✅/⬜ gc.sh

[최근 스프린트]
Sprint N: PASS/FAIL — <요약>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
