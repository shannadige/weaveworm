# J-001 Analyst, month-end close — close kickoff to controller's sign-off
<!-- weaveworm journey-map v1 -->
- **Role:** U-001
- **Scope:** From the analyst starting the close (pulling source exports) through the controller's sign-off, including the review round trip(s) in between.
- **State:** current+future

## Current state

### J-001.1 Pulls source data to kick off the close
- **Doing:** Manually exports data from the ERP, bank feed, and expense tool before starting reconciliation, observed in 5 of 6 usability sessions (E-001).
- **Friction:** The three systems don't connect to each other, so the analyst gathers everything by hand; P3: "Nothing talks to anything, so I go get it all myself." (E-001)

### J-001.2 Reconciles account by account while tracking progress outside the tool
- **Doing:** Reconciles in a spreadsheet and tracks which accounts are done in a personal checklist or notes file, observed in 4 of 6 sessions (E-006).
- **Friction:** Progress lives only in the analyst's own file; P2: "The tool doesn't know what's done, only I do." (E-006)

### J-001.3 Discovers stale bank data mid-reconciliation
- **Doing:** Finds balances that don't match and traces it to an outdated bank feed, observed in 3 of 6 sessions (E-002).
- **Friction:** The discovery happens well after starting, not before; P4: "I was forty minutes in before I realized the feed was from Tuesday." (E-002) Stakes are high: a stale feed reached a signed close in June and forced a restatement (E-002).

### J-001.4 Waits on a re-pulled export
- **Doing:** Re-requests the ERP export and waits; the ERP owner is often tied up in their own close (E-007).
- **Friction:** The wait runs roughly half a day; P2 and P5 described waiting "until after lunch" or "until the next morning" (E-003, medium confidence, self-reported by two participants, not observed directly). The ERP owner's unresponsiveness is a single anecdote (E-007, low confidence).

### J-001.5 Completes reconciliation and submits the close
- **Doing:** Finishes reconciling and submits the close to the controller (U-001's role block in roles.md; no session observed the submission itself).
- **Friction:** none observed (assumption).

### J-001.6 Answers the controller's questions on unreconciled balances
- **Doing:** Receives the close back from the controller and explains which accounts were reconciled against which source data (E-005, E-006).
- **Friction:** Review sends the close back at least once in most months; P6 (controller): "most closes at least once"; P2: "I plan for one round trip, sometimes two." (E-005, medium confidence, self-reported by two participants). The analyst cannot show what was reconciled against what without being asked, which is what triggers the round trip (E-005, E-006).

### J-001.7 Close is signed off
- **Doing:** Resubmits and the controller signs off after the review round trip(s) (U-002's role block in roles.md; no entry describes the sign-off moment itself).
- **Friction:** none observed (assumption).

## Future state

### Shifts
- **J-001.1:** The analyst knows, before starting reconciliation, whether the pulled source data is current, rather than finding out mid-work (OC-001 Analysts know their source data is current before they begin reconciling).
- **J-001.3:** The mid-reconciliation staleness discovery no longer happens; the analyst already knows at kickoff which sources are current and which are not (OC-001).
- **J-001.2:** What the analyst has reconciled, and against which source data, is visible beyond their own checklist (OC-002 The controller signs off on a close in one review pass).
- **J-001.6:** The controller's questions about what's reconciled are answered by what the close already shows, rather than requiring the analyst to explain after the fact (OC-002).
- **J-001.7:** The close is signed off in one review pass (OC-002).

### Unchanged
- **J-001.4:** Waiting on a re-pulled export stays as-is; no outcome in the charter addresses ERP turnaround time, and the bank feed refresh can't be pulled on demand (given: bank integration contract). Knowing about staleness earlier (J-001.1's shift) may reduce how often this wait is triggered, but doesn't shorten it when it is.
- **J-001.5:** Submission mechanics are unaddressed by the charter and stay as observed (assumption).
