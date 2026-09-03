---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Prototype:\\*\\*.*normative:.*incidental:"
flags: m
match: contains
---
The prototype line always draws the normative/incidental line explicitly, even when nothing is promoted. It is what stops an agent shipping the scaffolding.
