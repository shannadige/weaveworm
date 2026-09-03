---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^### S-001\\.7 "
flags: m
match: contains
---
F-001 has four stages and three Edges lines, so the spec has exactly seven criteria; the seventh must exist.
