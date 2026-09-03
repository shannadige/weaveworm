---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "\\*\\*Confidence:\\*\\* assumption-led"
match: not_contains
---
The header's assumption-led bullet is required only when the journey is wholly uncited. This journey has evidence, so the bullet must be absent.
