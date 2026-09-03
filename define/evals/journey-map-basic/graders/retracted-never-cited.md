---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "E-004"
match: not_contains
---
E-004 is retracted in the log and is never load-bearing, so the journey must not cite it.
