---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Done when:\\*\\* An analyst opening a close sees, for each of the three source exports, whether it is current for that close date before the first account is reconciled.*\\(B-001\\)"
flags: m
match: contains
---
`Done when:` is the brief's line copied verbatim with its citation, because the builder reads this file and not the brief.
