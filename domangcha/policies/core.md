# DOMANGCHA Shared Core Policy

DOMANGCHA uses one adaptive execution authority: `domangcha/engine.py`.

- Normalize intent, then select the minimum reliable route: DIRECT, LOOP, or GRAPH.
- Deterministic invariants override probabilistic classification.
- Preserve state when escalating routes.
- A writer is not the sole reviewer of a meaningful implementation.
- Never claim completion without relevant executable validation.
- External, destructive, or irreversible effects require explicit authority.
- Report progress by default, in the user's language: the selected route and why, loop iteration
  and budget on every pass, node and parallel-branch state during graph execution, and what a gate
  is asking to approve. Silence, hidden stalls, and undisclosed failures are policy violations.
- Render progress through `orchestration/status.py` so every surface reports it the same way.
