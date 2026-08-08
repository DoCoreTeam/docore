# DOMANGCHA v2.1.0 — Claude Code Adapter

This file contains Claude-specific integration only. Shared execution policy lives in `policies/` and deterministic control lives in `engine.py`.

## Claude integration

- `hooks/domangcha-ceo-enforcer.py` calls the canonical TaskRouter.
- `hooks/domangcha-ralph-loop.py` adapts Claude Stop events to canonical LOOP state.
- `agents/dc-*.md` preserve the 18 logical roles and are resolved through `manifests/agents.json`.
- Claude-in-Chrome may be used for interactive live-browser verification; Playwright remains the headless/CI regression fallback.
- Interactive approvals implement HUMAN_GATE. A rejected approval aborts the relevant branch.

Do not reconstruct the legacy mandatory CEO/FULL PIPELINE from prompts. Follow DIRECT, LOOP, or GRAPH returned by `engine.py`.

Official version source: `VERSION` = 2.1.0.
