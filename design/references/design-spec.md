# Design spec — v1

> **Status: v1 — settled and consumed.** Every format and lifecycle
> below is decided and consumed by the stage's six skills. The last
> open item (what deliver pulls) is now claimed by deliver's spec —
> see Open decisions.

Design turns define's handoff — pursued `O-NNN` opportunities — into
solutions a team can test and build, without ever re-arguing what
define settled. Five artifact kinds, in rough sequence: a design brief
per pursued opportunity, divergent concepts, a decision log, flows,
and a clickable prototype — with critique as the recurring gate that
checks the work against the charter it must not betray. Each artifact
exists to force a decision; each section earns its place by being
cited downstream or gating a write-time check.

The stage's two governing biases:

1. **Solutions are downstream of decisions, not taste.** Every
   load-bearing design choice is a `D-NNN` block with rationale,
   rejected alternatives, and what would reverse it — the design
   stage's evidence-log analog. A prototype nobody can trace to
   decisions is a mockup, not design.
2. **Untested is a label, not a verdict.** Design mints hypotheses,
   not evidence. A choice with no evidence behind it and no test yet
   is `(untested)` — legitimate, visible, and a seed for discover's
   research-plan. The loop closes through discover:
   `(untested)` decision → `Q-NNN` plan → usability-test-kit →
   `E-NNN` entries → the decision re-cited with evidence.

## Files

Default root: `design/` in the user's project, next to `define/` and
`research/`. If the user keeps design work elsewhere, ask once, then
reuse their answer for the session.

Every path above is relative to the working directory, the user's
project, never to the plugin root (`${CLAUDE_PLUGIN_ROOT}`, where this
spec lives): that folder is named after the stage but holds only spec
and voice files, is read-only, is never listed, searched, or written,
and is never where a project artifact is looked for.

```
design/
├── briefs/B-NNN-<slug>.md      # one brief per pursued opportunity (or coherent cluster)
├── concepts/B-NNN.md           # C-NNN concept blocks for that brief's sprint
├── decisions.md                # all D-NNN decision blocks
├── flows/F-NNN-<slug>.md       # one flow per brief × scope
├── prototypes/B-NNN/           # self-contained HTML prototype per brief
│   ├── index.html
│   └── README.md               # screen → F-NNN.S → D-NNN map
└── critiques/<date>-B-NNN.md   # dated critique passes
```

`<slug>` is 2–5 lowercase hyphenated words. Skills create every file
and header themselves.

## ID table

| ID | Artifact | Lives in | Cited by |
|---|---|---|---|
| `B-NNN` | Design brief | briefs/ | concepts, decisions, flows, prototypes, critiques |
| `C-NNN` | Concept | concepts/ | the choosing decision (`D-NNN`) |
| `D-NNN` | Design decision | decisions.md | flows, prototype annotations, critiques, deliver |
| `F-NNN` (stages `F-NNN.S`) | Flow | flows/ | prototype screens, usability-test tasks, deliver |

Same ID discipline as discover and define: sequential, zero-padded to
three digits (stage numbers `S` plain integers), permanent — never
renumbered, reused, or deleted; next = highest existing + 1, scanning
the artifact's file(s) first. Each kind counts independently, and
each sequence is global to the stage even where its files are
per-brief: the next `C-NNN` scans every file under `concepts/`, not
just the current brief's sprint, so two briefs never mint the same
concept ID. Upstream
IDs (`E-NNN`, `Q-NNN`, `CH-NNN`, `OC-NNN`, `U-NNN`, `J-NNN`, `O-NNN`,
voices P/R/M) are discover's and define's; design cites them and never
mints them.

## Uncertainty markers

Design uses define's vocabulary — `given (<source>)`, `(assumption)`,
`(unconfirmed)` — unchanged, plus one of its own:

- `(untested)` — a design choice with no cited evidence and no
  completed test behind it. Not a defect: the honest default state of
  most design work, and the queue usability testing pulls from. It
  clears only when the decision cites `E-NNN` entries from a test —
  never by the prototype merely existing.

## Confidence inheritance

Design consumes upstream artifacts; it never improves them. Define's
three rules carry over unchanged:

1. **Weakest link** — a decision's Confidence is the weakest
   load-bearing entry or artifact it cites.
2. **Only the evidence log raises a level** — test findings routed
   through discover's evidence-log are the only thing that clears
   `(untested)` or lifts a decision's Confidence. Writing design
   artifacts never changes anything upstream; if designing surfaces
   stronger evidence, route it there first, then re-cite.
3. **Assumptions are labeled, not laundered** — an unevidenced choice
   is `(untested)`; an intake answer is `(assumption)`; neither is
   ever dressed up as a cited claim.

Plus the design-stage corollary: **a decision's confidence never
exceeds the opportunity it serves.** Designing brilliantly against a
low-confidence `O-NNN` yields a low-confidence design, and the fix is
discover, not polish.

## Upstream contract

Design reads, and never writes:

- `define/opportunities.md` — **only `pursued` blocks are pull-able.**
  An open opportunity is not designable; the honest route is back to
  opportunity-map, where pursuing is a one-line status edit. If the
  user insists on designing an open block, design-brief redirects
  once, then proceeds on explicit override: the brief's `Pulls:` line
  reads `O-NNN — open, designed on user override (assumption)` — the
  override is the user's explicit call, so `(unconfirmed)`, define's
  marker for calls made without them, would misfile it; what's
  assumed is that the pursue call will be recorded. Design never
  edits opportunities.md itself, and critique names the
  unpursued pull in every pass until opportunity-map records the call.
- `define/charter.md` — Constraints are what design may not trade
  away; Non-goals are a write-time gate on brief and concept scope;
  `OC-NNN` metrics are what prototypes and tests get measured against.
  A `draft` (never-agreed) charter is usable — teams design against
  moving strategy all the time — but the brief records
  `Charter: draft (as read <date>)`, and critique's constraint lens
  rechecks against the charter as it stands at critique time, naming
  any constraint that shifted since the pull. Charter-fit is checked
  either way; what a draft charter can't provide is
  charter-agreement, and the critique on record says so.
- `define/roles.md`, `define/journeys/` — who the design serves and
  the shift it delivers. A brief serving no `J-NNN` shift names that
  gap.
- `research/evidence-log.md` — citable directly, same as define.

When define artifacts are missing, the Standalone fallback below
applies — design runs on labeled assumptions gathered at intake, and
never stalls on an absent file.

## Standalone fallback

The same doctrine as define's Standalone fallback (define-spec.md):
the dependency is on information, not files. Every upstream artifact
answers questions; when the artifact is absent, design-brief asks the
user those questions directly — a short intake before any writing —
and records the answers in the brief's own body. Design still never
mints upstream IDs; the brief is the assumption boundary, and
everything downstream (concepts, decisions, flows, prototypes) cites
the brief unchanged.

Per missing artifact, the intake floor:

- **No opportunities.md** — What problem is this design solving, in
  one sentence? For whom? Why now — what breaks if it stays unsolved?
  The brief's `Pulls:` line reads `none — assumption-led`; the problem
  statement lives in the heading as usual, `(assumption)`-labeled.
- **No charter.md** — What may the design not trade away, and who set
  each limit? What is explicitly not this design's job? What
  observable state means done? Recorded as brief-local `Constraints:`
  / `Out of scope:` / `Done when:` lines — `given (<source>)` when
  sourced, `(assumption)` otherwise.
- **No roles.md / journeys/** — Who is this for, and which moment of
  their current workflow does it change? A plain population phrase and
  a prose moment stand in for `U-NNN` / `J-NNN.S` citations.

Downstream artifacts inherit the stand-ins, labeled: where a concept
`Serves:` line or a flow header's `Role:` / `Journey:` line would
cite `U-NNN` / `J-NNN.S` / `OC-NNN`, an assumption-led run carries
the brief's population phrase or prose moment verbatim,
`(assumption)`-labeled — never an invented ID, never a blank.

What the user can't answer becomes a brief Open question — a
research-plan seed, never a blocker. Critique prices the debt rather
than gating on it: alongside the `(untested)` census it counts the
brief's `(assumption)` lines, and a design whose load-bearing lines
are mostly assumptions gets that named in the verdict, with define as
the pointed-to fix.

Promotion, not rewrite: when define artifacts appear later, backfill —
`Pulls:` gains its `O-NNN`, population phrases and prose moments gain
`U-NNN` / `J-NNN.S` citations, constraint lines re-point at the
charter — and the backfill walks downstream: concept `Serves:` lines
and flow headers carrying the brief's stand-ins gain the same
citations in the same pass. Backfilling citations is an allowed edit;
the brief heading never changes.

## Brief format (briefs/B-NNN-<slug>.md)

```markdown
# B-001 <the design's job, one problem-shaped sentence>
<!-- weaveworm design-brief v1 -->

- **Status:** open
- **Pulls:** O-003 (pursued 2026-08-12)
- **For:** U-002
- **Journey:** J-003.4
- **Moves:** OC-001
- **Charter:** agreed 2026-08-01
- **Constraints:**
  - <inherited line — cites the charter, carries its `given (<source>)`>
  - <brief-local line — marked `(brief)`, plus `given (<source>)` or `(assumption)`>
- **Out of scope:** <the charter Non-goals bordering this brief, plus brief-local exclusions>
- **Done when:** <the observable state, tied to the OC-NNN metric it moves — never a deliverable list>
- **Open questions:** <what the brief needs that nothing upstream answers — research-plan seeds>
```

Brief field rules:

- **The heading restates the opportunity as the design's job** — one
  sentence, problem-shaped, no solution named. "Trial users can reach
  a connected data source unaided" is a job; "a setup wizard" is a
  concept that hasn't earned a `C-NNN` yet.
- **`For:` / `Journey:` / `Moves:` cite, never restate** — duplicated
  prose drifts from its source; an ID can't. The Standalone fallback
  governs what stands in when the upstream artifact is absent.
- **`Charter:`** records what was read at pull time: `agreed <date>`,
  `draft (as read <date>)`, or `none — assumption-led`.
- **`Done when:`** is the brief's contract with validation: the
  observable state a test would confirm, tied to the metric of the
  outcome it moves.

Brief lifecycle (transitions and who writes them):

- `open` — brief written; no direction picked. Written by design-brief.
- `in-design (→ D-NNN)` — a concept-sprint pick is on record; flows
  and prototype build from it. Written by concept-sprint at the pick.
- `reviewed (<date>, → D-NNN)` — the newest critique pass found no
  constraint violations and no non-goal creep. Written by
  design-critique — its only write outside its own file (`parked`
  aside, which any skill records). The `→ D-NNN` carries the
  concept-sprint pick pointer forward: every post-pick status keeps
  the pointer visible, so flow-map and prototype never lose their
  trigger to a status change. This is deliberately a **partial
  gate**: reviewed means coherent and charter-true, ready to put in
  front of users — never done. A brief sitting at `reviewed` with no
  `Q-NNN` plan naming its test seeds is visible testing debt, and a
  standing critique finding until the plan exists.
- `validated (<date>, through D-NNN, → E-NNN…)` — a usability test
  ran this brief's test seeds, and the decisions its tested flows
  trace to now cite the resulting `E-NNN` entries. Requires a
  `reviewed`-clean critique on record first, dated on or after the
  pinned `through D-NNN` block was written: testing proves users
  succeed; only critique proves the charter wasn't traded away, and
  a critique older than the decisions being validated proved nothing
  about them — a stale one means the next action is a fresh pass,
  not the write. Written by decision-log when the last qualifying
  `(untested)` clears. `through D-NNN` pins the validation to the
  decision set it covered — the highest decision this brief's
  artifacts traced to at validation time.
- **Validation decays mechanically.** When any skill writes a new
  or reversing `D-NNN` against a `validated` brief — decision-log's
  usual write, or concept-sprint's at a re-pick — it flips Status
  back to `in-design — revalidation needed (→ D-NNN)` in the same
  pass. The old test evidence stays cited on the decisions it covered;
  what it can no longer vouch for is the design as it now stands.
- `parked — <reason> (was <status>)` — written by any skill on the
  user's call; the brief keeps its ID and artifacts. `(was <status>)`
  records the full prior Status line, pick pointer included, and
  design-brief restores it verbatim when the user unparks — a brief
  parked mid-design comes back mid-design, not `open`.

Allowed edits: everything but the heading. Backfilling citations per
the Standalone fallback is an allowed edit; a genuinely different job
is a new brief.

## Concept block format (concepts/B-NNN.md)

One sprint file per brief. File header: `# Concepts — B-001` +
`<!-- weaveworm concept-sprint v1 -->` + `- **Brief:** B-001`.

```markdown
## C-004 <the mechanism in a phrase>
- **Mechanism:** <how the moment works, as experience — what the user does and sees, never implementation>
- **Serves:** J-003.4 shift, OC-001
- **Trades:** <what this direction gives up, against which constraint or quality — the cost named>
- **Variants:** <surface variations explored and folded in, one line each>   (only when there are any)
- **Status:** chosen (→ D-012) | parked — <reason>
```

Concept rules:

- **Floor of 3 genuinely distinct directions before any pick.**
  Distinct means both halves differ: the `Mechanism:` lines describe
  different experiences, *and* the `Trades:` lines give up different
  costs — not different amounts of the same cost. The write-time
  check is the swap test: if two concepts' `Trades:` lines could be
  exchanged and still read true, they are one direction twice — fold
  one into the other's `Variants:`.
- **A variant is not a concept.** Same mechanism with a different
  surface lives on its parent's `Variants:` line, never as its own
  `C-NNN`.
- **The pick is a `D-NNN` block, never a concept edit.** The chosen
  concept's Status points at the deciding block; parked concepts keep
  their IDs and their reasons. When the deciding block is later
  reversed, the Status lines re-point — the old winner to
  `parked — pick reversed (→ D-NNN)`, the new one to its choosing
  block — concept-sprint's write, prompted by decision-log's
  blast-radius sweep, so the sprint file never claims a choice the
  log has overturned.
- **Iteration needs a source after the pick.** Before it, the sprint
  file is freely editable — divergence is the point, and adding or
  reshaping a concept needs no justification. After it, the sprint
  file is a record: the chosen direction evolves through decisions,
  and a parked concept reopens only on a named trigger — an `E-NNN`,
  a changed constraint (`given`), or a stakeholder call recorded as a
  `D-NNN` with the judgment labeled. Taste alone reopens nothing.

## Decision block format (decisions.md)

File header: `# Decisions` + `<!-- weaveworm decision-log v1 -->`.

```markdown
## D-012 <the decision, one sentence>
- **Brief:** B-001
- **Because:** <rationale — cites E-NNN entries, a constraint, or labeled judgment>
- **Rejected:** C-002 — <one-line why>; <non-concept alternative> — <one-line why>
- **Reverses on:** <the observation that would overturn this>
- **Confidence:** medium — weakest load-bearing entry is E-007   (or `(untested)`)
- **Status:** standing
```

Decision rules:

- **The bar is traced-or-contested.** A choice earns a `D-NNN` when a
  downstream artifact traces to it (a flow stage, a prototype screen,
  a test task), or when it rejected a real alternative someone could
  reopen. "One page vs. a wizard" qualifies; a button color doesn't,
  unless a constraint made it contested. Both failure modes are
  critique's to police: a stage tracing to no decision gets one
  minted, and a decision nothing traces to is flagged as noise — it
  keeps its ID, flagged, never deleted.
- **`Reverses on:` is mandatory.** A decision nothing could overturn
  is taste wearing a rationale; naming the overturning observation is
  what makes the log testable, and it is where usability-test tasks
  come from.
- **Statuses mirror the contradiction discipline**: `standing` |
  `reversed (→ D-NNN)`. When the named observation happens, the old
  block gains the pointer and the new block cites the evidence — a
  reversed decision is never edited into agreement.
- **Writing against a `validated` brief downgrades it.** A new or
  reversing `D-NNN` on a validated brief flips that brief's Status to
  `in-design — revalidation needed (→ D-NNN)` in the same pass, per
  the brief lifecycle. Validation is pinned to the decision set it
  covered; the log is where that pin is enforced.

## Flow file format (flows/F-NNN-<slug>.md)

One flow per brief × scope. Header:

```markdown
# F-002 <flow name> — B-001
<!-- weaveworm flow-map v1 -->
- **Brief:** B-001
- **Role:** U-002
- **Journey:** J-003.4
- **Concept:** C-004 (→ D-012)
```

Then numbered stages, and a closing Edges section:

```markdown
### F-002.1 <stage name>
- **Step:** <what the user does>
- **State:** <what the system shows — content and behavior, never visual style>
- **Decision:** D-012

## Edges
- **Error:** at F-002.3 — <what the user sees and can do> (D-015)
- **Empty:** at F-002.1 — <the first-run state> (D-016)
- **Interrupted:** not handled (open)
```

Flow rules:

- **At most 8 stages**, matching journeys; finer grain belongs in a
  narrower-scoped flow.
- **Every stage traces to a decision** — its `Decision:` line names
  the `D-NNN` behind it, or reads `— (needs one)`, which critique
  flags and decision-log resolves.
- **The Edges section is required per flow, anchored per stage.** It
  covers error, empty, and interrupted at minimum, each edge naming
  the `F-NNN.S` it branches from. An unhandled edge is written
  `not handled (open)` — a line, never a silence — and additional
  edge kinds are welcome. An edge whose handling is load-bearing gets
  its own `D-NNN` like any stage.
- **Flow lifecycle mirrors decision reversal.** A current flow
  carries no Status line. When material change supersedes one
  (reordered or re-scoped stages, a re-picked concept), the
  replacement is a fresh `F-NNN`, and the old file's header gains
  `- **Status:** superseded (→ F-NNN)` — the one edit ever made to
  a superseded flow; the record stays.

## Prototype format (prototypes/B-NNN/)

`index.html` plus `README.md`, per brief. Rules:

- **Self-contained** — no external requests, no build step, opens
  from file. Styled as the *user's product*, never weaveworm's brand.
- **Every screen is annotated**: its screen-level container carries
  `data-flow="F-002.3"` naming the stage it renders, and the README
  maps screen → `F-NNN.S` → `D-NNN`, so critique and deliver trace
  the prototype without reading markup.
- **Fidelity is bounded by the test seeds.** Anything a test task
  touches works: the happy path and every named edge are interactive.
  Everything else is static. Content is real-shaped where the content
  *is* the design (labeled as sample data in the README, never passed
  off as real). Beyond what a task exercises, polish is pixel theater
  — cost without information.
- **The README ends with the test seeds**: the task list a
  usability-test-kit run would use, one task per flow, each phrased
  as the user's goal with the success state the brief's `Done when:`
  cares about. The seeds are the `reviewed → validated` bridge — the
  exact handoff research-plan and usability-test-kit pick up.

## Critique format (critiques/<date>-B-NNN.md)

A dated pass, never edited after — the next pass is a new file. A
second pass on the same brief the same day suffixes the filename
`-2`, `-3`… (define's archive rule; a pass is never overwritten).
Header:

```markdown
# Critique — B-001 — <date>
<!-- weaveworm design-critique v1 -->
- **Brief:** B-001
- **Against:** charter (agreed 2026-08-01), O-003, J-003, decisions through D-021 (this brief's highest at pass time)
```

Then one section per lens, fixed set, in this order:

1. **Constraints** — was any charter or brief constraint traded away?
   Findings cite the constraint line and the offending artifact.
2. **Non-goals** — did scope creep past a written Non-goal or
   `Out of scope:` line?
3. **Shifts** — the journey shifts the brief cites: delivered,
   contradicted, or dropped? Each gets named.
4. **Roles** — does the design serve the cited `U-NNN`s, and did an
   uncited role become the real audience?
5. **Traceability** — both directions: stages and screens with no
   decision behind them; decisions nothing traces to.
6. **Debt census** — the count of `(untested)` decisions and
   `(assumption)` lines, with the research-plan seeds they imply.

Verdict per lens: `clean`, or findings citing IDs. Never a score —
a number is how a critique stops being argued with.

Critique's gating role, settled: **a partial gate.** A pass where
lenses 1 and 2 come back clean writes the brief's Status to
`reviewed (<date>, → D-NNN)`, the pick pointer carried forward —
design-critique's only write outside its own file (`parked` aside,
which any skill records). Critique never writes `validated`; it
mints no evidence, so
only cited test entries do that, per the brief lifecycle. And
`reviewed` is not a resting place: a brief sitting there with no
`Q-NNN` naming its test seeds is a standing finding in every
subsequent pass, and an override-pulled or draft-charter brief keeps
that named in every pass too.

## Open decisions

All settled 2026-09-01; item 8 claimed by deliver 2026-09-02:

1. ~~Brief status lifecycle, and whether `validated` requires a test
   or just a critique pass.~~ Resolved — both, as a two-tier gate:
   a clean critique writes `reviewed` (the partial gate — ready to
   test, deliberately not done), only cited test evidence writes
   `validated`, and validation is pinned to the decision set it
   covered, decaying when a later decision lands. See Brief format.
2. ~~The concept-distinctness rule.~~ Resolved — mechanism *and*
   trades must both differ; the swap test on `Trades:` lines is the
   write-time check; same-mechanism variations fold into `Variants:`.
   See Concept block format.
3. ~~Decision granularity.~~ Resolved — traced-or-contested: logged
   when a downstream artifact traces to it or a real alternative was
   rejected, with critique policing both failure modes. See Decision
   block format.
4. ~~Flow edge-case discipline.~~ Resolved — a required per-flow
   Edges section, each edge anchored to its stage; error, empty, and
   interrupted at minimum; unhandled edges written as open lines. See
   Flow file format.
5. ~~Prototype fidelity policy and annotation mechanism.~~ Resolved —
   fidelity bounded by the test seeds (what a task touches works, the
   rest is static); `data-flow` attributes plus the README map. See
   Prototype format.
6. ~~Whether critique gates transitions or advises.~~ Resolved — a
   partial gate: clean constraint and non-goal lenses write
   `reviewed`; critique never writes `validated`. See Critique
   format.
7. ~~The assumption-led path for teams with no define artifacts.~~
   Resolved — see Standalone fallback: intake questions per missing
   artifact, answers as labeled assumptions in the brief, critique
   counts the debt, citations backfilled when define lands.
8. ~~What exactly deliver will pull — which of these artifacts is
   the handoff surface.~~ Claimed — flows (each stage and edge
   becomes a criterion), decisions (carried with their `Reverses on:`
   lines as what the build may not change), and the prototype
   (its `data-flow` annotations and README map normative, its markup
   and sample data incidental), plus the brief's `Done when:` and the
   `OC-NNN` metrics it moves, the brief's open questions, and the
   findings of the critique pass that made it pull-able, as the
   spec's Open items. A brief is pull-able at `reviewed` or
   `validated`; `in-design` only on the user's explicit override,
   recorded on the spec. See deliver-spec.md, Upstream contract.
