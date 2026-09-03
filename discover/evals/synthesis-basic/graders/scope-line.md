---
type: regex
target:
  source: file
  path: research/synthesis/*.md
pattern: "^Scope: .*Q-001.*log: 8 entries"
flags: m
match: contains
---
The header's Scope line names the question(s) synthesized and the log size at the time, so a reader can tell how stale the readout is. The log had eight entries.
