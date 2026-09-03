---
name: decision-log
description: "The design stage's evidence log — record load-bearing design choices as D-NNN blocks in design/decisions.md: the decision in one sentence, its rationale (cited or labeled judgment), rejected alternatives, and what observation would reverse it; untested choices marked (untested) as seeds for usability testing. Use when a designer says \"log that decision\", \"why did we go this way\", \"record the tradeoff\", \"we decided X because Y\", reverses an earlier call, or another design skill needs a choice recorded. Do NOT use for recording research findings (use discover's evidence-log) or choosing between concepts without the sprint (use concept-sprint)."
---

# decision-log

The design stage's evidence log: the artifact critique argues with, and
the memory that outlives whoever made the call. Input: a design choice —
from concept-sprint's pick, a flow or prototype call, a critique finding
that a stage traces to nothing, a build-review finding that the build
hit a real limit, an outcome reading that matched a `Reverses on:` line,
or the user directly. Output: `design/decisions.md` per the spec's
decision block format, plus the brief Status writes this skill owns
(`validated` and its decay, below). Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/design-spec.md` before your first
write in a session — it owns the block format, the traced-or-contested
bar, confidence inheritance, and the brief lifecycle; do not improvise
fields. Project artifacts (`research/`, `define/`, `design/`,
`deliver/`) live under the working directory: read and write them by
those relative paths, and never build an absolute path from where the
spec lives, because `${CLAUDE_PLUGIN_ROOT}` and the folder above it hold
only spec and voice files, are read-only, and are never listed,
searched, or written. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Logging rules

- **The intake floor, per choice, one batched ask:** why this way,
  what else was on the table, and what observation would change your
  mind. Every block's fields come from that single pass; the
  fallbacks below (proposing the implied observation, the
  what-else-was-on-the-table nudge) live inside it, never as later
  drip.
- **The bar is traced-or-contested.** A choice earns a `D-NNN` when a
  downstream artifact traces to it (a flow stage, a prototype screen,
  a test task) or when it rejected a real alternative someone could
  reopen. "One page vs. a wizard" qualifies; a button color doesn't,
  unless a constraint made it contested. Both failure modes cost the
  team: an unlogged load-bearing choice is invisible until critique
  flags the stage citing nothing, and a log padded with taste calls
  buries the decisions that matter. When the user brings a choice
  below the bar, say where it lives instead — the flow's `State:`
  line, the prototype — rather than logging it to be polite.
- **`Because:` is cited or labeled, never retro-fitted.** Rationale
  cites `E-NNN` entries, names the inherited constraint with its
  `given (<source>)`, or states the judgment as judgment ("editor's
  call: fewer steps beats more guidance here"). A plausible story
  composed after the fact is worse than a labeled hunch — it reads as
  evidence and isn't. If the user can't say why beyond taste, that is
  the rationale; write it labeled.
- **`Reverses on:` is mandatory and observable.** Every block names
  the observation that would overturn it — something a test, a
  metric, or a user could actually show ("3 of 5 test users ask
  where the data went"). A decision nothing could overturn is taste
  wearing a rationale, and this line is where usability-test tasks
  come from; write it like a test will read it. If the user can't
  name one, propose the observation their own worry implies and
  confirm it.
- **`Rejected:` keeps the road not taken real.** Parked concepts by
  ID, non-concept alternatives in a phrase, each with its one-line
  why. An empty `Rejected:` line on a contested call means the
  alternatives are being forgotten, not that none existed — ask what
  else was on the table once.
- **Confidence is inherited, never asserted.** Weakest load-bearing
  citation sets the level; no cited evidence and no completed test
  means `(untested)` — the honest default, not a defect. A decision
  never rises above the opportunity its brief pulls: brilliant design
  against a low-confidence `O-NNN` is a low-confidence decision, and
  the fix is discover, not polish. `(untested)` clears only through
  the loop — a `Q-NNN` plan, a test, `E-NNN` entries cited back onto
  the block — never by assertion, consensus, or the prototype merely
  existing.
- **Reversal is a new block, never an edit.** When the named
  observation happens (or the team overrules), the old block gains
  `reversed (→ D-NNN)` and stays; the new block cites the evidence
  or labeled call that overturned it. Then sweep: find every flow
  stage, edge, prototype screen, and concept Status line tracing to
  the reversed block and report them in product terms ("the empty
  state at F-002.1, two prototype screens, and C-004's chosen status
  were built on the reversed call") — re-pointing them is flow-map's,
  prototype's, and concept-sprint's work, but naming the blast
  radius is this skill's, in the same pass. When a deliver build spec
  pins this brief, name that the spec is now stale and a fresh one is
  build-spec's next action.
- **Writing against a `validated` brief downgrades it, same pass.**
  A new or reversing `D-NNN` on a validated brief flips that brief's
  Status to `in-design — revalidation needed (→ D-NNN)`. The old
  test evidence stays cited on the decisions it covered; what it can
  no longer vouch for is the design as it now stands. Never log the
  block and leave the brief claiming a validation it has outgrown.
- **This skill writes `validated`.** When a test's `E-NNN` entries
  land on the last qualifying `(untested)` decision, and a
  `reviewed`-clean critique is on record dated on or after the
  pinned `through D-NNN` block was written, write the brief's Status
  `validated (<date>, through D-NNN, → E-NNN…)`, pinned to the
  highest decision the tested artifacts traced to. No clean critique
  on record, or only one older than the decisions being validated,
  means no `validated` — testing proves users succeed; only critique
  proves the charter wasn't traded away, and a stale pass proved
  nothing about the newer blocks. Say which is missing; a stale
  critique makes the fresh pass the named next action.

## After the log

Report per the voice contract: the file path, one line per block
written or reversed (ID, the decision in a phrase, its confidence in
plain terms), and the state line ("decisions.md: 9 standing, 1
reversed, 5 untested across B-001"). The decision this artifact
exists for is whether the design's riskiest call is safe to build on:
name the `(untested)` decision with the most tracing to it and say
what single test would clear it, phrased as a research-plan seed.
When the census grows — untested blocks accumulating faster than
tests clear them — say so plainly; that trend is the difference
between designing and guessing in bulk. On a reversal, end on the
blast radius instead: what needs re-pointing and which skill does it.

## What this skill refuses

- Laundering taste into rationale — an unevidenced call is logged as
  labeled judgment or not at all.
- A block without `Reverses on:` — unfalsifiable decisions don't get
  IDs.
- Editing a reversed decision into agreement, or deleting and
  renumbering any block — flagged noise keeps its ID too.
- Clearing `(untested)` by assertion — only cited `E-NNN` entries
  from a test do that.
- Writing `validated` without both gates — cited test evidence and a
  clean critique on record.
- Logging a new decision against a validated brief without flipping
  its Status in the same pass.
