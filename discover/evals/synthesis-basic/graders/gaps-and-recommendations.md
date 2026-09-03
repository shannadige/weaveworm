---
type: llm
target:
  source: file
  path: research/synthesis/*.md
---
Judge the Gaps and Recommendations sections. Pass only if every point holds.

1. Gaps names at least one population the Q-001 evidence structurally missed. The plan's Risks line supplies two: members who already lapsed over missed firings, and studios that fire monthly rather than weekly. Either counts; a gap drawn from the screener (partner-studio members only, staff excluded) also counts.
2. Gaps names the `unplanned` entries as questions the plan never asked: E-006 (managers enter the schedule after loading) and E-007 (members ask firing status in the WhatsApp group), as seeds of a next question. Naming one of the two with its topic is enough.
3. Every recommendation has a `From:` line naming a theme (T1, T2, ...) and a `Cost if wrong:` line. Fail if any recommendation cites no theme, or follows from nothing in Themes.
4. No recommendation rests solely on a `low` confidence theme without saying so in the recommendation itself.
5. The Contradictions section says which side of E-002 vs E-005 is stronger and why (E-005 is observed timestamps confirmed by the manager; E-002 is self-report from three participants), and names what would settle it. Fail if the contradiction is resolved by silently dropping one side from the themes.
