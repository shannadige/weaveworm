---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "<!-- weaveworm synthesis v1 -->"
match: contains
---
The file carries the skill's marker comment, which is how later stages recognize a synthesis.
