---
type: regex
target:
  source: file
  path: define/journeys/J-001-*.md
pattern: "\\b(wizard|Wizard|modal|Modal|AI|auto-[a-z]+|chatbot|assistant|dashboard|button)\\b"
match: not_contains
---
Future-state shifts describe what changes for the user, never the mechanism. Mechanism words are the tell.
