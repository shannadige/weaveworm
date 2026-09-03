---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Status:\\*\\* open\\s*$"
flags: m
match: contains
---
The user said not to hand it off yet. Handoff is the user's word, never assumed from the spec existing, so Status stays `open`.
