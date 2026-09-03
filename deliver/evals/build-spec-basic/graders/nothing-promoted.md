---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "promoted:"
match: not_contains
---
No decision promotes a rendering here (the README says the rule sentence and wait text are placeholders), so nothing may be promoted to normative.
