---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^# F-001 .* \u2014 B-001\\s*\\n<!-- weaveworm flow-map v1 -->\\s*\\n- \\*\\*Brief:\\*\\* B-001\\s*\\n- \\*\\*Role:\\*\\* U-001\\s*\\n- \\*\\*Journey:\\*\\* J-001\\.[13]"
flags: m
match: contains
---
The header carries the marker and cites the brief, the role, and the journey moment, in the spec's order.
