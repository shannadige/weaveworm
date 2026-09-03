---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^- \\*\\*Decision:\\*\\* *(D-\\d{3}|\u2014 \\(needs one\\))"
flags: m
match: contains
---
Each stage's `Decision:` line names a `D-NNN` or reads `— (needs one)`.
