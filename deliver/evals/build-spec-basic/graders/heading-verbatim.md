---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^# S-001 Analysts know whether each pulled source export is current before they reconcile the first account .{1,3} B-001"
flags: m
match: contains
---
The heading is the brief's heading verbatim plus the brief ID, so the spec's job can't drift from the brief's.
