# DOMANGCHA — Codex Adapter

Shared policy lives in `domangcha/policies/`; do not duplicate it here.

Before work, use `python3 domangcha/engine.py route "<request>"` when DOMANGCHA routing is requested. Follow the returned DIRECT, LOOP, or GRAPH route. Deterministic safety invariants cannot be overridden by model judgment.

Preserve existing `/ceo-*` command semantics. Codex does not emulate Claude-specific `Agent(...)` syntax; logical roles from `domangcha/manifests/agents.json` map onto runtime-native agents and capabilities. Checkpoint LOOP and GRAPH work under `.domangcha/checkpoints/`. Run `python3 -m unittest discover -s domangcha/tests` and `python3 domangcha/engine.py validate` after orchestration changes.
