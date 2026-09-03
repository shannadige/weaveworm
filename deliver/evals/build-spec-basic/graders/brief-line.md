---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Brief:\\*\\* B-001 .{1,3} reviewed \\(2026-08-28"
flags: m
match: contains
---
`Brief:` records the status read at pull time, `reviewed (2026-08-28, → D-001)`, so the spec shows what it was built on.
