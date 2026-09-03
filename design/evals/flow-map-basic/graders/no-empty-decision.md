---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^- \\*\\*Decision:\\*\\* *$"
flags: m
match: not_contains
---
A blank `Decision:` line is a silence; the spec's honest gap is `— (needs one)`.
