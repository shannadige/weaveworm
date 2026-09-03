# Decisions
<!-- weaveworm decision-log v1 -->

## D-001 Pick C-001: the analyst reads a currency readout at close kickoff, then proceeds as today
- **Brief:** B-001
- **Because:** E-002 shows the stale-data discovery happens mid-reconciliation; a readout at kickoff moves it before any account is opened without touching the ERP (given, finance systems roadmap 2026) or the spreadsheet (charter Non-goal). Editor's call: a readout beats a gate while the bank feed refreshes only nightly.
- **Rejected:** C-002 — surfaces staleness after work starts, which is the moment OC-001 exists to move; C-003 — a hard gate against a nightly-only refresh costs a day per stale feed
- **Reverses on:** 3 of 5 usability-test participants start reconciling with a source the readout showed as stale, without re-pulling it
- **Confidence:** (untested)
- **Status:** standing

## D-002 A source is "current" when its last refresh covers the period end, never when it is merely recent
- **Brief:** B-001
- **Because:** E-002: P4's feed was from Tuesday and the balances that failed were period-end balances; the analyst's question is "does this cover the period", not "is this from today". Editor's call on the wording.
- **Rejected:** showing only the raw refresh timestamp — leaves the analyst to do the date arithmetic on every close; comparing against the current time — flags a Friday-night refresh as stale on Monday morning when it is not
- **Reverses on:** a test participant reads "current" on a source that is stale for their close, or asks what "current" means
- **Confidence:** medium — weakest load-bearing artifact is O-001
- **Status:** standing

## D-003 A stale source warns and lets the analyst proceed; it never blocks the close
- **Brief:** B-001
- **Because:** The bank feed refreshes nightly and cannot be pulled on demand, given (bank integration contract), so a block costs a day; E-003 shows re-requests already cost half a day. Editor's call: an informed proceed beats a hard stop.
- **Rejected:** blocking until every source is current (C-003's gate) — costs a day per stale feed; proceeding with no warning — recreates the June restatement (E-002)
- **Reverses on:** a warned-and-proceeded close reaches the controller with a stale balance, repeating the June restatement pattern after the readout exists
- **Confidence:** (untested)
- **Status:** standing
