---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "^### T[6-9]\\b"
flags: m
match: not_contains
---
At most five themes. Further clusters are counted and rolled into one line.
