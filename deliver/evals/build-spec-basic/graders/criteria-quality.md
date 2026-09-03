---
type: llm
target:
  source: file
  path: deliver/specs/S-001-*.md
---
Judge the build spec against all of the following. Pass only if every point holds.

1. Criteria follow the flow in order: S-001.1 through S-001.4 correspond to F-001.1 (opens the close), F-001.2 (reads each export's currency), F-001.3 (handles a stale export), and F-001.4 (proceeds into reconciliation); then the error edge, the empty edge, and the open interrupted edge, in that order. Fail if a stage or edge is missing, merged, or out of order.
2. Every `Check:` line is a single observable statement of what the analyst does and what they then see. Fail if any Check line names a component, endpoint, table, event, or visual styling, or contains test code.
3. The error edge criterion cites D-002 and the empty edge criterion cites D-001, the decisions the flow's Edges lines name. Fail if either cites a different decision or none.
4. The open criterion's Check line says no handling is built and points at the stop condition that will settle it. Fail if it describes any handling.
5. Must not change lists D-001, D-002, and D-003, each with a `reverses on:` clause matching the decision log, and no decision the flow does not trace to.
6. The Stop conditions section carries the critique's Debt census finding (D-002's timestamp rule is untested) and the open edge, each phrased as a question in product terms with `— blocks S-001.N` or `— blocks none; informs <what>`. Fail if any item could only be answered by reading a spec, or lacks its blocks clause.
7. The `## For the builder` preamble tells the agent to build from the criteria and not the prototype's markup, to treat Must not change as fixed and stop rather than adapt, and to stop and ask at a stop condition rather than choose a default.
