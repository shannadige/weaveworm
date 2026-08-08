# Design spec — v1 (draft)

> **Status: scaffold — decisions closed.** The contract below is
> decided at the structural and doctrinal level: the open decisions at
> the bottom are resolved (bar what deliver owns). Sections marked
> `TODO` still owe exact field-by-field wording, written against the
> resolved rules. Nothing here is consumed by a published skill yet.

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
the artifact's file(s) first. Each kind counts independently. Upstream
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

TODO — carries define's rules verbatim (weakest load-bearing entry;
only the evidence log raises a level; assumptions labeled, not
laundered) plus the design-stage corollary: **a decision's confidence
never exceeds the opportunity it serves.** Exact wording pending.

## Upstream contract

Design reads, and never writes:

- `define/opportunities.md` — **only `pursued` blocks are pull-able.**
  An open opportunity is not designable; the honest route is back to
  opportunity-map to make the call. TODO: exact behavior when a user
  insists on designing an open block.
- `define/charter.md` — Constraints are what design may not trade
  away; Non-goals are a write-time gate on brief and concept scope;
  `OC-NNN` metrics are what prototypes and tests get measured against.
  TODO: behavior against a `draft` (never-agreed) charter.
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

What the user can't answer becomes a brief Open question — a
research-plan seed, never a blocker. Critique prices the debt rather
than gating on it: alongside the `(untested)` census it counts the
brief's `(assumption)` lines, and a design whose load-bearing lines
are mostly assumptions gets that named in the verdict, with define as
the pointed-to fix.

Promotion, not rewrite: when define artifacts appear later, backfill —
`Pulls:` gains its `O-NNN`, population phrases and prose moments gain
`U-NNN` / `J-NNN.S` citations, constraint lines re-point at the
charter. Backfilling citations is an allowed edit; the brief heading
never changes.

## Brief format (briefs/B-NNN-<slug>.md)

TODO. Planned fields: heading restating the opportunity as the
design's job (one sentence, problem-shaped); `Pulls:` (the `O-NNN`,
pursued date); `For:` / `Journey:` / `Moves:` (roles, shift, outcomes
— all cited, never restated); `Constraints:` (inherited `given` lines
plus brief-local ones); `Out of scope:`; `Done when:` (the observable
state, tied to the outcome's metric); `Open questions:`.

Status lifecycle — routing statuses, opportunity-style, each written
by the skill that causes the transition:

- `open` — brief written; no sprint yet.
- `in-design` — written by concept-sprint when the sprint file opens.
- `validated (<date>)` — the brief survived contact with users: a
  completed usability test whose `E-NNN` entries are cited by the
  brief's load-bearing decisions. Written in the same re-cite pass
  that clears those decisions' `(untested)` markers — a critique pass
  never confers it. Critique flags readiness; only the evidence log
  raises a level.
- `parked — <reason>` — shelved; the ID and file stay.

## Concept block format (concepts/B-NNN.md)

TODO. Planned shape: a sprint file per brief; `C-NNN` blocks each
one mechanism-in-a-phrase heading with `Mechanism:` (how it works, as
experience), `Serves:` (which shifts/outcomes), `Trades:` (what it
costs against which constraint), `Status: chosen (→ D-NNN) |
parked — <reason>`. The pick itself is a `D-NNN` block, not a concept
edit.

Floor of 3 genuinely distinct directions before any is chosen.
Distinctness is mechanism-deep and trade-visible: two concepts are
different directions only if their mechanisms differ **and** the
difference shows in their `Trades:` lines — three ideas that trade
away the same things are one direction in three costumes. Enforced
the way roles enforce it: every concept after the first carries
`Distinct from: C-NNN — <the mechanism difference>`. When a sprint
can't honestly reach 3, the skill pushes back once with divergence
prompts (invert a constraint; serve the shift by removing something);
if the user insists, the pick proceeds and the choosing `D-NNN`
records `chosen from a field of 2 — divergence floor unmet`, where
critique counts it.

## Decision block format (decisions.md)

Planned fields (exact wording TODO): heading as the decision in one
sentence; `Brief:`; `Because:` (rationale citing evidence,
constraints, or labeled judgment); `Rejected:` (alternatives with
one-line whys — including parked `C-NNN`s); `Reverses on:` (the
observation that would overturn it); `Confidence:` per inheritance
rules or `(untested)`.

What's load-bearing enough to log — the granularity rule, both sides:

- **Demand-driven.** A decision is minted when something downstream
  needs to trace to it: flow-map's "every stage traces to a decision
  or gets one" is the pump, prototype behaviors pull the same way,
  and the concept pick always logs. Nobody logs to feel decisive.
- **The block format is the filter.** A real decision can fill both
  `Rejected:` (an alternative someone would actually have taken) and
  `Reverses on:` (an observation that would overturn it). A choice
  that can't fill both honestly is taste or detail — legitimate, just
  not log-worthy. Same falsifiability discipline as challenge
  sentences.

Statuses: `standing | reversed — <what was observed> (→ D-NNN)` —
the contradiction discipline: a reversed decision keeps its ID and
points at its replacement; the corrected choice is a new block. No
draft state — a decision is made or it isn't logged; a tentative
choice is an unpicked concept or an open question, not a log entry.

## Flow file format (flows/F-NNN-<slug>.md)

Planned shape (exact wording TODO): one flow per brief × scope;
header cites `Brief:`, `Role:`, `Journey:` (the `J-NNN.S` moment it
redesigns); numbered stages `### F-NNN.S <stage>` with `Step:` (what
the user does), `State:` (what the system shows — content and
behavior, not visual style), `Edges:` (error/empty/interrupted
paths). Every stage traces to a decision or gets one.

`Edges:` is per stage and explicit-empty: every stage carries the
line, and `none — <why this stage can't fail>` is a legitimate value
— so silence is never ambiguous between "can't fail" and "didn't
think about it." The named edges are the prototype's interactivity
contract and the source of the test seeds' edge tasks.

Stage cap: at most 8, matching journeys, with the same escape — finer
grain belongs in a narrower-scoped flow.

## Prototype format (prototypes/B-NNN/)

Structural rules: self-contained HTML — no external requests, no
build step, opens from file; styled as the *user's product*, never
weaveworm's brand. The prototype's README ends with test seeds: the
task list a usability-test-kit run would use, one task per flow —
happy path plus that flow's named edges.

Fidelity policy — the test seeds set the budget:

- Everything a seeded task touches behaves: the happy path and the
  stage-named edges. Nothing else needs to.
- Content on tested screens is realistic — participants read content,
  so placeholder text there is a defect, not a shortcut. The one
  place *more* fidelity is mandatory.
- Visual polish goes only as far as a standing `D-NNN` requires. Past
  that line is pixel theater — effort that raises confidence in the
  artifact without raising evidence for any decision — and critique
  counts it.

Annotation — both mechanisms, so they can be diffed: each screen's
container carries `data-flow="F-NNN.S"`, and the README maps screens
→ `F-NNN.S` → `D-NNN`. A screen present in one and absent from the
other is a critique finding.

## Critique format (critiques/<date>-B-NNN.md)

A dated pass, never edited after. Findings cite IDs; verdict per
lens, never a score.

The lens list is fixed and closed — seven, every pass: charter
constraints (violated?), Non-goals (crept?), journey shifts
(delivered, contradicted, or dropped?), role coverage, decision
traceability (does the artifact trace?), the `(untested)` census,
the `(assumption)` census. A closed list is what makes dated passes
comparable — and a skipped lens a detectable defect.

Critique is advisory, never a gate: `validated` is evidence-gated
(see the brief lifecycle), and critique prices debt rather than
blocking on it. What keeps advisory from meaning ignorable is
carry-forward: each pass opens by re-listing the prior pass's
findings, each with a disposition — `fixed (→ D-NNN)`,
`accepted — <why>`, or `open`. A finding can be overruled; it can
never vanish. Exact block wording TODO.

## Open decisions

The decision record — resolved 2026-08-08 except what deliver owns:

1. ~~Brief status lifecycle.~~ Resolved — `open → in-design →
   validated (<date>) | parked — <reason>`; `validated` requires
   cited test evidence, never a critique pass. See Brief format.
2. ~~The concept-distinctness rule.~~ Resolved — different mechanism
   whose difference shows in the `Trades:` lines, enforced by
   `Distinct from:`; the floor of 3 pushes back once, then yields
   with the debt recorded in the choosing decision. See Concept
   block format.
3. ~~Decision granularity.~~ Resolved — demand-driven minting (flow
   stages and prototype behaviors pull; concept picks always log)
   plus the both-fields test: `Rejected:` and `Reverses on:` must
   fill honestly. See Decision block format.
4. ~~Flow edge-case discipline.~~ Resolved — per stage,
   explicit-empty (`none — <why>`); stage cap 8. See Flow file
   format.
5. ~~Prototype fidelity policy and annotation mechanism.~~ Resolved —
   the test seeds set the fidelity budget; `data-flow` attributes
   plus the README map, diffable. See Prototype format.
6. ~~Whether critique gates transitions or advises.~~ Resolved —
   advisory with carry-forward dispositions; fixed, closed list of
   seven lenses. See Critique format.
7. ~~The assumption-led path for teams with no define artifacts.~~
   Resolved — see Standalone fallback: intake questions per missing
   artifact, answers as labeled assumptions in the brief, critique
   counts the debt, citations backfilled when define lands.
8. What exactly deliver will pull — which of these artifacts is the
   handoff surface (likely flows + decisions + prototype, but that's
   deliver's spec to claim). Stays open; not this spec's to close.
