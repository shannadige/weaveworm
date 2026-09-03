---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^### S-001\\.1 .+F-001\\.1 \\(D-001\\)"
flags: m
match: contains
---
Each criterion heading cites its flow stage and the decision behind it, in the spec's form `— F-001.1 (D-001)`.
