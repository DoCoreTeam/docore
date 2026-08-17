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
One command selects DIRECT, LOOP, or GRAPH—then coordinates up to 18 logical specialists only when the task needs them.

*Your AI getaway car from development hell.*

[![Version](https://img.shields.io/badge/version-2.3.2-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Runtimes](https://img.shields.io/badge/Runtimes-Claude%20Code%20%7C%20Codex-5865F2?style=for-the-badge)](#runtime-compatibility)
[![Agents](https://img.shields.io/badge/Agents-18-FF6B6B?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha#the-18-agents)
[![Gates](https://img.shields.io/badge/Gates-5-orange?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha#the-5-gates)

<br/>

> **I typed one command and got back auth, payments, and a dashboard — tested, reviewed, security-audited. I went to get coffee.**
>
> *— Michael Dohyeon Kim, KDC CEO · builder of DOMANGCHA*

```bash
# Install (30 seconds)
npx domangcha
```

```bash
# Then, inside Claude Code or a Codex-enabled project:
/ceo "Build a Stripe invoicing tool for freelancers — invoices, email, paid/overdue dashboard"
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

`npx domangcha` installs the bundled DOMANGCHA plugin into a local Codex marketplace and enables its native skill. After installation, open `/hooks` once and trust the DOMANGCHA hook definition. From the next new Codex thread:

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

| Version | Feature |
|---|---|
| **v2.3.2** | **The single renderer stops carrying the phrasebook** — `orchestration/status.py` had reached 296 of its 300-line budget, so the next card would have broken `validate_line_limits`. The bilingual vocabulary (`LABELS`, `PLAN`, `NEXT`, `LANGS`) moved to `orchestration/wording.py`, leaving status.py at 226 lines with layout logic only. No behavior change: every card renders byte-identically and the same 86 tests pass. |
| **v2.3.1** | **Hooks stop misfiring on unrelated projects, and stale deployments become visible** — the Stop hook identified this repository by `domangcha/VERSION` + `package.json` alone, so any project that happens to keep its own `domangcha/VERSION` was validated as if it were the framework source and crashed on the missing manifest every turn; the manifest itself is now the identifier. The post-edit hook's `find_root()` walked past `$HOME` and ran `npm test` in whatever monorepo lived there, blocking edits to files outside any project; it now stops at `$HOME`. `RepositoryValidator` reported a missing or malformed manifest as a raw traceback instead of a validation error, so a broken repository looked like a crashed engine — missing, unreadable, and invalid JSON are now ordinary entries in `errors`. New `engine.py drift` compares the installed `~/.domangcha` runtime against this repository by content hash and reports stale files in `/ceo-status`: both VERSION files agree while the code differs, so a version check cannot see this, and a fix that never shipped stays silent until the stale path is reached. |
| **v2.3.0** | **Progress reporting is on by default** — the engine used to record route, loop, and branch state into checkpoints and `events.jsonl` with nothing rendering it, so a running engine looked like a stalled one. `orchestration/status.py` is now the single renderer for route, loop, graph, and parallel-branch cards (Korean by default, `--lang en`, secrets redacted). `engine.py route\|status` prints a card by default (`--format json` keeps the raw state), the Claude `UserPromptSubmit` hook injects the card plus a reporting contract, the Ralph `Stop` hook injects the live loop card every iteration, and the Codex control plane renders the same cards. Announce the route and why, report iteration and budget every pass, show branch results and join strategy at fan-in, explain gates in plain language, and never go silent through a long step. |
| **v2.2.0** | **Native Codex attachment** — bundles an installable Codex plugin with an implicitly matching DOMANGCHA skill and `UserPromptSubmit`, `PostToolUse`, `SubagentStop`, and `Stop` lifecycle hooks. Codex now receives automatic route/task injection, workspace checkpoints, tool and validation evidence, bounded continuation, and a deterministic completion command instead of relying on `AGENTS.md` alone. The installer registers the local marketplace and plugin automatically; users approve the hook definition once through `/hooks`. |
| **v2.1.1** | **Full public README restored and modernized** — restores the original bilingual hero, real sprint and bug-fix walkthroughs, 18-role catalog, five gates, release history, complete 19-command reference, requirements, and every install/update path. Legacy mandatory-pipeline claims are rewritten for adaptive DIRECT/LOOP/GRAPH behavior and Claude Code/Codex parity. |
| **v2.1.0** | **Adaptive DIRECT · LOOP · GRAPH architecture** — one deterministic TaskRouter evolves CEO SIZE ASSESSMENT, FAST PATH, Ralph, and FULL PIPELINE into a single authority. Adds typed graph contracts, bounded retry and joins, checkpoint/resume, human gates, budgets, structured events, Claude Code + Codex adapters, shared policies, authoritative manifests, and deterministic CI tests. Existing `/ceo-*` commands and all 18 roles remain compatible. |
| **v2.0.58** | **Browser verification now Chrome-extension-first** — app real-screen/visual/interaction QA now defaults to the Claude-in-Chrome extension (`mcp__claude-in-chrome__*`) instead of Playwright, since the extension verifies directly in the user's live Chrome session with no separate driver. New **"브라우저 검증 정책"** [BV-1]/[BV-2] in `ceo-standards`: [BV-1] Chrome extension = default; [BV-2] Playwright = fallback only (headless CI / regression suites / extension unavailable). Reflected in `/ceo-test` (STEP 4), `/ceo-debug` (STEP 4), `/ceo-ship` (STEP 5), 🟥 DC-QA, 🟩 DC-DEV-FE, and the install Playwright setup (repositioned as fallback). **Unaffected:** the `insane-search` engine's Playwright, which is for external URL-body scraping (WAF bypass), not app verification. |
| **v2.0.57** | **insane-search vendored — blocked-site bypass for research agents** — the [insane-search](https://github.com/fivetaku/insane-search) skill (MIT) is now vendored into `skills/insane-search/` and installed to `~/.claude/skills/`. 🟦 DC-RES and 🟦 DC-OSS now use its Phase 0→3 adaptive engine (`python3 -m engine`, curl_cffi TLS impersonation + Playwright) as the **default reader for fetching any external URL body** — not just an on-block fallback. Phase 0 tries official public APIs first (X/Reddit/YouTube/HN/arXiv), so plain URLs cost nothing extra, and WAF/bot-walled sites (Naver, Medium, StackOverflow, LinkedIn…) get bypassed automatically. Keyword discovery still goes through WebSearch/`gh search`; only URL-body fetching routes through the engine. Upstream plugin's GitHub-star/`${CLAUDE_PLUGIN_ROOT}` Step-0 hook stripped for vendored use. |
| **v2.0.56** | **Model tier re-assignment — dev on Opus, planning on Fable** — code-writing agents 🟩 DC-DEV-BE/FE/DB/OPS/MOB/INT now run on **`claude-opus-4-8`** (top coding model), and planning/judgment agents 🟦 DC-BIZ/RES/OSS run on **`claude-fable-5`** (fast). 🟥 DC-SEC/REV stay on `claude-opus-4-7`; 🟦 DC-ANA/KNW + 🟥 DC-QA stay on `claude-sonnet-4-6`; 🟩 DC-WRT/DOC/SEO + 🟨 DC-TOK stay on Haiku. Applied to all 9 agent frontmatters and the model-assignment table in root/global/project CLAUDE.md and `ceo-system` SKILL. |
| **v2.0.55** | **Feature Implementation Defaults baked in** — "build feature X" now auto-includes the full entity lifecycle by default. Every feature ships **full CRUD** (Create/Read/Update/Delete, soft-delete default), and collection entities get a **List** with four affordances built in: **search, sort, filter, and performant loading (server pagination by default; cursor for large sets; infinite-scroll via Q&A)**. List state (search/sort/filter/page) syncs to the URL. Encoded in `ceo-standards`, the 🟩 DC-DEV-BE/FE/DB agents, and CEO core rule 3-2 — DOC-FIRST completion criteria auto-expand these and 🟥 DC-REV/QA fail the sprint if any are missing. Opt out only by explicitly excluding in Q&A. |
| **v2.0.54** | **Ralph Loop is now a real engine, not a prompt** — `/ceo-ralph` used to be markdown instructions with no driver, so it stopped mid-task. v2.0.54 adds `domangcha-ralph-loop.py`, a **blocking Stop hook** that re-reads `.ralph/status.json` and forces continuation (`exit 2`) while `active && !exit_signal && loop_count < max_loops && breaker CLOSED`. Safety guards: `active` flag (zero effect outside a ralph loop), `max_loops` (default 30, hard ceiling 100), Circuit Breaker, atomic status writes. The CEO enforcer no longer injects the conflicting one-shot pipeline block for `/ceo-ralph` — it injects a ralph-specific reminder (max 2 Q&A, never stop, autonomous decisions). The loop now actually runs to completion. |
| **v2.0.51** | **FAST PATH Bug-Fix Demo (EN + KO)** — "Watch a Bug Fix" and "버그 수정 현장" sections added. Shows the full FAST PATH flow: RIPPLE CHECK → 00-summary.md → surgical fix → DC-REV → GATE 1-5 → deploy. EN scenario: Stripe webhook raw-body bug. KO scenario: 카카오페이 `tid` undefined guard. |
| **v2.0.50** | **README Sprint Demo — full agent detail + Korean scenario** — EN "Watch a Real Sprint" now shows DC-KNW GUARD advisory output, DC-DOC, and DC-TOK for every sprint. All agents have concrete, role-specific output (not just ✔). Korean "실제 스프린트 보기" section added with a KakaoPay-powered running crew app scenario. `error-registry` ERR-007 added: mandatory 7-point README section checklist on every update. |
| **v2.0.48** | **Auto-untrack existing `docs/` subdirs on update** — `install.sh` now runs `git rm -r --cached` on already-tracked `docs/` subdirectories when you `npx domangcha` on an existing project. Supports Korean/Unicode folder names via `core.quotepath=false`. Works on both fresh installs and updates. |
| **v2.0.47** | **Auto-inject `docs/*/` into user project `.gitignore`** — `npx domangcha` now automatically appends `docs/*/` to your project's `.gitignore` so local planning docs are never accidentally committed. 3-guard protection: skips `$HOME`, the DOMANGCHA repo itself, and non-git directories. Opt-out via `DOMANGCHA_SKIP_GITIGNORE=1`. |
| **v2.0.46** | **DC-KNW Security Hardening** — `dc-knw.md` adds 7 security rules: path traversal guard (reject `..`/absolute paths), frontmatter injection defense (escape `---` delimiters, fixed schema only), GUARD output quoted as data blocks, `.knw-queue/` size cap (100 files / 8KB per entry). |
| **v2.0.45** | **Knowledge Registry (DC-KNW — 18th Agent)** — `domangcha/knowledge-registry/` with 5 type folders (error/pattern/decision/workflow/skill), `.knw-queue/` approval pipeline, 3 seed entries from error-registry, and `/ceo-knowledge /ceo-learn /ceo-promote /ceo-forget` command suite. DC-KNW added to CORE (runs GUARD mode at every PHASE 1 as advisory). |
| **v2.0.44** | **DOC-FIRST enforced on all 4 stacks** — Ralph Loop now creates `docs/` before the autonomous loop starts (Phase 0 in `fix_plan.md`). Superpowers routes `writing-plans → approval → DOC-FIRST → executing-plans → GATE → deploy`. gstack DOC-FIRST via FULL PIPELINE made explicit. Standard also marked. Knowledge Registry system designed (DC-KNW, 18th agent) — implementation sprint in v2.0.45+. |
| **v2.0.43** | **Dynamic Stack Selection Rubric** — PHASE 0.3 now uses a 12-condition scoring table (`stack-selection-rubric.md`) instead of hardcoded 80/60/45/25 scores. Standard no longer always wins — each stack earns points based on actual task characteristics. |
| **v2.0.42** | **Gap Analysis + §6 Full Propagation** — §6 EXEC-001~004 rules added to `ceo-core/SKILL.md` and `ceo-sprint/SKILL.md`. Version update procedure now includes `~/.claude/CLAUDE.md` step in all 3 CLAUDE.md files. `ceo-system/SKILL.md` version procedure expanded to full 11-step list (was 6, missing `package.json` + root files). |
| **v2.0.41** | **Execution Integrity Rules (§6)** — 4 hard rules added to all CLAUDE.md files: no unverified completion, no mid-implementation stops, CLI direct execution, session report mandatory. EXEC-001~004 added to error-registry. GATE 2 now outputs a line-by-line checklist from `04-completion-criteria.md`. |
| **v2.0.40** | **Docs path slug sync** — README pipeline diagrams and `rule_doc_first.md` memory template updated to `YYYY-MM-DD-vX.X.X-<slug>/` convention. package.json description trimmed for npm search. |
| **v2.0.39** | **README + GitHub branding overhaul** — new hero "Claude Code without DOMANGCHA is half the toolkit", functional-first positioning, docs folder naming convention `YYYY-MM-DD-vX.X.X-<slug>`, npm keywords +4 (harness/agent-orchestration/vibe-coding/subagents). |
| **v2.0.38** | **Memory sync moved to Step 5** — memory templates now refresh before Playwright/git-hooks, so `set -e` failures can never skip the sync. Adds `rule_grand_principles.md` template + memory row in `/ceo-update` table. |
| **v2.0.37** | **Grand Principles (Karpathy)** — Andrej Karpathy's 4 coding grand principles merged into all CLAUDE.md files and `coding-style.md`. Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution — with DOMANGCHA context. |
| **v2.0.36** | **npx-first updates** — `/ceo-update` and `/ceo-version` now use `npx domangcha` as primary, `curl \| bash` as fallback. Fixes stale bin version + `curl -fsSL` safety flag. |
| **v2.0.35** | **DC-ANA (17th Agent)** — DOMANGCHA's internal codebase analyst. Absorbs all ECC code-explorer capabilities. Auto-triggered for gap analysis, refactoring, and LARGE/HEAVY tasks. `code-explorer` (ECC) calls now banned. |
| **v2.0.34** | **FAST PATH Lightweight DOC** — Every task, even small fixes, generates a `00-summary.md`. No more undocumented changes. |
| **v2.0.33** | **Memory Sync** — rule memories auto-refresh on every `npx domangcha` update. User feedback and project context are never overwritten. |
| **v2.0.31** | **Tradeoff Check** — CEO surfaces architectural risks and side effects before any Q&A or implementation begins. |
| **v2.0.30** | Agent color-coding system — visual group identification across all pipeline output. |

---

## 🔄 Updates

**How updates work:**

Files are installed to `~/.claude/` on first run. They do **not** auto-update while a project is in progress — the version at install time is what runs.

**To update:** re-run `npx domangcha`. Your error registry and project registries are preserved. Rule memories in `~/.claude/projects/*/memory/` are automatically refreshed with the latest version's rule definitions — user feedback and project context are never overwritten.

**Auto-update prompt (built-in):** Every `/ceo` call silently checks the npm registry for a newer version. If one exists, you'll see:

```
[CEO] New version v2.0.33 available (installed: v2.0.31).
Update before continuing? (y/n):
```

- `y` → runs `npx domangcha`, updates in-place, then continues with your task
- `n` / Enter → skips and continues without updating

Version check failures (offline, etc.) are silently ignored — your task is never blocked.

---

## 🖥️ Commands

Commands are intent adapters into the same TaskRouter. They do not create independent orchestration systems.

| Command | What it does |
|---|---|
| `/ceo "[task]"` | 🧭 Automatic DIRECT / LOOP / GRAPH routing |
| `/ceo-ralph "[task]"` | 🔁 Force minimum LOOP; safety may still escalate to GRAPH |
| `/ceo-clarify` | 💬 Clarify intent, scope, and completion criteria |
| `/ceo-design` | 🧭 Architecture/design intent routed by actual complexity |
| `/ceo-doc` | 📝 Documentation workflow |
| `/ceo-feature` | ✨ Feature implementation routed by scope |
| `/ceo-init` | 🔧 Project harness setup |
| `/ceo-debug "[bug]"` | 🐛 Investigate → fix → verify |
| `/ceo-plan` | 🗺️ Planning workflow |
| `/ceo-quality` | 📏 Deterministic quality checks |
| `/ceo-review` | 🔍 Independent quality and PR review |
| `/ceo-security` | 🔐 Security workflow; GRAPH where safety requires |
| `/ceo-test` | ✅ TDD + unit + E2E + browser QA |
| `/ceo-ship` | 📦 Gate → review → build → deploy |
| `/ceo-status` | 📊 DIRECT status lookup |
| `/ceo-update` | ⬆️ Guarded installer update |
| `/ceo-version` | 🏷️ Deterministic version consistency check |
| `/ceo-knowledge "[query]"` | 🧠 Search knowledge registry by ID or keyword |
| `/ceo-learn "[pattern]"` | 📝 Stage new knowledge entry to review queue |

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

| | |
|---|---|
| Claude Code or OpenAI Codex | At least one supported coding-agent runtime |
| Python | 3.10+ for the deterministic orchestration engine |
| Node.js | 14+ for npm installation |
| `git` | Installer, repository checks, and reviewable diffs |

---

## 🚀 Install · Update

**Option 1 — npx (recommended)**
```bash
npx domangcha
```

**Option 2 — curl**
```bash
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash
```

**Option 3 — global install**
```bash
npm install -g domangcha && domangcha
```

Re-running always pulls the latest. Your registries (errors, instincts, history) are preserved.

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
명령 하나가 DIRECT, LOOP, GRAPH 중 최소 복잡도를 선택하고, 필요할 때만 최대 18개 논리 역할을 조율합니다.

*개발 지옥에서 도망쳐 — 돔황차🚗💨*

[![Version](https://img.shields.io/badge/version-2.3.2-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Runtimes](https://img.shields.io/badge/런타임-Claude%20Code%20%7C%20Codex-5865F2?style=for-the-badge)](#runtime-compatibility)
[![Agents](https://img.shields.io/badge/에이전트-18명-FF6B6B?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha)
[![Gates](https://img.shields.io/badge/게이트-5개-orange?style=for-the-badge)](https://github.com/DoCoreTeam/domangcha)

> **명령 하나 쳤더니 인증, 결제, 대시보드가 돌아왔다. 테스트 통과, 보안 감사 완료, 코드 리뷰까지.**
>
> *— Michael Dohyeon Kim, KDC CEO · DOMANGCHA 제작자*

```bash
# 방법 1 — npx (권장)
npx domangcha

# 방법 2 — curl
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash
```

```bash
/ceo "프리랜서용 Stripe 인보이스 툴 만들어줘 — 인보이스 생성, 이메일 발송, 미납/완납 대시보드"
```

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

| 버전 | 기능 |
|---|---|
| **v2.3.2** | **단일 렌더러에서 문구 사전 분리** — `orchestration/status.py`가 300줄 제한 중 296줄까지 차서, 카드를 하나만 더 추가해도 `validate_line_limits`가 깨지는 상태였습니다. 이중 언어 문구 테이블(`LABELS`, `PLAN`, `NEXT`, `LANGS`)을 `orchestration/wording.py`로 옮겨 status.py는 레이아웃 로직만 남은 226줄이 됐습니다. 동작 변화 없음 — 모든 카드가 이전과 동일하게 렌더링되고 같은 86개 테스트가 통과합니다. |
| **v2.3.1** | **훅 오탐 제거 + 배포 누락 가시화** — Stop 훅이 `domangcha/VERSION` + `package.json`만 보고 이 저장소를 식별해서, 자기 앱 버전을 우연히 `domangcha/VERSION`에 두는 프로젝트를 프레임워크 소스로 오인하고 매 턴 없는 매니페스트를 찾다 크래시했습니다. 이제 매니페스트 자체가 식별자입니다. post-edit 훅의 `find_root()`는 `$HOME` 위로 올라가 거기 있는 모노레포에서 `npm test`를 돌려 프로젝트 밖 파일 편집을 차단했습니다. 이제 `$HOME`에서 멈춥니다. `RepositoryValidator`는 매니페스트가 없거나 깨졌을 때 검증 오류 대신 raw 트레이스백으로 죽어서, 망가진 저장소가 죽은 엔진처럼 보였습니다. 이제 없음·읽기 실패·잘못된 JSON 모두 평범한 `errors` 항목입니다. 신규 `engine.py drift`는 설치된 `~/.domangcha` 런타임을 이 저장소와 내용 해시로 비교해 오래된 파일을 `/ceo-status`에 보고합니다. 양쪽 VERSION이 같은데 코드만 다른 상황은 버전 비교로 잡을 수 없고, 배포되지 않은 수정은 그 경로에 도달할 때까지 조용하기 때문입니다. |
| **v2.3.0** | **진행 상황 보고 기본 활성화** — 엔진은 라우트·루프·브랜치 상태를 체크포인트와 `events.jsonl`에 기록만 하고 **렌더링하는 코드가 없었습니다**. 그래서 돌고 있는 엔진이 멈춘 엔진처럼 보였습니다. 이제 `orchestration/status.py`가 라우트·루프·그래프·병렬 브랜치 카드를 렌더링하는 단일 지점입니다(한국어 기본, `--lang en`, secret 자동 마스킹). `engine.py route\|status`는 기본이 카드 출력이고(`--format json`으로 원시 상태 유지), Claude `UserPromptSubmit` 훅이 카드와 **보고 규칙**을 주입하며, Ralph `Stop` 훅이 매 회차 실제 루프 카드를 주입하고, Codex 컨트롤 플레인도 같은 카드를 씁니다. 라우트와 이유를 먼저 알리고, 매 반복마다 회차·예산·실제 변화를 보고하고, 조인 시점에 브랜치 결과와 join 전략을 보여주고, 게이트를 사람의 말로 설명하고, 긴 단계에서 침묵하지 않습니다. |
| **v2.2.0** | **Codex 네이티브 밀착 통합** — 자동 매칭되는 DOMANGCHA skill과 `UserPromptSubmit`, `PostToolUse`, `SubagentStop`, `Stop` lifecycle hook을 갖춘 설치형 Codex plugin을 번들했습니다. 이제 Codex가 `AGENTS.md`만 읽는 대신 라우트/task ID 자동 주입, 워크스페이스 체크포인트, 도구·검증 근거 기록, 제한된 자동 계속, 결정론적 완료 명령을 사용합니다. 인스톨러가 로컬 marketplace와 plugin을 자동 등록하며 사용자는 `/hooks`에서 최초 1회 신뢰하면 됩니다. |
| **v2.1.1** | **기존 공개 README 수준 완전 복원 및 현대화** — 영문·한국어 히어로, 실제 스프린트·버그 수정 데모, 18개 역할, 5개 게이트, 변경 이력, 19개 전체 명령어, 요구사항, 모든 설치·업데이트 경로를 복원했습니다. 과거의 전체 파이프라인 강제 설명은 DIRECT/LOOP/GRAPH 적응형 실행과 Claude Code/Codex 동등성에 맞게 교체했습니다. |
| **v2.1.0** | **적응형 DIRECT · LOOP · GRAPH 아키텍처** — CEO SIZE ASSESSMENT, FAST PATH, Ralph, FULL PIPELINE을 하나의 결정론적 TaskRouter 권한으로 통합했습니다. 타입 그래프 계약, 제한된 재시도와 조인, 체크포인트/재개, 사람 승인 게이트, 예산, 구조화 이벤트, Claude Code + Codex 어댑터, 공유 정책과 권위 매니페스트를 추가했습니다. 기존 `/ceo-*` 명령과 18개 역할은 유지됩니다. |
| **v2.0.58** | **브라우저 검증 기본을 Chrome 확장 우선으로 전환** — 실행 중인 앱의 실화면·시각·인터랙션 QA를 Playwright 대신 **Claude-in-Chrome 확장**(`mcp__claude-in-chrome__*`) 기본으로 변경. 확장은 사용자 실제 Chrome 세션에서 별도 드라이버 없이 바로 검증 가능. `ceo-standards`에 **"브라우저 검증 정책"** [BV-1]/[BV-2] 신설: [BV-1] Chrome 확장=기본, [BV-2] Playwright=폴백(헤드리스 CI·회귀 스위트·확장 미가용 시에만). `/ceo-test`(STEP 4)·`/ceo-debug`(STEP 4)·`/ceo-ship`(STEP 5)·🟥 DC-QA·🟩 DC-DEV-FE 및 install Playwright 셋업(폴백으로 재포지셔닝)에 일괄 반영. **무관·유지:** `insane-search` 엔진의 Playwright는 외부 URL 본문 스크래핑(WAF 우회)용으로 본 정책과 별개. |
| **v2.0.57** | **insane-search 내장 — 리서치 에이전트 차단 우회** — [insane-search](https://github.com/fivetaku/insane-search) 스킬(MIT)을 `skills/insane-search/`로 vendoring하고 `~/.claude/skills/`에 설치. 🟦 DC-RES·🟦 DC-OSS가 외부 URL 본문 수집 시 Phase 0→3 적응형 엔진(`python3 -m engine`, curl_cffi TLS 임퍼소네이션 + Playwright)을 **차단 여부와 무관하게 기본 리더로 우선 사용**(fallback 아님). Phase 0가 공식 공개 API(X·Reddit·YouTube·HN·arXiv)를 먼저 시도해 일반 URL도 손해 없고, WAF/봇 차단 사이트(Naver·Medium·StackOverflow·LinkedIn 등)는 자동 우회. 키워드 탐색은 WebSearch·`gh search`, URL 본문 수집만 엔진 경유. 업스트림 플러그인의 GitHub-star/`${CLAUDE_PLUGIN_ROOT}` Step-0 훅은 vendoring용으로 제거. |
| **v2.0.56** | **모델 티어 재배정 — 개발은 Opus, 기획은 Fable** — 코드 개발 에이전트 🟩 DC-DEV-BE/FE/DB/OPS/MOB/INT을 **`claude-opus-4-8`**(최고 코딩 모델)로, 기획/판단 에이전트 🟦 DC-BIZ/RES/OSS를 **`claude-fable-5`**(고속)로 전환. 🟥 DC-SEC/REV는 `claude-opus-4-7` 유지, 🟦 DC-ANA/KNW + 🟥 DC-QA는 `claude-sonnet-4-6` 유지, 🟩 DC-WRT/DOC/SEO + 🟨 DC-TOK는 Haiku 유지. 에이전트 frontmatter 9개와 루트/글로벌/프로젝트 CLAUDE.md·`ceo-system` SKILL의 배정 테이블에 일괄 반영. |
| **v2.0.55** | **기능 구현 기본 정책 내장 (Feature Defaults)** — "X 기능 만들어줘"만 해도 엔티티 수명주기 전체가 기본 포함됨. 모든 기능에 **CRUD 전체**(생성/조회/수정/삭제, 소프트삭제 기본), 컬렉션 엔티티엔 **List + 4어포던스 기본 탑재**: **검색·정렬·필터 + 성능 로딩(기본 서버 페이지네이션, 대용량 cursor, 피드형은 Q&A로 무한스크롤)**. 검색/정렬/필터/페이지 상태는 URL에 동기화. `ceo-standards`·🟩 DC-DEV-BE/FE/DB 에이전트·CEO 핵심규칙 3-2에 내장 — DOC-FIRST 완료기준에 자동 전개되고 🟥 DC-REV/QA가 누락 시 FAIL. Q&A에서 명시 제외해야만 빠짐. |
| **v2.0.54** | **Ralph Loop이 진짜 엔진이 됨 (프롬프트 → 코드)** — 기존 `/ceo-ralph`는 드라이버 없는 마크다운 지침이라 중간에 멈췄음. v2.0.54에서 **Stop hook 루프 엔진** `domangcha-ralph-loop.py` 추가: `.ralph/status.json`을 읽어 `active && !exit_signal && loop_count<max_loops && breaker CLOSED`면 `exit 2`로 재진입을 강제해 **끝까지 루프**. 안전가드 — `active` 플래그(루프 밖 세션엔 무영향), `max_loops`(기본30·절대상한100), Circuit Breaker, atomic status 쓰기. enforcer는 `/ceo-ralph`에 충돌하던 1회성 파이프라인 블록 대신 **ralph 전용 reminder**(질문 최대2·멈춤금지·자율결정) 주입. 이제 루프가 실제로 완료까지 돈다. |
| **v2.0.51** | **FAST PATH 버그 수정 데모 (EN + KO)** — "Watch a Bug Fix"와 "버그 수정 현장" 신규 추가. RIPPLE CHECK → 00-summary.md → 외과적 수정 → 🟥 DC-REV → GATE 1-5 → 배포 전체 흐름 시각화. EN: Stripe webhook raw-body 버그. KO: 카카오페이 `tid` undefined 가드 누락. |
| **v2.0.50** | **README 스프린트 데모 전면 강화 + 한국 시나리오** — EN "Watch a Real Sprint"에 DC-KNW GUARD 어드바이저리 블록, DC-DOC, DC-TOK 출력 추가. 전 에이전트 출력이 역할별 구체적 내용으로 확장. 한국 시나리오 "실제 스프린트 보기" 신규 작성(동네 러닝 크루 앱, 카카오페이 회비 정산). `error-registry` ERR-007 추가: 업데이트마다 7개 README 섹션 전수 점검 필수. |
| **v2.0.49** | **docs/ 자동 언트래킹 개선** — `install.sh` 캐시 무효화 + `update_notice` semver 방향 비교 수정. 버전 배지 자동 갱신 보강. |
| **v2.0.48** | **기존 `docs/` 하위 폴더 언트래킹 자동화** — `npx domangcha` 실행 시 이미 git 추적 중인 `docs/` 하위 폴더를 `git rm -r --cached`로 자동 언트래킹. 한글/유니코드 폴더명 지원 (`core.quotepath=false`). 신규 설치·업데이트 모두 적용. |
| **v2.0.47** | **사용자 프로젝트 `.gitignore` 자동 처리** — `npx domangcha` 실행 시 사용자 프로젝트의 `.gitignore`에 `docs/*/` 자동 주입. 기획 문서가 실수로 커밋되지 않도록 방지. 3중 가드: `$HOME` 스킵, DOMANGCHA 레포 자체 스킵, git 레포 없음 스킵. 비활성화: `DOMANGCHA_SKIP_GITIGNORE=1`. |
| **v2.0.46** | **DC-KNW 보안 강화** — `dc-knw.md`에 7개 보안 규칙 추가: path traversal 방어(../ 거부), frontmatter injection 방어(--- 이스케이프, 고정 스키마), GUARD 출력 인용 블록 처리, .knw-queue/ 크기 제한(100파일/8KB). |
| **v2.0.45** | **Knowledge Registry (DC-KNW — 18번째 직원)** — `domangcha/knowledge-registry/` 5개 타입 폴더(error/pattern/decision/workflow/skill), `.knw-queue/` 승인 파이프라인, error-registry 시드 3개 엔트리, `/ceo-knowledge /ceo-learn /ceo-promote /ceo-forget` 명령어. DC-KNW가 CORE 에이전트로 매 PHASE 1마다 GUARD 모드 자동 실행 (advisory only). |
| **v2.0.44** | **전체 4개 스택 DOC-FIRST 강제화** — Ralph Loop: fix_plan.md Phase 0에 docs/ 생성 단계 추가, Superpowers: writing-plans → 승인 → DOC-FIRST → executing-plans → GATE → deploy 흐름 명시, gstack/Standard도 DOC-FIRST 표기 일관화. Knowledge Registry(DC-KNW 18번째 직원) 설계 완료 → v2.0.45에서 구현. |
| **v2.0.43** | **동적 스택 선택 루브릭** — PHASE 0.3에 12개 조건 × 4 스택 점수 테이블(`stack-selection-rubric.md`) 도입. 하드코딩 80/60/45/25 대신 업무 특성에 따라 점수 계산 → Standard 자동 1위 편향 제거. |
| **v2.0.42** | **갭분석 + §6 전체 전파** — `ceo-core/SKILL.md`와 `ceo-sprint/SKILL.md`에 §6 EXEC-001~004 추가. 버전 업데이트 절차에 `~/.claude/CLAUDE.md` 항목 명시 (3개 CLAUDE.md 전부). `ceo-system/SKILL.md` 버전 절차 6개→11개 확장 (`package.json` 및 루트 파일 누락 수정). |
| **v2.0.41** | **실행 신뢰성 원칙 §6** — 모든 CLAUDE.md에 4개 강제 규칙 추가: 완료 미검증 금지, 중간 멈춤 금지, CLI 직접 실행, 세션 리포트 필수. EXEC-001~004 error-registry 등록. GATE 2에 `04-completion-criteria.md` 라인별 체크리스트 강화. |
| **v2.0.40** | **Docs 경로 slug 동기화** — README 파이프라인 다이어그램 및 `rule_doc_first.md` 메모리 템플릿을 `YYYY-MM-DD-vX.X.X-<slug>/` 컨벤션으로 업데이트. package.json description 트림. |
| **v2.0.39** | **README + GitHub 브랜딩 개편** — 새 히어로 "DOMANGCHA 없는 Claude Code는 반쪽짜리", 기능 중심 포지셔닝, docs 폴더명 컨벤션 `YYYY-MM-DD-vX.X.X-<slug>`, npm keywords +4 추가. |
| **v2.0.38** | **메모리 동기화 Step 5로 이동** — Playwright/git-hooks 실패 전에 메모리 템플릿이 갱신됨. `set -e`로 인한 스킵 완전 차단. `rule_grand_principles.md` 템플릿 + `/ceo-update` 테이블 memory 항목 추가. |
| **v2.0.37** | **대원칙 (Karpathy)** — Andrej Karpathy의 4대 코딩 원칙을 모든 CLAUDE.md와 `coding-style.md`에 병합. Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution — DOMANGCHA 컨텍스트 적용. |
| **v2.0.36** | **npx 우선 업데이트** — `/ceo-update`, `/ceo-version`이 `npx domangcha`를 1순위, `curl \| bash`를 fallback으로 사용. bin 버전 싱크 + `curl -fsSL` 보안 플래그 통일. |
| **v2.0.35** | **DC-ANA (17번째 에이전트)** — DOMANGCHA 전용 내부 코드베이스 분석가. ECC code-explorer 기능 완전 흡수. 갭분석·리팩터링·LARGE/HEAVY 업무 시 자동 소환. `code-explorer`(ECC) 직접 호출 금지. |
| **v2.0.34** | **FAST PATH 경량 DOC** — 소규모 수정도 `00-summary.md` 자동 생성. 문서 없는 변경 원천 차단. |
| **v2.0.33** | **메모리 자동 동기화** — `npx domangcha` 업데이트 시 규칙 메모리 자동 갱신. 사용자 피드백/프로젝트 컨텍스트는 절대 덮어쓰지 않음. |
| **v2.0.31** | **트레이드오프 체크** — Q&A 및 구현 시작 전 CEO가 아키텍처 리스크와 부작용을 사전에 표면화. |
| **v2.0.30** | 에이전트 컬러 코딩 시스템 — 파이프라인 출력 전체에서 그룹 시각적 식별. |

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

| 명령어 | 동작 |
|---|---|
| `/ceo "[업무]"` | 🧭 DIRECT / LOOP / GRAPH 자동 라우팅 |
| `/ceo-ralph "[업무]"` | 🔁 최소 LOOP 강제, 안전상 필요하면 GRAPH 승격 |
| `/ceo-clarify` | 💬 의도·범위·완료 기준 명확화 |
| `/ceo-design` | 🧭 실제 복잡도에 따른 설계 워크플로 |
| `/ceo-doc` | 📝 문서 워크플로 |
| `/ceo-feature` | ✨ 범위에 따라 라우팅되는 기능 구현 |
| `/ceo-init` | 🔧 프로젝트 하네스 초기화 |
| `/ceo-debug "[버그]"` | 🐛 조사 → 수정 → 검증 |
| `/ceo-plan` | 🗺️ 계획 워크플로 |
| `/ceo-quality` | 📏 결정론적 품질 검사 |
| `/ceo-review` | 🔍 독립 품질·PR 리뷰 |
| `/ceo-security` | 🔐 보안 워크플로, 필요 시 GRAPH |
| `/ceo-test` | ✅ TDD + 단위 + E2E + 브라우저 QA |
| `/ceo-ship` | 📦 게이트 → 리뷰 → 빌드 → 배포 |
| `/ceo-status` | 📊 DIRECT 현황 조회 |
| `/ceo-update` | ⬆️ 보호된 인스톨러 업데이트 |
| `/ceo-version` | 🏷️ 결정론적 버전 일관성 검사 |
| `/ceo-knowledge "[검색어]"` | 🧠 ID 또는 키워드로 지식 레지스트리 검색 |
| `/ceo-learn "[패턴]"` | 📝 새 지식 항목을 검토 큐에 등록 |

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

| | |
|---|---|
| Claude Code 또는 OpenAI Codex | 지원 코딩 에이전트 런타임 하나 이상 |
| Python | 결정론적 엔진용 3.10 이상 |
| Node.js | npm 설치용 14 이상 |
| `git` | 설치·저장소 검사·리뷰 가능한 diff |

---

### 🚀 설치 · 업데이트

**방법 1 — npx (권장)**
```bash
npx domangcha
```

**방법 2 — curl**
```bash
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash
```

**방법 3 — 전역 설치**
```bash
npm install -g domangcha && domangcha
```

인스톨러를 다시 실행하면 항상 최신 버전을 가져옵니다. 레지스트리(에러, 본능, 히스토리)는 보존됩니다. `~/.claude/projects/*/memory/`의 규칙 메모리는 최신 버전 정의로 자동 갱신되며, 사용자 피드백/프로젝트 컨텍스트는 절대 덮어쓰지 않습니다.

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
