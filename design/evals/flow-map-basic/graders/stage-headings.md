---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^### F-001\\.[1-8] \\S"
flags: m
match: contains
---
Stages are headed `### F-001.<n> <name>` so prototype screens and test tasks can cite `F-001.3`.
