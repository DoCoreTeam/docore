# DOMANGCHA v3.0.1 — Adaptive Execution

DOMANGCHA ships two install shapes. The default is a per-project loop; the full
18-agent harness is one flag away, and neither overwrites the other.

## Install shapes

There is one command and no install-mode flag. `npx domangcha` reads where it runs:

| Where it runs | What it installs |
|---|---|
| inside a project | the loop there: `LOOP.md`, `CLAUDE.md`, `scripts/loop.mjs`, `.claude/`, `.cursor/`, `.loop/` |
| outside a project | the harness into `~/.claude` and `~/.domangcha` |
| `/ceo` with no harness | offers to install the harness, then runs the request |

A project holding `.loop/` and `scripts/loop.mjs` owns its protocol: the global
`UserPromptSubmit` hook yields to it instead of emitting a route card, so one protocol
reaches the model at a time. `/ceo` is the exception and the escalation path — it always
reaches the router. Everything below describes the harness.
Loop policy is in `domangcha/policies/loop.md`.

## Request flow

```text
Request → IntentNormalizer → TaskRouter → DIRECT | LOOP | GRAPH → validation → completion
```

- DIRECT: explanations, formatting, lookup, and trivial isolated changes. No mandatory planner, recursive loop, agent fan-out, DOC folder, version bump, or publish.
- LOOP: bounded PLAN → EXECUTE → VALIDATE → ACT using the evolved Ralph state and checkpoint system.
- GRAPH: typed state/nodes/edges with parallel branches, retry/fallback, joins, checkpoint/resume, and HUMAN_GATE.

Use `python3 domangcha/engine.py route "<request>"`. Claude's UserPromptSubmit hook calls the same router automatically. Model output may propose an ambiguous classification but cannot override deterministic safety invariants.

## Invariants

- Preserve state when escalating DIRECT → LOOP → GRAPH.
- Security-sensitive, destructive, cross-cutting, resumable, or approval-gated work uses GRAPH.
- A meaningful implementation's writer cannot be its only reviewer.
- Validate ordinary facts—schemas, files, versions, tests, budgets, route enums—in code.
- Never commit, push, publish, deploy, or perform irreversible work without task-specific authority.
- Persist no secrets in checkpoints or structured logs.
- Report progress by default, in the user's language: route and reason up front, loop iteration and
  budget every pass, node and parallel-branch state during graph execution, and what each gate is
  asking to approve. `domangcha/orchestration/status.py` renders these cards for every surface.

Shared policy is under `domangcha/policies/`. Claude-specific agents and hooks are adapters; Codex uses `AGENTS.md`. Agent roles are defined by `domangcha/manifests/agents.json`, and model selection is capability/policy based rather than a permanent model ID.

## Commands

Loop projects need no slash command — the prompt hook injects the protocol and the
active policies on every prompt. The commands below belong to the full harness.

- `/ceo "task"`: automatic route
- `/ceo-ralph "task"`: minimum LOOP route
- `/ceo-debug`, `/ceo-test`, `/ceo-review`, `/ceo-security`, `/ceo-ship`: preserved workflow intents routed through the same engine
- `/ceo-status`: read-only status

## Validation

```bash
python3 -m unittest discover -s domangcha/tests
python3 domangcha/engine.py validate
```

Official version source: `domangcha/VERSION` = 3.0.1.
