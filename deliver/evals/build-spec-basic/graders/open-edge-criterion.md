---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^### S-001\\.\\d+ interrupted( at F-001(\\.\\d+)?)? .{1,3} open"
flags: m
match: contains
---
The flow's `Interrupted: not handled (open)` becomes an open criterion headed by kind and stage with no decision cited, never a silence an agent would fill.
