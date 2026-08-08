---
name: domangcha
description: Run software-engineering work through DOMANGCHA's adaptive DIRECT, LOOP, or GRAPH execution. Use when the user mentions DOMANGCHA, /ceo, Ralph, loop engineering, graph engineering, or asks Codex to implement, debug, refactor, review, test, secure, or ship work with persistent orchestration and completion evidence.
---

# DOMANGCHA for Codex

Codex lifecycle hooks already created the canonical task, selected its route, and injected a control command into developer context. Do not create a second plan or router.

## Required workflow

1. Read the injected `[DOMANGCHA CODEX CONTROL]` block. Retain its `task_id`, route, and exact control command.
2. Inspect the repository and execute the user request using the selected route.
3. Record meaningful milestones with:

```bash
<control-command> progress --task-id <task-id> --message "<milestone>"
```

4. Before reporting completion, run task-relevant tests, lint, typecheck, build, or deterministic checks. The PostToolUse hook records successful validation commands automatically.
5. Finish through the control plane:

```bash
<control-command> complete --task-id <task-id> --summary "<result>"
```

For GRAPH work that made meaningful changes, add independent review evidence:

```bash
<control-command> complete --task-id <task-id> --summary "<result>" --review "<reviewer and findings>"
```

If completion evidence is missing, the Stop hook can continue the turn with the exact missing requirement. Do not claim completion before the command succeeds.

## Route behavior

- `DIRECT`: answer or make the smallest isolated change; no planner graph, recursive loop, forced docs, or agent fan-out.
- `LOOP`: PLAN → EXECUTE → VALIDATE → ACT, with bounded correction and progress recording.
- `GRAPH`: preserve explicit branches, independent builder/reviewer roles, safety boundaries, checkpoints, and human approval when requested.

Use Codex-native subagents only when independent branches or independent review add value. Never emulate Claude-specific `Agent(...)` syntax.

## Resume and status

Use the injected control command:

```bash
<control-command> status --task-id <task-id>
<control-command> resume --task-id <task-id>
```

Checkpoints live in the workspace under `.domangcha/`. Do not edit checkpoint JSON manually.
