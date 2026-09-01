---
name: flow-map
description: "The articulation stage of design — turn a brief's chosen concept into F-NNN flow files: numbered stages of user step, system state, and edge paths, each stage traced to the D-NNN decision behind it and to the J-NNN.S journey moment it redesigns. Use when a designer says \"map the flow\", \"what are the steps\", \"detail the happy path\", \"what happens when it fails\", or a concept was just chosen and they want it concrete. Do NOT use for current-state journeys (use define's journey-map), choosing the concept (use concept-sprint), or building screens (use prototype)."
---

# flow-map

<!-- TODO: scaffold — body unwritten. House structure below; spec is
${CLAUDE_PLUGIN_ROOT}/references/design-spec.md (read before first
write in a session). -->

Input: a brief with a chosen concept (`D-NNN`), the journey it
redesigns. Output: `design/flows/F-NNN-<slug>.md` per the spec's flow
format. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Mapping rules

- TODO: one flow per brief × scope; stage cap and the
  narrower-scope escape hatch (mirroring journey-map).
- TODO: `State:` as content and behavior, never visual style.
- TODO: edge discipline — error/empty/interrupted paths; where
  they're mandatory.
- TODO: stage-to-decision tracing — a stage no decision covers gets
  one routed through decision-log, not an inline improvisation.
- TODO: the shift check — the flow must deliver the `J-NNN.S` shift
  the brief cites, or name why it diverged.
- TODO: supersession — materially changed flow is a fresh `F-NNN`
  with dependent-sweep of prototype screens and test tasks.

## After the mapping

- TODO: summary lines per the voice contract; force the decision —
  which flow gets
  prototyped first, and which edge is riskiest untested.

## What this skill refuses

- TODO: flows for an unchosen concept; visual prescription inside
  `State:` lines.
