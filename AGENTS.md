# DOMANGCHA — Codex Adapter

Shared policy lives in `domangcha/policies/`; do not duplicate it here.

When the bundled DOMANGCHA Codex plugin is installed, its `UserPromptSubmit` hook automatically creates the task, selects DIRECT/LOOP/GRAPH, and injects the canonical control command. Use the `domangcha` skill and complete through that command. The `PostToolUse` and `Stop` hooks retain validation evidence and bounded completion enforcement.

Without the plugin, use `python3 domangcha/engine.py route "<request>"` as a degraded manual fallback. Deterministic safety invariants cannot be overridden by model judgment.

Status reporting is on by default. `engine.py route|status` and `scripts/control.py status|resume|progress` render a human-readable card (`--format json` for raw state, `--lang en` for English). Report the route and its reason up front, loop iteration and budget on every pass, node and parallel-branch state during graph execution, and what a gate is asking to approve — in the user's language, without going silent through long steps.

Preserve existing `/ceo-*` command semantics. Codex does not emulate Claude-specific `Agent(...)` syntax; logical roles from `domangcha/manifests/agents.json` map onto runtime-native agents and capabilities. Checkpoint LOOP and GRAPH work under `.domangcha/checkpoints/`. Run `python3 -m unittest discover -s domangcha/tests` and `python3 domangcha/engine.py validate` after orchestration changes.
