---
name: outcome-review
description: "The closing stage of deliver — after a slice ships and its window passes, read the instruments against the charter's OC-NNN metrics and guardrails: moved, flat, regressed, or too early; route the numbers into discover's evidence log; credit the brief's Done when and never a single decision; and force keep, iterate, or revert. Use when a designer says \"did it work\", \"did the metric move\", \"read the results\", \"what did we learn from launch\", or a shipped slice's window has ended. Do NOT use for choosing metrics (use define's success-metrics), specifying events (use instrumentation-plan), or logging evidence directly (route through discover's evidence-log)."
---

# outcome-review

The closing stage of deliver: where a shipped build stops being a build
and becomes a reading against the outcome the charter named. Input: the
brief, its spec, the slices marked `shipped` with their dates, the
instruments behind the spec's `Moves:` metrics and the charter's
guardrails, and the numbers — the user's read, an export, or a query
result (ask once if define, design, or research work lives elsewhere).
Output: `deliver/outcomes/<date>-B-NNN.md` per the spec's outcome review
format, written only after the readings are in
`research/evidence-log.md` (a `too early` record excepted), and the
spec's Status becoming `measured (<date>, → outcomes/<date>-B-NNN.md)`
when any verdict is other than `too early`. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/deliver-spec.md` before your first
write in a session — it owns the record format, the window rule, the
verdict forms, and what a reading may and may not prove; do not
improvise verdicts. Project artifacts (`research/`, `define/`,
`design/`, `deliver/`) live under the working directory the session
started in; read and write them by those relative paths and never `cd`.
`${CLAUDE_PLUGIN_ROOT}` and the folder above it are not the project,
even though that folder also has stage-named subfolders: they hold only
spec and voice files, are read-only, and are never listed, searched, or
written. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Reading rules

- **The intake floor, one batched pass:** which slices shipped and
  when (slice-plan's dates are the record; confirm, don't re-ask);
  the window, when the charter's metric line has none; where the
  numbers are and what they say; and what else changed during the
  window that could explain a move — a launch, a pricing change, a
  campaign. That last question is mandatory, and `none known` is an
  answer.
- **Evidence first.** Each reading lands in the evidence log through
  discover's evidence-log before this record cites it: a `Source:`
  naming the query, window, and date, Confidence per that spec's
  rules, and the `Q-NNN` plan block it answers (research-plan's
  analytics row) or `unplanned` per the log's rule. Deliver mints no
  `E-NNN`; a review whose `Evidence:` line is neither entries nor
  the spec's `too early` form is not written. Say plainly when the
  log write is the step in the way.
- **The header keeps the spec's forms.** `Shipped:` is slice IDs
  with slice-plan's dates; `Window:` is the length, the slice it
  counts from, and the end date, or the spec's no-moving-slice form.
  Neither line explains itself: what the record can't say in those
  forms is said in chat, and a header with nothing to put on
  `Shipped:` is the no-shipped-slice branch, which writes nothing.
- **The window is the charter's**, counted from the shipped date of
  the last slice that moves the metric; when the charter's line is
  directional with no window, use the one agreed at intake and record
  it on the header. Any read before the window ends is `too early
  (window ends <date>)`, written as a record when the user asks for
  it, with what it would take to read sooner; its Decision reads `too
  early — read again after <date>` and the spec's Status is left
  alone. No slice at `shipped` on record means no window to count
  and no record to write: nothing is written, the readings the user
  brought may still be logged through evidence-log (marked there as
  readings with no shipped slice behind them), and the reply routes
  to build-review first, then slice-plan on its clean pass — a
  shipped date said in chat is not the record. When slices did ship
  and none moves the metric (every one carries `none alone`), the
  verdict is `too early (no moving slice shipped)`; that form is
  reserved for shipped slices and never stands in for a missing
  record. A spec whose `Moves:` reads `none named
  (assumption-led)` has no metric to read: name success-metrics,
  then build-spec's `Moves:` backfill, then instrumentation-plan,
  and write nothing.
- **Verdict per metric and per guardrail, baseline beside observed,
  always.** `moved`, `flat`, `regressed`, `too early`, or `first
  reading <value>`; guardrails `held`, `breached`, `unmeasured`, or
  `too early` (the reading is in but the window has not ended;
  `unmeasured` means no instrument or reading behind it).
  A `moved` with no baseline is refused — the honest verdict is
  `first reading <value>`, which becomes the baseline: an
  instrumentation-plan re-run records it on the block, the charter
  backfills it through success-metrics, and the next window is the
  first real read.
- **A reading proves the brief's Done when, not any single choice.**
  Cite it here and in the log, and say what it moved in the brief's
  own terms. It never clears an `(untested)` decision — too much
  changes in a window to credit one choice — so the decision log is
  not re-cited from here; `iterate` names the question the reading
  raises as a research-plan seed, and a usability test that isolates
  the decision is still the route to clearing it. When the user wants
  the number to count for a decision, say why it can't, in plain
  words, and what test would.
- **Confounds are named next to the verdict.** `Also changed in
  window:` sits in the header, and a `moved` with an uncaptured
  confound is the cheapest way to fool a team; when the user names
  one, the header carries it, the chat read says the move is shared
  with it, and the verdict stays one of the spec's forms.
- **The decision is forced, and define's two writes are named.**
  `keep` (the reading stands); `iterate` (back to design-brief or
  research-plan with the reading as evidence); `revert` (a decision's
  `Reverses on:` observation happened — the user takes the reading,
  as its `E-NNN`, to design's decision-log, which records the
  reversal, and the spec is superseded by its lifecycle). Then
  the two writes that let define's objectives learn what delivery
  bought, named every run and never made here: success-metrics
  records the result on the charter's metric line, judged against
  the agreed target — so `moved` here can be `short` there; say so
  in plain words before it looks like a disagreement — and
  opportunity-map closes the pursued opportunity as `delivered` with
  this verdict and this file's path.
- **A record is dated and never edited.** The next reading is a new
  file; a `too early` record followed by a real one is the expected
  sequence, not a correction.

## After the write

Report per the voice contract: the file path, one line per metric
with baseline, observed, and verdict, the guardrails in a phrase,
the confound if any, and the state line ("outcome 2026-10-28, B-001
(trial users reach a connected source unaided): OC-001 moved 41% →
58%, 1 guardrail held, no confounds named"). The decision this
artifact exists for: keep, iterate, or revert — name your read and
the one-line why. Then the single next action: the success-metrics
run that writes the result on the charter, with the opportunity-map
close following it; after a `first reading`, the instrumentation-plan
re-run that records the baseline comes first. On the no-shipped-slice
branch there is no file to report: say what was logged and that the
record waits on a shipped slice, and close on build-review as the
first step, with slice-plan recording the ship date after its clean
pass.

## What this skill refuses

- Reading a metric with no instrument on record, or writing a review
  with no evidence-log entry behind it.
- `moved` without a baseline, or any verdict read before the window
  ends other than `too early`.
- Clearing an `(untested)` decision from a launch reading.
- Editing the charter, the decision log, or the opportunity backlog —
  the two define writes are named, never made.
- Declaring the outcome from the build merely shipping.
- Writing a record with no slice at `shipped` on record — every
  `too early` form describes a shipped slice's window, never a
  missing one.
