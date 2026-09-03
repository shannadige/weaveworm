# Roles
<!-- weaveworm user-roles v1 -->

## U-001 Analyst, month-end close
- **Kind:** user
- **Does:** pulls exports from the ERP, bank feed, and expense tool; reconciles account by account in a spreadsheet; tracks progress in a personal checklist; submits the close to the controller
- **Needs:** current source data before starting, and a way to show what has been reconciled
- **Goals:** a close that is signed off in one pass, without restating anything after the fact
- **Evidence:** E-001, E-002, E-006
- **Corroborates:** E-003
- **Confidence:** high — weakest load-bearing entry is E-001
- **Voices:** P1, P2, P3, P4, P5

## U-002 Controller
- **Kind:** stakeholder
- **Does:** reviews the submitted close, questions unreconciled or unexplained balances, signs off or sends it back
- **Needs:** to see which accounts were reconciled against which source data, without asking
- **Goals:** sign off with confidence that nothing in the close is stale
- **Evidence:** E-005
- **Confidence:** medium — weakest load-bearing entry is E-005
- **Voices:** P6
- **Distinct from:** U-001 — reviews and signs the close rather than assembling it; holds veto over submission
