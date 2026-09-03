---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "^### .*E-00[25].* vs\\.? .*E-00[25]"
flags: m
match: contains
---
E-005 (members see the notification, but after the deadline) carries `Contradicts: E-002` (members never see it). Both are in scope, so the Contradictions section must hold a `<claim A> (E-002) vs <claim B> (E-005)` heading with both sides cited.
