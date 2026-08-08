# DOMANGCHA Shared Core Policy

DOMANGCHA uses one adaptive execution authority: `domangcha/engine.py`.

- Normalize intent, then select the minimum reliable route: DIRECT, LOOP, or GRAPH.
- Deterministic invariants override probabilistic classification.
- Preserve state when escalating routes.
- A writer is not the sole reviewer of a meaningful implementation.
- Never claim completion without relevant executable validation.
- External, destructive, or irreversible effects require explicit authority.
