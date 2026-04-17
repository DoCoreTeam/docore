# docrew — The AI Chief Executive for Claude Code

> **EN** — You are the Founder. docrew runs your entire engineering team.
>
> **KO** — 당신은 창업자입니다. docrew가 당신의 전체 엔지니어링 팀을 운영합니다.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-docrew-blue)](https://claude.ai/code)

---

## This is not a prompt. This is an engineering team.

> 이것은 프롬프트가 아닙니다. 엔지니어링 팀입니다.

**EN** — Every serious software team needs specialists: a business strategist, researcher, database architect, frontend engineer, backend engineer, security auditor, QA lead, technical writer, DevOps engineer. Hiring all of them costs $2M+ per year.

docrew gives you all 16 — orchestrated by an AI Chief Executive who never forgets a step, never skips a gate, and always asks the right questions before writing a single line of code.

**KO** — 진지한 소프트웨어 팀에는 전문가가 필요합니다. 이들을 모두 고용하면 연간 20억 원 이상이 들고, 완벽하게 조율하는 것은 거의 불가능합니다.

docrew는 이 16명 전부를 제공합니다 — 단 하나의 명령으로, 단 한 단계도 빠뜨리지 않고, 코드 한 줄 쓰기 전에 반드시 올바른 질문을 먼저 묻는 AI 최고경영자가 오케스트레이션합니다.

```bash
# Install once. Runs everywhere. / 한 번 설치. 어디서나 실행.
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/docrew/main/docore/install.sh | bash
```

```bash
# Give orders. CEO handles the rest.
/ceo Build a SaaS app with auth, payments, and a dashboard
/ceo 인증, 결제, 대시보드가 있는 SaaS 앱 만들어줘
```

---

## What makes docrew different / docrew가 다른 이유

### 1. Asks before acting / 행동 전 반드시 묻습니다

**EN** — Other AI tools start writing code the moment you press Enter. docrew asks up to 12 targeted questions — one at a time, step by step, adjusting each question based on your previous answer. Only after all questions are answered does the pipeline begin. No guessing. No wasted work.

**KO** — 다른 AI 도구는 Enter를 누르는 순간 코드를 씁니다. docrew는 최대 12개 질문을 스텝바이스텝으로 묻습니다 — 앞 답변을 반영해 다음 질문을 조정하면서. 답변이 완전히 끝난 후에만 파이프라인이 시작됩니다.

---

### 2. 16 specialists working in parallel / 16명의 전문가가 병렬로 작동합니다

**EN** — Three planners analyze your business case and scout the best open-source tools. CORE specialists build simultaneously: database, backend, frontend, DevOps, docs. EXTENDED specialists (mobile, integrations, copy, SEO) are added only when the task actually needs them. Three evaluators then audit every line for quality, security, and correctness.

**KO** — 3명의 기획자가 사업 타당성을 분석하고 최적의 오픈소스 도구를 탐색합니다. CORE 전문가들이 동시에 빌드합니다: DB, 백엔드, 프론트엔드, DevOps, 문서. EXTENDED 전문가(모바일, 연동, 카피, SEO)는 실제로 필요할 때만 추가됩니다. 3명의 평가자가 모든 코드를 품질, 보안, 정확성으로 동시에 감사합니다.

---

### 3. Never ships broken code / 망가진 코드를 절대 배포하지 않습니다

**EN** — Every output passes 5 mandatory gates. 300-line files are blocked automatically. If a reviewer finds a bug, the system loops back to the builder — up to 3 times — until it passes. Builder and Reviewer are always different agents. No one grades their own homework.

**KO** — 모든 산출물은 5개의 필수 게이트를 통과합니다. 300줄 초과 파일은 자동 차단됩니다. 리뷰어가 버그를 발견하면 시스템이 빌더에게 돌아가 최대 3회 재작업합니다. 빌더와 리뷰어는 항상 다른 에이전트입니다.

---

### 4. Gets smarter every session / 매 세션마다 더 똑똑해집니다

**EN** — docrew maintains an error registry. Every mistake becomes a GATE pattern — so it never happens again. It learns your project's coding patterns as instincts. The longer you use it, the better it knows your codebase.

**KO** — docrew는 오류 레지스트리를 유지합니다. 모든 실수는 GATE 패턴으로 기록되어 반복되지 않습니다. 프로젝트 코딩 패턴을 인스팅트로 학습합니다. 사용할수록 코드베이스를 더 잘 이해합니다.

---

### 5. One command surface / 단일 커맨드 인터페이스

**EN** — docrew installs and orchestrates best-in-class external tools internally. You don't need to learn them. You don't see them. You just use `/ceo-*` and docrew handles the rest.

**KO** — docrew는 최고의 외부 도구들을 내부적으로 설치하고 오케스트레이션합니다. 직접 배울 필요도, 볼 필요도 없습니다. `/ceo-*` 만 사용하면 docrew가 나머지를 처리합니다.

---

## Quick Install / 빠른 설치

```bash
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/docrew/main/docore/install.sh | bash
```

**EN** — One command installs everything. Re-running always updates to the latest version.

**KO** — 명령 하나로 모든 것이 설치됩니다. 재실행하면 항상 최신 버전으로 업데이트됩니다.

### Update / 업데이트

```bash
# Inside Claude Code / Claude Code 안에서
/ceo-update

# Terminal / 터미널에서
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/docrew/main/docore/install.sh | bash
```

| What gets updated | Behavior |
|-------------------|----------|
| docrew agents, commands, SKILL.md | ✅ Always overwritten to latest |
| Orchestrated tools (ECC, gstack, Superpowers) | ✅ Full replacement |
| Registries (error-registry etc.) | ⏭️ Preserved — your data stays |

---

## How It Works / 작동 방식

```
/ceo Build me a SaaS
          │
          ▼
⓪  Q&A ── Step-by-step, up to 12 questions
           앞 답변이 다음 질문을 조정
          │
          ▼
① PLANNER (parallel / 병렬)
  ├── DC-BIZ  Is this worth building?
  ├── DC-RES  Tech research & patterns
  └── DC-OSS  Top 3 open-source tools
          │
          ▼  → PLAN.md
          │
② GENERATOR (parallel / 병렬)
  CORE — always:
  ├── DC-DEV-DB   Schema + migrations
  ├── DC-DEV-BE   API + business logic
  ├── DC-DEV-FE   UI + pages
  ├── DC-DEV-OPS  CI/CD + harness
  └── DC-DOC      API docs
  EXTENDED — added when needed:
  ├── DC-DEV-MOB  Mobile
  ├── DC-DEV-INT  External APIs
  ├── DC-WRT      Marketing copy
  └── DC-SEO      SEO
          │
          ▼
③ CYCLE ── IMPLEMENT → REVIEW → TEST  (max 3x)
          │
          ▼
④ EVALUATOR (simultaneous / 동시)
  ├── DC-QA   Tests & edge cases
  ├── DC-SEC  OWASP Top 10, auth, RLS
  └── DC-REV  Code quality, 300-line limit
          │
          ▼
⑤ GATE 1-5 ── All must pass
          │
          ▼
⑥ REPORT ── Code + tests + docs + git commit
```

---

## Commands / 커맨드

### Main Pipeline / 메인 파이프라인

| Command | EN | KO |
|---------|----|----|
| `/ceo [task]` | Q&A → full 16-agent pipeline | Q&A 후 16개 에이전트 전체 파이프라인 |
| `/ceo-feature [feature]` | Full feature lifecycle | 기능 전체 라이프사이클 |
| `/ceo-init` | Initialize project | 프로젝트 초기화 |
| `/ceo-status` | Show current status | 현재 상태 조회 |
| `/ceo-update` | Update all components to latest | 모든 컴포넌트 최신 버전 업데이트 |

### Tactical Orchestrators / 전술 오케스트레이터

| Command | What it does | 설명 |
|---------|-------------|------|
| `/ceo-plan [feature]` | Q&A → research → implementation plan | Q&A + 리서치 + 구현 계획 |
| `/ceo-review` | Security + quality + PR review | 보안 + 품질 + PR 리뷰 |
| `/ceo-test` | TDD + unit + E2E + browser QA | TDD + 유닛 + E2E + 브라우저 QA |
| `/ceo-ship` | Gate → review → build → deploy | 게이트 → 리뷰 → 빌드 → 배포 |
| `/ceo-design [ui]` | Direction → system → components → review | 방향 → 시스템 → 컴포넌트 → 리뷰 |
| `/ceo-debug [bug]` | Investigate → fix → perf → verify | 조사 → 수정 → 성능 → 검증 |
| `/ceo-quality` | Health → coverage → refactor → security | 헬스 → 커버리지 → 리팩터 → 보안 |
| `/ceo-security` | Secrets → OWASP → auth → API | 시크릿 → OWASP → 인증 → API |
| `/ceo-doc` | Codemaps → API docs → SEO | 코드맵 → API 문서 → SEO |
| `/ceo-learn` | Extract → instincts → retro | 추출 → 인스팅트 → 회고 |

---

## 16 Agents / 16개 에이전트

| Phase | Tier | Agent | Role | Model |
|-------|------|-------|------|-------|
| PLANNER | CORE | DC-BIZ | Business Judge | Opus |
| PLANNER | CORE | DC-RES | Researcher | Haiku |
| PLANNER | CORE | DC-OSS | Open Source Scout | Opus |
| GENERATOR | CORE | DC-DEV-FE | Frontend Developer | Sonnet |
| GENERATOR | CORE | DC-DEV-BE | Backend Developer | Sonnet |
| GENERATOR | CORE | DC-DEV-DB | Database Engineer | Sonnet |
| GENERATOR | CORE | DC-DEV-OPS | DevOps Engineer | Sonnet |
| GENERATOR | CORE | DC-DOC | Documentation Writer | Haiku |
| GENERATOR | EXTENDED | DC-DEV-MOB | Mobile Developer | Sonnet |
| GENERATOR | EXTENDED | DC-DEV-INT | Integration Engineer | Sonnet |
| GENERATOR | EXTENDED | DC-WRT | Writer / Copywriter | Sonnet |
| GENERATOR | EXTENDED | DC-SEO | SEO / AEO / GEO Specialist | Haiku |
| EVALUATOR | CORE | DC-QA | QA Engineer | Haiku |
| EVALUATOR | CORE | DC-SEC | Security Reviewer | Opus |
| EVALUATOR | CORE | DC-REV | Code Reviewer | Opus |
| SUPPORT | CORE | DC-TOK | Token Optimizer | Haiku |

---

## Quality Gates / 품질 게이트

> **EN** — Every output passes 5 mandatory gates. No exceptions.
>
> **KO** — 모든 산출물은 5개 필수 게이트를 통과합니다. 예외 없음.

| Gate | Check |
|------|-------|
| GATE 1 | Error registry scan + **300-line file limit** (auto-blocked) |
| GATE 2 | All completion criteria verified |
| GATE 3 | Version tag `v0.0.0` present |
| GATE 4 | Builder ≠ Reviewer (enforced) |
| GATE 5 | Breaking changes blocked without approval |

---

## Coding Standards / 코딩 표준

> **EN** — Non-negotiable. Enforced by GATE 1 on every file.
>
> **KO** — 협상 불가. GATE 1이 모든 파일에 강제 적용.

| Rule | Detail |
|------|--------|
| **300 lines max per file** | GATE 1 auto-blocks violations |
| 50 lines max per function | — |
| 4 levels max nesting | — |
| Immutability | Always create new objects, never mutate |
| Error handling | Explicit at every level |
| Input validation | At all system boundaries |
| Tests | Required for every feature |
| RLS | Row Level Security always |

---

## Security Built-in / 내장 보안

> **EN** — Security runs on every sprint, not just at the end.
>
> **KO** — 보안은 마지막이 아닌 매 스프린트에 실행됩니다.

| Rule | Detail |
|------|--------|
| OWASP Top 10 | Reviewed every sprint |
| JWT | httpOnly cookies only |
| Encryption | AES-256-GCM for all PII |
| Rate limiting | All endpoints |
| Input validation | Zod at all boundaries |
| RLS | Always enforced |

---

## Requirements / 요구사항

| Requirement | Details |
|-------------|---------|
| [Claude Code](https://claude.ai/code) | Required |
| Anthropic API key | Opus + Sonnet + Haiku access |
| `git` | For installer |

---

## License / 라이선스

MIT — see [LICENSE](LICENSE)

---

*Built by **docrew** / CEO of KDC*
