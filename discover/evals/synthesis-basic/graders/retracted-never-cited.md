---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "^(###|- \\*\\*(From|Stronger|Confidence):\\*\\*).*E-004"
flags: m
match: not_contains
---
E-004 (the countdown "finding") is retracted in the log, so it is never load-bearing: it must not appear in a theme, contradiction, or recommendation heading, nor on a From, Stronger, or Confidence line. Naming it in Gaps as the reason a hole exists is allowed.
