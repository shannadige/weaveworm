---
name: build-spec
description: "The handoff stage of deliver — turn a reviewed brief's flows, decisions, and prototype into an S-NNN build spec: one acceptance criterion per flow stage and per edge citing the D-NNN behind it, the load-bearing decisions carried with what would reverse them, the prototype marked normative or incidental, and the open items packaged for a human engineer or a coding agent. Use when a designer says \"write the spec\", \"hand this to engineering\", \"what does the build need to do\", \"give my agent something to build from\", or a critique just came back clean. Do NOT use for choosing the design (use design's concept-sprint), mapping flows (use design's flow-map), splitting the work into increments (use slice-plan), or reviewing what got built (use build-review)."
---

# build-spec

The handoff stage of deliver, and the stage's assumption boundary:
slices, instruments, reviews, and outcomes all cite the spec and
never reach past it. Input: a brief at a spec-able status, its
current flows (never a superseded one), the decisions those flows
trace to in `design/decisions.md`, the prototype's README map, the
newest critique, and the charter lines the brief cites (ask once if
design, define, or research work lives elsewhere). Output:
`deliver/specs/S-NNN-<slug>.md` (deliver root per the spec — ask
once if delivery work lives elsewhere) per the spec's build spec
format, Status `open`, and `handed off` at the close on the user's
word. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/deliver-spec.md` before your first
write in a session — it owns the spec format, criteria rules,
lifecycle, recipient packaging, and the Standalone fallback; do not
improvise fields. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Spec rules

- **The intake floor, one batched pass before writing:** who
  receives this — a human engineer or a coding agent — asked once per
  session and reused; which of the brief's flows are in scope (all
  current ones unless the user narrows it); and which of the
  critique's carried findings the user can settle right now. Nothing
  else is asked while design is on file; when it isn't, the
  Standalone fallback's questions below join this same pass. The
  builder's questions are the Open section's job, not intake's.
- **`reviewed` and `validated` briefs are spec-able.** A clean
  critique proves the design is still on charter; a usability test
  before building is welcome and not required. Check that the
  status hasn't outlived its pass: design never reverts `reviewed`,
  so a newer critique with a Constraints or Non-goals finding means
  a fresh pass comes first — say so in product terms ("the latest
  critique found the design trading away a constraint; the status
  predates it"). An `in-design` brief, `revalidation needed`
  included, gets one redirect — the critique is a single run, and
  it's what proves the charter wasn't traded away — then proceeds on
  explicit override per the spec's `Brief:` form with the full
  status carried, and the plain warning that build-review will name
  the missing critique in every pass. An `open` brief is never
  spec-able: nothing has been chosen, so there's nothing to build. A
  `parked` brief routes to design-brief to unpark. The brief itself
  is never edited.
- **The heading is the brief's heading, verbatim, plus its ID.** A
  brief heading never changes, so the copy can't drift; a different
  job is a different brief and a different spec. `Brief:` records the
  status and pick pointer read at pull time; `Critique:` names the
  pass that made the brief spec-able and which findings ride into
  Open, or says why there is no pass, in the spec's forms.
- **One criterion per flow stage and one per Edges line, in flow
  order, edges after their flow's stages.** Nothing merged, nothing
  skipped: a stage with no criterion is a stage the builder will
  improvise. Each heading cites its stage and decision; each `Check:`
  is one observable line — what the user does, and what they then
  see. Never implementation (no component, endpoint, table, or event
  names), never visual style. That line is precise enough for an
  agent to turn into a test and for a human to confirm by hand; the
  spec writes no test code. An edge with no decision of its own
  cites its anchor stage's; an open edge the flow left unanchored
  heads by kind and stage with no decision cited.
- **A stage with no decision behind it stops the write.** A flow line
  reading `— (needs one)` means the design hasn't decided; a
  criterion written over it encodes taste as a requirement. Route to
  design's decision-log, then resume — say which stage and why. This
  stop needs a flow file to say it; with no decision log at all, the
  Standalone fallback's stand-ins apply instead.
- **An open edge is an open criterion.** `not handled (open)` in the
  flow becomes a criterion whose Check line says no handling is built
  and points at the Open item that will settle it. Silence here is
  the one thing a coding agent will fill on its own.
- **Must not change carries every standing decision the flows trace
  to**, each with its `Reverses on:` line verbatim, plus any decision
  that promotes a prototype rendering. This list is what tells the
  builder which choices are load-bearing; a decision missing from it
  is one the build may reverse without anyone noticing. `Decisions:
  through D-NNN` pins the set — the highest decision this brief's
  artifacts trace to — and that pin is what every downstream skill
  measures staleness against.
- **The prototype line always draws the normative/incidental line
  explicitly**, even when nothing is promoted: stage annotations and
  the README map are the design; markup, styling, copy, and sample
  data are placeholders. A rendering becomes normative only through
  a cited decision, written `promoted: <what> (D-NNN)` — never
  because it looked finished. The README map is read at
  `design/prototypes/B-NNN/README.md` and nowhere else by default; a
  README found at any other path (nested inside the prototype folder,
  say) still supplies the map, but its location is a design-side
  defect owned by prototype, named in the `## For the builder`
  preamble with the path it was found at, and repeated in the report.
  Reading it silently would tell the builder the design is in order
  when the next skill to look for the map will not find it.
- **Recipient packaging changes two things and nothing else.** The
  preamble under `## For the builder` and the Open section's heading:
  `## Handoff agenda` for a human, read as the questions to settle
  together; `## Stop conditions` for an agent, read as what it may
  not decide alone, with the preamble telling it to build from the
  criteria, treat Must not change as fixed, and stop and ask rather
  than choose a default. Criteria, Must not change, and the Open
  items themselves are identical for both — every item is the
  question in product terms plus the criterion it blocks (or `blocks
  none; informs <what>`); a human can skip precision they don't
  need; an agent can't invent precision that isn't there. Open items
  come from four places: the critique's carried findings, open
  edges, the brief's open questions that bear on the build, and
  intake gaps. An item that could only be answered by reading a spec
  is misphrased. The recipient can change later on the user's word:
  the line, preamble, and heading swap together, nothing else moves.
- **A design change after handoff is a fresh spec, never an edit.**
  Until handoff, a re-run regenerates the `open` spec in place, ID
  kept, and says so. From `handed off` on, compare the brief's
  highest traced decision to the pin on any re-run. If it moved,
  write the successor with `Supersedes: S-NNN`, add
  `superseded (→ S-NNN)` to the old spec's Status — the one edit ever
  made to it — and say that shipped slices stay on record while
  slice-plan will name what replaces the unshipped ones. If the pin
  holds, the only edits are the spec's allowed list: Status, Open
  items gaining `settled: <answer> (<date>)`, and citation backfill.
  Criteria text never changes; a criterion an answer would change is
  the fresh-spec case.
- **Standalone fallback.** Missing design artifacts never stall the
  spec — the dependency is on information, not files. Walk the
  prototype with the user in one batched pass per the spec's intake
  floor: no brief → the job, for whom, done-when, and the number it
  moves (`Moves:` cites the `OC-NNN` when a charter names it, and
  reads `none named (assumption-led)` otherwise); no flows → per
  screen, what the user does and sees, and what happens on error,
  empty, and interrupted; no decision log → which choices matter,
  why, and what would change the user's mind; no charter → what
  can't be traded away and who set it. Answers become
  `(assumption)`-labeled criteria and Must not change lines, with
  prose moments standing in for stage citations and the Must not
  change phrase standing in for the decision; unanswered edges
  become open criteria; never a minted ID, never a blank. When
  design or the charter lands later, backfill citations, `Moves:`
  included, and walk the same backfill into the slice and
  instrument lines that carried the stand-ins — the one edit a
  criterion ever takes.
- **Handoff is a status the user writes through you.** The spec is
  `open` until the user confirms it's going to a builder; then
  `handed off (<date>, to human | agent)`. Confirming is the run's
  forced decision, never assumed from the spec existing.

## After the write

Report per the voice contract: the file path, then one line each for
the criteria (how many from stages, from edges, and open), the
decisions carried, the open items, and the recipient — plus the state
line ("S-001 open: B-001 (trial users reach a connected source
unaided), 11 criteria (7 stages, 3 edges, 1 open), 6 decisions
carried, 3 stop conditions, for an agent"). The decision this artifact
exists for: does this hand off now, or which open item has to close
first — name your read and the one-line why. If the spec is
override-pulled or assumption-led, say which single step (the
critique run, a decision-log entry for the undecided stage) would
firm it up before a builder starts.

## What this skill refuses

- A spec from an `open` brief, or from an `in-design` one without
  the explicit override path.
- A criterion over a stage with no decision — the route is
  decision-log first.
- Implementation names, visual style, or test code in a Check line.
- Editing a handed-off criterion beyond a citation backfill — a
  changed design is a fresh spec.
- Promoting a prototype rendering to normative without a cited
  decision, or lifting prototype markup into the spec as
  requirements.
- Tickets, estimates, owners, sequencing, or dates — what ships
  first is slice-plan's; the rest belongs to the team's tools.
- Minting upstream IDs — an absent artifact gets labeled assumptions
  per the Standalone fallback, never a fabricated citation.
