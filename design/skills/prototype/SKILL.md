---
name: prototype
description: "The materialization stage of design — build a self-contained HTML prototype for a brief: no external requests, no build step, styled as the user's product, every screen annotated with the F-NNN.S flow stage it renders, ending in the task seeds a usability test would run. Use when a designer says \"prototype this\", \"make it clickable\", \"build something we can test\", \"show me the flow working\", or flows just landed and they want them tangible. Do NOT use for mapping the flow itself (use flow-map), running the test (use discover's usability-test-kit), or production frontend work."
---

# prototype

The materialization stage of design: the brief's flows made walkable,
built to be tested, not admired. Input: a brief's `F-NNN` flows and
the decisions they trace to. No flows means nothing to render — route
to flow-map; a prototype improvised past the flows is a mockup with
annotations missing. Output: `design/prototypes/B-NNN/` —
`index.html` plus `README.md` mapping screen → `F-NNN.S` → `D-NNN`,
per the spec's prototype format. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/design-spec.md` before your first
write in a session — it owns the format, the fidelity policy, and the
annotation mechanism; do not improvise. Conversation runs per the
voice contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` —
register, translation, and question/report shape live there, not
here.

## Prototype rules

- **Self-contained, absolutely.** One `index.html` that opens from
  file: zero external requests — no CDN scripts, no web fonts, no
  remote images — and no build step. A prototype that needs a network
  or a toolchain fails in exactly the room it exists for: someone
  else's machine, mid-test. Inline everything; system font stacks and
  embedded data URIs are the ceiling.
- **Styled as the user's product, never weaveworm's.** Ask once for
  their tokens or a screenshot to match; with neither, default to
  deliberately plain — neutral type, their product's plain language,
  no decorative system. The thing under test is the flow, and chrome
  that photographs well steals attention from it. Test participants
  should believe they're in a rough version of the real product, not
  a template.
- **Fidelity is bounded by the test seeds.** Anything a test task
  touches works: the happy path and every named edge from the flows
  are interactive — the error state reachable, the empty state shown
  first-run, the interrupted path resumable if the flow handles it.
  Everything else is static, and pixel theater begins exactly there:
  polish beyond what a task exercises is cost without information.
  Content is real-shaped where the content *is* the design (labels,
  empty-state copy, data density), built as sample data and labeled
  so in the README, never passed off as real.
- **Every screen names the stage it renders.** The screen-level
  container carries `data-flow="F-002.3"`, and the README's map
  (screen → `F-NNN.S` → `D-NNN`) says the same thing for readers who
  never open markup. An unannotated screen is a screen no flow asked
  for — which means a decision nobody logged; either it earns its
  stage through flow-map or it doesn't get built.
- **Building is a test of the flows, and divergence routes upstream.**
  When rendering a stage reveals the flow is wrong — a step that
  can't work at this density, an edge the flow never named — the fix
  is a flow-map edit or a `D-NNN` through decision-log, then the
  prototype follows. Never a silent prototype-only patch: the moment
  screens diverge from stages, the annotations lie, and everything
  critique and testing trace through them lies too. Say what building
  surfaced; that friction is the cheapest research the stage gets.
- **The README ends with the test seeds.** One task per flow, each
  phrased as the user's goal in their words ("get your sales data
  connected"), never as UI directions ("click Connect"), with the
  success state the brief's `Done when:` cares about. The seeds are
  the `reviewed → validated` bridge — written exactly for
  research-plan and usability-test-kit to lift unchanged.

## After the build

Report per the voice contract: the directory path, one line per
screen (the stage it renders, interactive or static), one line for
the sample data labeled as such, and the state line ("B-001
prototype: 6 screens covering F-002 (connect a source) and F-003
(recover a failed sync), happy path and 3 edges interactive, 4 test
seeds"). The decision this artifact exists for:
test it or keep building on belief — name the `(untested)` decisions
the seeds would exercise, ranked by what's tracing to them, and force
the call on running the test. The single next action when the user is
ready: a research-plan run that lifts the seeds into `Q-NNN`s. If
critique hasn't passed the brief yet, say the order plainly — a
critique pass makes the brief `reviewed`, and testing an unreviewed
design risks validating a charter violation.

## What this skill refuses

- Prototyping unmapped flows, or screens no flow stage asked for —
  flow-map first, then build.
- External requests or a build step — a prototype that can't open
  from file on a stranger's laptop isn't done.
- Weaveworm's own styling, or template chrome standing in for the
  user's product.
- Interactive polish past the test seeds — static is correct for
  everything no task touches.
- Patching a flow problem in the prototype alone — divergence routes
  through flow-map and decision-log, narrated.
- Passing sample data off as real — real-shaped is labeled in the
  README, every time.
