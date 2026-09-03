---
type: llm
target:
  source: file
  path: research/synthesis/*.md
---
Judge the Themes section against the log's confidence levels: E-001 high, E-002 medium (Stakes high), E-003 medium, E-005 high, E-006 high, E-007 low, E-008 medium. Pass only if every point holds.

1. Every theme's stated confidence equals the lowest level among the entries its heading cites. A theme citing E-002, E-003, or E-008 is at most `medium`; a theme citing E-007 is `low`. Fail on any theme rated above its weakest cited entry.
2. Each theme's confidence line names the weakest entry ("weakest cited entry is E-008" or equivalent).
3. Any theme that cites E-002 states both its confidence and that the stakes are high (a missed bisque firing costs two weeks and members have lapsed over it), so a medium label cannot read as low importance.
4. No theme rests on a single entry. A theme is two or more entries pointing the same way.
5. No claim appears in a theme that is not in the log. Fail if a theme asserts something no cited entry says (for example that the app's notification design is at fault, which no entry establishes).
