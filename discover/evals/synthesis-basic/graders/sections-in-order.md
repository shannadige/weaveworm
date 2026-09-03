---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "## Themes[\\s\\S]*## Contradictions[\\s\\S]*## Gaps[\\s\\S]*## Recommendations"
match: contains
---
Sections in the fixed order: Themes, Contradictions, Gaps, Recommendations. Recommendations last, so they read as downstream of findings.
