---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^### F-001\\.(9|[1-9][0-9])\\b"
flags: m
match: not_contains
---
No ninth stage. Finer grain belongs in a narrower-scoped flow.
