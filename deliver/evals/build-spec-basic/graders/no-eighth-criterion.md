---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^### S-001\\.(8|9|[1-9][0-9])\\b"
flags: m
match: not_contains
---
One criterion per stage and one per edge, nothing merged and nothing added: seven and no more.
