---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "<!-- weaveworm build-spec v1 -->"
match: contains
---
The file carries the skill's marker comment, which is how slice-plan, instrumentation-plan, and build-review recognize a spec.
