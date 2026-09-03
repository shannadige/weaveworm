# Decisions
<!-- weaveworm decision-log v1 -->

## D-001 Currency is shown on one pre-close check page listing all three exports, before any account is opened
- **Brief:** B-001
- **Because:** the stale-data discovery happens well after reconciliation starts (E-002), and analysts already gather all three exports in one motion at kickoff (E-001), so the check belongs at that moment and nowhere later
- **Rejected:** C-002 — an inline warning on each account row surfaces staleness only after work has started, the moment E-002 says is already too late; C-003 — a source-by-source wizard adds steps to a kickoff analysts do in one pass (E-001)
- **Reverses on:** analysts skip the check page and open accounts directly in 2 or more of 6 test sessions
- **Confidence:** high — weakest load-bearing entry is E-001
- **Status:** standing

## D-002 An export counts as current when its own timestamp falls on or after the close date; the check never re-fetches a source
- **Brief:** B-001
- **Because:** the bank feed cannot be pulled on demand — given (bank integration contract) — and the ERP cannot change this year — given (finance systems roadmap 2026) — so the export's own timestamp is the only currency signal the build can read
- **Rejected:** querying each source live for its last refresh — impossible for the bank feed under the contract and an ERP change for the rest; asking the analyst to declare currency — E-002 shows they do not know until a balance fails to match
- **Reverses on:** an export whose timestamp is on or after the close date is still found stale during reconciliation, in any session or production close
- **Confidence:** (untested)
- **Status:** standing

## D-003 A stale export names its source and the wait a fresh one takes, and the analyst may proceed with it flagged rather than being blocked
- **Brief:** B-001
- **Because:** a re-requested ERP export takes roughly half a day (E-003), so blocking the close on currency turns a known wait into a stalled close; the flag keeps the staleness visible instead of silent
- **Rejected:** blocking reconciliation until all three exports are current — converts a half-day wait into a stalled close (E-003); proceeding silently — reproduces the June restatement (E-002)
- **Reverses on:** analysts who proceed on a flagged stale export re-pull it mid-close anyway in most observed closes
- **Confidence:** medium — weakest load-bearing entry is E-003
- **Status:** standing
