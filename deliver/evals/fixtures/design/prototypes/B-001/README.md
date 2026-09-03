# Prototype — B-001

Opens from `index.html` with no build step. Styled as Ledgerline, the
finance team's own tool.

## Screens

| Screen | Renders | Decision |
|---|---|---|
| `check-page` | F-001.1, F-001.2 | D-001, D-002 |
| `stale-export` (panel on `check-page`) | F-001.3 | D-003 |
| `first-account` | F-001.4 | D-003 |
| `check-page` with no exports | Empty edge at F-001.1 | D-001 |
| `check-page` with an unreadable date | Error edge at F-001.1 | D-002 |

## Sample data

Every export date, balance, and account name on the screens is sample
data written for the test tasks. The close date shown (2026-08-31) and
the "usually about half a day" wait text are placeholders, not the
design. The rule sentence on the check page ("current when the export
is dated on or after the close date") is illustrative copy and has not
been promoted by any decision.

## Test seeds

1. Start the August close and tell me which exports you would trust
   to reconcile from right now. Success: the analyst names the stale
   bank export before opening any account.
2. The bank export is stale and the refresh is tonight. Get to your
   first account. Success: the analyst proceeds with the flag rather
   than stopping, and can say which accounts carry it.
