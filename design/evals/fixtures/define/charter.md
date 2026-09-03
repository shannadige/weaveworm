# Product charter — Ledgerline
<!-- weaveworm product-charter v1 -->

- **Status:** agreed (2026-08-20)
- **Owner:** head of product

## Challenges

### CH-001 The close slips because analysts discover stale source data after reconciliation has started
- **Evidence:** E-002, E-003
- **Corroborates:** E-001
- **Confidence:** medium — weakest load-bearing entry is E-003
- **Stakes:** high — carried from E-002

### CH-002 Controller review sends the close back because analysts cannot show what has been reconciled against what
- **Evidence:** E-005, E-006
- **Confidence:** medium — weakest load-bearing entry is E-005

## Vision
Analysts start every close knowing their source data is current, and controllers sign off on the first pass because the close shows its own work.

## Desired outcomes

### OC-001 Analysts know their source data is current before they begin reconciling
- **From:** CH-001
- **For:** U-001

### OC-002 The controller signs off on a close in one review pass
- **From:** CH-002
- **For:** U-002

## Success metrics
- **OC-001:** mid-close re-pulls per close — 1.4 (measured 2026-08-01) → 0 within two closes — E-002 shows every re-pull is a stale-data discovery
- **OC-002:** review round trips per close — 1.6 (measured 2026-08-01) → 1 within three closes — (ambition)
- **Guardrails:**
  - close duration in working days — currently 4.5
- **Instrumented by:** close-tracker export, monthly

## Constraints
- The bank feed refreshes nightly and cannot be pulled on demand — given (bank integration contract)
- No change to the ERP this year — given (finance systems roadmap 2026)

## Non-goals
- Replacing the analysts' spreadsheets as the reconciliation surface

## Open questions
- Whether the expense tool export is ever stale in the same way the bank feed is
