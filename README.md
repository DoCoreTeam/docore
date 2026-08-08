# 🚗💨 DOMANGCHA v2.1.0

### Adaptive DIRECT · LOOP · GRAPH engineering for Claude Code and OpenAI Codex

[![Version](https://img.shields.io/badge/version-2.1.0-brightgreen?style=for-the-badge)](domangcha/VERSION)
[![Agents](https://img.shields.io/badge/Agent_Roles-18-FF6B6B?style=for-the-badge)](#18-logical-agent-roles)
[![Runtime](https://img.shields.io/badge/Runtimes-Claude%20%7C%20Codex-blue?style=for-the-badge)](#runtime-parity)

DOMANGCHA selects the minimum orchestration complexity required for reliable execution:

```text
User Request
     │
     ▼
Intent Normalization
     │
     ▼
TaskRouter
     ├── DIRECT  small/read-only work
     ├── LOOP    bounded iterative engineering
     └── GRAPH   explicit complex execution topology
```

It evolves the existing CEO SIZE ASSESSMENT, FAST PATH, FULL PIPELINE, Ralph Loop, DC agents, hooks, and GATE concepts into one deterministic execution authority. It does not bolt a competing graph router onto the old system.

## Install

```bash
npx domangcha
```

The installer configures the Claude Code adapter and installs the shared runtime-neutral engine. Codex projects use the repository `AGENTS.md`; project/runtime-specific installation can be selected as dual-runtime installer support expands.

## Why adaptive routing?

Not every request benefits from a planner, recursive loop, or agent fan-out.

| Route | Best for | Deliberately avoids |
|---|---|---|
| DIRECT | explanation, formatting, summary, lookup, trivial isolated edits | planner graphs, recursive loops, mandatory DOC output, unnecessary model calls |
| LOOP | bug fixes, iterative refactors, validate-and-correct work | multi-agent topology when a single bounded cycle is enough |
| GRAPH | cross-cutting architecture, security, DB+API+UI, parallel branches, pause/resume, destructive work | prompt-only transitions and unbounded context |

Routing is deterministic first. Semantic model classification is allowed only at ambiguous score boundaries, returns a structured enum, and cannot lower a route required by a safety invariant.

## Canonical architecture

```text
Request
  → IntentNormalizer
  → TaskRouter
      ├─ DirectExecutor
      ├─ LoopExecutor (evolved Ralph)
      └─ GraphExecutor
           ├─ typed GraphState
           ├─ Node/Edge contracts
           ├─ retry/fallback
           ├─ fan-out/join
           ├─ checkpoint/resume
           └─ HUMAN_GATE
  → deterministic validators
  → complete / pause / fail
```

Canonical implementation:

- `domangcha/engine.py` — CLI and single routing entrypoint
- `domangcha/orchestration/` — contracts, router, loop, graph, checkpoint, validation
- `domangcha/adapters/` — capability and model-policy resolution
- `domangcha/manifests/` — agent, command, and version sources of truth
- `domangcha/policies/` — shared Claude/Codex policy
- `domangcha/graphs/` — versioned graph definitions

## TaskRouter invariants

- Read-only explanation/formatting is DIRECT.
- Normal iterative implementation is at least LOOP.
- Security-sensitive, destructive, cross-cutting, resumable, or approval-gated work is GRAPH.
- DB + API + frontend changes are GRAPH.
- `/ceo-ralph` means minimum LOOP, not permission to bypass GRAPH safety rules.
- DIRECT can escalate to LOOP; LOOP can escalate to GRAPH without discarding task state.
- Unsafe de-escalation after irreversible mutation is forbidden.

Try the router:

```bash
python3 domangcha/engine.py route "Explain this module"
python3 domangcha/engine.py route "Fix this bug and iterate until tests pass"
python3 domangcha/engine.py route "Change auth, DB schema, API, and frontend"
```

## Loop engineering

The existing Ralph workflow is preserved and promoted:

```text
PLAN → EXECUTE → VALIDATE → ACT
                         ├─ success → COMPLETE
                         ├─ failure → bounded retry
                         └─ topology discovered → GRAPH
```

The engine tracks max iterations, retry budget, no-progress hashes, repeated-error fingerprints, decisions, validation feedback, and checkpoint state. A model-set `exit_signal` is insufficient without fix-plan, tests, evaluator, and gate evidence.

## Graph engineering

Graph nodes declare type, timeout, retry limit, idempotency, required capabilities, and failure/fallback destination. Edges use registered deterministic guards. Free-text model output never directly selects the next node.

Supported node types:

- DETERMINISTIC
- LLM
- AGENT
- TOOL
- VALIDATOR
- HUMAN_GATE
- JOIN

Side effects are classified as PURE, IDEMPOTENT, or NON_IDEMPOTENT. Non-idempotent nodes are not automatically retried without a receipt or compensation policy.

## Checkpoint and approval

LOOP and GRAPH state is versioned and written atomically. Persisted state is allowlisted and secret-like keys are redacted.

```text
RUNNING → WAITING_FOR_APPROVAL → APPROVED / REJECTED → RESUME / ABORT
```

Interactive runtimes can request approval directly. Delegated/cloud execution checkpoints and returns a reviewable pause instead of assuming a synchronous terminal.

## Runtime parity

| Guarantee | Claude Code | Codex Local/IDE | Codex Cloud |
|---|---|---|---|
| Shared router/contracts | ✅ | ✅ | ✅ |
| Native instructions | CLAUDE.md | AGENTS.md | AGENTS.md |
| Logical agent roles | Claude subagents | runtime-native agents | delegated agents when available |
| Checkpoint format | shared | shared | shared |
| Interactive HITL | native | native when interactive | checkpoint/pause |
| Browser verification | Claude-in-Chrome; Playwright fallback | capability-resolved | CI/headless capability |
| Deterministic validators | CLI/hooks | CLI/hooks | CLI/CI |

The runtime detector resolves capabilities such as shell, network, browser, subagents, background execution, checkpointing, workspace writes, and interactive approval. Unknown model or runtime is not an automatic failure.

## Commands

Existing command names remain compatible.

| Command | Adaptive meaning |
|---|---|
| `/ceo "task"` | automatic DIRECT/LOOP/GRAPH routing |
| `/ceo-ralph "task"` | minimum LOOP route |
| `/ceo-debug` | iterative debug intent |
| `/ceo-test` | validation workflow |
| `/ceo-review` | independent review workflow |
| `/ceo-security` | security profile; GRAPH invariant where applicable |
| `/ceo-feature` | feature intent routed by actual scope |
| `/ceo-ship` | guarded external side-effect workflow |
| `/ceo-status` | DIRECT status lookup |
| `/ceo-update` | guarded installer update |

Commit, push, npm publish, and deploy are no longer implicit completion steps for ordinary work. They require task-specific authority.

## 18 logical agent roles

`domangcha/manifests/agents.json` is authoritative. Agent markdown files preserve provider-specific prompts, while model selection uses intent policies rather than permanent provider model IDs.

| Group | Roles |
|---|---|
| PLANNER | DC-ANA, DC-BIZ, DC-RES, DC-OSS, DC-KNW |
| GENERATOR | DC-DEV-BE, DC-DEV-DB, DC-DEV-FE, DC-DEV-INT, DC-DEV-MOB, DC-DEV-OPS, DC-DOC, DC-WRT, DC-SEO |
| EVALUATOR | DC-QA, DC-SEC, DC-REV |
| SUPPORT | DC-TOK |

Agents are nodes chosen when they add value. DIRECT does not invoke expensive evaluators. Meaningful GRAPH implementation preserves writer/reviewer separation.

## GATE evolution

GATE remains a user-facing quality concept, but enforcement is code-owned.

- repository/manifest/version validation
- route and schema validation
- graph reachability and terminal validation
- bounded retry checks
- checkpoint compatibility
- builder/reviewer identity separation
- task-relevant typecheck, lint, test, and build
- explicit HUMAN_GATE for destructive or irreversible actions

The 300-line guideline applies to hand-maintained production source with explicit exemptions for generated, vendor, and unavoidable installer/configuration artifacts.

## Security

- untrusted worker/tool output cannot control edges
- artifact paths are constrained to the workspace
- checkpoints and logs redact secret-like fields
- external/destructive actions use explicit authority
- prompt injection does not override code invariants
- retries respect idempotency and side-effect receipts

## Development and validation

```bash
npm test
```

This runs orchestration unit tests, routing and failure behavior, manifest/version validation, and shell syntax checks.

```bash
python3 -m unittest discover -s domangcha/tests -v
python3 domangcha/engine.py validate
npm pack --dry-run
```

## Migration from v2.0

- CEO SIZE ASSESSMENT became the canonical TaskRouter.
- FAST PATH became true DIRECT execution.
- Ralph became the canonical bounded LOOP executor.
- FULL PIPELINE became a versioned GRAPH definition.
- Claude hooks became thin adapters.
- `AGENTS.md` adds native Codex instructions.
- repeated route/gate/model/version metadata moved into manifests and shared policy.
- mandatory publish/deploy behavior was removed from ordinary completion.

## License

MIT

---

## 한국어 요약

DOMANGCHA v2.1.0은 모든 작업에 18개 에이전트와 전체 파이프라인을 강제하지 않습니다. 요청을 먼저 정규화하고 DIRECT, LOOP, GRAPH 중 신뢰성에 필요한 최소 복잡도를 선택합니다.

- 간단한 설명·요약·조회·사소한 수정은 DIRECT
- 반복 수정과 검증이 필요한 작업은 기존 Ralph를 발전시킨 LOOP
- 보안·파괴적 변경·복합 아키텍처·병렬 작업·중단/재개가 필요한 작업은 GRAPH

Claude Code와 OpenAI Codex는 같은 엔진·상태·검증 규칙을 사용하고, CLAUDE.md와 AGENTS.md에는 런타임 차이만 둡니다. 기존 `/ceo-*` 명령과 18개 역할은 유지됩니다.
