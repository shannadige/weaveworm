---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "<!-- weaveworm journey-map v1 -->"
match: contains
---
The file carries the skill's marker comment, which is how later stages recognize a journey file.
