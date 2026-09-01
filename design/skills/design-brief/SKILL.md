---
name: design-brief
description: "The first stage of design — turn a pursued O-NNN opportunity into a B-NNN design brief: the design's job as one problem-shaped sentence, with roles, journey moment, outcomes, and inherited constraints cited from define, never restated. Use when a designer says \"let's design this\", \"start on O-003\", \"write the design brief\", \"kick off design for the pursued opportunity\", or an opportunity was just marked pursued and they want next steps. Do NOT use for choosing what to pursue (use define's opportunity-map), exploring solutions (use concept-sprint), or recording design decisions (use decision-log)."
---

# design-brief

<!-- TODO: scaffold — body unwritten. House structure below; spec is
${CLAUDE_PLUGIN_ROOT}/references/design-spec.md (read before first
write in a session). -->

Input: a `pursued` block in `define/opportunities.md`, plus the
charter, roles, and journeys it cites. Output:
`design/briefs/B-NNN-<slug>.md` per the spec's brief format.
Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Brief rules

- TODO: pull only `pursued` blocks; the refusal/redirect path for
  open ones.
- TODO: cite, never restate — the brief points at `O-NNN`/`OC-NNN`/
  `U-NNN`/`J-NNN.S`; duplicated prose drifts.
- TODO: constraint inheritance from the charter; brief-local
  constraints and their marking.
- TODO: `Done when:` discipline — observable state tied to the
  outcome's metric, never a deliverable list.
- TODO: Non-goals gate at write time.
- TODO: assumption-led path (charter draft or absent).

## After the brief

- TODO: summary lines per the voice contract; force the decision —
  is this brief's
  scope one sprint or two, and what's the first concept question.

## What this skill refuses

- TODO: designing from an open (non-pursued) opportunity without the
  explicit override path.
- TODO: inventing constraints or restating upstream artifacts.
