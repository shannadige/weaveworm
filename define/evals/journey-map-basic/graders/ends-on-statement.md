---
type: regex
target: last_message
pattern: '\?\s*$'
match: not_contains
---
The voice contract's Reporting section closes every run on the decision or next action stated as a statement, never a question. A reply whose last line ends in a question mark hands the decision back instead of forcing it.
