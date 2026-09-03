---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "^### T1 .*E-00[0-9]"
flags: m
match: contains
---
Themes are headed `### T<n> <claim> (E-NNN, E-NNN)` with the entry IDs inline. A theme sentence with no E-ID is an opinion, not a finding.
