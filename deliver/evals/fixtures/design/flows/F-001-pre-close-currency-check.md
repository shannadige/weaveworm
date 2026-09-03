# F-001 Pre-close currency check — B-001
<!-- weaveworm flow-map v1 -->
- **Brief:** B-001
- **Role:** U-001
- **Journey:** J-001.1, J-001.3
- **Concept:** C-001 (→ D-001)

### F-001.1 Opens the close
- **Step:** The analyst opens the month's close from the close list.
- **State:** A check page for that close date lists the three source exports (ERP, bank feed, expense tool), each with the date it was taken and whether it is current for this close.
- **Decision:** D-001

### F-001.2 Reads each export's currency
- **Step:** The analyst reads the currency line for each export.
- **State:** Each export reads current or stale, judged from the export's own timestamp against the close date, and the page states that rule in one line the analyst can read.
- **Decision:** D-002

### F-001.3 Handles a stale export
- **Step:** The analyst chooses what to do about an export that reads stale.
- **State:** The stale export is named with the wait a fresh one usually takes for that source, and the analyst can wait for it or proceed with the export flagged as stale.
- **Decision:** D-003

### F-001.4 Proceeds into reconciliation
- **Step:** The analyst confirms the check and moves to the first account.
- **State:** Reconciliation opens with any stale export still carrying its flag, visible on every account that draws on it until a fresh export replaces it.
- **Decision:** D-003

## Edges
- **Error:** at F-001.1 — an export on file has no readable timestamp: it reads unknown currency, names the file it came from, and is treated as stale from then on (D-002)
- **Empty:** at F-001.1 — no export has been pulled for this close yet: all three sources read not yet pulled, and the analyst cannot move to accounts until at least one export is on file (D-001)
- **Interrupted:** not handled (open)
