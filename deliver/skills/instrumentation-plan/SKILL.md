---
name: instrumentation-plan
description: "The measurement stage of deliver — write I-NNN instrument blocks: the event behind each OC-NNN metric a brief moves, the F-NNN.S stage it fires at, what it carries, and its baseline, plus the guardrails the charter names. Use when a designer says \"how will we know it worked\", \"what should we track\", \"set up the metrics\", \"what events do we need\", or a spec or slice exists and its metric has no event behind it. Do NOT use for choosing the metrics themselves (use define's success-metrics), reading the numbers after launch (use outcome-review), or analytics tooling setup."
---

# instrumentation-plan

The measurement stage of deliver: where the charter's metrics get an
event, a place in the flow, and a starting number, so that shipping can
be read instead of guessed at. Input: the charter's Success metrics
section (its `OC-NNN` lines, guardrails, and `Instrumented by:`), the
build spec's `Moves:` line, and the flows its criteria cite (ask once if
define or design work lives elsewhere). Output:
`deliver/instrumentation.md` (deliver root per the spec — ask once if
delivery work lives elsewhere) per the spec's instrument block format,
created with its header or appended — one file across all specs, because
metrics are charter-global. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/deliver-spec.md` before your first
write in a session — it owns the block format, the baseline route,
statuses, and ID rules; do not improvise fields. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory the session started in; read and write them by those relative
paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder above it
are not the project, even though that folder also has stage-named
subfolders: they hold only spec and voice files, are read-only, and are
never listed, searched, or written. Conversation runs per the voice
contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register,
translation, and question/report shape live there, not here.

## Instrument rules

- **The intake floor, one batched pass:** where the numbers come
  from today (the charter's `Instrumented by:` line is the starting
  answer); whether a baseline exists for each metric in scope and
  where; and what already fires that the build could reuse. Tool
  names are recorded as the user gives them and never chosen here.
- **Exactly one instrument per metric line the spec moves, and one
  per charter guardrail.** A metric with no instrument is a metric
  that will never be read — name it as unmeasurable rather than
  leaving the gap. A guardrail nobody can wire gets a line saying it
  stays unmeasured and why, so the outcome review inherits an honest
  blank instead of a missing one.
- **`Fires at:` is a named flow stage or a slice boundary.** An event
  nobody can place in the flow is an event nobody will wire. When the
  metric's moment isn't in any criterion — the outcome shows up
  after the flow ends — anchor it to the slice that ships the flow
  and say the reading is downstream of the build; before slice-plan
  has run, anchor to the flow's last stage and say slice-plan will
  move it.
- **An assumption-led spec has nothing to instrument yet.** `Moves:
  none named (assumption-led)` routes to define's success-metrics,
  then build-spec backfills the line, then back here. When the
  spec's criteria cite prose moments instead of stages, `Fires at:`
  cites the criterion (`S-001.3`) until a stage citation lands.
- **`Carries:` is product language.** "Which source type was
  connected, and whether help was opened first", never a field or
  table name; the builder translates at the boundary, and the spec's
  criteria rule applies here too.
- **Baselines are measured, never invented.** `<value> (measured
  <date>)` when the user has one; `unknown (unmeasured)` when they
  don't — and offer to draft the measurement question through
  discover's research-plan, its analytics row, the same route define
  uses. A baseline measured here, or handed back by an outcome
  review as a `first reading`, is recorded on the block and marked
  `Charter: not yet backfilled`; the charter is backfilled by
  define's success-metrics, which every run names as the next action
  while that mark stands on any block. The run that finds the
  charter's line carrying the value flips the mark to `backfilled
  <date>`. This skill never edits the charter.
- **Metrics come from the charter.** An instrument for a metric the
  charter doesn't name is refused; the route is success-metrics
  first, then back here. A charter `Secondary (requested)` line may
  be instrumented on the user's insistence, in the spec's
  `secondary:` form, which says it measures no outcome in as many
  words.
- **Statuses:** `specified` here; `firing (<date>, → reviews/…)` is
  build-review's write when its Instruments lens confirms the event;
  `retired — <reason>` on the user's word, the ID kept. Instruments
  are never deleted.
- **Re-runs append, never duplicate.** A metric that already has an
  instrument gets that block updated per the spec's allowed edits —
  a moved stage, a landed baseline, the `Charter:` flip — not a
  second block; a different event is a new block and the old one
  retires. Two instruments on one metric is an unresolved argument
  about what the metric means; send that back to success-metrics.

## After the write

Report per the voice contract: the file path, one line per
instrument with the metric and the stage it fires at, the baseline
state in plain terms, and the state line ("3 instruments: 2 with
baselines, 1 unmeasured; 1 guardrail unwired"). The decision this
artifact exists for: which baseline gets measured before the first
slice ships — name your pick and the one-line why, since a metric
read with no baseline is the first reading, not a result. Whenever
any block reads `Charter: not yet backfilled`, the single next
action is define's success-metrics to backfill it, named every run
until the mark clears; otherwise the close is the baseline pick,
with the research-plan run that would measure it.

## What this skill refuses

- An instrument for a metric the charter doesn't name.
- Inventing a baseline, or writing one without its measured date.
- Editing the charter, or any define file.
- Implementation names in `Carries:`, or choosing analytics tooling.
- Two instruments on one metric.
