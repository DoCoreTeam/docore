# DOMANGCHA Runtime Payload v2.3.1

This directory is the installable DOMANGCHA payload.

```text
engine.py          canonical CLI/router entrypoint
orchestration/     typed contracts, router, loop, graph, checkpoints, validators, status cards
adapters/          runtime capability and model-policy resolution
manifests/         authoritative agents, commands, and version surfaces
graphs/            versioned graph definitions
policies/          shared Claude/Codex policies
agents/            18 logical role prompts
commands/          backward-compatible command adapters
hooks/             Claude Code adapters
../plugins/        Codex-native skill and lifecycle hooks
skills/            reusable role/domain knowledge
```

Run:

```bash
python3 domangcha/engine.py route "Explain this repository"          # human-readable card
python3 domangcha/engine.py route "Explain this repository" --format json
python3 domangcha/engine.py status <task_id> --workspace <project> --lang en
python3 domangcha/engine.py validate
python3 -m unittest discover -s domangcha/tests
```

See the repository root README for architecture, runtime parity, migration, commands, and security details.
