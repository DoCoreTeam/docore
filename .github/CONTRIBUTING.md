# Contributing to DOMANGCHA

Thank you for contributing to DOMANGCHA — adaptive DIRECT, LOOP, and GRAPH engineering for Claude Code and OpenAI Codex with 18 logical agent roles.

## Table of Contents

- [Issues](#issues)
- [Pull Requests](#pull-requests)
- [Adding a New Agent](#adding-a-new-agent)
- [Coding Conventions](#coding-conventions)
- [Commit Message Format](#commit-message-format)
- [Code of Conduct](#code-of-conduct)

---

## Issues

### Bug Reports

If you found a bug, please open an issue using the **Bug Report** template. Include:

- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, shell, runtime and version: Claude Code, Codex Local/IDE, or Codex Cloud)

### Feature Requests

For new ideas or improvements, open an issue using the **Feature Request** template. Describe:

- The problem you are trying to solve
- Your proposed solution
- Any alternatives you considered

---

## Pull Requests

1. **Fork** the repository and create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the [Coding Conventions](#coding-conventions) below.

3. Test your changes locally before submitting.

4. Open a Pull Request against `main` with a clear description of what changed and why.

5. Address any review feedback promptly.

---

## Adding a New Agent

All agents live in `domangcha/agents/`. To add a new agent:

1. Create `domangcha/agents/dc-your-agent.md` using the existing frontmatter format.
2. Add the role ID, group, and ModelPolicy intent to `domangcha/manifests/agents.json`.
3. Keep provider-independent identity in the manifest and provider-specific prompt details in the agent file.
4. Update README role documentation when the public role catalog changes.
5. Run `npm test`; the manifest validator rejects count or name drift.

---

## Coding Conventions

### Shell Scripts

- All scripts must be POSIX-compatible bash.
- After editing `install.sh` or any shell script, validate syntax before committing:
  ```bash
  bash -n scripts/your-script.sh
  ```
- Use `#!/usr/bin/env bash` as the shebang line.
- Prefer absolute paths in scripts where applicable.
- Keep scripts focused — one clear responsibility per script.

### Markdown Files

- Keep lines readable (no hard wrapping required, but avoid extremely long lines).
- Use ATX-style headings (`#`, `##`, `###`).
- Code blocks must specify the language for syntax highlighting.

### File Size

- Keep hand-maintained production source around 300 lines where reasonable. Generated, vendor, lock, schema, and unavoidable installer/configuration artifacts are explicit exceptions.

---

## Commit Message Format

All commits must follow this format:

```
v{VERSION}: description of the change
```

Examples:

```
v2.0.12: Add DC-NEW agent for data analysis
v2.0.13: Fix install.sh path resolution on macOS
```

The version number must match the current value in `domangcha/VERSION`. Do not increment MINOR or MAJOR versions unless the change warrants it and is explicitly discussed with the maintainer.

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold these standards:

- Use welcoming and inclusive language.
- Respect differing viewpoints and experiences.
- Accept constructive criticism gracefully.
- Focus on what is best for the community.
- Show empathy toward other contributors.

Violations may be reported to the project maintainer at kko2349@gmail.com.

---

Thank you for helping make DOMANGCHA better.
