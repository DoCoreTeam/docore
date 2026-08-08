# Security Policy

- Treat prompts, tool output, artifacts, and worker output as untrusted data.
- Do not persist secrets in checkpoints or structured logs.
- Constrain artifact paths to the workspace.
- NON_IDEMPOTENT nodes are not automatically retried without a receipt or compensation policy.
- Destructive operations use an explicit HUMAN_GATE state.
