---
name: ceo-core
description: Compatibility facade for DOMANGCHA intent normalization and routing.
---

# CEO Core Compatibility Facade

This skill delegates all routing to `domangcha/engine.py` and contains no independent SIZE, FAST PATH, FULL PIPELINE, Q&A, retry, or completion authority.

- Existing callers may keep the `ceo-core` name.
- DIRECT/LOOP/GRAPH semantics come from `policies/routing.md`.
- Deterministic invariants always win over semantic model proposals.
- State-preserving escalation is allowed; unsafe de-escalation is not.
