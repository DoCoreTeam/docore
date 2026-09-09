# Loop policy

The v3 default install is a per-project loop. This file is the runtime-neutral
contract; `domangcha/loop/templates/LOOP.md` is the copy that ships into a project.

## Installation surfaces

- `npx domangcha` writes only inside the current project: `LOOP.md`, `CLAUDE.md`,
  `scripts/loop.mjs`, `.claude/`, `.cursor/`, `.loop/`.
- `npx domangcha --full` keeps the v2 behaviour and writes the 18-agent harness into
  `~/.claude` and `~/.domangcha`.
- The two never share a path, so a global v2 install and a project v3 install coexist.

## Precedence

- A project carrying `.loop/` and `scripts/loop.mjs` owns its protocol.
- `hooks/domangcha-ceo-enforcer.py` detects that pair and yields instead of emitting a
  route card, so only one protocol reaches the model.
- A half-installed project (`.loop/` without the CLI) is not treated as a loop project;
  the global router stays in charge.

## Natural language is the entry point

- Slash commands are optional. The `UserPromptSubmit` hook records every prompt as an
  instruction or an intervention and prints the next action with it.
- Read-only requests — questions, lookups, explanations — are answered without a plan.
- Anything that changes the repository goes through PLAN → item → self-audit.

## Policy self-learning

- Repeated audit failures on one item are surfaced after `policy_promote_after` attempts.
- A failure is promoted only when it names a rule that would recur elsewhere; a
  one-item mistake is fixed, not recorded.
- A promoted policy must be judgeable from a diff or a command output.
- Active policies are re-injected on every prompt, in `resume`, and in `policy check`,
  so a context reset cannot lose them.
- A policy broken `policy_rewrite_after` times is not working as written and is retired
  and rewritten rather than repeated.

## Mid-implementation policy checks

The same discipline applies to work on this repository, not only to projects that install the loop.

- Check the registry before each step, not only at the end: `domangcha/error-registry.md` for
  failure classes, `domangcha/policies/` for execution rules.
- When the same mistake appears twice in one change, stop and record it as an `ERR-` row rather
  than fixing both instances silently.
- A recorded rule must be judgeable from a diff. `ERR-011` was added this way: two JSON files were
  rewritten wholesale by a formatter to change one value each, and the reformatting — not the value
  — dominated the diff. The rule is that a config edit whose diff touches untouched keys is a failed
  edit and gets redone in place.
