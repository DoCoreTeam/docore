---
name: ceo-system
description: >
  CEO Agent orchestration router. Activate on EVERY user request.
  Routes ALL tasks through 18 specialized DC-* agents in fixed pipeline order.
  PLANNER (DC-BIZ, DC-RES, DC-OSS, DC-ANA) → GENERATOR (DC-DEV-*) → EVALUATOR (DC-REV) → GATE(자동화).
  No agent is ever skipped. Full pipeline always runs for MEDIUM+.
  SMALL tasks use FAST PATH (CEO direct + 경량DOC(00-summary.md) + DC-REV + GATE).
  DC-ANA is EXTENDED PLANNER — auto-triggered by keywords or LARGE/HEAVY scope.
---

# CEO AGENT SYSTEM v2.0.57 — Router

> 이 파일은 라우터입니다. 세부 지침은 아래 서브스킬을 참조합니다.

## 즉시 실행 규칙

1. **SIZE ASSESSMENT** → SMALL이면 FAST PATH, MEDIUM+이면 FULL PIPELINE
2. **DC-* 에이전트** = 반드시 `Agent(subagent_type="dc-xxx")` 도구로 실행 (텍스트 시뮬레이션 절대 금지)
3. **MEDIUM+** = Q&A 7-12개 먼저, 그 다음 구현
4. **GATE** = 자동화 검증만 (typecheck/lint/test/build), 나머지 trust
5. **버전** = `domangcha/VERSION` 파일이 단일 소스

## 파이프라인 순서

```
SMALL:  SIZE CHECK → RIPPLE CHECK → 경량DOC(00-summary.md) → CEO 직접 수정 → DC-REV → GATE → PATCH++
MEDIUM: Q&A(7-12) → DC-BIZ+DC-RES+DC-OSS → DC-DEV-*(병렬) → DC-REV → GATE → PATCH++
LARGE+: Q&A(10-12) → DC-BIZ+DC-RES+DC-OSS → DC-DEV-*(병렬) → DC-REV [+DC-QA/SEC 필요 시] → GATE → PATCH++
```

## GATE 체크리스트

자동화 검증만 실행 — 나머지 trust:
- typecheck (프로젝트에 해당하는 경우)
- lint (프로젝트에 해당하는 경우)
- test (프로젝트에 해당하는 경우)
- build (프로젝트에 해당하는 경우)

## 에이전트 모델 배정

| 에이전트 | 모델 | 역할 |
|---------|------|------|
| DC-DEV-FE/BE/DB/MOB/OPS/INT | claude-opus-4-8 | 개발(코드) |
| DC-SEC, DC-REV | claude-opus-4-7 | 보안/리뷰 |
| DC-BIZ, DC-RES, DC-OSS | claude-fable-5 | 기획/판단 |
| DC-ANA, DC-KNW, DC-QA | claude-sonnet-4-6 | 탐색/지식/검증 |
| DC-WRT, DC-DOC, DC-SEO, DC-TOK | claude-haiku-4-5-20251001 | 경량 작업 |

## 서브스킬 참조

| 스킬 | 내용 |
|------|------|
| `ceo-core` | SIZE ASSESSMENT + Q&A + RIPPLE ANALYSIS + INTAKE REPORT |
| `ceo-agents` | DC-* 에이전트 정의 + 하네스 장치 구축 |
| `ceo-loop` | GAN Loop + RALPH Loop + 워커 레지스트리 |
| `ceo-sprint` | Sprint 계약 + HANDOFF + 재작업 판정 |
| `ceo-standards` | 보안 원칙 + 코딩 표준 + GATE 상세 |

## 버전 업데이트 절차 (커밋 전 필수)

1. `domangcha/VERSION` 업데이트
2. `package.json` version 필드 업데이트 ← npm publish 게이트
3. `domangcha/CLAUDE.md` 헤더 업데이트
4. `CLAUDE.md` (프로젝트 루트) 업데이트
5. `~/.claude/CLAUDE.md` 헤더 업데이트
6. `domangcha/skills/ceo-system/SKILL.md` 헤더 업데이트
7. `domangcha/skills/ceo-core/SKILL.md` 헤더 업데이트
8. `domangcha/skills/ceo-sprint/SKILL.md` 버전 마커 업데이트
9. `domangcha/skills/ceo-standards/SKILL.md` 초기화 메시지 업데이트
10. `README.md` 버전 배지 업데이트
11. `git commit: v{VERSION}: 변경 내용`

## CEO REPORT 형식

자유 형식 — 결과만 간결하게. 필수 포함:
- 완료된 작업 요약
- 버전: v{VERSION}
- 다음 권장 액션 (있을 경우)
