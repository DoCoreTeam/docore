<div align="center"><pre>
██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██║  ██║██╔══██╗
██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║      ███████║███████║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║      ██╔══██║██╔══██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╗ ██║  ██║██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
</pre></div>

<div align="center">

### 🚗💨 DOMANGCHA — Adaptive Engineering for Claude Code & OpenAI Codex

**Your coding agent is powerful. DOMANGCHA gives it the right amount of orchestration.**
One command, nothing to memorise: `npx domangcha` reads where you are and installs what that place needs.
Then just say what you want — the loop plans, audits and reports, and calls for the 18 specialists on its own.

*Your AI getaway car from development hell.*

[![Version](https://img.shields.io/badge/version-3.0.4-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Runtimes](https://img.shields.io/badge/Runtimes-Claude%20Code%20%7C%20Codex-5865F2?style=for-the-badge)](#runtime-compatibility)
[![Agents](https://img.shields.io/badge/Agents-18-FF6B6B?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha#the-18-agents)
[![Gates](https://img.shields.io/badge/Gates-5-orange?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha#the-5-gates)
[![Node](https://img.shields.io/badge/Node-22.13%2B-339933?style=for-the-badge&logo=nodedotjs)](https://nodejs.org)

<br/>

> **I typed one command and got back auth, payments, and a dashboard — tested, reviewed, security-audited. I went to get coffee.**
>
> *— Michael Dohyeon Kim, KDC CEO · builder of DOMANGCHA*

```bash
# In a project it installs the loop here; outside one it installs the harness.
npx domangcha
```

```bash
# Then just say what you want. No slash command needed.
Build a Stripe invoicing tool for freelancers — invoices, email, paid/overdue dashboard
```

```bash
# Nothing else to learn. Say it however you like.
Refactor payments end to end and ship it
```

</div>

---

## ⚡ Why DOMANGCHA?

Claude Code and OpenAI Codex are powerful, but a trivial edit should not pay for an 18-agent pipeline—and a risky cross-cutting change should not rely on one unbounded prompt. **DOMANGCHA selects the minimum reliable execution shape**: DIRECT for simple work, LOOP for iterative correction, and GRAPH for explicit multi-stage topology. One deterministic router owns the decision; agents and models may advise, but code controls transitions.

<table>
<tr>
<td width="50%">

**🤖 Other AI tools**

```
You press Enter
└── 200 lines of code, immediately
    └── Wrong direction, wasted sprint
        └── Start over...
```

</td>
<td width="50%">

**🚗💨 DOMANGCHA**

```
You press Enter
└── Deterministic TaskRouter
    ├── DIRECT → answer or surgical edit
    ├── LOOP   → plan → execute → validate
    └── GRAPH  → branches → joins → gates
```

</td>
</tr>
</table>

| | DOMANGCHA | Typical AI tool |
|---|:---:|:---:|
| Complexity-aware execution | ✅ DIRECT / LOOP / GRAPH | ❌ One workflow for everything |
| Deterministic control flow | ✅ Typed routes and guarded edges | ❌ Prompt-only decisions |
| Role separation by specialist | ✅ Up to 18 logical roles | ❌ Single writer/reviewer |
| Builder ≠ Reviewer (enforced) | ✅ Always | ❌ None |
| Breaking-change protection | ✅ Gate 5 blocks | ❌ None |
| Mistakes → permanent patterns | ✅ error-registry | ❌ None |
| Checkpoint / resume | ✅ LOOP and GRAPH | ❌ Context-window dependent |
| Claude + Codex policy parity | ✅ Shared policy source | ❌ Runtime-specific drift |

---

## 🚀 Getting started

```bash
npx domangcha
```

That is the whole setup. Run it inside your project and say what you want in plain
language — no slash command, no flag, nothing to memorise.

```
you  ▸ add a login screen with email and password

     ▸ 🔁 DOMANGCHA · P0001 v0.2.0 ▓▓▓▓▓▓░░░░ 60% · items 3/5 · next I04
     ▸ writing the plan first (LOOP.md section 1), then item by item
```

Questions and lookups are answered directly. Anything that changes the repository goes
through plan → item → self-audit → pass, and every pass reports where it stands.

**Run it again to update.** The CLI is refreshed; your `LOOP.md`, `CLAUDE.md` and `.loop/`
state are never overwritten.

<details>
<summary><b>Details — where it installs, other package managers, options</b></summary>

<br/>

`npx domangcha` reads where you are:

| Where you run it | What it installs |
|---|---|
| inside a project | the loop, right there — offline, never writes to `~/.claude` |
| outside a project | the 18-agent harness into `~/.claude` and `~/.domangcha` |

A project is a directory carrying `.git`, `package.json`, `pyproject.toml`, `go.mod`,
`Cargo.toml`, `pom.xml`, `build.gradle`, `Gemfile`, `composer.json`, `Makefile` or
`CMakeLists.txt`. The two never share a path, so an existing global install keeps working.

> **Run it, do not add it as a dependency.** npm shows `npm i domangcha` on every package
> page; this is a tool you run. Use `npx`, or `pnpm dlx` / `yarn dlx`. `npm i` inside a
> pnpm workspace fails with `Cannot read properties of null (reading 'matches')` — that is
> npm choking on pnpm's `node_modules`, and it can desynchronise your lockfile.

```bash
pnpm dlx domangcha            # pnpm project
yarn dlx domangcha            # Yarn project
npx domangcha --lang en       # English documents and CLI (default is Korean)
npx domangcha --no-migrate    # keep an existing CLAUDE.md where it is
npx domangcha --agents        # also symlink AGENTS.md and GEMINI.md to LOOP.md
```

Requires Node 22.13+ for the loop (`node:sqlite`, no dependencies). The harness needs
Python 3.10+, bash and git, and installs from the network.

To update the harness: `curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash`,
or run `npx domangcha` from outside any project. Your registries are preserved.

</details>

### It decides when to escalate — you do not

Inside a loop project the global router steps aside and `LOOP.md` drives. When a request
is genuinely graph-scale, the loop asks the harness router and tells you, rather than
waiting for a magic word:

```
you  ▸ rewrite auth and run the migration

     ▸ harness router says: GRAPH (hard graph invariant: security)
     ▸ the loop can carry this as usual; if the 18 agents and gates would genuinely
       help, offer that to the user and escalate only once they agree
```

`/ceo` still forces the escalation if you want it, and installs the harness on demand.
It is a shortcut, never a requirement.

### Policies the agent writes for itself

A context reset normally erases "you already told me that." Repeated audit failures
become durable rules instead:

```
fail I01 ▸ hardcoded the strings again
         ▸ self-audit: I01 has failed 2 times; the same mistake is repeating
policy add ▸ P001 i18n keys
```

`P001` is re-injected on every later prompt, in `resume` after a context reset, and in
every item's self-audit — three paths, so a compaction cannot lose it. A rule broken three
times is retired and rewritten rather than repeated. Rules must be judgeable from a diff:
"be careful about i18n" is rejected in favour of "adding a user-facing string means editing
the ko and en message files in the same commit."

The loop speaks Korean and English; `--lang en` at install or `loop config set lang en` later
switches messages, the plan template and the protocol document.

---

## 🧭 Adaptive Execution Architecture

```text
User Request
     │
     ▼
Intent Normalization
     │
     ▼
TaskRouter (deterministic first)
     ├── Tier 1 · DIRECT
     ├── Tier 2 · LOOP
     └── Tier 3 · GRAPH
                    ├── deterministic edges
                    ├── agent/tool/validator nodes
                    ├── parallel branches and joins
                    ├── bounded retry/fallback
                    ├── checkpoint/resume
                    └── explicit human approval
```

| Route | Use it for | What DOMANGCHA deliberately avoids |
|---|---|---|
| **DIRECT** | explanations, formatting, summaries, lookups, trivial isolated edits | planner graphs, recursive loops, DOC explosion, unnecessary agent calls |
| **LOOP** | normal bug fixes, iterative refactors, validate-and-correct work | multi-agent topology when one bounded cycle is enough |
| **GRAPH** | cross-cutting architecture, security, DB+API+UI, parallel work, destructive or resumable workflows | free-text edge selection, unbounded retries, hidden failure paths |

Routing is deterministic first. Complexity scoring considers mutation scope, file and subsystem breadth, iteration, security, destructive effects, parallelism, approval, and resumability. An LLM can propose a route only at an ambiguous boundary; schema validation and code-owned invariants decide the final route. DIRECT may escalate to LOOP and LOOP to GRAPH while preserving task state.

### One orchestration authority

DOMANGCHA v2.1 does not add a Graph Router beside the CEO and Ralph routers. It promotes the existing architecture:

| Existing DOMANGCHA concept | v2.1 canonical responsibility |
|---|---|
| CEO SIZE ASSESSMENT | deterministic `TaskRouter` |
| FAST PATH | true Tier 1 DIRECT execution |
| Ralph Loop | bounded Tier 2 LOOP executor |
| FULL PIPELINE | versioned Tier 3 GRAPH definition |
| DC-* agents | logical roles invoked as graph/loop nodes |
| GATE 1–5 | task-relevant deterministic validators and approval boundaries |
| hooks | thin runtime adapters; never a second router |
| error/knowledge registries | repeated-failure evidence and reusable guidance |

### LOOP: bounded iteration

```text
PLAN → EXECUTE → VALIDATE → ACT
                         ├── success → COMPLETE
                         ├── failure → bounded retry
                         └── topology discovered → escalate to GRAPH
```

LOOP tracks termination criteria, max iterations, retry budget, no-progress hashes, repeated-error fingerprints, validator feedback, decision history, and compact checkpoints. A model-written “done” flag is not sufficient without completion evidence.

### GRAPH: explicit topology

A graph contains typed state, nodes, guarded edges, branches, joins, retry and fallback paths, checkpoints, budgets, and terminal states. Node types include `DETERMINISTIC`, `LLM`, `AGENT`, `TOOL`, `VALIDATOR`, `HUMAN_GATE`, and `JOIN`. Side effects are classified as `PURE`, `IDEMPOTENT`, or `NON_IDEMPOTENT`; unsafe side effects are not blindly retried.

Dynamic fan-out supports `ALL`, `ANY`, `QUORUM`, and `BEST_EFFORT` joins with concurrency, branch timeout, wave timeout, token, tool-call, and retry budgets. Human approval is persisted as `WAITING_FOR_APPROVAL`, so cloud/delegated runs can pause and return a reviewable checkpoint.

### Status reporting is on by default

An engine that works silently feels like an engine that is stuck. Every surface — the CLI, the Claude hooks, and the Codex control plane — renders the same cards from `orchestration/status.py`, so you can see the route, the loop, and the parallel branches while they run.

```text
🚂 DOMANGCHA · GRAPH 🧭 (score 10)        🔁 LOOP 5/30  ▓▓░░░░░░░░ 17%
├ why: hard graph invariant: parallel      ├ retry left 5 · no progress 0/3
├ plan: typed node graph, branches, join   ├ budget: model 7/12 · tool 31/80
└ next: report per node and per branch     └ state: RUNNING ⏳

🧭 GRAPH full_pipeline@1  ▓▓▓▓▓░░░░░ 50% 3/6 nodes
├ done: intake ✅ · plan ✅ · build ✅
├ running: review ⏳ (attempt 1)
├ parallel(build): dc-dev-be ✅ | dc-dev-fe ✅ | dc-sec ❌ · join=ALL
└ awaiting approval: gate 🙋
```

`engine.py route|status` prints a card by default; `--format json` returns the raw state and `--lang en` switches language (`DOMANGCHA_STATUS_LANG` sets the default). The reporting contract itself is injected by the hooks: announce the route and why, report loop iteration and budget every pass, show branch results and the join strategy at fan-in, explain in plain language what a gate is asking to approve, and never go silent through a long step or hide a stalled loop.

### Runtime compatibility

| Guarantee | Claude Code | Codex Local / IDE | Codex Cloud |
|---|---|---|---|
| Shared router, state, and validators | ✅ | ✅ | ✅ |
| Native attachment | hooks + commands | plugin skill + lifecycle hooks | plugin skill + checkpoints |
| Logical agent roles | Claude subagents | runtime-native agents | delegated agents when available |
| Human approval | interactive | interactive when supported | checkpoint and review |
| Browser verification | Claude-in-Chrome; Playwright fallback | capability-resolved | CI/headless capability |
| Checkpoint format | shared | shared | shared |

Runtime behavior is capability-based—not hard-coded to provider model names. Model policies express `HIGH_REASONING`, `BALANCED`, `FAST_CHEAP`, `LONG_CONTEXT`, or `REVIEW`; each adapter maps them to what is actually available. Unknown runtime or model names do not fail by default.

#### Codex-native attachment

Installing the harness (run `npx domangcha` outside a project) puts the bundled DOMANGCHA plugin into a local Codex marketplace and enables its native skill. After installation, open `/hooks` once and trust the DOMANGCHA hook definition. From the next new Codex thread:

- `UserPromptSubmit` automatically creates a canonical task and injects its route and task ID.
- the `domangcha` skill tells Codex how to execute and report through that same state.
- `PostToolUse` records mutations, successful validation commands, and independent subagent evidence.
- `Stop` allows DIRECT answers to finish immediately, but boundedly continues unfinished LOOP/GRAPH work when completion evidence is absent.
- state survives under the workspace `.domangcha/` directory, so follow-ups and continuation prompts reuse the same task instead of restarting.

The hooks are code control, not another prompt-only router: they call the same `ExecutionCoordinator` and `TaskRouter` used by Claude and the CLI.

---

## 🎬 Watch a Real Sprint

> `/ceo "Build a Stripe-powered invoicing tool for freelancers — create invoices, send via email, track paid/overdue"`

```
[INTENT PARSED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input:   Build a Stripe-powered invoicing tool for freelancers —
         create invoices, send via email, track paid/overdue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parsed:  Freelancer creates an invoice for a client, emails it with a
         Stripe payment link, tracks real-time payment status
         (draft → sent → paid/overdue) in a dashboard
Goal:    Invoice create → email send → Stripe pay → dashboard auto-update (3 flows)
Scope:   IN  — invoice CRUD, Stripe Payment Links, email via Resend, webhook status sync
         OUT — tax calculation, multi-currency, accounting software sync, PDF export
Context: Web app / greenfield / Stripe confirmed / stack TBD → Q&A needed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[TASKROUTER]
Task:   Freelancer invoicing tool (Stripe + email + status dashboard)
Route:  GRAPH — DB + API + UI + payments + independent validation

[TRADEOFF CHECK] ✅ CLEAR — No architectural risks detected. Proceeding to Q&A.

[CEO] Q1: What's your stack? (Next.js / Express / other?)
> Next.js 14 + Supabase

[CEO] Q2: Should freelancers manage multiple clients, each with their own invoice history?
> Yes — each client has a profile, invoices are linked to a client

[CEO] Q3: When a client pays via Stripe, should the invoice status update automatically (webhook)?
> Yes, paid status should flip in real time — no manual refresh

[CEO] Q4: What does "done" look like? Which flows need to work end-to-end in the browser?
> ① Create invoice → send to client email  ② Client clicks link → pays via Stripe
> ③ Dashboard shows "Paid" automatically. All 3 in Stripe test mode.

[CEO] Q5: Auth for the freelancer — GitHub OAuth, email/password, or something else?
> GitHub OAuth — quickest to set up

[Q&A COMPLETE] ✅  Stack / data model / Stripe webhook / done criteria / auth confirmed

[TASK REFINED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Original Input:  Stripe-powered invoicing tool for freelancers
Q&A Summary:     Next.js 14 + Supabase / clients table per user /
                 Stripe Payment Links + webhook / Resend email / GitHub OAuth /
                 3 E2E flows in Stripe test mode
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Final Task:   Next.js 14 + Supabase + Stripe + Resend.
              GitHub OAuth login, RLS on all tables.
              clients + invoices + stripe_events tables.
              CRUD invoices → generate Stripe Payment Link →
              send email via Resend → webhook flips status to "paid".
Done When:    ① Freelancer creates invoice → client receives email with pay link
              ② Client pays via Stripe (test mode) → webhook fires
              ③ Dashboard shows invoice status "Paid" without page refresh
Out of Scope: Tax calculation, multi-currency, PDF export, accounting integrations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[DOC-FIRST] Creating docs/2026-05-01-v2.0.33/
  ✔ 00-requirements.md       (invoice lifecycle + Stripe webhook + Resend SLA)
  ✔ 01-architecture.md       (GitHub OAuth → Supabase RLS + Stripe webhook flow)
  ✔ 02-task-breakdown.md     P0: Auth+RLS+Stripe  P1: Invoice CRUD+email  P2: Dashboard UI
  ✔ 03-test-strategy.md      (Stripe test mode E2E + webhook signature security test)
  ✔ 04-completion-criteria.md  (3-flow checklist + rollback criteria)
[DOC COMPLETE]

━━━━━━━━━━━━━━━ PHASE 1: PLANNER ━━━━━━━━━━━━━━━
[DC-KNW GUARD] Scanning knowledge registry for relevant patterns...
  └── KNW-001 [HIGH]     File 300-line limit — keep webhook handler in its own file
  └── KNW-002 [CRITICAL] No hardcoded secrets — Stripe keys via env only, never source
  → advisory only, proceeding

DC-BIZ  ✔  Freelancer invoicing is a proven pain point. Stripe + Resend is the right v1 wedge.
            Revenue model is clear (usage-based SaaS potential). Build.
DC-RES  ✔  Stripe Payment Links (no custom checkout) cuts implementation by ~60%.
            Resend DX > SendGrid for developer onboarding. Supabase Realtime handles live status.
DC-OSS  ✔  stripe-node (39k★, official) · resend (5k★, clean API) · @supabase/ssr (SSR-safe auth).
            All actively maintained, MIT-compatible.
DC-KNW  ✔  GUARD scan complete. 2 relevant advisories surfaced. Registry up to date.

━━━━━━━━━━━━━━━ PHASE 2: BUILDER ━━━━━━━━━━━━━━━
DC-DEV-DB   ✔  4 migrations: users (OAuth, UUID PK) · clients (per-user, RLS policy) ·
                invoices (status: draft/sent/paid/overdue, FK → clients) ·
                stripe_events (webhook log, idempotency key)
DC-DEV-BE   ✔  /api/invoices (GET/POST/PATCH/DELETE) · /api/invoices/[id]/send (Resend trigger)
                /api/stripe/webhook (sig verify → status flip) — 3 routes, 0 N+1 queries
DC-DEV-FE   ✔  ClientList · InvoiceForm · InvoiceTable · StatusBadge · SendButton · Dashboard
                6 components · Supabase Realtime subscription on invoice status
DC-DEV-OPS  ✔  .env.example (STRIPE_SECRET · STRIPE_WEBHOOK_SECRET · RESEND_API_KEY ·
                NEXT_PUBLIC_SUPABASE_URL) · Vercel config · webhook endpoint registered
DC-DOC      ✔  API reference (3 endpoints) · Setup guide: Stripe webhook + Resend onboarding ·
                .env.example field annotations · architecture diagram

━━━━━━━━━━━━━━━ PHASE 3: EVALUATOR ━━━━━━━━━━━━━
DC-QA   ✔  22 unit tests (invoice CRUD + webhook handler) · 3 E2E flows in Stripe test mode ·
            edge cases: duplicate webhook event, expired payment link
DC-SEC  ✔  Stripe webhook sig verified (stripe.webhooks.constructEvent) · RLS on all 4 tables ·
            0 hardcoded secrets · NEXT_PUBLIC prefix audit passed · 0 vulnerabilities
DC-REV  ✔  93/100 · no logic duplication · types sound · webhook idempotency confirmed

━━━━━━━━━━━━━━━━━━ GATE 1–5 ━━━━━━━━━━━━━━━━━━━
① Scan       ✅  0 error-registry hits · all files ≤ 300 lines
② Criteria   ✅  3 E2E flows passing in Stripe test mode
③ Version    ✅  v2.0.49 consistent across all files
④ Separation ✅  Builder ≠ Reviewer confirmed
⑤ Breaking   ✅  Greenfield — no breaking changes

DC-TOK  ✔  Context: 34% used (44k / 128k tokens)

[CEO REPORT] ✅ Done in 31 minutes.
  Files: 19 new  ·  Tests: 22 passing  ·  Security: Stripe sig + RLS  ·  Deploy: Vercel ready
```

**A complete invoicing tool with real Stripe payments. You didn't write a line.**

---

## 🐛 Watch a Bug Fix

> `/ceo "Freelancers say invoices stay 'Pending' forever after the client pays — Stripe dashboard shows the payment went through"`

```
[INTENT PARSED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input:   Invoices stuck on "Pending" after Stripe payment — confirmed paid in Stripe dashboard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parsed:  Stripe webhook fires successfully (Stripe logs show 200 expected) but the invoice
         status in Supabase never flips from "sent" → "paid"
Goal:    Identify root cause, fix webhook handler, confirm status auto-updates end-to-end
Scope:   IN  — webhook handler bug only
         OUT — UI changes, new features, unrelated refactors
Context: Next.js 14 + Supabase · existing codebase · Stripe test mode · 1-2 files affected
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[TASKROUTER]
Task:   Fix webhook signature verification / status update bug
Route:  LOOP  (1-2 files, iterative fix + regression validation)

[LOOP — ITERATION 1]
🔧 Fix target:  app/api/stripe/webhook/route.ts  (signature verify + status flip)
🌊 Ripple:      app/api/invoices/[id]/route.ts   (PATCH endpoint called by webhook)
                components/StatusBadge.tsx        (reads invoice.status — no change needed)
⚡ Root cause hunt: webhook handler uses req.json() instead of raw body buffer
                    → stripe.webhooks.constructEvent() always throws SignatureVerificationError
                    → catch block silently returns 200 → Stripe stops retrying → status never flips

[DOC] docs/2026-05-02-v2.0.51-webhook-sig-fix/00-summary.md  ✔ created

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// BEFORE — req.json() destroys the raw body Stripe needs to verify the signature
export async function POST(req: Request) {
  const body = await req.json()              // ❌ parsed JSON, sig check fails
  const sig  = req.headers.get('stripe-signature')!
  const event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!)

// AFTER — read raw Buffer so Stripe's HMAC check passes
export async function POST(req: Request) {
  const rawBody = Buffer.from(await req.arrayBuffer())  // ✅ raw bytes preserved
  const sig     = req.headers.get('stripe-signature')!
  const event   = stripe.webhooks.constructEvent(rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DC-REV  ✔  Fix is surgical and correct. Raw buffer pattern is the documented Stripe approach.
            No other callers affected. Idempotency key logic untouched. APPROVED.
            Suggestion (non-blocking): add an integration test that sends a real Stripe test event
            to cover this path in CI — logged as improvement ticket.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━ GATE 1–5 ━━━━━━━━━━━━━━━━━━━━━━━━━

① Scan       ✅  0 error-registry hits · webhook/route.ts 38 lines (≤ 300)
② Criteria   ✅  Stripe test webhook fired → invoice status flips to "paid" in < 1 s
③ Version    ✅  v2.0.51 consistent across all files
④ Separation ✅  CEO fixed · DC-REV reviewed — roles separated
⑤ Breaking   ✅  Internal handler only — no API contract change

[CEO LOOP REPORT] ⚡ Done in 4 minutes.
  1 file changed (2-line fix) · Stripe webhook now verifies correctly · Status flips live
```

**One bug, one function, four minutes. The rest of the codebase didn't move.**

---

## 🔄 Pipeline

```text
/ceo "task"
      │
      ▼
┌──────────────────────┐
│ INTENT NORMALIZATION │  request, goal, scope, constraints, risk signals
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ TASKROUTER           │  deterministic filter → complexity score
└───┬─────────┬────────┘
    │         │
    │ obvious │ ambiguous boundary only
    │         └── structured semantic proposal → schema + invariant validation
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ DIRECT                 LOOP                       GRAPH              │
│ answer / small edit     PLAN → EXECUTE             typed state       │
│ focused validation     → VALIDATE → ACT            guarded edges     │
│                        bounded retry                fan-out / join    │
│                        Ralph memory                 checkpoint / HITL │
└───────────┬──────────────────┬──────────────────────────┬─────────────┘
            └──────────────────┴──────────────────────────┘
                               ▼
                    task-relevant validators
                               ▼
                    COMPLETE / PAUSED / FAILED
```

Complex feature requests still use the familiar PLANNER → BUILDER → EVALUATOR flow inside GRAPH. Small read-only requests do not create planning documents or invoke all agents. Meaningful implementation preserves Builder ≠ Reviewer; destructive, security-sensitive, or irreversible steps require an explicit approval edge.

---

## 👥 The 18 Agents

<table>
<thead>
<tr><th>Phase</th><th>Agent</th><th>Role</th><th>Model Policy</th></tr>
</thead>
<tbody>
<tr><td rowspan="5"><b>🧠 PLANNER</b></td>
  <td><code>DC-BIZ</code></td><td>Business Judge</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-RES</code></td><td>Researcher</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-OSS</code></td><td>OSS Scout</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-ANA</code></td><td>Codebase Analyst</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-KNW</code></td><td>Knowledge Curator</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td rowspan="9"><b>🔨 BUILDER</b></td>
  <td><code>DC-DEV-DB</code></td><td>Database Engineer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-BE</code></td><td>Backend Developer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-FE</code></td><td>Frontend Developer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-OPS</code></td><td>DevOps Engineer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-MOB</code></td><td>Mobile Developer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-INT</code></td><td>Integration Engineer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DOC</code></td><td>Documentation Writer</td><td>FAST_CHEAP</td></tr>
<tr><td><code>DC-WRT</code></td><td>Copywriter</td><td>FAST_CHEAP</td></tr>
<tr><td><code>DC-SEO</code></td><td>SEO / AEO / GEO</td><td>FAST_CHEAP</td></tr>
<tr><td rowspan="3"><b>🔍 EVALUATOR</b></td>
  <td><code>DC-QA</code></td><td>QA Engineer</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-SEC</code></td><td>Security Reviewer</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-REV</code></td><td>Code Reviewer</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><b>⚙️ SUPPORT</b></td>
  <td><code>DC-TOK</code></td><td>Token Optimizer</td><td>FAST_CHEAP</td></tr>
</tbody>
</table>

> Roles are selected by route and task needs. DIRECT normally invokes none. LOOP uses only the roles needed for iteration. GRAPH may fan out across independent roles. `domangcha/manifests/agents.json` is the authoritative 18-role manifest.

---

## 🛡️ The 5 Gates

> Gates are applied when relevant to the work. DIRECT avoids ceremonial evaluators; code mutation, security, release, and destructive workflows receive the validators and approval boundaries they require.

| Gate | Check |
|:---:|---|
| **① SCAN** | error patterns, secrets, repository rules, maintainability checks |
| **② CRITERIA** | task-specific completion evidence, tests, lint, typecheck, build |
| **③ CONSISTENCY** | manifests, versions, graph schema, reachable terminal states |
| **④ SEPARATION** | meaningful implementation cannot be its only reviewer |
| **⑤ SAFETY** | breaking, destructive, or irreversible work requires explicit approval |

---

## 🆕 What's New

| Version | What changed |
|---|---|
| **v3.0.4** | No slash command is required: the loop asks the harness router itself; README usage cut to one block |
| **v3.0.3** | Install-time output is bilingual, English first, everywhere |
| **v3.0.2** | Never edits your package.json; an update says it is an update; `npm i` vs `npx` spelled out |
| **v3.0.1** | The loop carries the reporting contract itself, so progress is reported inside a loop project too |
| **v3.0.0** | One flag-free command installs by location; plain language runs a project loop, `/ceo` raises it to the harness; policies self-learn; Korean and English |
| **v2.3.2** | The single renderer stops carrying the phrasebook |
| **v2.3.1** | Hooks stop misfiring on unrelated projects, and stale deployments become visible |
| **v2.3.0** | Progress reporting is on by default |
| **v2.2.0** | Native Codex attachment |
| **v2.1.1** | Full public README restored and modernized |
| **v2.1.0** | Adaptive DIRECT · LOOP · GRAPH architecture |
| **v2.0.58** | Browser verification now Chrome-extension-first |

24 older releases: [full changelog](https://github.com/DoCoreTeam/domangcha/releases)

---

## 🔄 Updates

**How updates work:**

Files are installed to `~/.claude/` on first run. They do **not** auto-update while a project is in progress — the version at install time is what runs.

**To update the harness:** run `curl -fsSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash`, or `npx domangcha` from outside a project. Your error registry and project registries are preserved. Rule memories in `~/.claude/projects/*/memory/` are automatically refreshed with the latest version's rule definitions — user feedback and project context are never overwritten.

**Auto-update prompt (built-in):** Every `/ceo` call silently checks the npm registry for a newer version. If one exists, you'll see:

```
[CEO] New version v2.0.33 available (installed: v2.0.31).
Update before continuing? (y/n):
```

- `y` → reinstalls the harness in place, then continues with your task
- `n` / Enter → skips and continues without updating

Version check failures (offline, etc.) are silently ignored — your task is never blocked.

---

## 🖥️ Commands

**Every command here is optional.** Plain language does the same work; these are shortcuts.

In a loop project: `/plan` writes the plan for a new instruction, `/loop` resumes the next
item, `/policy` checks active policies against your diff. The CLI behind them is
`node scripts/loop.mjs` — run `help` for every subcommand, `resume` for what to do next,
`status --all` for every registered project.

With the harness: `/ceo "task"` routes explicitly, and 18 more `/ceo-*` intents
(`-ralph -debug -test -review -security -ship -plan -design -feature -doc -clarify -init
-quality -status -update -version -knowledge -learn`) name a workflow. They are adapters
into the same TaskRouter, which already reads plain prompts — so none of them is required.

---

## 📐 Coding Standards

Non-negotiable. Gate 1 enforces on every file.

```
✓ 300 lines max per file  ·  50 lines max per function  ·  4 levels max nesting
✓ Immutability — always create new, never mutate existing
✓ Explicit error handling at every level  ·  Input validation at every boundary
✓ Tests required for every feature  ·  Row-Level Security on every table
```

---

## 📦 Requirements

DOMANGCHA is a runtime-aware developer harness for Claude Code and OpenAI Codex. It uses native capabilities when available and preserves the same routing, safety, state, and reviewer-separation guarantees across runtimes.

| | Project loop (inside a project) | Harness (outside a project, or `/ceo`) |
|---|---|---|
| Coding agent | Claude Code, or Cursor | Claude Code, or OpenAI Codex |
| Node.js | **22.13+** — `node:sqlite`, no npm dependencies | 14+ for npm installation |
| Python | not used | 3.10+ for the deterministic orchestration engine |
| `git` | commits each passing item | installer, repository checks, reviewable diffs |
| Network | not required — templates ship in the package | required — pulls `install.sh` from GitHub |

---

## 🔀 Coming from v2.x

Nothing breaks and nothing was removed.

- **Keep everything as-is** — your harness is untouched. Refresh it with the curl one-liner
  above, or by running `npx domangcha` from outside any project.
- **Try the loop on one project** — `cd` into it and run `npx domangcha`. Your global install
  stays; inside that project the router yields to `LOOP.md`, and `/ceo` brings it straight back.
- **An existing project `CLAUDE.md`** moves to `.claude/heavy/CEO.md` and is read back for
  items marked heavy. Pass `--no-migrate` to keep it in place.
- **Going back** — delete `LOOP.md`, `scripts/loop.mjs` and `.loop/`, then restore `CLAUDE.md`
  from `.claude/heavy/CEO.md`.

**Codex first run:** restart Codex, open `/hooks`, and trust the DOMANGCHA plugin hooks once. Start a new thread; routing and task state are then attached automatically. Use `$domangcha` explicitly when you want to force skill selection.

---

<details>
<summary><b>🇰🇷 한국어 (Korean) — 클릭하여 펼치기 / Click to expand</b></summary>

<br/>
<div align="center"><pre>
██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██║  ██║██╔══██╗
██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║      ███████║███████║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║      ██╔══██║██╔══██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╗ ██║  ██║██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
</pre></div>

### 🚗💨 돔황차 — Claude Code와 OpenAI Codex를 위한 적응형 엔지니어링

**강력한 코딩 에이전트에 필요한 만큼의 오케스트레이션만 더합니다.**
명령 하나, 외울 것 없음: `npx domangcha` 가 실행한 자리를 보고 필요한 것을 설치합니다.
그다음엔 그냥 말하면 됩니다 — 루프가 계획하고 감사하고 보고하며, 필요하면 18명 크루를 스스로 부릅니다.

*개발 지옥에서 도망쳐 — 돔황차🚗💨*

[![Version](https://img.shields.io/badge/version-3.0.4-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Runtimes](https://img.shields.io/badge/런타임-Claude%20Code%20%7C%20Codex-5865F2?style=for-the-badge)](#runtime-compatibility)
[![Agents](https://img.shields.io/badge/에이전트-18명-FF6B6B?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha)
[![Gates](https://img.shields.io/badge/게이트-5개-orange?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha)
[![Node](https://img.shields.io/badge/Node-22.13%2B-339933?style=for-the-badge&logo=nodedotjs)](https://nodejs.org)

> **명령 하나 쳤더니 인증, 결제, 대시보드가 돌아왔다. 테스트 통과, 보안 감사 완료, 코드 리뷰까지.**
>
> *— Michael Dohyeon Kim, KDC CEO · DOMANGCHA 제작자*

```bash
# 프로젝트 안이면 여기에 루프를, 프로젝트 밖이면 하네스를 설치합니다
npx domangcha
```

```bash
# 그다음엔 그냥 하고 싶은 일을 말하면 됩니다. 슬래시 커맨드 불필요.
프리랜서용 Stripe 인보이스 툴 만들어줘 — 인보이스 생성, 이메일 발송, 미납/완납 대시보드
```

```bash
# 더 배울 것 없습니다. 편한 대로 말하면 됩니다.
결제 전체 리팩터링하고 배포까지
```

---

### 🚀 시작하기

```bash
npx domangcha
```

세팅은 이게 전부입니다. 프로젝트 안에서 실행하고, 하고 싶은 일을 그냥 말하면 됩니다 —
슬래시 커맨드도, 플래그도, 외울 것도 없습니다.

```
당신 ▸ 이메일·비밀번호로 로그인 화면 만들어줘

     ▸ 🔁 DOMANGCHA · P0001 v0.2.0 ▓▓▓▓▓▓░░░░ 60% · 항목 3/5 · 다음 I04
     ▸ 먼저 플랜을 씁니다 (LOOP.md 1절), 그다음 항목 하나씩
```

질문이나 조회는 바로 답합니다. 저장소를 바꾸는 일만 플랜 → 항목 → 자가감사 → 통과를
거치고, 매 패스마다 지금 어디쯤인지 보고합니다.

**업데이트도 같은 명령입니다.** CLI 만 갱신되고 `LOOP.md`, `CLAUDE.md`, `.loop/` 상태는
덮어쓰지 않습니다.

<details>
<summary><b>자세히 — 어디에 설치되는지, 다른 패키지 매니저, 옵션</b></summary>

<br/>

`npx domangcha` 는 실행한 자리를 보고 판단합니다.

| 어디서 실행했나 | 무엇을 설치하나 |
|---|---|
| 프로젝트 안 | 그 자리에 루프 — 오프라인, `~/.claude` 무접촉 |
| 프로젝트 밖 | `~/.claude` 와 `~/.domangcha` 에 18 에이전트 하네스 |

프로젝트로 인정하는 기준은 `.git`, `package.json`, `pyproject.toml`, `go.mod`,
`Cargo.toml`, `pom.xml`, `build.gradle`, `Gemfile`, `composer.json`, `Makefile`,
`CMakeLists.txt` 중 하나가 있는 디렉터리입니다. 두 방식은 경로를 공유하지 않으므로
기존 전역 설치가 그대로 살아 있습니다.

> **설치하지 말고 실행하세요.** npm 페이지는 모든 패키지에 `npm i domangcha` 를 자동으로
> 띄우지만 이건 실행하는 도구입니다. `npx`, 또는 `pnpm dlx` / `yarn dlx` 를 쓰세요.
> pnpm 워크스페이스에서 `npm i` 를 하면 `Cannot read properties of null (reading 'matches')`
> 로 실패하는데, npm 이 pnpm 의 `node_modules` 를 읽지 못해서이며 lockfile 이 어긋날 수 있습니다.

```bash
pnpm dlx domangcha            # pnpm 프로젝트
yarn dlx domangcha            # Yarn 프로젝트
npx domangcha --lang en       # 문서와 CLI 를 영어로 (기본은 한국어)
npx domangcha --no-migrate    # 기존 CLAUDE.md 를 그 자리에 그대로 둠
npx domangcha --agents        # AGENTS.md, GEMINI.md 를 LOOP.md 로 심볼릭 링크
```

루프는 Node 22.13 이상이 필요합니다 (`node:sqlite`, 의존성 없음). 하네스는 Python 3.10 이상,
bash, git 이 필요하고 네트워크로 설치됩니다.

하네스 갱신: `curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash`
또는 프로젝트 밖에서 `npx domangcha`. 레지스트리는 보존됩니다.

</details>

### 언제 올릴지는 도구가 판단합니다

루프 프로젝트 안에서는 전역 라우터가 물러나고 `LOOP.md` 가 주도합니다. 그러다 요청이
정말 그래프 규모면, 루프가 하네스 라우터에게 직접 물어보고 알려줍니다 — 매직 워드를
기다리지 않습니다.

```
당신 ▸ 인증 갈아엎고 마이그레이션 돌려줘

     ▸ 하네스 라우터 분류: GRAPH (hard graph invariant: security)
     ▸ 루프로 그대로 진행해도 됩니다. 18 에이전트와 게이트가 정말 도움이 되겠다 싶으면
       사용자에게 제안하고 승인받은 뒤에만 올리세요
```

`/ceo` 로 직접 올릴 수도 있고, 하네스가 없으면 그때 설치를 제안합니다.
어디까지나 단축키이지 필수가 아닙니다.

### 에이전트가 스스로 쓰는 정책

컨텍스트가 초기화되면 "아까 말했잖아"가 사라집니다. 반복된 감사 실패를 지속되는
규칙으로 바꿔 둡니다.

```
fail I01 ▸ 또 하드코딩
         ▸ 자체감사: I01 감사 실패 2회 누적, 같은 실수가 반복되고 있음
policy add ▸ P001 i18n 키 강제
```

`P001` 은 이후 모든 프롬프트, 컨텍스트 초기화 후의 `resume`, 매 항목 자가감사
세 경로로 다시 주입됩니다. 같은 정책을 3회 어기면 반복하는 대신 폐기하고 더 구체적으로
다시 씁니다. 규칙은 diff 로 위반 여부를 판정할 수 있어야 하며, "i18n 을 잘 지킨다" 대신
"사용자 노출 문자열을 추가하면 같은 커밋에서 ko en 메시지 파일을 함께 수정한다" 같은
형태만 인정합니다.

루프는 한국어와 영어를 모두 씁니다. 설치할 때 `--lang en`, 또는 나중에
`loop config set lang en` 으로 메시지·플랜 템플릿·프로토콜 문서가 함께 바뀝니다.

---

### ⚡ 왜 DOMANGCHA인가?

Claude Code와 OpenAI Codex는 강력하지만, 간단한 수정에 18개 에이전트 전체 파이프라인을 돌릴 이유는 없습니다. 반대로 보안·DB·API·UI가 얽힌 변경을 단일 프롬프트에 맡겨서도 안 됩니다. **DOMANGCHA는 신뢰성에 필요한 최소 실행 구조**인 DIRECT, LOOP, GRAPH를 결정론적으로 선택합니다.

<table>
<tr>
<td width="50%">

**🤖 다른 AI 도구들**

```
엔터를 치는 순간
└── 코드 200줄, 즉시
    └── 틀린 방향, 낭비된 스프린트
        └── 처음부터 다시...
```

</td>
<td width="50%">

**🚗💨 DOMANGCHA**

```
엔터를 치는 순간
└── 결정론적 TaskRouter
    ├── DIRECT → 답변 또는 국소 수정
    ├── LOOP   → 계획 → 실행 → 검증
    └── GRAPH  → 분기 → 조인 → 게이트
```

</td>
</tr>
</table>

| | DOMANGCHA | 일반 AI 도구 |
|---|:---:|:---:|
| 복잡도별 실행 | ✅ DIRECT / LOOP / GRAPH | ❌ 모든 일에 같은 워크플로 |
| 결정론적 제어 흐름 | ✅ 타입 라우트 + 가드 엣지 | ❌ 프롬프트 전용 판단 |
| 전문가 역할 분리 | ✅ 최대 18개 논리 역할 | ❌ 작성자 단독 검토 |
| 빌더 ≠ 리뷰어 강제 | ✅ 항상 분리 | ❌ 없음 |
| 파괴적 변경 보호 | ✅ Gate 5 차단 | ❌ 없음 |
| 실수 → 영구 패턴 등록 | ✅ error-registry | ❌ 없음 |
| 체크포인트 / 재개 | ✅ LOOP와 GRAPH | ❌ 컨텍스트 창에 종속 |
| Claude + Codex 정책 동등성 | ✅ 공통 정책 원본 | ❌ 런타임별 드리프트 |

---

### 🎬 실제 스프린트 보기

> `/ceo "동네 러닝 크루 관리 앱 만들어줘 — 모임 생성, 카카오페이 회비 정산, 출석 체크"`

```
[INTENT PARSED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
입력:   동네 러닝 크루 — 모임 생성, 카카오페이 회비 정산, 출석 체크
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
정제:   크루 멤버가 모임을 생성하고, 카카오페이로 회비를 요청·정산하며,
        출석을 기록해 개인 참여 통계를 확인하는 서비스
목표:   모임 생성 → 회비 요청(카카오페이) → 출석 체크 → 대시보드 (3개 플로)
범위:   포함 — 모임 CRUD, 카카오페이 결제 요청, 출석·통계
        제외 — 실시간 채팅, GPS 경로, 이미지 업로드, Apple Watch 연동
맥락:   웹앱 / 그린필드 / 카카오 API 확정 / 스택 미정 → Q&A 필요
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[TASKROUTER]
업무:   러닝 크루 관리 (카카오페이 + 출석 + 대시보드)
라우트: GRAPH — DB + API + UI + 결제 + 독립 검증

[TRADEOFF CHECK] ✅ 이상 없음. Q&A 진행.

[CEO] Q1: 스택은 어떻게 할까요?
> Next.js 14 + Supabase

[CEO] Q2: 카카오 로그인도 쓸까요?
> 네 — 회비도 카카오페이라 자연스러움

[CEO] Q3: 회비 정산 방식은?
> 크루장이 금액 설정 후 요청 → 멤버가 카카오페이로 개별 납부

[CEO] Q4: "완료" 기준이 뭔가요?
> ① 모임 생성 → 멤버 초대  ② 회비 요청 → 카카오페이 납부 → 상태 자동 업데이트
> ③ 출석 체크 → 대시보드 참여율 표시 (카카오페이 테스트 모드)

[CEO] Q5: 모임 최대 규모는?
> 30명 이하 소모임

[Q&A COMPLETE] ✅  스택 / 카카오 로그인·페이 / 완료 기준 / 규모 확인

[TASK REFINED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
원본 입력:  동네 러닝 크루 관리 앱
Q&A 핵심:  Next.js 14 + Supabase / 카카오 로그인 + 카카오페이 /
            모임·멤버·회비·출석 테이블 / 최대 30인 / 3 E2E 플로
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
최종 태스크: Next.js 14 + Supabase + 카카오 로그인 + 카카오페이 결제 요청.
             RLS 전체 테이블 적용.
             crews · members · dues · attendance 테이블.
             모임 CRUD → 카카오페이 회비 요청 → webhook 납부 확인 → 출석 기록.
완료 조건:  ① 크루장 모임 생성 → 멤버 초대 이메일 발송
            ② 회비 요청 → 카카오페이 결제 → webhook → 납부 상태 자동 업데이트
            ③ 출석 체크 → 대시보드에 멤버별 참여율 표시
제외 범위:  실시간 채팅, GPS 경로, 이미지 업로드, Apple Watch 연동
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[DOC COMPLETE] docs/2026-05-02-v2.0.49-running-crew-app/ 생성 완료
  ✔ 00-requirements.md       (모임 라이프사이클 + 카카오페이 webhook + 출석 집계)
  ✔ 01-architecture.md       (카카오 OAuth → Supabase RLS + 카카오페이 webhook 플로)
  ✔ 02-task-breakdown.md     P0: 인증+RLS+카카오페이  P1: 모임·회비 CRUD  P2: 출석+대시보드
  ✔ 03-test-strategy.md      (카카오페이 테스트 모드 E2E + webhook 서명 검증)
  ✔ 04-completion-criteria.md  (3-플로 체크리스트 + 롤백 기준)

━━━━━━━━━━━━━━━ PHASE 1: 기획 ━━━━━━━━━━━━━━━
[DC-KNW GUARD] 지식 레지스트리 스캔 중...
  └── KNW-002 [CRITICAL] 소스코드 시크릿 하드코딩 금지 — 카카오 API 키 env 처리 필수
  └── KNW-001 [HIGH]     파일 300줄 초과 주의 — 카카오페이 핸들러 파일 분리 권고
  → advisory only, 계속 진행

DC-BIZ  ✔  동네 소모임 회비 정산 Pain Point 명확. 카카오페이 국내 결제 1위 — 사용자 마찰 최소화.
            크루장 확보 시 바이럴 가능성 있음. 빌드.
DC-RES  ✔  카카오페이 단건 결제 API v1 — Ready Payment → Approve 2단계 플로.
            카카오 REST API 직접 호출이 공식 SDK 대비 안정적.
            Supabase Realtime으로 납부 상태 즉시 반영 가능.
DC-OSS  ✔  axios (105k★, REST 호출) · @supabase/ssr (SSR 안전 auth) · date-fns (날짜 처리).
            모두 활성 유지보수, MIT 라이선스.
DC-KNW  ✔  GUARD 스캔 완료. 2개 advisory 전달. 레지스트리 최신 상태.

━━━━━━━━━━━━━━━ PHASE 2: 빌드 ━━━━━━━━━━━━━━━
DC-DEV-DB   ✔  5개 마이그레이션: users (카카오 OAuth, UUID PK) · crews (크루 정보, 크루장 FK) ·
                members (crew_id × user_id, 역할: leader/member, RLS) ·
                dues (금액·상태: pending/paid, 카카오 tid) · attendance (crew_id × user_id × 날짜)
DC-DEV-BE   ✔  /api/crews (CRUD) · /api/dues/[id]/request (카카오페이 Ready 호출)
                /api/kakao/webhook (Approve 확인 → 상태 flip) · /api/attendance (출석 토글)
                — 4개 라우트, 카카오페이 서명 검증 포함, webhook 멱등성 처리
DC-DEV-FE   ✔  CrewDashboard · MemberList · DuesCard · AttendanceToggle · PaymentBadge
                5개 컴포넌트 · Supabase Realtime 구독으로 납부 상태 즉시 반영
DC-DEV-OPS  ✔  .env.example (KAKAO_CLIENT_ID · KAKAO_PAY_CID · KAKAO_SECRET ·
                NEXT_PUBLIC_SUPABASE_URL) · Vercel 환경 변수 · 카카오 redirect URI 등록 가이드
DC-DOC      ✔  카카오페이 API 연동 가이드 (Ready→Approve 플로 다이어그램) ·
                env 설명 주석 · 카카오 개발자 콘솔 설정 3단계 가이드

━━━━━━━━━━━━━━━ PHASE 3: 평가 ━━━━━━━━━━━━━━━
DC-QA   ✔  19개 단위 테스트 (CRUD + webhook 핸들러) · 3 E2E 플로 카카오페이 테스트 모드 통과
            엣지 케이스: 중복 webhook 이벤트, 결제 취소 처리
DC-SEC  ✔  카카오페이 webhook 서명 검증 · RLS 5개 테이블 전체 · 카카오 키 env 격리 ·
            NEXT_PUBLIC 접두사 감사 통과 · 0 취약점
DC-REV  ✔  91/100 · 카카오페이 Approve 멱등성 확인 · 타입 안전 · 중복 로직 없음

━━━━━━━━━━━━━━━━━━ 게이트 1–5 ━━━━━━━━━━━━━━━━━━
① 스캔       ✅  error-registry 0 히트 · 전체 파일 ≤ 300줄
② 기준       ✅  3개 E2E 플로 카카오페이 테스트 모드 통과
③ 버전       ✅  v2.0.49 전체 파일 일치
④ 분리       ✅  빌더 ≠ 리뷰어 확인
⑤ 파괴적    ✅  그린필드 — 파괴적 변경 없음

DC-TOK  ✔  컨텍스트 31% 사용 (40k / 128k 토큰)

[CEO 리포트] ✅ 28분 완료.
  파일: 17개 신규  ·  테스트: 19개 통과  ·  보안: 카카오 서명 + RLS  ·  배포: Vercel 준비 완료
```

**카카오페이로 회비 정산하는 앱. 코드 한 줄 안 썼다.**

---

### 🐛 버그 수정 현장

> `/ceo "크루장이 회비 납부 확인했다는데 앱에서는 계속 미납으로 뜬다고 제보가 왔어"`

```
[INTENT PARSED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
입력:   카카오페이 결제 완료인데 앱에서 미납으로 표시됨 — 카카오 콘솔에서는 결제 성공 확인
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
정제:   카카오페이 webhook은 정상 수신되지만 dues 테이블 status가
        "pending" → "paid"로 flip되지 않는 버그
목표:   webhook 핸들러 결함 파악 → 수정 → 납부 상태 실시간 반영 확인
범위:   포함 — webhook 핸들러 단일 수정
        제외 — UI 변경, 신규 기능, 무관 리팩터링
맥락:   Next.js 14 + Supabase · 기존 코드 · 카카오페이 테스트 모드 · 1-2 파일 예상
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[TASKROUTER]
업무:   카카오페이 webhook 상태 업데이트 버그 수정
라우트: LOOP  (1-2 파일, 반복 수정 + 회귀 검증)

[LOOP — 1회차]
🔧 수정 대상:  app/api/kakao/webhook/route.ts  (tid 매칭 + 상태 업데이트 로직)
🌊 파급 범위:  app/api/dues/[id]/route.ts      (PATCH 호출부 — 수정 불필요 확인)
               components/DuesCard.tsx          (status 읽기 전용 — 수정 불필요)
⚡ 근본 원인:  webhook payload의 tid(결제 고유번호) 비교 시 undefined 가드가 없음
               → 첫 번째 webhook은 tid 매칭 성공 후 DB 업데이트
               → 카카오페이 재시도 webhook은 tid가 undefined → 조건문 skip →
                  status 업데이트 없이 200 반환 → 결제 확인이 간헐적으로 누락됨

[DOC] docs/2026-05-02-v2.0.51-kakao-tid-fix/00-summary.md  ✔ 생성 완료

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// BEFORE — tid undefined 체크 없음 → 재시도 webhook 때 update 통째로 skip
const { tid, pg_token } = payload.payment_action_response
if (tid === existingDue.kakao_tid) {            // ❌ tid가 undefined면 false → skip
  await supabase.from('dues').update({ status: 'paid' }).eq('id', dueId)
}

// AFTER — undefined 먼저 잡고 비교
const { tid, pg_token } = payload.payment_action_response
if (!tid) {                                     // ✅ 방어: undefined/null 즉시 거부
  return NextResponse.json({ error: 'tid missing' }, { status: 400 })
}
if (tid === existingDue.kakao_tid) {
  await supabase.from('dues').update({ status: 'paid' }).eq('id', dueId)
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DC-REV  ✔  수정 정확. undefined 방어 패턴은 카카오페이 공식 문서 권장 방식.
            다른 호출부 영향 없음. 멱등성 키 로직 보존됨. APPROVED.
            개선 제안(논블로킹): 카카오 webhook 재시도 케이스를 단위 테스트로 추가 —
            개선 티켓으로 등록됨.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 게이트 1–5 ━━━━━━━━━━━━━━━━━━━━━━━━

① 스캔       ✅  error-registry 0 히트 · webhook/route.ts 42줄 (≤ 300줄)
② 기준       ✅  카카오페이 재시도 webhook 발화 → dues.status "paid" 자동 전환 확인
③ 버전       ✅  v2.0.51 전체 파일 일치
④ 분리       ✅  CEO 수정 · DC-REV 리뷰 — 역할 분리 확인
⑤ 파괴적    ✅  내부 핸들러만 수정 — API 계약 변경 없음

[CEO LOOP 리포트] ⚡ 5분 완료.
  수정 1개 파일 (3줄) · 카카오 재시도 webhook 정상 처리 · 납부 상태 즉시 반영
```

**버그 하나, 파일 하나, 5분. 나머지 코드는 손대지 않았다.**

---

### 🆕 최신 업데이트

| 버전 | 바뀐 것 |
|---|---|
| **v3.0.4** | 슬래시 커맨드 불필요 — 루프가 하네스 라우터에 직접 질의, README 사용법 한 곳으로 압축 |
| **v3.0.3** | 설치 시점 출력 전부 이중언어, 영어 우선 |
| **v3.0.2** | 사용자 package.json 을 건드리지 않음, 업데이트를 업데이트라고 알림, `npm i` 와 `npx` 구분 안내 |
| **v3.0.1** | 루프가 보고 계약을 직접 실어, 루프 프로젝트에서도 진행 상황을 보고함 |
| **v3.0.0** | 플래그 없는 한 명령이 실행 위치를 보고 설치, 자연어는 프로젝트 루프 · `/ceo` 는 하네스로 승격, 정책 자가학습, 한국어·영어 지원 |
| **v2.3.2** | 단일 렌더러에서 문구 사전 분리 |
| **v2.3.1** | 훅 오탐 제거 + 배포 누락 가시화 |
| **v2.3.0** | 진행 상황 보고 기본 활성화 |
| **v2.2.0** | Codex 네이티브 밀착 통합 |
| **v2.1.1** | 기존 공개 README 수준 완전 복원 및 현대화 |
| **v2.1.0** | 적응형 DIRECT · LOOP · GRAPH 아키텍처 |
| **v2.0.58** | 브라우저 검증 기본을 Chrome 확장 우선으로 전환 |

이전 25개 릴리스: [전체 변경 이력](https://github.com/DoCoreTeam/domangcha/releases)

---

### 🔄 적응형 파이프라인

```text
/ceo "업무"
      │
      ▼
의도 정규화 → 결정론적 TaskRouter
      ├── DIRECT  설명·요약·조회·국소 수정
      ├── LOOP    PLAN → EXECUTE → VALIDATE → ACT
      └── GRAPH   타입 상태 → 가드 엣지 → 분기/조인
                                  → 체크포인트 → 승인 게이트
      │
      ▼
업무에 필요한 검증만 수행
      │
      └── COMPLETE / PAUSED / FAILED
```

- **DIRECT**는 플래너 그래프, 재귀 루프, 불필요한 문서와 다중 에이전트를 만들지 않습니다.
- **LOOP**는 기존 Ralph를 발전시켜 최대 반복, 재시도 예산, 무진행·동일 오류 감지, 검증 피드백과 종료 근거를 관리합니다.
- **GRAPH**는 보안, 파괴적 변경, DB+API+UI, 병렬 작업, 중단·재개가 필요한 업무에만 사용합니다.
- LLM은 경계가 모호할 때 구조화된 라우트를 제안할 수 있지만, 안전 불변식과 최종 전이는 코드가 결정합니다.
- DIRECT → LOOP → GRAPH 승격 시 기존 작업 상태를 보존합니다.
- Claude Code는 `CLAUDE.md`, Codex는 `AGENTS.md`를 사용하지만 공유 정책·엔진·체크포인트·검증 규칙은 같습니다.

---

### 📣 진행 상황 보고 (기본 활성)

조용히 도는 엔진은 멈춘 엔진처럼 보입니다. CLI·Claude 훅·Codex 컨트롤 플레인이 모두
`orchestration/status.py`의 같은 카드를 사용하므로, 라우트와 루프와 병렬 브랜치를 **진행 중에** 볼 수 있습니다.

```text
🚂 DOMANGCHA · GRAPH 🧭 (score 10)        🔁 LOOP 5/30  ▓▓░░░░░░░░ 17%
├ 이유: hard graph invariant: parallel     ├ 재시도 여유 5 · 정체 0/3
├ 계획: 타입 노드 그래프 · 병렬 · join      ├ 예산: model 7/12 · tool 31/80
└ 다음: 노드·브랜치별 진행 보고             └ 상태: RUNNING ⏳

🧭 GRAPH full_pipeline@1  ▓▓▓▓▓░░░░░ 50% 3/6 노드
├ 완료: intake ✅ · plan ✅ · build ✅
├ 진행: review ⏳ (시도 1)
├ 병렬(build): dc-dev-be ✅ | dc-dev-fe ✅ | dc-sec ❌ · join=ALL
└ 승인 대기: gate 🙋
```

`engine.py route|status`는 기본으로 카드를 출력합니다. 원시 상태는 `--format json`,
언어는 `--lang ko|en`(기본값은 `DOMANGCHA_STATUS_LANG`)으로 바꿉니다. 보고 규칙 자체는 훅이 주입합니다 —
라우트와 그 이유를 먼저 알리고, 매 반복마다 회차·예산·실제 변화를 보고하고, 조인 시점에 브랜치 결과와
join 전략을 보여주고, 승인 게이트 앞에서 무엇을 왜 승인받는지 사람의 말로 설명하고,
긴 단계에서 침묵하거나 정체된 루프를 감추지 않습니다.

---

### 👥 18명의 에이전트

<table>
<thead>
<tr><th>단계</th><th>에이전트</th><th>역할</th><th>모델 정책</th></tr>
</thead>
<tbody>
<tr><td rowspan="5"><b>🧠 기획자</b></td>
  <td><code>DC-BIZ</code></td><td>사업 타당성 판단</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-RES</code></td><td>기술 리서치</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-OSS</code></td><td>오픈소스 도구 탐색</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-ANA</code></td><td>코드베이스 분석가</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-KNW</code></td><td>지식 레지스트리 큐레이터</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td rowspan="9"><b>🔨 빌더</b></td>
  <td><code>DC-DEV-DB</code></td><td>데이터베이스 엔지니어</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-BE</code></td><td>백엔드 개발자</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-FE</code></td><td>프론트엔드 개발자</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-OPS</code></td><td>DevOps 엔지니어</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-MOB</code></td><td>모바일 개발자</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DEV-INT</code></td><td>통합(Integration) 엔지니어</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-DOC</code></td><td>문서 작성자</td><td>FAST_CHEAP</td></tr>
<tr><td><code>DC-WRT</code></td><td>카피라이터</td><td>FAST_CHEAP</td></tr>
<tr><td><code>DC-SEO</code></td><td>SEO / AEO / GEO</td><td>FAST_CHEAP</td></tr>
<tr><td rowspan="3"><b>🔍 평가자</b></td>
  <td><code>DC-QA</code></td><td>QA 엔지니어</td><td>BALANCED / HIGH_REASONING</td></tr>
<tr><td><code>DC-SEC</code></td><td>보안 리뷰어</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><code>DC-REV</code></td><td>코드 리뷰어</td><td>HIGH_REASONING / REVIEW</td></tr>
<tr><td><b>⚙️ 지원</b></td>
  <td><code>DC-TOK</code></td><td>토큰 예산 관리</td><td>FAST_CHEAP</td></tr>
</tbody>
</table>

> 역할은 라우트와 업무에 따라 선택됩니다. DIRECT는 보통 역할을 호출하지 않고, LOOP는 반복에 필요한 역할만, GRAPH는 독립 작업에 필요한 역할을 병렬 호출합니다. 권위 원본은 `domangcha/manifests/agents.json`입니다.

---

### 🛡️ 5개의 게이트

> 업무 위험도에 맞는 게이트를 적용합니다. DIRECT에는 의례적인 평가기를 붙이지 않으며, 코드 변경·보안·릴리스·파괴적 작업에는 필요한 검증과 승인 경계를 강제합니다.

| 게이트 | 검증 항목 |
|:---:|---|
| **① 스캔** | 오류 패턴, 비밀정보, 저장소 규칙, 유지보수성 검사 |
| **② 기준** | 업무별 완료 근거, 테스트, 린트, 타입체크, 빌드 |
| **③ 일관성** | 매니페스트, 버전, 그래프 스키마, 도달 가능한 종료 상태 |
| **④ 분리** | 의미 있는 구현의 작성자와 유일 리뷰어를 분리 |
| **⑤ 안전** | 파괴적·비가역·호환성 파괴 작업에 명시적 승인 |

---

### 🖥️ 명령어

**여기 있는 명령은 전부 선택 사항입니다.** 자연어로 말해도 같은 일을 하고, 이건 단축키입니다.

루프 프로젝트에서는 `/plan` 이 새 지시의 플랜을 쓰고, `/loop` 가 다음 항목부터 재개하고,
`/policy` 가 활성 정책을 현재 변경분에 대조합니다. 그 뒤의 CLI 는 `node scripts/loop.mjs` 이고,
`help` 로 전체 하위 명령, `resume` 으로 다음에 할 일, `status --all` 로 등록된 모든 프로젝트를
볼 수 있습니다.

하네스가 있으면 `/ceo "업무"` 로 명시 라우팅을 하고, 18개 `/ceo-*` 인텐트
(`-ralph -debug -test -review -security -ship -plan -design -feature -doc -clarify -init
-quality -status -update -version -knowledge -learn`) 가 워크플로를 지정합니다. 전부 같은
TaskRouter 로 들어가는 어댑터이고, 그 라우터는 이미 평범한 프롬프트를 읽습니다 —
그래서 어느 것도 필수가 아닙니다.

---

### 📐 코딩 표준

타협 불가. Gate 1이 모든 파일에서 강제합니다.

```
✓ 파일당 최대 300줄  ·  함수당 최대 50줄  ·  중첩 최대 4단계
✓ 불변성(Immutability) — 항상 새로 만들고, 절대 변경하지 않기
✓ 모든 계층에서 명시적 에러 처리  ·  모든 경계에서 입력 검증
✓ 모든 기능에 테스트 필수  ·  모든 테이블에 RLS 적용
```

---

### 📦 요구사항

| | 프로젝트 루프 (프로젝트 안) | 하네스 (프로젝트 밖, 또는 `/ceo`) |
|---|---|---|
| 코딩 에이전트 | Claude Code 또는 Cursor | Claude Code 또는 OpenAI Codex |
| Node.js | **22.13 이상** — `node:sqlite`, npm 의존성 없음 | npm 설치용 14 이상 |
| Python | 사용 안 함 | 결정론적 엔진용 3.10 이상 |
| `git` | 항목이 통과할 때마다 커밋 | 설치·저장소 검사·리뷰 가능한 diff |
| 네트워크 | 불필요 — 템플릿이 패키지에 동봉됨 | 필요 — GitHub 에서 `install.sh` 를 받아옴 |

---

### 🔀 v2.x 에서 올라오기

깨지는 것도, 없어지는 것도 없습니다.

- **지금 그대로 쓰고 싶다** — 하네스는 건드려지지 않았습니다. 위 curl 명령이나, 프로젝트 밖에서
  `npx domangcha` 로 갱신하세요.
- **한 프로젝트에서만 루프를 써 보고 싶다** — 그 폴더에서 `npx domangcha`. 전역 설치는 그대로
  있고, 그 프로젝트 안에서만 라우터가 `LOOP.md` 에 자리를 내줍니다.
- **프로젝트에 이미 `CLAUDE.md` 가 있다면** 자동으로 `.claude/heavy/CEO.md` 로 옮겨지고 중량
  항목에서 다시 읽힙니다. 그 자리에 두려면 `--no-migrate`.
- **되돌리려면** `LOOP.md`, `scripts/loop.mjs`, `.loop/` 를 지우고 `.claude/heavy/CEO.md` 를
  `CLAUDE.md` 로 복원하면 됩니다.

**Codex 최초 실행:** Codex를 재시작하고 `/hooks`에서 DOMANGCHA plugin hook을 최초 1회 신뢰하세요. 새 스레드부터 라우팅과 작업 상태가 자동으로 붙습니다. skill 선택을 명시하려면 `$domangcha`를 사용합니다.

</details>

---

<div align="center">

**Escape development hell. 🚗💨 DOMANGCHA is your getaway car.**

[![GitHub](https://img.shields.io/badge/GitHub-DoCoreTeam-181717?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha)
[![npm](https://img.shields.io/badge/npm-domangcha-CB3837?style=for-the-badge&logo=npm)](https://www.npmjs.com/package/domangcha)

---

**Built by [Michael Dohyeon Kim](https://github.com/DoCoreTeam)**
CEO of KDC (Korea Development Company) · Serial builder · Claude Code power user

*I built DOMANGCHA because I was drowning in manual orchestration.*
*Now I ship features in hours that used to take days.*
*This is my exact setup — open-sourced.*

MIT License · Star it if it's useful ⭐

</div>
