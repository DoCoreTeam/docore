<div align="center"><pre>
██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██║  ██║██╔══██╗
██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║      ███████║███████║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║      ██╔══██║██╔══██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╗ ██║  ██║██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
</pre></div>

<div align="center">

### 🚗💨 DOMANGCHA — 18-Agent Harness for Claude Code

**Claude Code without DOMANGCHA is half the toolkit.**
One command orchestrates 18 AI specialists: spec → code → tests → security → review → ship.

*Your AI getaway car from development hell.*

[![Version](https://img.shields.io/badge/version-2.0.58-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Required-5865F2?style=for-the-badge)](https://claude.ai/code)
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
# Then, inside Claude Code:
/ceo "Build a Stripe invoicing tool for freelancers — invoices, email, paid/overdue dashboard"
```

</div>

---

## ⚡ Why DOMANGCHA?

Claude Code is powerful — but routing work between tools, enforcing quality gates, and keeping 18 workflows consistent adds real overhead. **DOMANGCHA eliminates that**: one command routes through **PLANNER → GENERATOR → EVALUATOR**, runs agents in parallel, and gates every output before shipping.

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
└── "Hold on — I have questions"
    └── 12 sharp questions
        └── Risk check → 18 specialists
            → 5 gates → ship
```

</td>
</tr>
</table>

| | DOMANGCHA | Typical AI tool |
|---|:---:|:---:|
| Requirements before code | ✅ Up to 12 questions | ❌ Codes immediately |
| Tradeoff check before building | ✅ Catches risks upfront | ❌ None |
| Role separation by specialist | ✅ 18 agents, parallel | ❌ Single model |
| Builder ≠ Reviewer (enforced) | ✅ Always | ❌ None |
| Breaking-change protection | ✅ Gate 5 blocks | ❌ None |
| Mistakes → permanent patterns | ✅ error-registry | ❌ None |
| Rule memory auto-sync on update | ✅ v2.0.33 | ❌ None |

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

[CEO SIZE ASSESSMENT]
Task:   Freelancer invoicing tool (Stripe + email + status dashboard)
Rating: MEDIUM  →  FULL PIPELINE

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

[CEO SIZE ASSESSMENT]
Task:   Fix webhook signature verification / status update bug
Rating: SMALL  →  FAST PATH  (1-2 files, no schema change, confirmed reproduction path)

[FAST PATH]
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

[CEO FAST REPORT] ⚡ Done in 4 minutes.
  1 file changed (2-line fix) · Stripe webhook now verifies correctly · Status flips live
```

**One bug, one function, four minutes. The rest of the codebase didn't move.**

---

## 🔄 Pipeline

```
/ceo "Build a Stripe invoicing tool for freelancers"
           │
           ▼
    ┌─────────────────┐
    │  INTENT PARSE   │  Every input → structured [INTENT PARSED] block
    └────────┬────────┘
             │  Input / Parsed / Goal / Scope / Context
             ▼
    ┌──────────────────┐
    │ TRADEOFF CHECK   │  CEO scans for risks before any code is written
    └────────┬─────────┘
             │  ✅ CLEAR → proceed   ⚠️ DETECTED → show risks + 4 options
             ▼
    ┌─────────────┐
    │  STACK SEL  │  CEO analyzes your task and recommends the best stack
    └──────┬──────┘
           │  [1] Standard    ████████ 80%  18 agents, full pipeline
           │  [2] Ralph Loop  ██████   60%  autonomous until done
           │  [3] gstack      ████     40%  web E2E + browser QA
           │  [4] Superpowers ██       25%  design-first, plan-heavy
           ▼
    ┌─────────────┐
    │    Q & A    │  Up to 12 questions — adaptive, one at a time
    └──────┬──────┘
           │  Stack? Done criteria? External APIs? Auth? Deploy target?
           ▼
    ┌──────────────────┐
    │  TASK SYNTHESIS  │  Q&A answers → structured [TASK REFINED] block
    └────────┬─────────┘
             │  Final task / Done criteria / Out-of-scope locked
             ▼
    ┌─────────────┐
    │  DOC-FIRST  │  ← IMMUTABLE RULE — all stacks, no exceptions
    └──────┬──────┘
           │  docs/YYYY-MM-DD-vX.X.X-<slug>/
           │  ├── 00-requirements.md         functional + non-functional reqs
           │  ├── 01-architecture.md         system design, data flow
           │  ├── 02-task-breakdown.md       tasks + priority P0/P1/P2
           │  ├── 03-test-strategy.md        test strategy + security criteria
           │  └── 04-completion-criteria.md  done condition + exit + rollback
           │  ↳ Planner self-checks for gaps → asks user if needed → [DOC COMPLETE]
           ▼
    ┌─────────────┐
    │   PLANNER   │  DC-BIZ · DC-RES · DC-OSS · DC-KNW  (parallel)
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │   BUILDER   │  DB · BE · FE · OPS · DOC  (parallel CORE)
    └──────┬──────┘  + MOB · INT · WRT · SEO   (added on demand)
           │  implement → ripple analysis → review  (max 3 loops)
           ▼
    ┌─────────────┐
    │  EVALUATOR  │  DC-QA + DC-SEC + DC-REV   (simultaneous)
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │  GATE 1–5   │  All must pass before ship
    └──────┬──────┘
           ▼
        🚀 SHIP
```

---

## 👥 The 18 Agents

<table>
<thead>
<tr><th>Phase</th><th>Agent</th><th>Role</th><th>Model</th></tr>
</thead>
<tbody>
<tr><td rowspan="5"><b>🧠 PLANNER</b></td>
  <td><code>DC-BIZ</code></td><td>Business Judge</td><td>Opus</td></tr>
<tr><td><code>DC-RES</code></td><td>Researcher</td><td>Sonnet</td></tr>
<tr><td><code>DC-OSS</code></td><td>OSS Scout</td><td>Opus</td></tr>
<tr><td><code>DC-ANA</code></td><td>Codebase Analyst</td><td>Sonnet</td></tr>
<tr><td><code>DC-KNW</code></td><td>Knowledge Curator</td><td>Sonnet</td></tr>
<tr><td rowspan="9"><b>🔨 BUILDER</b></td>
  <td><code>DC-DEV-DB</code></td><td>Database Engineer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-BE</code></td><td>Backend Developer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-FE</code></td><td>Frontend Developer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-OPS</code></td><td>DevOps Engineer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-MOB</code></td><td>Mobile Developer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-INT</code></td><td>Integration Engineer</td><td>Sonnet</td></tr>
<tr><td><code>DC-DOC</code></td><td>Documentation Writer</td><td>Haiku</td></tr>
<tr><td><code>DC-WRT</code></td><td>Copywriter</td><td>Haiku</td></tr>
<tr><td><code>DC-SEO</code></td><td>SEO / AEO / GEO</td><td>Haiku</td></tr>
<tr><td rowspan="3"><b>🔍 EVALUATOR</b></td>
  <td><code>DC-QA</code></td><td>QA Engineer</td><td>Sonnet</td></tr>
<tr><td><code>DC-SEC</code></td><td>Security Reviewer</td><td>Opus</td></tr>
<tr><td><code>DC-REV</code></td><td>Code Reviewer</td><td>Opus</td></tr>
<tr><td><b>⚙️ SUPPORT</b></td>
  <td><code>DC-TOK</code></td><td>Token Optimizer</td><td>Haiku</td></tr>
</tbody>
</table>

> **CORE** (runs every sprint) — BIZ, RES, OSS, KNW, DB, BE, FE, OPS, QA, SEC, REV, DOC, TOK  
> **EXTENDED** (added on demand) — ANA, MOB, INT, WRT, SEO

---

## 🛡️ The 5 Gates

> Every output must pass **all five**. No exceptions.

| Gate | Check |
|:---:|---|
| **① SCAN** | error-registry pattern scan + **300-line file limit (auto-blocked)** |
| **② CRITERIA** | All completion criteria verified 100% |
| **③ VERSION** | Version tag matches `domangcha/VERSION` |
| **④ SEPARATION** | Builder ≠ Reviewer — always enforced |
| **⑤ BREAKING** | Breaking changes blocked without **explicit user approval** |

---

## 🆕 What's New

| Version | Feature |
|---|---|
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

Every command triggers the multi-agent system to orchestrate tasks across planning, building, quality, and deployment phases.

| Command | What it does |
|---|---|
| `/ceo "[task]"` | 🚀 Full pipeline — version check → Q&A → 18 agents → GATE → ship |
| `/ceo-ralph "[task]"` | 🔁 Autonomous loop until completion criteria met |
| `/ceo-init` | 🔧 Project harness setup |
| `/ceo-debug "[bug]"` | 🐛 Investigate → fix → verify |
| `/ceo-review` | 🔍 Security + quality + PR review |
| `/ceo-test` | ✅ TDD + unit + E2E + browser QA |
| `/ceo-ship` | 📦 Gate → review → build → deploy |
| `/ceo-status` | 📊 Show current status |
| `/ceo-knowledge "[query]"` | 🧠 Search knowledge registry by ID or keyword |
| `/ceo-learn "[pattern]"` | 📝 Stage new knowledge entry to review queue |
| `/ceo-promote` | ✅ Promote queued entries to registry after review |
| `/ceo-forget KNW-ID` | 🗑️ Remove a knowledge entry from the registry |

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

DOMANGCHA is a developer tool built for Claude Code users who want AI-driven automation and multi-agent coordination without manual orchestration.

| | |
|---|---|
| [Claude Code](https://claude.ai/code) | Required |
| Anthropic API Key | Opus + Sonnet + Haiku access |
| `git` | For installer |

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

### 🚗💨 돔황차 — Claude Code용 18개 에이전트 하네스

**DOMANGCHA 없는 Claude Code는 반쪽짜리입니다.**
명령 하나로 18명 AI 전문가를 오케스트레이션 — 기획 → 구현 → 테스트 → 보안 → 리뷰 → 배포까지.

*개발 지옥에서 도망쳐 — 돔황차🚗💨*

[![Version](https://img.shields.io/badge/version-2.0.58-brightgreen?style=for-the-badge&logo=github)](https://github.com/DoCoreTeam/domangcha/blob/main/domangcha/VERSION)
[![npm](https://img.shields.io/npm/v/domangcha?style=for-the-badge&logo=npm&color=CB3837)](https://www.npmjs.com/package/domangcha)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-필수-5865F2?style=for-the-badge)](https://claude.ai/code)
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

Claude Code는 강력하지만 — 작업 배분, 품질 게이트 강제, 18개 워크플로 일관성 유지에는 오버헤드가 생깁니다. **DOMANGCHA가 그걸 없애줍니다**: 명령 하나로 **PLANNER → GENERATOR → EVALUATOR**를 병렬 실행하고, 모든 산출물을 게이트 후 배포합니다.

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
└── "잠깐, 질문이 있어요"
    └── 12개 핵심 질문
        └── 리스크 체크 → 18명 전문가
            → 5 게이트 → 출시
```

</td>
</tr>
</table>

| | DOMANGCHA | 일반 AI 도구 |
|---|:---:|:---:|
| 코드 전 요구사항 분석 | ✅ 최대 12개 질문 | ❌ 바로 코딩 |
| 구현 전 트레이드오프 체크 | ✅ 리스크 사전 발굴 | ❌ 없음 |
| 전문가 역할 분리 | ✅ 18명 병렬 운영 | ❌ 단일 모델 |
| 빌더 ≠ 리뷰어 강제 | ✅ 항상 분리 | ❌ 없음 |
| 파괴적 변경 보호 | ✅ Gate 5 차단 | ❌ 없음 |
| 실수 → 영구 패턴 등록 | ✅ error-registry | ❌ 없음 |
| 업데이트 시 규칙 메모리 자동 갱신 | ✅ v2.0.33 | ❌ 없음 |

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

[CEO 규모 판정]
업무:   러닝 크루 관리 (카카오페이 + 출석 + 대시보드)
판정:   MEDIUM  →  FULL PIPELINE

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

[CEO 규모 판정]
업무:   카카오페이 webhook 상태 업데이트 버그 수정
판정:   SMALL  →  FAST PATH  (1-2 파일, 스키마 변경 없음, 재현 경로 확인됨)

[FAST PATH]
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

[CEO FAST 리포트] ⚡ 5분 완료.
  수정 1개 파일 (3줄) · 카카오 재시도 webhook 정상 처리 · 납부 상태 즉시 반영
```

**버그 하나, 파일 하나, 5분. 나머지 코드는 손대지 않았다.**

---

### 🆕 최신 업데이트

| 버전 | 기능 |
|---|---|
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

### 🔄 파이프라인

```
/ceo "프리랜서용 Stripe 인보이스 툴 만들어줘"
           │
           ▼
    ┌───────────────────┐
    │  인텐트 파싱      │  모든 입력 → 구조화된 [INTENT PARSED] 블록 출력
    └────────┬──────────┘
             │  원본 / 정제 / 목표 / 범위 / 전제
             ▼
    ┌──────────────────┐
    │  트레이드오프 체크│  CEO가 구현 전 리스크를 스캔
    └────────┬─────────┘
             │  ✅ 이상 없음 → 진행   ⚠️ 위험 감지 → 리스크 + 4가지 선택지 제시
             ▼
    ┌─────────────┐
    │  스택 선택  │  CEO가 업무 분석 후 최적 스택 추천
    └──────┬──────┘
           │  [1] 스탠다드    ████████ 80%  18명 풀 파이프라인 (기본)
           │  [2] 랄프루프    ██████   60%  완료 기준 정의 후 자율 반복
           │  [3] gstack     ████     40%  웹 E2E + 브라우저 QA 강화
           │  [4] 슈퍼파워   ██       25%  설계 중심, 계획 먼저
           ▼
    ┌─────────────┐
    │    Q & A    │  최대 12개 질문 (한 번에 하나씩, 적응형)
    └──────┬──────┘
           │  스택? 완료 기준? 외부 API? 인증? 배포?
           ▼
    ┌──────────────────┐
    │  태스크 정제      │  Q&A 답변 → 구조화된 [TASK REFINED] 블록 출력
    └────────┬─────────┘
             │  최종 태스크 / 완료 조건 / 제외 범위 확정
             ▼
    ┌─────────────┐
    │  문서 먼저  │  ← 절대 불변 — 어떤 스택이든, 예외 없음
    └──────┬──────┘
           │  docs/YYYY-MM-DD-vX.X.X-<slug>/
           │  ├── 00-requirements.md        기능/비기능 요구사항
           │  ├── 01-architecture.md        시스템 설계, 데이터 흐름
           │  ├── 02-task-breakdown.md      태스크 목록 + 우선순위(P0/P1/P2)
           │  ├── 03-test-strategy.md       테스트 전략 + 보안/보완 기준
           │  └── 04-completion-criteria.md 완료 조건 · 종료 기준 · 롤백 기준
           │  ↳ 기획자 자가점검 → 갭 발견 시 추가 질문 → [DOC COMPLETE]
           ▼
    ┌─────────────┐
    │    기  획   │  DC-BIZ · DC-RES · DC-OSS · DC-KNW  (병렬)
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │    빌  드   │  DB · BE · FE · OPS · DOC  (병렬 CORE)
    └──────┬──────┘  + 모바일 · 연동 · 카피 · SEO  (필요 시 추가)
           │  구현 → 파급 분석 → 리뷰  (최대 3회 반복)
           ▼
    ┌─────────────┐
    │    평  가   │  DC-QA + DC-SEC + DC-REV   (동시 진행)
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │  게이트 1-5 │  전부 통과해야 출시
    └──────┬──────┘
           ▼
        🚀 출시
```

---

### 👥 18명의 에이전트

<table>
<thead>
<tr><th>단계</th><th>에이전트</th><th>역할</th><th>모델</th></tr>
</thead>
<tbody>
<tr><td rowspan="5"><b>🧠 기획자</b></td>
  <td><code>DC-BIZ</code></td><td>사업 타당성 판단</td><td>Opus</td></tr>
<tr><td><code>DC-RES</code></td><td>기술 리서치</td><td>Sonnet</td></tr>
<tr><td><code>DC-OSS</code></td><td>오픈소스 도구 탐색</td><td>Opus</td></tr>
<tr><td><code>DC-ANA</code></td><td>코드베이스 분석가</td><td>Sonnet</td></tr>
<tr><td><code>DC-KNW</code></td><td>지식 레지스트리 큐레이터</td><td>Sonnet</td></tr>
<tr><td rowspan="9"><b>🔨 빌더</b></td>
  <td><code>DC-DEV-DB</code></td><td>데이터베이스 엔지니어</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-BE</code></td><td>백엔드 개발자</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-FE</code></td><td>프론트엔드 개발자</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-OPS</code></td><td>DevOps 엔지니어</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-MOB</code></td><td>모바일 개발자</td><td>Sonnet</td></tr>
<tr><td><code>DC-DEV-INT</code></td><td>통합(Integration) 엔지니어</td><td>Sonnet</td></tr>
<tr><td><code>DC-DOC</code></td><td>문서 작성자</td><td>Haiku</td></tr>
<tr><td><code>DC-WRT</code></td><td>카피라이터</td><td>Haiku</td></tr>
<tr><td><code>DC-SEO</code></td><td>SEO / AEO / GEO</td><td>Haiku</td></tr>
<tr><td rowspan="3"><b>🔍 평가자</b></td>
  <td><code>DC-QA</code></td><td>QA 엔지니어</td><td>Sonnet</td></tr>
<tr><td><code>DC-SEC</code></td><td>보안 리뷰어</td><td>Opus</td></tr>
<tr><td><code>DC-REV</code></td><td>코드 리뷰어</td><td>Opus</td></tr>
<tr><td><b>⚙️ 지원</b></td>
  <td><code>DC-TOK</code></td><td>토큰 예산 관리</td><td>Haiku</td></tr>
</tbody>
</table>

> **CORE** (매 스프린트 가동) — BIZ, RES, OSS, KNW, DB, BE, FE, OPS, QA, SEC, REV, DOC, TOK  
> **EXTENDED** (필요 시 추가) — ANA, MOB, INT, WRT, SEO

---

### 🛡️ 5개의 게이트

> 모든 산출물은 **다섯 개를 전부** 통과해야 합니다. 예외 없음.

| 게이트 | 검증 항목 |
|:---:|---|
| **① 스캔** | error-registry 패턴 스캔 + **300줄 초과 파일 자동 차단** |
| **② 기준** | 모든 완료 기준 충족 100% 검증 |
| **③ 버전** | 버전 태그 = `domangcha/VERSION` 일치 확인 |
| **④ 분리** | 빌더 ≠ 리뷰어 — 항상 강제 |
| **⑤ 파괴** | 파괴적 변경 → **사용자 명시 승인 없으면 차단** |

---

### 🖥️ 명령어

| 명령어 | 동작 |
|---|---|
| `/ceo "[업무]"` | 🚀 전체 파이프라인 — Q&A → 18명 → GATE → 출시 |
| `/ceo-ralph "[업무]"` | 🔁 완료 기준 충족까지 자율 반복 루프 |
| `/ceo-init` | 🔧 프로젝트 하네스 초기화 |
| `/ceo-debug "[버그]"` | 🐛 조사 → 수정 → 검증 |
| `/ceo-review` | 🔍 보안 + 품질 + PR 리뷰 |
| `/ceo-test` | ✅ TDD + 단위 + E2E + 브라우저 QA |
| `/ceo-ship` | 📦 게이트 → 리뷰 → 빌드 → 배포 |
| `/ceo-status` | 📊 현황 조회 |
| `/ceo-knowledge "[검색어]"` | 🧠 ID 또는 키워드로 지식 레지스트리 검색 |
| `/ceo-learn "[패턴]"` | 📝 새 지식 항목을 검토 큐에 등록 |
| `/ceo-promote` | ✅ 검토 완료된 항목을 레지스트리로 승격 |
| `/ceo-forget KNW-ID` | 🗑️ 지식 레지스트리 항목 삭제 |

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
| [Claude Code](https://claude.ai/code) | 필수 |
| Anthropic API 키 | Opus + Sonnet + Haiku 액세스 |
| `git` | 인스톨러용 |

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
