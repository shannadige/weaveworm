---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^## Stop conditions"
flags: m
match: contains
---
For an agent recipient the Open section is headed `## Stop conditions`: what the agent may not decide alone.
