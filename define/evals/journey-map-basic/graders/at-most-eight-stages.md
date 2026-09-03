---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "^### J-001\\.(9|[1-9][0-9])\\b"
flags: m
match: not_contains
---
No ninth stage. Finer grain belongs in a narrower-scoped journey.
