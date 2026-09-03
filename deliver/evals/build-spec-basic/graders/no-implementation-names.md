---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "\\b(endpoint|API|component|database|schema|SQL|JSON|React|CSS|hex|px)\\b"
match: not_contains
---
Check lines are what the user does and then sees, never implementation or visual style. Implementation words are the tell.
