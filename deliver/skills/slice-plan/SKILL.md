---
name: slice-plan
description: "The scoping stage of deliver — cut an S-NNN build spec into SL-NNN slices that each deliver a journey shift on their own, move the charter metric where one can, and force the call on which ships first. Use when a designer says \"what's the smallest version\", \"what ships first\", \"cut this down\", \"MVP of this\", or a spec was just written and it's more than one release. Do NOT use for writing the spec (use build-spec), sprint or ticket planning (the team's tools), or estimating effort."
---

# slice-plan

The scoping stage of deliver: where a spec becomes the increments a team
can ship, each one a change the user would notice. Input: a build spec
(any status but `superseded`) and, when there is one, the brief it
serves — for the `J-NNN.S` shifts and `OC-NNN` metrics a slice has to
carry on its own. Output: `deliver/slices/S-NNN.md` (deliver root per
the spec — ask once if delivery work lives elsewhere) per the spec's
slice block format, created with its header or updated. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/deliver-spec.md` before your first
write in a session — it owns the block format, legitimacy test, coverage
rule, statuses, and ID rules; do not improvise fields. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory: read and write them by those relative paths, and never build
an absolute path from where the spec lives, because
`${CLAUDE_PLUGIN_ROOT}` and the folder above it hold only spec and voice
files, are read-only, and are never listed, searched, or written.
Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Slicing rules

- **The intake floor, one batched pass:** what the team can ship in
  one go; whether any of the spec is already built; and which of the
  brief's shifts matters most to the charter right now. Effort,
  owners, and dates are not asked — they're the team's, and they
  aren't what a slice is made of.
- **A slice delivers a journey shift on its own.** Its heading is
  that shift as the user experiences it, and `Delivers:` cites the
  `J-NNN.S` the brief cites. Moving a metric alone is preferred;
  `Moves: none alone — <why it still ships>` is honest when the
  shift is real and the number only moves with a later slice. A slice
  that does neither is a task list wearing a slice's clothes — refuse
  to write it, and say what shift it would need to carry to qualify.
- **Assumption-led specs pass their stand-ins down.** When the spec's
  `Brief:` reads `none — assumption-led`, `Delivers:` carries the
  spec heading's job `(assumption)`-labeled (or the brief's
  `Journey:` prose moment, when a brief exists without a journey)
  and `Moves:` copies the spec's line, never an invented ID; both
  gain citations when build-spec backfills.
- **Coverage is total.** Every criterion lands in exactly one slice or
  under `## Deferred` with a reason and what would un-defer it.
  Nothing is dropped silently. An open criterion is deferred until
  its Open item settles, and its line says that settling it with any
  handling is a new decision past the pin — the criterion that ships
  will be the successor spec's.
- **The whole-thing case is written, not manufactured.** When the
  smallest legitimate slice is the entire spec, write one slice whose
  heading names the one shift and say so in chat. Increments invented
  to look iterative each ship nothing a user notices.
- **First slice is the forced decision.** Order beyond that is the
  team's; record it here only as the order of blocks, never as
  sprints or dates.
- **Statuses are written on the user's word, gated by review.**
  `shipped (<date>)` only after a build-review pass on that slice came
  back clean on its Criteria and Decisions lenses — check the newest
  review before writing it, and name the missing or failing pass if
  there isn't one. `dropped — <reason>` keeps the ID and moves its
  criteria to Deferred or another slice in the same pass.
  outcome-review reads shipped dates to compute windows, so a shipped
  date is never approximate.
- **A successor spec gets a fresh slice file.** When build-spec has
  superseded the spec, new slices cite the new criteria and each
  names the unshipped old slices it replaces on `Replaces:`, and
  each replaced block in the old file gains `dropped — replaced by
  SL-NNN (S-NNN)` in the same pass, its criteria left in place — the
  one edit ever made to a superseded spec's slice file. Shipped
  slices of the old spec are never re-cut; they're on record.
- **Re-runs update, never duplicate.** Same spec, changed team
  capacity or a settled Open item → move criteria between `planned`
  blocks and Deferred per the spec's allowed edits, never out of a
  shipped slice, and say what moved. IDs are never reused.

## After the write

Report per the voice contract: the file path, one line per slice
with the shift and metric it carries, the deferred count with reasons
in a phrase, and the state line ("S-001 (trial users reach a
connected source unaided): 3 slices, 2 criteria deferred until stop
condition 2 settles"). The decision this artifact exists for: which
slice ships first — name your pick and the one-line why, in terms of
which shift the charter needs soonest. If the first slice carries
`none alone`, say which later slice makes the number move and that
the reading stays blind until it ships.

## What this skill refuses

- A slice that delivers no shift and moves no metric.
- Manufacturing increments when one slice is the honest answer.
- Writing `shipped` with no clean build review on record.
- Estimates, owners, dates, sprint names, or ticket references inside
  a slice.
- Dropping a criterion without a Deferred line or a slice that takes
  it.
