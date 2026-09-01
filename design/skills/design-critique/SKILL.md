---
name: design-critique
description: "The gate stage of design — run a dated critique pass over a brief's artifacts against fixed lenses: charter constraints violated, non-goals crept into, journey shifts dropped or contradicted, roles unserved, decisions untraced, (untested) choices counted. Verdicts per lens with cited IDs, never a score. Use when a designer says \"critique this\", \"review the design\", \"does this hold up\", \"are we still on charter\", or before handing work to testing or delivery. Do NOT use for code review, reviewing research instruments (use discover), or fixing what it finds (route fixes through the owning skill)."
---

# design-critique

<!-- TODO: scaffold — body unwritten. House structure below; spec is
${CLAUDE_PLUGIN_ROOT}/references/design-spec.md (read before first
write in a session). -->

Input: a brief and every design artifact citing it, plus the charter,
journeys, and roles upstream. Output:
`design/critiques/<date>-B-NNN.md` per the spec's critique format.
Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Critique rules

- TODO: fixed lenses, run in order; findings cite IDs; verdict per
  lens, never a composite score.
- TODO: dated and immutable — a critique is a record, never edited;
  the next pass is a new file.
- TODO: findings route to owners — constraint violations to the
  brief/decision, dropped shifts to flow-map, untraced screens to
  decision-log; critique names, never fixes.
- TODO: the `(untested)` census — count, stakes-weight, and the
  cheapest test per high-stakes item.
- TODO: whether critique gates a brief status transition or stays
  advisory (open decision in the spec).

## After the critique

- TODO: summary lines per the voice contract — verdicts one line per
  lens; force the decision: fix, test, or accept each finding, named
  per finding.

## What this skill refuses

- TODO: scoring; editing artifacts it critiques; softening a
  violation into a suggestion.
