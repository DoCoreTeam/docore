# Routing Policy

- DIRECT: read-only work and trivial isolated changes with minimal validation.
- LOOP: iterative implementation that does not need a multi-agent topology.
- GRAPH: cross-cutting, security-sensitive, destructive, parallel, resumable, or approval-gated work.
- `/ceo` uses automatic routing. `/ceo-ralph` sets LOOP as the minimum route.
- A model may propose a route only at an ambiguous boundary; code validates the final route.
