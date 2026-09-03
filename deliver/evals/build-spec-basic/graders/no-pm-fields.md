---
type: regex
target:
  source: file
  path: deliver/specs/S-001-*.md
pattern: "\\b(sprint|ticket|story points?|estimate[sd]?|Jira|assignee|owner:)\\b"
flags: i
match: not_contains
---
Tickets, estimates, owners, and sequencing belong to the team's tools; what ships first is slice-plan's.
