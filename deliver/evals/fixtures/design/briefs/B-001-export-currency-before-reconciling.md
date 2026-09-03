# B-001 Analysts know whether each pulled source export is current before they reconcile the first account
<!-- weaveworm design-brief v1 -->

- **Status:** reviewed (2026-08-28, → D-001)
- **Pulls:** O-001 (pursued 2026-08-22)
- **For:** U-001
- **Journey:** J-001.1, J-001.3
- **Moves:** OC-001
- **Charter:** agreed 2026-08-20
- **Constraints:**
  - The bank feed refreshes nightly and cannot be pulled on demand — given (bank integration contract)
  - No change to the ERP this year — given (finance systems roadmap 2026)
  - Currency is judged from the export the analyst already pulled, never by fetching the source again (brief) — given (bank integration contract)
- **Out of scope:** replacing the analysts' spreadsheets as the reconciliation surface (charter non-goal); shortening the wait for a re-requested ERP export (J-001.4 stays unchanged); showing the controller what was reconciled against what (O-002, not pursued)
- **Done when:** An analyst opening a close sees, for each of the three source exports, whether it is current for that close date before the first account is reconciled, and mid-close re-pulls per close fall toward the OC-001 target of 0.
- **Open questions:**
  - Whether the expense tool export is ever stale in the same way the bank feed is (charter open question)
  - What analysts do on a close day when the bank export is stale and the nightly refresh is hours away
