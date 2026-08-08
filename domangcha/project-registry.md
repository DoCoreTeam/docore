# DOMANGCHA Project Registry

## PRJ-DOMANGCHA

- Status: ACTIVE
- Version source: `domangcha/VERSION`
- Architecture: one adaptive TaskRouter with DIRECT, LOOP, GRAPH executors
- Runtime targets: Claude Code, Codex Local, Codex IDE, Codex Cloud
- Agent source: `manifests/agents.json`
- Command source: `manifests/commands.json`
- Model selection: HIGH_REASONING, BALANCED, FAST_CHEAP, LONG_CONTEXT, REVIEW policies resolved by runtime capability
- Constraints: backward-compatible `/ceo-*` names, deterministic edges, resumable state, no implicit publish/deploy
