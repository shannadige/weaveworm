---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^## Edges\\s*\\n[\\s\\S]*^- \\*\\*Error:\\*\\* at F-001\\.\\d[\\s\\S]*^- \\*\\*Empty:\\*\\*[\\s\\S]*^- \\*\\*Interrupted:\\*\\* at F-001\\.\\d"
flags: m
match: contains
---
The Edges section is required, with error, empty, and interrupted at minimum, each handled edge anchored to the stage it branches from.
