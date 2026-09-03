# B-001 Analysts can tell, before reconciling a single account, whether each source export is current
<!-- weaveworm design-brief v1 -->

- **Status:** in-design (→ D-001)
- **Pulls:** O-001 (pursued 2026-08-24)
- **For:** U-001
- **Journey:** J-001.1, J-001.3
- **Moves:** OC-001
- **Charter:** agreed 2026-08-20
- **Constraints:**
  - The bank feed refreshes nightly and cannot be pulled on demand — charter constraint, given (bank integration contract)
  - No change to the ERP this year — charter constraint, given (finance systems roadmap 2026)
  - Nothing new for the analyst to install; the check has to reach them where they already start the close (brief) (assumption)
- **Out of scope:** Replacing the analysts' spreadsheets as the reconciliation surface (charter Non-goal); shortening the ERP owner's turnaround on re-requested exports (brief-local, no outcome covers it)
- **Done when:** An analyst starting a close can say, before opening the first account, whether each of the three sources is current, and mid-close re-pulls (the OC-001 metric) fall from 1.4 per close toward 0 within two closes
- **Open questions:** Is the expense tool export ever stale the way the bank feed is? (carried from the charter's open question)
