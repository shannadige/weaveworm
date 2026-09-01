---
name: prototype
description: "The materialization stage of design — build a self-contained HTML prototype for a brief: no external requests, no build step, styled as the user's product, every screen annotated with the F-NNN.S flow stage it renders, ending in the task seeds a usability test would run. Use when a designer says \"prototype this\", \"make it clickable\", \"build something we can test\", \"show me the flow working\", or flows just landed and they want them tangible. Do NOT use for mapping the flow itself (use flow-map), running the test (use discover's usability-test-kit), or production frontend work."
---

# prototype

<!-- TODO: scaffold — body unwritten. House structure below; spec is
${CLAUDE_PLUGIN_ROOT}/references/design-spec.md (read before first
write in a session). -->

Input: a brief's `F-NNN` flows and the decisions they trace to.
Output: `design/prototypes/B-NNN/` — `index.html` plus a `README.md`
mapping screens → flow stages → decisions, per the spec's prototype
format. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Prototype rules

- TODO: self-containment — opens from file, zero external requests.
- TODO: styled as the user's product (their tokens if they have
  them), never weaveworm's brand.
- TODO: fidelity policy — real enough to test the flow's happy path
  and named edges; where "pixel theater" begins.
- TODO: annotation mechanism — every screen carries its `F-NNN.S`;
  an unannotated screen is an unlogged decision.
- TODO: test seeds — the README ends with one task per flow, shaped
  for usability-test-kit to consume.
- TODO: divergence discipline — where building reveals a flow is
  wrong, the fix routes through flow-map/decision-log, never a
  silent prototype-only patch.

## After the build

- TODO: summary lines per the voice contract; force the decision —
  test it or ship the
  learning question to research-plan; name the `(untested)` choices
  the test should target.

## What this skill refuses

- TODO: prototyping unmapped flows; screens that render no flow
  stage; external dependencies.
