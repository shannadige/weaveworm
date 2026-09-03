---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "^- \\*\\*Recipient:\\*\\* agent"
flags: m
match: contains
---
The user named a coding agent as the recipient, which selects the preamble and the Open section's heading.
