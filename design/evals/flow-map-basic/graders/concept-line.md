---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^- \\*\\*Concept:\\*\\* C-001 \\(.*D-001\\)"
flags: m
match: contains
---
The flow names the chosen concept and the decision that chose it; a flow drawn from an unchosen concept launders the pick.
