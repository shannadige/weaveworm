---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^- \\*\\*Empty:\\*\\*.*not handled \\(open\\)"
flags: m
match: contains
---
The user said the first-close empty state is undesigned, so it is written open, never silent and never invented.
