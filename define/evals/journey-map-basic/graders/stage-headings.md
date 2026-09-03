---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "^### J-001\\.[1-8] \\S"
flags: m
match: contains
---
Stages are headed `### J-001.<n> <name>` so opportunities can cite `J-001.4`.
