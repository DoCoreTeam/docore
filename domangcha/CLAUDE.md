# DOMANGCHA v3.0.5 — Claude Code Adapter

This file contains Claude-specific integration only. Shared execution policy lives in `policies/` and deterministic control lives in `engine.py`.

## Two install shapes

- `npx domangcha` decides by location: inside a project it installs the loop there (`loop/templates/` → project root) and never writes to `~/.claude`; outside a project it runs `install.sh` and installs everything below into `~/.claude` and `~/.domangcha`.
- `hooks/domangcha-ceo-enforcer.py` yields when the project carries `.loop/` and `scripts/loop.mjs`, so a global install and a loop project never both speak — except for `/ceo`, which always reaches the router and is the documented escalation path.
- `loop/templates/scripts/loop.mjs` gates `/ceo` on machines without the harness and offers to install it, so a loop-only project still has a route up.

## Claude integration

- `hooks/domangcha-ceo-enforcer.py` calls the canonical TaskRouter.
- `hooks/domangcha-ralph-loop.py` adapts Claude Stop events to canonical LOOP state and injects the live loop card.
- `orchestration/status.py` is the single renderer for route, loop, graph, and parallel-branch cards. Status reporting is on by default; both hooks inject the card plus the reporting contract.
- `agents/dc-*.md` preserve the 18 logical roles and are resolved through `manifests/agents.json`.
- Claude-in-Chrome may be used for interactive live-browser verification; Playwright remains the headless/CI regression fallback.
- Interactive approvals implement HUMAN_GATE. A rejected approval aborts the relevant branch.

Do not reconstruct the legacy mandatory CEO/FULL PIPELINE from prompts. Follow DIRECT, LOOP, or GRAPH returned by `engine.py`.

Official version source: `VERSION` = 3.0.5.
