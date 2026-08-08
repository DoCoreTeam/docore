---
name: ceo-loop
description: Compatibility facade for the bounded canonical LoopExecutor.
---

# CEO Loop Compatibility Facade

Loop control belongs to `orchestration/loop.py`. This skill supplies no prompt-only retry authority.

- Preserve Ralph PROMPT/fix-plan/decision UX.
- Enforce max iterations, retry budget, repeated-error and no-progress detection in code.
- Persist checkpoints after every iteration.
- Escalate to GRAPH when topology, security, destructive action, or approval requires it.
- Completion requires deterministic validator evidence.
