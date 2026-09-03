# Deliver spec — v1

> **Status: v1 — settled and consumed.** Every format and lifecycle
> below is decided (open decisions closed 2026-09-02, amended by the
> three-agent audit the same day) and consumed by the stage's five
> skills. A skill that needs a field this spec lacks changes the spec
> first.

Deliver turns design's handoff — a brief that critique has passed
and, ideally, a test has validated — into a build that a human
engineer or a coding agent produces without deciding anything
load-bearing by accident, and then reads whether the outcome the
charter named actually moved. Three artifact kinds and two dated
records: a build spec per brief, slices of that spec, instrument
blocks behind the charter's metrics, build reviews, and outcome
reviews. Each artifact exists to force a decision; each section earns
its place by being cited downstream or gating a write-time check.

Deliver is not project management. Sprints, tickets, estimates,
owners, release comms, rollout mechanics, and environments belong to
the engineering team's tools. Deliver owns two questions only: what
must be true of the build, and did the outcome move. A skill that
can't cite a flow, a decision, or a metric is outside the stage.

The stage's three governing biases:

1. **Write for the reader who can't ask.** A human engineer fills
   gaps from judgment and comes back with questions; an agent fills
   gaps with plausible defaults and doesn't. The spec is authored for
   the stricter reader and serves both: explicit gaps, mandatory
   edges, decisions carried with their reversal conditions, and a
   normative/incidental line drawn through the prototype. The
   recipient changes the packaging of open items, never the
   precision of the spec.
2. **Fidelity is to decisions, not pixels.** The build is reviewed
   against `D-NNN` blocks and `F-NNN.S` stages, not against the
   prototype's rendering. A deviation that gets logged is design
   continuing; a deviation nobody logged is a decision reversed in
   silence — the failure mode the whole stage exists to catch.
3. **Built is not delivered.** A shipped build proves nothing about
   the outcome. Only the `OC-NNN` metric moving, measured through
   the instruments this stage specified and logged as evidence
   through discover, closes the loop. Deliver mints no evidence:
   production numbers enter `research/evidence-log.md` through
   discover's evidence-log skill, and the outcome review cites them
   from there.

## Files

Default root: `deliver/` in the user's project, next to `design/`,
`define/`, and `research/`. If the user keeps delivery work elsewhere,
ask once, then reuse their answer for the session.

```
deliver/
├── specs/S-NNN-<slug>.md       # one build spec per brief (per handoff); criteria S-NNN.N
├── slices/S-NNN.md             # SL-NNN slice blocks for that spec
├── instrumentation.md          # all I-NNN instrument blocks
├── reviews/<date>-S-NNN.md     # dated build review passes
└── outcomes/<date>-B-NNN.md    # dated outcome reviews
```

`<slug>` is 2–5 lowercase hyphenated words. Skills create every file
and header themselves.

## ID table

| ID | Artifact | Lives in | Cited by |
|---|---|---|---|
| `S-NNN` (criteria `S-NNN.N`) | Build spec | specs/ | slices, instruments, reviews, outcomes |
| `SL-NNN` | Slice | slices/ | reviews (what was built), outcomes (what shipped) |
| `I-NNN` | Instrument | instrumentation.md | reviews (firing?), outcomes (the numbers) |

Same ID discipline as the stages before: sequential, zero-padded to
three digits (criterion numbers `N` plain integers), permanent —
never renumbered, reused, or deleted; next = highest existing + 1,
scanning the artifact's file(s) first. Each kind counts
independently, and each sequence is global to the stage even where
its files are per-spec: the next `SL-NNN` scans every file under
`slices/`. Reviews and outcomes are dated records, not ID'd
artifacts, like design's critiques. Upstream IDs (`E-NNN`, `Q-NNN`,
`CH-NNN`, `OC-NNN`, `U-NNN`, `J-NNN`, `O-NNN`, `B-NNN`, `C-NNN`,
`D-NNN`, `F-NNN`, voices P/R/M) are discover's, define's, and
design's; deliver cites them and never mints them.

## Uncertainty markers

Deliver uses design's vocabulary — `given (<source>)`, `(assumption)`,
`(unconfirmed)`, `(untested)` — unchanged, and adds none. The two
gaps a marker might have covered have forms already: an instrument
with no data yet carries `Baseline: unknown (unmeasured)` (define's
`(unmeasured)` marker on deliver's own field), and a metric read
before its window carries the outcome verdict `too early`. Every new marker is vocabulary the user has to
learn; these two don't earn one.

## Confidence inheritance

Deliver consumes upstream artifacts; it never improves them. Design's
rules carry over unchanged — weakest link; only the evidence log
raises a level; assumptions labeled, not laundered; a decision's
confidence never exceeds the opportunity it serves — plus the
deliver-stage corollary: **a criterion's confidence is the confidence
of the decision it traces to.** Building an `(untested)` decision
faithfully yields an `(untested)` build: legitimate, visible in the
build review's census, and resolved only by the test that decision
was waiting for — never by shipping (see Outcome review format).

## Upstream contract

Deliver reads, and never writes:

- `design/briefs/` — **`reviewed` and `validated` briefs are
  spec-able.** A clean critique proves the design is still on
  charter; a usability test is welcome before building and not
  required. The pass whose date sits on the brief's `reviewed` or
  `validated` line is what made it spec-able; design never reverts
  that status, so when a newer critique on record carries a
  Constraints or Non-goals finding, the status has outlived its pass —
  redirect to design-critique before writing. An `in-design` brief
  gets one redirect to design-critique, then proceeds on explicit
  override: the spec's `Brief:` line reads `B-NNN — in-design
  (→ D-NNN), specified on user override (assumption)`, and
  build-review names the missing critique in every pass until one
  lands. `in-design — revalidation needed (→ D-NNN)` is `in-design`
  for this purpose: same redirect, same override, the full status
  carried on the `Brief:` line. An `open` brief is never spec-able —
  nothing has been chosen. A `parked` brief is redirected to
  design-brief to unpark. Deliver never edits a brief.
- `design/decisions.md` — the constraint set for the build. Every
  `standing` decision the spec's flows trace to is carried into the
  spec's Must not change list with its `Reverses on:` line. The
  spec's `Decisions: through D-NNN` pin is what staleness is measured
  against: when the brief's decisions move past the pin, the spec is
  superseded, never edited (see Spec lifecycle).
- `design/flows/` — the criteria source. Each `F-NNN.S` stage and
  each Edges line becomes exactly one criterion; an edge written
  `not handled (open)` becomes a criterion that says so and an Open
  item, never a silence. A flow marked `superseded` is never
  spec'd; its successor is.
- `design/prototypes/B-NNN/` — reference, never source. Normative:
  the `data-flow` stage annotations and the README's screen → stage →
  decision map. Incidental: markup, styling, copy, and sample data —
  the builder works from the criteria, and an agent is told so in the
  spec's preamble. A decision may promote a rendering to normative
  (the copy is the design; a layout a decision chose) — recorded on
  the spec's `Prototype:` line as `promoted: <what> (D-NNN)`, never
  assumed.
- `design/critiques/` — the pass named on the brief's status line is
  what made it spec-able; the findings on any lens that pass left
  short of `clean` ride into the spec's Open section as items, cited
  by lens.
- `define/charter.md` — `OC-NNN` metrics and guardrails are what
  instruments measure and outcomes are read against; Constraints
  remain what the build may not trade away. Deliver never edits the
  charter: a baseline measured here is recorded on the instrument
  block, and the run ends by naming define's success-metrics as the
  next action to backfill it.
- `research/evidence-log.md` — citable directly. Production readings
  land here through discover's evidence-log skill, with a `Source:`
  line specific enough to relocate (for a reading: the query, window,
  and date) and the `Q-NNN` plan block they answer or `unplanned` per
  that log's rule, before any outcome review cites them; deliver
  mints no `E-NNN`.

## Standalone fallback

Same doctrine as define's and design's: the dependency is on
information, not files. A team that arrives with a prototype and
nothing behind it — no flows, no decision log, often no brief —
still gets a spec. build-spec walks the prototype with the user in a
short intake before writing, and records the answers in the spec's
own body. Deliver still never mints upstream IDs; the spec is the
assumption boundary, and everything downstream (slices, instruments,
reviews) cites it unchanged.

The intake floor, per missing artifact:

- **No brief** — What is this build's job, in one sentence, for whom?
  What observable state means done, and which number does it move?
  The spec's `Brief:` line reads `none — assumption-led`; the job
  becomes the heading, `(assumption)`-labeled; `Done when:` carries
  the answer in prose, `(assumption)`-labeled; `Moves:` cites the
  `OC-NNN` whenever a charter names the number, and otherwise reads
  `none named (assumption-led)`.
- **No flows** — Walking the prototype screen by screen: what does
  the user do here, and what do they then see? What happens on error,
  on empty, and when they're interrupted? Each answer becomes a
  criterion whose stage citation is a prose moment instead of an
  `F-NNN.S`, `(assumption)`-labeled; each unanswered edge becomes an
  open criterion and an Open item.
- **No decision log** — Which choices in this prototype matter, why,
  and what would change your mind about each? Answers become
  Must not change lines, `(assumption)`-labeled, each with a reversal
  observation in the user's words. A criterion heading's decision
  slot then carries the short phrase of the Must not change line it
  rests on, `(assumption)`-labeled, in place of a `D-NNN`; the
  `(needs one)` stop applies only when a flow file exists to say it.
- **No prototype annotations** — a prototype with no `data-flow`
  annotations and no README map has nothing normative in it: the
  `Prototype:` line reads `normative: none — the criteria are the
  design (assumption); incidental: everything rendered`.
- **No charter** — What may the build not trade away, and who set
  each limit? Recorded as Must not change lines, `given (<source>)`
  when sourced, `(assumption)` otherwise. With no metric named,
  `Moves:` reads `none named (assumption-led)` and instrumentation-plan
  redirects to define's success-metrics rather than inventing one.

What the user can't answer becomes an Open item — never a blocker.
Build-review prices the debt rather than gating on it: its Scaffolding
lens counts the spec's `(assumption)` lines alongside its other
findings, and a spec whose Must not change list is mostly assumptions
gets that named in the verdict, with design as the pointed-to fix.

Downstream stand-ins: the spec is the assumption boundary, so the
artifacts below it carry its stand-ins and never invent an ID. A
slice's `Delivers:` carries the brief's `Journey:` line as it stands
(a `J-NNN.S`, or its `(assumption)`-labeled prose moment) and, with
no brief, the spec heading's job verbatim, `(assumption)`-labeled;
a slice's `Moves:` copies the spec's line. An instrument's `Fires
at:` cites the criterion (`S-001.3`) when that criterion's stage is a
prose moment. A spec whose `Moves:` reads `none named
(assumption-led)` has nothing to instrument: instrumentation-plan
routes to define's success-metrics, build-spec backfills the line,
and instrumentation follows. A build review of such a spec has no
pin: its header reads `Brief decisions now: none — assumption-led`
and its Decisions lens judges the `(assumption)` Must not change
lines, quoting the line in place of a `D-NNN`. An outcome review for
a spec with no brief is keyed `outcomes/<date>-S-NNN.md` with
`Brief: none — assumption-led`.

Promotion, not rewrite: when design artifacts appear later, backfill —
`Brief:` gains its `B-NNN` (an override-pulled `Brief:` gains the
critique's date the same way), prose moments gain `F-NNN.S`
citations, Must not change lines gain `D-NNN`s, `Moves:` gains its
`OC-NNN` once success-metrics names one. The same pass walks
downstream, as design's backfill does: slice `Delivers:` and
`Moves:` lines and instrument `Fires at:` lines gain their citations
alongside the spec's. This is the one edit ever made to a criterion:
its citation. Its check text never changes.

## Build spec format (specs/S-NNN-<slug>.md)

```markdown
# S-001 <the brief's heading, verbatim> — B-001
<!-- weaveworm build-spec v1 -->

- **Status:** open
- **Brief:** B-001 — reviewed (2026-09-01, → D-012)
- **Supersedes:** S-000 (only on a successor; omit on a first spec)
- **Recipient:** agent
- **Flows:** F-002, F-003
- **Decisions:** through D-021
- **Prototype:** prototypes/B-001/ — normative: stage annotations, README map; incidental: markup, styling, copy, sample data; promoted: F-002.3 copy (D-018)
- **Moves:** OC-001
- **Done when:** <the brief's line, verbatim> (B-001)
- **Critique:** 2026-09-01 — findings carried: Shifts 1, Debt census 3   (or `2026-09-01 — none carried` / `none — in-design override` / `none — assumption-led`)

## For the builder
<the recipient preamble — see Recipient packaging>

## Criteria

### S-001.1 <criterion name> — F-002.1 (D-012)
- **Check:** <what the user does, and what they then see>

### S-001.4 error at F-002.3 (D-015)
- **Check:** <what the user sees and can do when it fails>

### S-001.6 interrupted at F-002.2 — open
- **Check:** unhandled by design; build no handling. Open item 2.

### S-001.7 <criterion name> — after choosing a source, the user lands on its first table (assumption) — one page, never a wizard (assumption)
- **Check:** <the same one observable line>   (assumption-led form: a prose moment and a Must not change phrase stand in for F-NNN.S and D-NNN until backfill)

## Must not change
- **D-012** <the decision, one sentence> — reverses on: <the observation>
- **D-015** …

## Stop conditions      (or `## Handoff agenda` for a human recipient)
1. <the question, in product terms> — blocks S-001.6
2. <the question, in product terms> — blocks none; informs <what>
```

Spec field rules:

- **The heading is the brief's heading, verbatim, plus the brief
  ID.** Brief headings never change, so the copy can't drift; a
  different job is a different brief and a different spec.
- **`Brief:`** records the status read at pull time with its pick
  pointer, so the spec shows what it was built on. The override form
  is in the Upstream contract.
- **`Recipient:`** is `human` or `agent`, asked once per session and
  reused. It selects the preamble and the Open section's heading, and
  changes nothing else. On the user's word it may be switched later:
  the line, the preamble, and the heading swap together, and nothing
  else in the file moves.
- **`Decisions: through D-NNN`** pins the spec to the decision set it
  compiled. It is the staleness check for every skill downstream.
- **`Prototype:`** always draws the normative/incidental line
  explicitly, even when nothing is promoted — the line is what stops
  an agent shipping the scaffolding.
- **`Moves:` and `Done when:` cite the brief**, never restate it; the
  Done when text is copied verbatim with its citation because the
  builder reads this file, not the brief.
- **`Critique:`** names the pass that made the brief spec-able and
  which of its findings ride into the Open section; `none — in-design
  override` and `none — assumption-led` say why there is no pass, and
  are backfilled with the date when one lands.

Criteria rules:

- **One criterion per flow stage and one per Edges line, in flow
  order, edges after their flow's stages.** Nothing is merged and
  nothing is skipped: a stage with no criterion is a stage the
  builder will improvise.
- **The heading cites the stage and the decision** (`F-002.1
  (D-012)`); an edge heading names its kind and anchor (`error at
  F-002.3 (D-015)`). An edge with no decision of its own cites its
  anchor stage's decision; an open edge the flow left unanchored
  heads by kind and stage with no decision cited
  (`interrupted at F-002.2 — open`). A stage whose flow line
  reads `— (needs one)` is not spec-able: route to design's
  decision-log first, since a criterion with no decision behind it
  is taste the builder will encode. On an assumption-led spec the
  Standalone fallback's stand-in forms apply instead.
- **`Check:` is one observable line: what the user does, and what
  they then see.** Never implementation (no component, endpoint, or
  data-model names), never visual style. That line is precise enough
  for an agent to turn into a test and for a human to confirm by
  hand; the spec writes no test code.
- **An open edge is an open criterion.** Its Check line says no
  handling is built and points at the Open item that will settle it.
  Silence here is the one thing a coding agent will fill.
- **Criteria are immutable from handoff.** An `open` spec nobody has
  received is build-spec's to regenerate in place, ID kept, said in
  chat. From `handed off` on, a criterion's text never changes — the
  exception is a citation backfill under the Standalone fallback. A
  design change is a fresh spec (see Spec lifecycle).

Must not change rules:

- **Every `standing` decision the spec's flows trace to appears
  here, with its `Reverses on:` line verbatim.** This is what tells
  the builder which choices are load-bearing versus incidental; a
  decision missing from this list is one the build may reverse
  without anyone noticing.
- Decisions promoted from the prototype (`promoted:` on the
  `Prototype:` line) appear here too.

Spec lifecycle (transitions and who writes them). Status is one
value, and it moves forward in this order; a later trigger for an
earlier value is recorded in the triggering skill's own file, and
the Status line is left alone with that said in chat:

- `open` — spec written; not yet given to a builder. Written by
  build-spec, and regenerated in place by build-spec on a re-run
  until handoff.
- `handed off (<date>, to human | agent)` — the user confirmed the
  handoff at the end of a build-spec run (its forced decision).
  Written by build-spec.
- `built (<date>, through SL-NNN)` — counting this pass and the
  review files on record, every slice not `dropped` has a pass whose
  Criteria and Decisions lenses came back clean, whatever the slices'
  own statuses say. Written by build-review — one of its two writes
  outside its own file (the other is an instrument's `firing`). A
  later slice cut after this (a Deferred criterion un-deferred) gets
  its own clean pass, which re-writes the `through SL-NNN` pointer.
  Per-slice progress lives on slice statuses, not here.
- `measured (<date>, → outcomes/<date>-B-NNN.md)` — an outcome review
  exists for a shipped slice of this spec with at least one verdict
  other than `too early`. Written by outcome-review; a `too early`
  record leaves Status alone.
- `superseded (→ S-NNN)` — **a design change after handoff is a
  fresh spec, never an edit.** When the brief's decisions move past
  the `through D-NNN` pin (a new or reversing `D-NNN` — the same
  event that flips a validated brief to `in-design — revalidation
  needed`), build-spec writes the successor with `Supersedes: S-NNN`
  and adds this line to the old spec: the one edit ever made to a
  superseded spec. Shipped slices of the old spec stay on record;
  unshipped ones are replaced by name in the successor's slice file.
  Build-review detects staleness on its own too: a pass whose brief
  decisions exceed the pin says so first, and its next action is the
  fresh spec.

Allowed edits after handoff: the Status line; Open items gaining
`settled: <answer> (<date>)`; citation backfill per the Standalone
fallback; the `Recipient:` swap with its preamble and Open heading.
Nothing else.

## Recipient packaging

The one place the stage branches, and it branches on two things only.
The same Open list — the critique's carried findings, `not handled
(open)` edges, the brief's open questions that bear on the build, and
intake gaps — is written once, each item in one form for both
recipients: the question in product terms, then `— blocks S-NNN.N`
or `— blocks none; informs <what>`. The recipient chooses its
heading and the preamble above the criteria. Criteria, Must not
change, the Open items, and every header line are identical for both
recipients.

For `human`, the preamble reads, in substance: this spec is the
record of what the design decided; the criteria are the acceptance
checks; the Must not change list is the set of choices that need a
conversation before they move; the Open section is the agenda for the
handoff conversation. The Open heading is `## Handoff agenda`, read
as the questions to settle together.

For `agent`, the preamble reads, in substance: build from the
criteria, never from the prototype's markup; the Must not change list
is fixed — if implementing a criterion requires changing one, stop
and report rather than adapt; the Open section is a list of stop
conditions — on reaching one, stop and ask, never choose a default.
The Open heading is `## Stop conditions`, read as what the agent may
not decide alone, with the criterion each one blocks. The spec is
written to be read directly by an engineer's coding-agent
session as its operating brief; no companion file exists, so the one
file stays the one record.

An Open item closes by gaining `settled: <answer> (<date>)` — the
answer stays visible with the question, and a criterion the answer
would change is a fresh spec, not an edit.

## Slice block format (slices/S-NNN.md)

```markdown
# Slices — S-001
<!-- weaveworm slice-plan v1 -->
- **Spec:** S-001

## SL-001 <the shift this slice delivers, as the user experiences it>
- **Criteria:** S-001.1–S-001.4, S-001.7
- **Delivers:** J-003.4 shift (B-001)
- **Moves:** OC-001   (or `none alone — <why it still ships>`)
- **Replaces:** SL-004 (unshipped)   (only in a successor spec's file)
- **Status:** planned

## Deferred
- S-001.6 — <reason, and what would un-defer it>
- S-001.8 — open until Open item 2 settles; settling it with any handling is a fresh spec, where the successor criterion is sliced
```

Slice rules:

- **A slice delivers a journey shift on its own.** Its heading is
  that shift as the user experiences it, and `Delivers:` cites the
  `J-NNN.S` the brief cites (on an assumption-led spec, the stand-in
  per the Standalone fallback). Moving a metric alone is preferred;
  `Moves: none alone — <why>` is allowed when the shift is real and
  the metric only moves with a later slice. A slice that does neither
  is a task list, and slice-plan refuses to write it.
- **Coverage is total.** Every criterion lands in exactly one slice or
  in Deferred with a reason and an un-defer condition. Nothing is
  silently dropped. An open criterion is deferred until its Open item
  settles, and its line says that settling with any handling is a
  new decision past the pin, so the criterion that ships is the
  successor spec's.
- **The whole-thing case is written, not manufactured.** When the
  smallest legitimate slice is the entire spec, the file holds one
  slice and says so in its heading's shift; no increments are
  invented to look iterative.
- **First slice is the forced decision** at write time; order beyond
  that is the team's, recorded here only as slice order.
- **Statuses:** `planned` | `shipped (<date>)` | `dropped — <reason>`.
  `shipped` is written by slice-plan on the user's word, after a
  build-review pass on that slice came back clean on its Criteria and
  Decisions lenses; outcome-review reads shipped dates to compute
  windows. A dropped slice keeps its ID and its criteria move to
  Deferred or to another slice in the same pass.
- **On a successor spec**, the new slice file names which unshipped
  slices of the superseded spec each new slice replaces; shipped ones
  are never re-cut. In the same pass each replaced block in the old
  file gains `dropped — replaced by SL-NNN (S-NNN)`, its criteria
  left where they are: the one edit ever made to a superseded spec's
  slice file.

Allowed edits: Status; `Criteria:` and `Moves:` on `planned` blocks,
in a pass that says what moved; Deferred lines. A `shipped` block
never changes.

## Instrument block format (instrumentation.md)

File header: `# Instrumentation` +
`<!-- weaveworm instrumentation-plan v1 -->`. One file across all
specs, since metrics are charter-global.

```markdown
## I-003 <the event, as the user action it records>
- **Measures:** OC-001   (or `guardrail: <the charter guardrail line>` / `secondary: <the charter line> — measures no outcome (requested)`)
- **Fires at:** F-002.4   (or `SL-002 ships`, or `S-001.3` on an assumption-led spec)
- **Carries:** <what the event records, in product terms>
- **Baseline:** 41% (measured 2026-09-10)   (or `unknown (unmeasured)`)
- **Charter:** backfilled 2026-09-11   (or `not yet backfilled`)
- **Status:** specified
```

Instrument rules:

- **Exactly one instrument per metric line the spec's `Moves:`
  cites**, and one per charter guardrail — or a line saying the
  guardrail stays unmeasured and why. A metric with no instrument is
  a metric that will never be read, and instrumentation-plan names
  it as such rather than leaving it; two instruments on one metric
  is an unresolved argument about what the metric means, and goes
  back to success-metrics. A charter `Secondary (requested)` line may
  be instrumented on the user's insistence, in the `secondary:` form.
- **`Fires at:` is a named stage or a slice boundary.** An event
  nobody can place in the flow is an event nobody will wire. Before
  slice-plan has run there is no `SL-NNN` to name: anchor to the
  flow's last stage and move it when the slice exists.
- **`Carries:` is product language.** "Which source type was
  connected", never a field or table name; the builder translates at
  the boundary.
- **`Baseline:`** is `<value> (measured <date>)` or
  `unknown (unmeasured)`. A baseline measured here is recorded on
  this block only; the charter is backfilled through define's
  success-metrics, which every instrumentation-plan run names as its
  next action while any block reads `Charter: not yet backfilled`.
  `Charter:` flips to `backfilled <date>` on the instrumentation-plan
  run that finds the charter's metric line carrying the value. An
  outcome review's `first reading <value>` verdict lands here the
  same way, as the block's `Baseline:`, on the next run.
- **Metrics come from the charter.** An instrument for a metric the
  charter doesn't name is refused; the route is define's
  success-metrics first, then back here.
- **Statuses:** `specified` | `firing (<date>, → reviews/<date>-S-NNN.md)`
  (written by build-review when its Instruments lens confirms it —
  for a slice-boundary event, in a pass run on the slice after it
  shipped) | `retired — <reason>` (written by instrumentation-plan on
  the user's word). Instruments are never deleted; a retired one
  keeps its ID.

Allowed edits: `Fires at:`, `Baseline:`, `Charter:`, and Status, by
the writers named above. `Measures:` and `Carries:` never change; a
different event is a new block and the old one retires.

## Build review format (reviews/<date>-S-NNN.md)

A dated pass, never edited after — the next pass is a new file. A
second pass on the same spec the same day suffixes the filename
`-2`, `-3`…. Header:

```markdown
# Build review — S-001 — 2026-09-12
<!-- weaveworm build-review v1 -->
- **Spec:** S-001 (decisions through D-021)
- **Slice:** SL-001
- **Reviewed:** <what and where: commit, staging URL, or a demo walkthrough, and with whom>
- **Brief decisions now:** through D-021   (or `through D-024 — spec stale` / `none — assumption-led`)
```

A pass needs a slice file: with none on record, the route is
slice-plan first. A pass on a `shipped` slice is allowed — its
Criteria and Decisions verdicts go on record and gate nothing, and
the Instruments lens is why it was run.

Then one section per lens, fixed set, in this order:

1. **Criteria** — per `S-NNN.N` in the slice, edge criteria
   included: `met`, `deviated — <how>`, or `missing`. Every
   criterion in the slice is listed; an unlisted criterion is an
   unreviewed one.
2. **Edges** — the open-edge check, the one thing Criteria can't
   express: for each open criterion in the slice, `clear` (nothing
   was built over it) or `filled — <what was built>`. A filled open
   edge is a decision the builder made alone.
3. **Decisions** — any Must not change decision the build
   contradicts. The finding is written `contradicts D-015 — <how>`
   (on an assumption-led spec, the Must not change line quoted in
   place of the ID) plus one of: `reason — <the limit found>, routed
   to decision-log`; `mistake — S-001.4 re-issued`; `undetermined`.
   The reviewer asks the user which it is during the pass; when the
   user can't say (the builder isn't in the room), it stays
   `undetermined` and the next pass re-asks.
4. **Instruments** — each `I-NNN` whose `Fires at:` falls in this
   slice: `firing` or `silent`. When the spec's `Moves:` metric has
   no block at all, the lens reads `none specified — OC-001
   unmeasurable until instrumentation-plan runs`, never `clean`.
5. **Scaffolding** — prototype sample data, placeholder copy, or
   incidental markup shipped as real; plus the census of the spec's
   `(assumption)` lines and override notes (a missing critique, an
   assumption-led brief), named every pass until resolved.

Verdict per lens: `clean`, or findings citing IDs. Never a score.

Gating, settled: **a partial gate on the slice.** A slice may be
recorded `shipped` only after a pass whose Criteria and Decisions
lenses are clean; a `deviated`, `missing`, or contradiction finding
holds it. When, counting this pass and the review files on record,
every slice not `dropped` has such a pass, build-review writes the
spec's Status to `built (<date>, through SL-NNN)` — one of its two
writes outside its own file; the other is flipping an instrument to
`firing`. Edges, Instruments, and Scaffolding findings don't hold
the slice; they're named, and they recur until fixed.

A contradicted decision is the headline finding, and it holds the
slice until named. `reason` means the builder hit a real limit — a
constraint discovered in implementation, a rejected alternative that
turned out necessary — and the route is the user taking the limit to
design's decision-log, which writes the new or reversing `D-NNN` and,
by its own rule, flips a validated brief's Status; the spec's pin is
now exceeded, and a fresh spec follows.
`mistake` means the build simply diverged; the criterion is
re-issued as the finding and the slice is re-reviewed after the fix.
Review names and routes; it never fixes, and it never edits the
build, the spec, or the design.

Staleness: when the brief's decisions exceed the spec's pin at pass
time, the header says so, the verdicts still stand for the slice as
reviewed, and the pass ends by naming the fresh spec as the next
action. A stale pass still gates and still writes: shipping a
faithful build of a design that has since moved is the team's call,
made with the header in front of them.

## Outcome review format (outcomes/<date>-B-NNN.md)

A dated record per brief, written when a shipped slice's window has
passed — or earlier, to record `too early` when the user asks before
then. Never edited after; the next reading is a new file, and a
second record on the same brief the same day suffixes the filename
`-2`, `-3`…. Header:

```markdown
# Outcome review — B-001 — 2026-10-15
<!-- weaveworm outcome-review v1 -->
- **Brief:** B-001   (or `none — assumption-led`, the file keyed by S-NNN)
- **Spec:** S-001   (or `S-001, S-002` when shipped slices span a superseded spec and its successor; both gain `measured`)
- **Shipped:** SL-001 (2026-09-14), SL-002 (2026-09-28)
- **Window:** 30 days from SL-002 — ends 2026-10-28 (charter: OC-001 within 30 days)   (per metric section instead, when the metrics' windows differ)
- **Evidence:** E-041, E-042   (or `none — too early (window ends 2026-10-28)`)
- **Also changed in window:** <anything else that could explain a move, or `none known`>
```

Then one section per metric the spec's `Moves:` cites, a Guardrails
section, and the decision:

```markdown
## OC-001 <the charter's metric line, verbatim>
- **Instrument:** I-003
- **Baseline:** 41% (measured 2026-09-10)
- **Observed:** 58% over 2026-09-28 – 2026-10-28 (E-041)
- **Verdict:** moved

## Guardrails
- <guardrail line> — held (E-042)   (or `breached (E-NNN)` / `unmeasured`)

## Decision
keep   (or `iterate — <what the reading raises>` / `revert — D-015 reverses on <observation>: happened` / `too early — read again after <date>`)
```

Outcome rules:

- **Evidence first.** The readings land in `research/evidence-log.md`
  through discover's evidence-log — a `Source:` line naming the
  query, window, and date; Confidence per that spec's rules — before
  this record cites them. Deliver mints no `E-NNN`; a review whose
  `Evidence:` line is neither entries nor the `too early` form is
  not written.
- **The window is the charter's** `within <window>` for that metric,
  counted from the shipped date of the last slice that moves it. When
  the charter has none (a directional target waiting on a baseline),
  the window is agreed at intake and recorded on the header. Any read
  before the window ends is `too early (window ends <date>)`, and the
  record says what it would take to read sooner. When no shipped
  slice moves the metric (every shipped slice carries `none alone`,
  or the moving slice was dropped or deferred), there is no start
  date: the verdict is `too early (no moving slice shipped)`.
- **Verdict per metric:** `moved`, `flat`, `regressed`, `too early`,
  or `first reading <value>`. Baseline and observed always appear
  together; a `moved` with no baseline is refused — the honest
  verdict is `first reading <value>`, which becomes the baseline:
  instrumentation-plan records it on the block, success-metrics
  backfills the charter, and the next window is the first real read.
- **A reading proves the brief's Done when, not any single choice.**
  It is cited here and in the evidence log; it never clears an
  `(untested)` decision, because too much changes in a window to
  credit one choice. The route to clearing stays a usability test that
  isolates the decision. `iterate` names the question the reading
  raises as a research-plan seed.
- **`Also changed in window:`** is mandatory — a launch, a pricing
  change, a marketing push — or `none known`. A `moved` next to an
  uncaptured confound is the cheapest way to fool a team.
- **The decision is forced:** `keep` (the reading stands, nothing to
  do); `iterate` (back to design-brief or research-plan with the
  reading as evidence); `revert` (a decision's `Reverses on:`
  observation happened — design's decision-log records the reversal,
  and the spec is superseded per its lifecycle); or, on a record
  whose every verdict is `too early`, `too early — read again after
  <date>`. Deliver writes nothing upstream in any case; the record
  is here, and the spec's Status becomes `measured (<date>, →
  outcomes/<date>-B-NNN.md)` — unless every verdict is `too early`,
  which leaves the Status alone.
- **The run ends by naming define's two writes.** The reading reaches
  the charter through define's success-metrics, which appends the
  result line on the metric (judged against the target, so a `moved`
  here can be `short` there — say so in plain words), and reaches the
  backlog through define's opportunity-map, which closes the pursued
  block as `delivered` with this verdict and this file's path. Those
  two writes are how define's objectives learn what delivery bought;
  outcome-review names them every time and never makes them. A
  `first reading` verdict names one more step ahead of them: the
  instrumentation-plan re-run that records it as the baseline.

## Open decisions

All settled 2026-09-02:

1. ~~Which brief statuses are spec-able.~~ Resolved — `reviewed` and
   `validated` cleanly; `in-design` on override after one redirect,
   with the override written on `Brief:` and named every build-review
   pass; `open` never. See Upstream contract.
2. ~~Criterion granularity and check form.~~ Resolved — one per
   stage and one per edge, in flow order; a single `Check:` line as
   what the user does and then sees, never implementation; the same
   form for both recipients, and the spec writes no test code. See
   Build spec format.
3. ~~The normative/incidental line through the prototype.~~ Resolved
   — stage annotations and README map normative; markup, styling,
   copy, and sample data incidental by default; a decision promotes
   a rendering via `promoted:` on the `Prototype:` line. See Upstream
   contract.
4. ~~Recipient packaging.~~ Resolved — one file, no companion; the
   recipient selects the preamble and the Open heading (`Handoff
   agenda` / `Stop conditions`) and nothing else; the agent form is
   written to be read directly by a coding-agent session. See
   Recipient packaging.
5. ~~Slice legitimacy.~~ Resolved — delivers a shift alone, required;
   moves a metric alone, preferred with `none alone — <why>` allowed;
   neither is refused; the whole-thing case is one slice, written as
   such. See Slice block format.
6. ~~Instrument format and the baseline route.~~ Resolved — baseline
   recorded on the instrument block; `Charter:` tracks the backfill;
   every run ends by naming define's success-metrics as the next
   action; deliver never edits the charter. See Instrument block
   format.
7. ~~Build review lenses, what a clean review writes, and the
   reversal-versus-mistake rule.~~ Resolved — five lenses; Criteria
   and Decisions clean gates the slice, and the last slice writes
   `built`; a contradicted decision holds the slice until the user
   names it a reason (routed to decision-log, spec superseded) or a
   mistake (criterion re-issued). See Build review format.
8. ~~Outcome review: window, verdicts, what it forces, re-citation.~~
   Resolved — the charter's window, or one agreed at intake; four
   verdicts plus `first reading <value>` where no baseline exists;
   keep / iterate / revert forced, `too early` recorded without
   evidence and without touching the spec; a reading proves the
   brief's Done when and never clears an `(untested)` decision. See
   Outcome review format.
9. ~~Spec lifecycle and decay.~~ Resolved — a design change after
   handoff is a fresh spec with `Supersedes:`, the old one marked
   `superseded (→ S-NNN)` as its only edit; criteria are immutable;
   shipped slices stay, unshipped ones are replaced by name. See Spec
   lifecycle.
10. ~~Whether deliver needs its own uncertainty marker.~~ Resolved —
    none; `unknown (unmeasured)` and `too early` cover the gaps. See
    Uncertainty markers.
11. ~~The standalone fallback intake floor.~~ Resolved — build-spec
    walks the prototype with the user; answers become
    `(assumption)`-labeled criteria and Must not change lines; the
    Scaffolding lens counts the debt; citations backfill as the one
    allowed criterion edit. See Standalone fallback.
