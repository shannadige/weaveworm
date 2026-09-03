---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*D-003\\*\\* .*reverses on: analysts who proceed on a flagged stale export re-pull it mid-close anyway"
flags: m
match: contains
---
Every standing decision the flow traces to appears under Must not change with its `Reverses on:` line verbatim; D-003 is the last and easiest to drop.
