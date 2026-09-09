# DOMANGCHA Error Registry

The registry stores recurring failure classes; executable prevention belongs to validators and tests.

| ID | Failure class | Deterministic prevention |
|---|---|---|
| ERR-001 | Oversized hand-maintained source | line-limit validator with explicit exemptions |
| ERR-002 | Hard-coded secret | secret scan + checkpoint/log redaction |
| ERR-003 | Version/metadata drift | manifest and release-surface validator |
| ERR-004 | Builder is sole reviewer | execution-identity validator |
| ERR-005 | Unverified completion | route-specific validation evidence |
| ERR-006 | Infinite/no-progress retry | max attempts, budgets, progress hash, error fingerprint |
| ERR-007 | Duplicate side effect on retry | idempotency classification and receipts |
| ERR-008 | Prompt-controlled transition | structured result + deterministic edge guard |
| ERR-009 | Approval path bypass | graph path validation + HUMAN_GATE state |
| ERR-010 | Secret/path leakage in state | allowlisted state, redaction, workspace containment |
| ERR-011 | Whole-file rewrite for a one-value edit | edit config in place; a reformatted diff is a failed edit |

New failures are recorded as structured evidence first and curated after validation. A worker must not mutate this registry repeatedly during retries.
