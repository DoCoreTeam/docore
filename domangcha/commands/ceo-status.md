# /ceo-status — Execution Status

Canonical engine의 DIRECT read-only checkpoint/status adapter다.

```bash
python3 ~/.domangcha/domangcha/engine.py status <task_id> --workspace <project>
```

보고 항목:

- task ID, route, route history
- current status/node
- completed and pending nodes
- attempts, budget usage, error fingerprints
- checkpoint version/time
- pending approval
- artifact references

Secret values와 untrusted artifact 전문은 출력하지 않는다.
