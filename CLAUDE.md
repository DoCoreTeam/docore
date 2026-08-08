# DOMANGCHA v2.1.1 — Adaptive Execution

DOMANGCHA has one orchestration authority: `domangcha/engine.py`.

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

Shared policy is under `domangcha/policies/`. Claude-specific agents and hooks are adapters; Codex uses `AGENTS.md`. Agent roles are defined by `domangcha/manifests/agents.json`, and model selection is capability/policy based rather than a permanent model ID.

## Commands

- `/ceo "task"`: automatic route
- `/ceo-ralph "task"`: minimum LOOP route
- `/ceo-debug`, `/ceo-test`, `/ceo-review`, `/ceo-security`, `/ceo-ship`: preserved workflow intents routed through the same engine
- `/ceo-status`: read-only status

## Validation

```bash
python3 -m unittest discover -s domangcha/tests
python3 domangcha/engine.py validate
```

Official version source: `domangcha/VERSION` = 2.1.1.
