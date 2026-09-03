---
type: regex
target:
  source: file
  path: design/flows/F-001-*.md
pattern: "^- \\*\\*State:\\*\\*.*\\b(red|yellow|green|blue|bold|font|pixel|px|card grid|colou?r|icon)\\b"
flags: mi
match: not_contains
---
`State:` is content and behavior; visual style is prototype's call, made later.
