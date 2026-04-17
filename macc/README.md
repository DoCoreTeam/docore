# 👔 MACC — Multi-Agent Claude Crew

> You are the Founder. MACC runs your entire engineering team.
> 당신은 창업자입니다. MACC가 당신의 전체 엔지니어링 팀을 운영합니다.

```bash
# Install / 설치
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/macc/main/macc/install.sh | bash

# Give orders. CEO handles the rest. / 지시만 내려주세요.
/ceo "Build a SaaS app with auth, payments, and a dashboard"
```

## Why CEO is different / CEO가 다른 이유

**EN** — Every other AI tool starts writing code the moment you press Enter. CEO stops and asks the right questions first. Then 16 specialists build in parallel — planners, developers, QA engineers, security reviewers — all coordinated, all accountable, all running through 5 mandatory quality gates before anything reaches you.

**KO** — 다른 AI 도구는 Enter를 누르는 순간 코드를 씁니다. CEO는 먼저 올바른 질문을 합니다. 그리고 16명의 전문가가 병렬로 빌드합니다 — 기획자, 개발자, QA 엔지니어, 보안 리뷰어 — 모두 조율되고, 모두 책임지며, 모두 5개의 필수 게이트를 통과한 후 당신에게 전달됩니다.

## How it works / 작동 방식

```
/ceo "Build me a SaaS" → /ceo "SaaS 만들어줘"
     │
     ▼
⓪ Q&A ── CEO asks before acting / 행동 전 질문
     │       "Tech stack? Platform? Done criteria? Constraints?"
     ▼
① PLANNER ── DC-BIZ + DC-RES + DC-OSS → PLAN.md
     ▼
② GENERATOR (parallel / 병렬)
     │  DC-DEV-FE + DC-DEV-BE + DC-DEV-DB + DC-DEV-MOB
     │  DC-DEV-OPS + DC-DEV-INT + DC-WRT + DC-DOC + DC-SEO
     ▼
③ CYCLE ── IMPLEMENT → REVIEW → TEST → (fix if needed, max 3x)
     ▼
④ EVALUATOR ── DC-QA + DC-SEC + DC-REV (simultaneously / 동시)
     ▼
⑤ GATE 1-5 ── All must pass / 전부 통과 필수
     ▼
⑥ REPORT ── Code + tests + docs + git commit v0.x.0
```

## Commands / 명령어

### CEO Commands / CEO 커맨드

| Command / 커맨드 | What it does (EN) | 설명 (KO) | Tools |
|-----------------|------------------|-----------|-------|
| `/ceo "task"` | Q&A → full 16-agent pipeline | Q&A 후 16개 에이전트 전체 파이프라인 | All 16 agents |
| `/ceo-feature "feature"` | Full feature lifecycle end-to-end | 기능 처음부터 끝까지 | plan+test+review+ship |
| `/ceo-plan "feature"` | Q&A + BIZ + research + OSS + plan | 기획 전체 오케스트레이터 | DC-BIZ/RES/OSS + ECC + gstack |
| `/ceo-review` | Security + quality + PR review | 리뷰 전체 오케스트레이터 | ECC + gstack + DC-SEC/REV |
| `/ceo-test` | TDD + unit + E2E + browser QA | 테스트 전체 오케스트레이터 | ECC + gstack + DC-QA |
| `/ceo-ship` | Gate + review + build + deploy + QA | 배포 전체 오케스트레이터 | gstack + ECC + DC-DEV-OPS |
| `/ceo-design "ui"` | Direction + system + components + review | 디자인 전체 오케스트레이터 | gstack × 5 + ECC + DC-DEV-FE |
| `/ceo-debug "bug"` | Investigate + fix + perf + verify | 디버그 전체 오케스트레이터 | gstack + ECC |
| `/ceo-quality` | Health + coverage + refactor + security | 품질 전체 오케스트레이터 | gstack + ECC + DC-QA/SEC/REV |
| `/ceo-security` | Secrets + OWASP + auth + API | 보안 전체 오케스트레이터 | ECC + DC-SEC |
| `/ceo-doc` | Codemaps + API docs + docs + SEO | 문서 전체 오케스트레이터 | gstack + ECC + DC-DOC/SEO |
| `/ceo-learn` | Patterns + instincts + retro | 학습 전체 오케스트레이터 | gstack + ECC |
| `/ceo-init` | Initialize project | 프로젝트 초기화 | — |
| `/ceo-status` | Show current status | 현재 상태 조회 | — |

### ECC Commands / ECC 커맨드

79 commands from [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)

| Category / 카테고리 | Commands / 커맨드 |
|--------------------|------------------|
| Planning / 기획 | `/plan` `/feature-dev` `/implement` `/spec` `/prp-prd` `/prp-plan` `/prp-implement` `/prp-commit` `/prp-pr` `/multi-plan` `/multi-execute` `/multi-frontend` `/multi-backend` `/multi-workflow` |
| Review / 리뷰 | `/code-review` `/review-pr` `/security-review` `/quality-gate` `/santa-loop` `/refactor-clean` `/perf-check` `/test-coverage` `/python-review` `/go-review` `/rust-review` `/cpp-review` `/flutter-review` `/kotlin-review` |
| Test / 테스트 | `/tdd` `/test` `/e2e` `/go-test` `/rust-test` `/cpp-test` `/flutter-test` `/kotlin-test` |
| Build / 빌드 | `/build-fix` `/go-build` `/rust-build` `/cpp-build` `/flutter-build` `/kotlin-build` `/gradle-build` |
| Session / 세션 | `/save-session` `/resume-session` `/sessions` `/checkpoint` `/context-budget` `/aside` |
| Learning / 학습 | `/learn` `/learn-eval` `/evolve` `/instinct-status` `/instinct-import` `/instinct-export` `/promote` `/prune` `/projects` |
| Hooks / 훅 | `/hookify` `/hookify-configure` `/hookify-help` `/hookify-list` |
| DevOps | `/pipeline` `/pm2` `/setup-pm` `/devfleet` |
| Docs / 문서 | `/docs` `/update-docs` `/update-codemaps` `/report` |
| Cost / 비용 | `/cost-estimate` `/model-route` `/prompt-optimize` |
| Loop / 루프 | `/loop-start` `/loop-status` `/orchestrate` |
| Misc / 기타 | `/debug` `/design` `/ui-design` `/jira` `/skill-create` `/skill-health` `/agent-sort` `/rules-distill` `/evaluate-oss` |

### gstack Commands / gstack 커맨드

35+ commands from [garrytan/gstack](https://github.com/garrytan/gstack)

| Category / 카테고리 | Commands / 커맨드 |
|--------------------|------------------|
| Ship / 배포 | `/ship` `/land-and-deploy` `/canary` `/setup-deploy` |
| QA / 테스트 | `/qa` `/qa-only` `/test` `/benchmark` |
| Review / 리뷰 | `/review` `/health` `/investigate` |
| Planning / 기획 | `/plan` `/autoplan` `/plan-ceo-review` `/plan-eng-review` `/plan-design-review` `/office-hours` |
| Design / 디자인 | `/design` `/design-review` `/design-consultation` `/design-html` `/design-shotgun` |
| Docs / 문서 | `/docs` `/document-release` |
| Learning / 학습 | `/learn` `/retro` `/checkpoint` |
| Safety / 안전 | `/freeze` `/unfreeze` `/guard` `/careful` |
| Browser / 브라우저 | `/browse` `/connect-chrome` `/setup-browser-cookies` |
| Misc / 기타 | `/codex` `/cso` `/gstack-upgrade` |

## 16 Agents / 16개 에이전트

| Phase | Agent | Role (EN) | 역할 (KO) | Model |
|-------|-------|-----------|-----------|-------|
| PLANNER | DC-BIZ | Business Judge | 사업 타당성 판단 | Opus |
| PLANNER | DC-RES | Researcher | 리서처 | Haiku |
| PLANNER | DC-OSS | Open Source Scout | 오픈소스 탐색 | Opus |
| GENERATOR | DC-DEV-FE | Frontend Developer | 프론트엔드 개발자 | Sonnet |
| GENERATOR | DC-DEV-BE | Backend Developer | 백엔드 개발자 | Sonnet |
| GENERATOR | DC-DEV-DB | Database Engineer | DB 엔지니어 | Sonnet |
| GENERATOR | DC-DEV-MOB | Mobile Developer | 모바일 개발자 | Sonnet |
| GENERATOR | DC-DEV-OPS | DevOps Engineer | DevOps 엔지니어 | Sonnet |
| GENERATOR | DC-DEV-INT | Integration Engineer | 통합 엔지니어 | Sonnet |
| GENERATOR | DC-WRT | Writer / Copywriter | 카피라이터 | Sonnet |
| GENERATOR | DC-DOC | Documentation Writer | 기술 문서 작가 | Haiku |
| GENERATOR | DC-SEO | SEO / AEO / GEO | SEO 전문가 | Haiku |
| EVALUATOR | DC-QA | QA Engineer | QA 엔지니어 | Haiku |
| EVALUATOR | DC-SEC | Security Reviewer | 보안 리뷰어 | Opus |
| EVALUATOR | DC-REV | Code Reviewer | 코드 리뷰어 | Opus |
| SUPPORT | DC-TOK | Token Optimizer | 토큰 최적화 | Haiku |

## Quality Gates / 품질 게이트

| Gate | Check (EN) | 검사 항목 (KO) |
|------|------------|---------------|
| GATE 1 | Error patterns + **300-line limit** (auto-blocked) | 오류 패턴 + **300줄 초과 자동 차단** |
| GATE 2 | All completion criteria met | 완료 조건 충족 |
| GATE 3 | Version tag matches `macc/VERSION` | 버전 태그 존재 |
| GATE 4 | Builder ≠ Reviewer (enforced) | 빌더 ≠ 리뷰어 강제 |
| GATE 5 | No breaking changes without approval | 승인 없는 브레이킹 체인지 차단 |

## Structure / 구조

```
macc/
├── CLAUDE.md                    ← CEO brain entry point / CEO 두뇌 진입점
├── install.sh                   ← One-line installer / 원라인 설치 스크립트
├── agents/                      ← 16 agent definitions / 16개 에이전트 정의
│   └── dc-biz.md ... dc-tok.md
├── commands/                    ← 14 CEO commands / 14개 CEO 커맨드
│   ├── ceo.md ceo-feature.md ceo-plan.md ceo-review.md
│   ├── ceo-test.md ceo-ship.md ceo-design.md ceo-debug.md
│   ├── ceo-quality.md ceo-security.md ceo-doc.md ceo-learn.md
│   ├── ceo-init.md ceo-status.md
├── skills/ceo-system/SKILL.md   ← Full orchestration system / 전체 오케스트레이션
└── templates/                   ← error-registry, skill-registry, project-registry, decision-log
```

## License / 라이선스

MIT
