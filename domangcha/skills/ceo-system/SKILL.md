---
name: ceo-system
description: DOMANGCHA adaptive execution adapter. Uses one deterministic TaskRouter for DIRECT, LOOP, and GRAPH.
---

# DOMANGCHA Adaptive Execution

The canonical authority is `domangcha/engine.py`; this skill does not define a second router.

1. Normalize the request and call the engine route command.
2. DIRECT uses minimal context and validation without mandatory agents or DOC output.
3. LOOP reuses the bounded Ralph executor and checkpoint state.
4. GRAPH uses typed state, nodes, deterministic edges, retry/fallback, joins, checkpoints, and HUMAN_GATE.
5. A model cannot lower a route selected by a safety invariant.
6. Resolve logical roles from `manifests/agents.json` through runtime-native capabilities.
7. Use policies rather than hard-coded provider model IDs.
8. Do not commit, push, publish, deploy, or perform irreversible work without task-specific authority.

Shared policies live under `domangcha/policies/`. Claude-specific instructions live in CLAUDE.md; Codex-specific instructions live in AGENTS.md.
