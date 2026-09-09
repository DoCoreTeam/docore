# DOMANGCHA v3.0.1 — LOOP project autonomous dev protocol

This file is the only working rulebook, loaded every session
In this project these rules take precedence over any global rules (~/.claude/CLAUDE.md)
Add project conventions to the appendix at the bottom only; leave the body alone
The heavy rules (the 18-agent harness) live in .claude/heavy/CEO.md and are read only for items marked heavy

Slash commands are optional; plain natural language drives this protocol
The UserPromptSubmit hook records every prompt as an instruction or an intervention and prints the
next action together with the active policies, so following the hook output is enough

## 0 State and tools

- The only basis for resuming: .loop/PLAN.md — even after a context reset this file alone continues from the next item
- Accumulated policies: .loop/POLICY.md — repeated mistakes promoted by self-audit, checked line by line in every item audit
- Record CLI: node scripts/loop.mjs (written as loop below); instructions, interventions and implementations are stored in .loop/loop.db
- Recorded automatically by hooks: user prompts (instruction or intervention), file edits, session start, context compaction
- Recorded by the agent: loop plan new, plan check, plan confirm, plan revise, start, pass, fail, hold, final
- First action right after a session starts or the context is cleared: read the loop resume output (the hook prints it; run it yourself if you do not see it)

## 1 Loop 1 — plan before doing

On a new instruction, follow this order before touching code
An instruction given in plain language, with no slash command, follows the same procedure

Exceptions where no plan is written (answer directly and stop)
- Requests that do not change the repository: questions, lookups, explanations, summaries, reading code
- Changes so self-evident there is nothing to audit, such as fixing one typo
- When it is unclear whether a request qualifies, write the plan

1 Run loop resume to see whether a plan is active; if one is, treat the new instruction as an intervention and apply section 2
2 Run loop plan new --title "title" --instruction ins_xxxx --target vX.Y.Z (the ins id is in the hook output; from the current package.json version, raise minor for a feature and patch for a fix)
3 Write the goal, out of scope, definition of done, references and items in .loop/PLAN.md
4 Revise until loop plan check passes
5 If plan_confirm is true, show the user a plan summary (item count, target version, out of scope), wait for their reply, and run loop plan confirm once they confirm
6 If plan_confirm is false, run loop plan confirm immediately

Writing items

- One item is a unit that a single self-audit can judge (at most 5 changed files; 1 to 4 audit criteria recommended)
- Scope: list the files or directories to change; mark new files "new"
- Audit criteria: only runnable commands with expected results, or observable conditions; never vague phrasing like "works well"
- Depends: preceding item ids, or "none"
- Mode: light by default; payments, authentication, permissions, data deletion, external APIs and secret handling are heavy
- Order: schema, server, screen, i18n, documentation by default, with dependencies deciding the real order
- An inserted item takes the previous number plus a letter (insert after I03 becomes I03a); never renumber existing items
- To drop an item, set its status to cancelled (reason) and keep the line

## 2 Loop 2 — implement an item and audit it

Repeat this per item and do not touch the next item until this one passes

1 Run loop start Ixx and treat the printed scope and audit criteria as the brief; in heavy mode read heavy_doc first
2 Implement, staying inside the scope
3 Run the 7-point self-audit
  a Scope match: the changed files in git status match the item scope; revert out-of-scope changes or record the reason in the summary
  b Static checks: cmd_typecheck passes, and cmd_lint passes if lint is configured
  c Item criteria: actually run or verify each criterion line and keep one line of evidence for each
  d Secrets and settings: no keys, tokens or passwords in the diff; new settings go to the database with UI management rather than new env vars (reusing existing env keys is fine)
  e i18n: every new user-facing string goes through an i18n key, with the default-language and English message files updated together
  f Side effects: nothing breaks another item's passing condition; re-run the related tests
  g Policy compliance: run loop policy check and compare every active rule against this change,
    record any breach with loop policy hit P00x --note "what you broke", fix it and compare again,
    never pass an item while a policy is broken
4 Decide
  - All satisfied: loop pass Ixx --summary "what you implemented" --notes "audit evidence + policy check result"; the CLI commits with a target-version-item-id message
  - Not satisfied but fixable inside the item: record loop fail Ixx --reason "reason", fix it, run loop start Ixx again and return to 3
  - Not satisfied and the plan itself must change: go to 5
5 Plan revision (the body of the loop)
  Triggers
  - A missing prerequisite: insert an item before the current one
  - Follow-up work discovered: append an item
  - The item is too large for a single audit: split it in two or more
  - The audit criteria are wrong or insufficient: fix the criteria
  - A user intervention changes the scope: add, edit or cancel items
  - Blocked by something external: loop hold Ixx --reason "reason"
  Procedure: edit the items in PLAN.md, run loop plan revise --level patch|minor --note "what and why" --ref audit:Ixx or --ref iv_xxxx, then continue section 2 against the revised plan
  Version rule: adding, editing or splitting items is patch; a user intervention that changes the goal or scope is minor
6 Limits (adjust with loop config)
  - max_audit_retries (default 3): past this many attempts on one item, loop hold it and ask the user to decide
  - max_plan_revisions_per_item (default 3): past this many revisions caused by one item, ask the user to decide

Handling interventions

- The hook records user prompts as iv_xxxx; the agent decides whether the intervention changes the plan
- If it does, apply it through the section 5 procedure (--ref iv_xxxx)
- If it does not, answer and continue; the CLI absorbs it when the item passes
- If it is a new feature unrelated to the current plan, propose a separate plan after this one finishes
- On "stop" or "abort", run loop hold or loop plan abort at once and record why

## 3 Context clearing and resuming

- Two clearing events: the tool's automatic compaction (the tool decides when) and the user's manual /clear
- Do not try to predict compaction; PLAN.md is current after every passing item, so nothing is lost whenever it happens
- When loop pass prints a checkpoint and a /clear suggestion, pass it to the user verbatim (shown every checkpoint_every passes)
- Resuming after a clear
  1 Read the loop resume output (the SessionStart hook prints it)
  2 If an item is active, its implementation state is unknown, so run loop start Ixx --force and redo the self-audit from section 2 step 3
  3 Otherwise start section 2 from the first pending item
  4 If the plan file and the database disagree, the plan file wins
- Never infer the earlier conversation on resume; take facts only from PLAN.md, git log and loop history

## 4 Final self-audit

After every item passes

1 Run cmd_typecheck, cmd_lint, cmd_test and cmd_build in full
2 Verify each line of the definition of done
3 Review the whole diff: git diff <start commit>..HEAD --stat (the start commit is in the PLAN.md header); no out-of-scope changes, no secrets, no hardcoded strings
4 Match items against results: the files in each item's scope actually exist or changed
5 Run loop policy check against the whole diff and confirm zero breaches
6 If this plan produced any policy hit, judge whether that rule worked and rewrite it if it did not
7 Record the result in the PLAN.md final-audit section (commands run and their results, the policy check result, and what you found)
8 Run loop final --result pass --summary "summary"; the CLI handles the completion commit, tag and archive
9 If something is unmet, record loop final --result fail --summary "reason", add remedial items with plan revise, and return to section 2

## 5 Heavy mode

- Heavy means applying the full DOMANGCHA harness (18 agents, gates, HUMAN_GATE) to that item alone
- On start, an item in heavy mode reads heavy_doc (.claude/heavy/CEO.md by default) and applies those rules to that item only
- Record what the heavy rules produced in pass --notes as well
- Light items never read heavy_doc
- /ceo raises a whole request to the harness; if it is not installed, the loop offers to install it first

## 6 Policy self-learning

To stop repeating the same mistake, audit failures are promoted into rules that every later item checks

Promotion

1 When loop fail records policy_promote_after (default 2) failures on one item, the CLI flags it as a promotion candidate
2 Decide whether the cause is specific to this item or a general rule that would recur elsewhere
3 For a general rule: loop policy add --title "short title" --rule "what not to do and what to do instead" --origin audit:Ixx
4 For an item-specific mistake: fix it and do not promote a policy
5 A rule the user pointed out is promoted the same way, with --origin iv_xxxx

Writing a rule

- State an observable action; never "be careful" or "pay attention"
- Whether it was broken must be decidable from a diff or a command output
- One policy covers one thing; two things become two policies
- Example — bad: "follow i18n properly"; good: "adding a user-facing string means editing the ko and en message files in the same commit"

Rewriting and retiring

- A policy broken policy_rewrite_after (default 3) times is not written as something you can act on: retire it and write a more specific one
- When a structural change makes a rule meaningless: loop policy retire P00x --reason "reason"
- Growing the list is not the goal; delete rules that no longer earn their place

Injection paths

- Every prompt: the UserPromptSubmit hook prints the active policies with the directive
- Session start and after a context clear: included in the loop resume output
- Item audit: compared directly with loop policy check in section 2 step 3-g
- Three paths, so a context reset cannot lose them

## 7 Output and style

- Commit messages: item commits vX.Y.Z-Ixx: title, completion commit vX.Y.Z: plan title (the CLI writes both)
- Documents: terse lines, no decorative punctuation, no emoji, versions written v0.0.0
- Settings live in the database with UI management rather than new env vars

## Appendix — project conventions

- (add per project, e.g. package manager, test commands, design system INDEX path, supported languages)
