# Design spec — v1 (draft skeleton)

> **Status: scaffold.** The contract below is the planned shape — decided
> at the structural level, open at the field level. Sections marked
> `TODO` are unwritten; the Open decisions list at the bottom is the
> work remaining before any skill ships. Nothing here is consumed by a
> published skill yet.

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

TODO: the assumption-led path (no define artifacts at all — how much
of design legitimately runs on labeled assumptions before it becomes
dishonest).

## Brief format (briefs/B-NNN-<slug>.md)

TODO. Planned fields: heading restating the opportunity as the
design's job (one sentence, problem-shaped); `Pulls:` (the `O-NNN`,
pursued date); `For:` / `Journey:` / `Moves:` (roles, shift, outcomes
— all cited, never restated); `Constraints:` (inherited `given` lines
plus brief-local ones); `Out of scope:`; `Done when:` (the observable
state, tied to the outcome's metric); `Open questions:`. Status
lifecycle TODO — likely `open → in-design → validated | parked`.

## Concept block format (concepts/B-NNN.md)

TODO. Planned shape: a sprint file per brief; `C-NNN` blocks each
one mechanism-in-a-phrase heading with `Mechanism:` (how it works, as
experience), `Serves:` (which shifts/outcomes), `Trades:` (what it
costs against which constraint), `Status: chosen (→ D-NNN) |
parked — <reason>`. Floor of 3 genuinely distinct directions before
any is chosen — distinctness rules TODO. The pick itself is a `D-NNN`
block, not a concept edit.

## Decision block format (decisions.md)

TODO. Planned fields: heading as the decision in one sentence;
`Brief:`; `Because:` (rationale citing evidence, constraints, or
labeled judgment); `Rejected:` (alternatives with one-line whys —
including parked `C-NNN`s); `Reverses on:` (the observation that
would overturn it); `Confidence:` per inheritance rules or
`(untested)`. Statuses TODO — likely `standing | reversed (→ D-NNN)`,
mirroring the contradiction discipline.

## Flow file format (flows/F-NNN-<slug>.md)

TODO. Planned shape: one flow per brief × scope; header cites
`Brief:`, `Role:`, `Journey:` (the `J-NNN.S` moment it redesigns);
numbered stages `### F-NNN.S <stage>` with `Step:` (what the user
does), `State:` (what the system shows — content and behavior, not
visual style), `Edges:` (error/empty/interrupted paths — TODO whether
mandatory per stage or per flow). Stage cap TODO (likely 8, matching
journeys). Every stage traces to a decision or gets one.

## Prototype format (prototypes/B-NNN/)

TODO. Planned rules: self-contained HTML — no external requests, no
build step, opens from file; styled as the *user's product*, never
weaveworm's brand; every screen annotated with the `F-NNN.S` it
renders (mechanism TODO — likely `data-flow` attributes plus a
README.md mapping screens → flows → decisions); interactive enough to
test the flow's happy path and named edges, no more. The prototype's
README ends with test seeds: the task list a usability-test-kit run
would use, one task per flow. Fidelity policy TODO — where "real
enough to test" ends and "pixel theater" begins.

## Critique format (critiques/<date>-B-NNN.md)

TODO. Planned shape: a dated pass, never edited after — findings
against fixed lenses: charter constraints (violated?), Non-goals
(crept?), journey shifts (delivered, contradicted, or dropped?),
role coverage, decision consistency (does the artifact trace?),
`(untested)` census. Findings cite IDs; verdict per lens, not a
score. TODO: whether critique gates a status transition (e.g. brief
→ `validated`) or stays advisory.

## Open decisions

The field-level work, roughly in dependency order:

1. Brief status lifecycle, and whether `validated` requires a test or
   just a critique pass.
2. The concept-distinctness rule — what makes two concepts genuinely
   different directions rather than one direction twice.
3. Decision granularity — what's load-bearing enough to log; the
   failure mode on both sides (a log of everything is a log of
   nothing).
4. Flow edge-case discipline — mandatory edges per stage vs. per
   flow.
5. Prototype fidelity policy and annotation mechanism.
6. Whether critique gates transitions or advises.
7. The assumption-led path for teams with no define artifacts.
8. What exactly deliver will pull — which of these artifacts is the
   handoff surface (likely flows + decisions + prototype, but that's
   deliver's spec to claim).
