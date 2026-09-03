---
type: llm
target:
  source: file
  path: design/flows/F-001-*.md
---
Judge the flow file against all of the following. Pass only if every point holds.

1. Stages are the analyst's units of progress from opening the close to opening the first account (open the close, read the verdicts, proceed or wait, pull exports, start reconciling, or an equivalent breakdown), between three and eight of them. Fail if any stage is reconciliation work past the first account, which the user placed out of scope.
2. Every `Step:` is what the analyst does, and every `State:` is what the system shows as content and behavior (which sources, what verdict wording means, what proceeding records), never visual style or layout.
3. Every stage's `Decision:` traces to the decision that covers it: the kickoff readout and the exports-as-today stages to D-001 (the pick), the verdict wording stage to D-002 (current means covers the period end), the proceed-or-wait stage to D-003 (warn, never block). Fail if a stage cites a decision that does not cover what the stage does, or if a stage that plainly rests on one of these three reads `(needs one)`.
4. The Edges section has error, empty, and interrupted entries. The error edge (refresh date unreadable, shown as unknown, analyst may proceed) is anchored to a stage and traces to D-003 or another decision that covers it. The empty edge (first close, no history) reads `not handled (open)`. The interrupted edge (analyst returns later, verdicts re-checked) is anchored to the proceed-or-wait stage and cites a decision or `(needs one)`.
5. The flow delivers the brief's J-001.1 shift (the analyst knows before starting whether the pulled data is current): reading the flow, the analyst learns each source's currency before pulling any export.
6. No `State:` line touches the spreadsheet as a surface (the charter Non-goal); reconciliation stays where it is today.
