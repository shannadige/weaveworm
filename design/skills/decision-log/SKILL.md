---
name: decision-log
description: "The design stage's evidence log — record load-bearing design choices as D-NNN blocks in design/decisions.md: the decision in one sentence, its rationale (cited or labeled judgment), rejected alternatives, and what observation would reverse it; untested choices marked (untested) as seeds for usability testing. Use when a designer says \"log that decision\", \"why did we go this way\", \"record the tradeoff\", \"we decided X because Y\", reverses an earlier call, or another design skill needs a choice recorded. Do NOT use for recording research findings (use discover's evidence-log) or choosing between concepts without the sprint (use concept-sprint)."
---

# decision-log

<!-- TODO: scaffold — body unwritten. House structure below; spec is
${CLAUDE_PLUGIN_ROOT}/references/design-spec.md (read before first
write in a session). -->

Input: a design choice — from concept-sprint, flow-map, prototype, or
the user directly. Output: `design/decisions.md` per the spec's
decision block format.

## Logging rules

- TODO: the load-bearing bar — what earns a block vs. what stays in
  the artifact; failure modes on both sides.
- TODO: `Because:` discipline — cited evidence, inherited constraint,
  or judgment labeled as judgment; never retro-fitted rationale.
- TODO: `Reverses on:` as a falsifiability line — every decision
  names its overturning observation.
- TODO: `(untested)` marking and how it clears (only through
  discover's loop, never by assertion).
- TODO: reversal discipline — `reversed (→ D-NNN)`, never edits;
  dependent-sweep of flows/prototypes citing the reversed block.
- TODO: confidence inheritance — a decision never more confident
  than the opportunity it serves.

## After the log

- TODO: chat summary; surface the `(untested)` census when it grows.

## What this skill refuses

- TODO: laundering taste into rationale; logging without a
  `Reverses on:` line.
- TODO: deleting or renumbering blocks.
