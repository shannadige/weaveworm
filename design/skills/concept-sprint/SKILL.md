---
name: concept-sprint
description: "The divergence stage of design — generate 3+ distinct C-NNN concept directions for a B-NNN brief, each a mechanism stated as experience with its trades against constraints named, then force the pick (recorded as a D-NNN decision; parked concepts keep their IDs). Use when a designer says \"how might we solve this\", \"give me some directions\", \"explore concepts for the brief\", \"what are our options here\", or a brief just landed and they want solution ideas. Do NOT use for writing the brief (use design-brief), detailing the chosen direction (use flow-map), or logging the choice's rationale alone (use decision-log)."
---

# concept-sprint

The divergence stage of design: the one place directions multiply before
everything downstream converges. Input: a `B-NNN` brief and everything
it cites — the brief is the assumption boundary, so concepts cite it and
never reach past it; if no brief exists, route to design-brief first
(its Standalone fallback covers missing define artifacts — a sprint
without a brief has nothing to trade against). Output:
`design/concepts/B-NNN.md` per the spec's concept block format (`C-NNN`
numbering is stage-global: the next ID scans every file under
`design/concepts/`, not just this brief's sprint), and at the pick, the
choosing `D-NNN` in `design/decisions.md` per the decision block format,
with the brief's Status flipped to `in-design (→ D-NNN)` in the same
pass. Read the spec at `${CLAUDE_PLUGIN_ROOT}/references/design-spec.md`
before your first write in a session — it owns the block formats, ID
rules, and the post-pick iteration discipline; do not improvise fields.
Project artifacts (`research/`, `define/`, `design/`, `deliver/`) live
under the working directory; `${CLAUDE_PLUGIN_ROOT}` holds only the spec
and voice files, is read-only, and is never listed, searched, or
written. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Sprint rules

- **The intake floor, one batched pass at sprint start:** the
  directions already in the user's head (they join as C-blocks, on
  equal footing), the constraint they most expect to bind, and what
  they'd worry about shipping each direction they brought. One named
  exception to the voice contract's batched-pass rule: a concept
  generated mid-sprint whose cost you can't name gets its
  what-would-worry-you question asked when it exists, because the
  trade question can't precede the concept.
- **The floor is 3 distinct directions before any pick.**
  Distinct means both halves differ: the `Mechanism:` lines describe
  different experiences, *and* the `Trades:` lines give up different
  costs — not different amounts of the same cost. The write-time
  check is the swap test: if two concepts' `Trades:` lines could be
  exchanged and still read true, they are one direction twice — fold
  one into the other's `Variants:`. A restyled duplicate never counts
  toward the floor, and every direction is written as if it could
  win; a strawman propped next to the favorite is one concept wearing
  three IDs.
- **Mechanism is experience, never implementation.** `Mechanism:`
  says what the user does and sees at the brief's journey moment.
  "She pastes a URL and watches her data land in the workspace" is a
  mechanism; "a background job polls the source API" is
  implementation — build's concern, not a design direction. A concept
  the user states in implementation terms gets written as the
  experience it would produce, and you say so.
- **Every concept costs something.** `Trades:` names what the
  direction gives up, against which brief constraint, outcome, or
  quality. A trade-free concept is unexamined, not superior — find
  its cost before writing it, and if you can't name one, ask the user
  what they'd worry about shipping it, because a concept with no
  named cost can't be honestly picked against.
- **A variant is not a concept.** Same mechanism with a different
  surface lives on its parent's `Variants:` line, one line each,
  never as its own `C-NNN`. Variants are where surface exploration
  gets recorded without diluting the floor.
- **User-supplied directions join as C-blocks, on equal footing.**
  The solution held at brief time, or any direction the user brings
  mid-sprint, gets its `C-NNN`, its mechanism written as experience,
  and its trades named like any other — and the sprint still
  diverges past it. Say the direction is theirs when you write it;
  silent absorption reads as being ignored, per the voice contract.
- **The pick is a `D-NNN` block, never a concept edit.** Rationale,
  the parked concepts as `Rejected:` entries with one-line whys, a
  mandatory `Reverses on:`, and Confidence per the spec's
  inheritance rules — `(untested)` unless the pick cites evidence,
  and never higher than the opportunity the brief pulls. The chosen
  concept's Status points at the block, parked concepts keep their
  IDs and reasons, and the brief flips to `in-design (→ D-NNN)` — or,
  when the brief stands `validated`, to the spec's decay form
  `in-design — revalidation needed (→ D-NNN)`; a re-pick never leaves
  a validation claim standing. Concepts are never edited into
  winners.
- **Assumption-led briefs pass their stand-ins down.** When the
  brief carries no `J-NNN.S` or `OC-NNN` to cite, a concept's
  `Serves:` line carries the brief's population phrase or prose
  moment verbatim, `(assumption)`-labeled, per the spec's Standalone
  fallback — never an invented ID — and gains the citation when
  define's backfill lands.
- **Before the pick the file is a playground; after it, a record.**
  Pre-pick, adding and reshaping concepts needs no justification —
  divergence is the point, and a re-run extends the sprint. Post-pick
  the chosen direction evolves through decisions, and a parked
  concept reopens only on a named trigger: an `E-NNN`, a changed
  `given` constraint, or a stakeholder call recorded as a `D-NNN`
  with the judgment labeled. Taste alone reopens nothing.

## After the sprint

Report per the voice contract: the file path, one line per concept
(ID, the mechanism in a phrase, the cost it accepts), and the state
line ("B-001 sprint: 4 directions, 1 user-supplied, none picked").
The decision this artifact exists for is the pick — name your
recommended direction and the trade it accepts in one line, and force
the choice. When the pick can't happen yet, name the single next
action instead: usually the one question or piece of evidence that
would separate the front-runners, phrased as a research-plan seed.
And when the pick lands `(untested)` with high stakes — hard to
reverse, or load-bearing for the brief's `Done when:` — say the
cheap test first, before flows and a prototype build on it.

## What this skill refuses

- One concept presented as a sprint, or any pick before the floor of
  three distinct directions is met.
- Counting a variant, restyled duplicate, or strawman toward the
  floor.
- A pick without its `D-NNN` — a Status line never carries the
  choice on its own.
- Editing a parked concept into the chosen one, or reshaping any
  concept after the pick without a decision behind it.
- Reopening a parked concept on taste alone — the spec's named
  triggers or nothing.
- Writing implementation into `Mechanism:` lines — it gets translated
  to experience, narrated.
