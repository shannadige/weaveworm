---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Decisions:\\*\\* through D-003"
flags: m
match: contains
---
The pin is the highest decision the brief's artifacts trace to (D-003). Every downstream skill measures staleness against it.
