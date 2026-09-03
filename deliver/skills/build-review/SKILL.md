---
name: build-review
description: "The gate stage of deliver — run a dated review of a build against its S-NNN spec through fixed lenses: criteria met, deviated, missing, or unverified; edges handled; standing decisions silently reversed; instruments firing; prototype scaffolding shipped as real. Verdicts per lens with cited IDs, never a score; deviations routed to the owning skill, never fixed here. Use when a designer says \"review the build\", \"does this match the design\", \"did they build what we decided\", \"check the staging build\", or a slice is about to ship. Do NOT use for code review, critiquing the design itself (use design's design-critique), or fixing what it finds."
---

# build-review

The gate stage of deliver: the pass that checks what got built
against what the design decided, before it ships. Input: a build
spec, the slice under review, the spec's decisions pin, the
instruments whose `Fires at:` falls in this slice, and the build
itself — a commit, a staging URL, a demo, or the user walking you
through it — plus `design/decisions.md` as it stands now, not as it
stood at handoff. Output: `deliver/reviews/<date>-S-NNN.md` per the
spec's build review format, and the writes this skill makes outside
its own file: the spec's Status to `built (<date>, through SL-NNN)`
when a clean pass covers the last planned slice, and an instrument's
Status to `firing` when its lens confirms it. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/deliver-spec.md` before your first
write in a session — it owns the lens set, the verdict forms, the
gate, and the routing rule; do not improvise lenses. Conversation
runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Review rules

- **The intake floor, one batched pass:** what is being reviewed and
  where (the build's location and who showed it), and which slice it
  claims. One named exception to the voice contract's batched-pass
  rule: reason-or-mistake is asked only when the Decisions lens
  finds a contradiction, because the question has no meaning until
  the contradiction is in front of the user. Nothing else; the input
  is the build and the artifacts as they stand. A build described
  rather than shown (an account in chat, a written report) is still
  input: `Reviewed:` names the secondhand account, and the pass runs
  on what it says and no further. A pass needs a slice
  file — with none on record, slice-plan comes first — and may run
  on a slice already `shipped`, where the gate lenses go on record
  and gate nothing and the Instruments lens is the point.
- **Staleness is named first.** Before any lens, compare the brief's
  highest traced decision to the spec's `through D-NNN` pin. If the
  design moved past the spec, the header says so, the verdicts still
  stand for the slice as reviewed, the gate still works (shipping a
  faithful build of a moved design is the team's call, made with the
  header in front of them), and the pass closes on the fresh spec as
  the next action. On an assumption-led spec there is no pin: the
  header reads `none — assumption-led`, the Decisions lens judges
  the `(assumption)` Must not change lines and quotes the line in
  place of an ID, and the Scaffolding census names the debt. Check
  the spec's Status in the same breath: one still `open` was never
  handed off, yet a build exists. The `Spec:` line says so, the
  lenses run and gate as usual, the `built` write is not made over
  `open` (Status moves forward in order), and the close names
  build-spec recording the handoff on the user's word ahead of any
  per-finding call; the next pass, counting this one, makes the
  write.
- **Fixed lenses, fixed order, verdict per lens.** Criteria, Edges,
  Decisions, Instruments, Scaffolding — all five run every pass, in
  that order, each closing `clean` or with findings citing `S-NNN.N`,
  `F-NNN.S`, `D-NNN`, or `I-NNN`. Every criterion in the slice, edge
  criteria included, is listed under Criteria as `met`, `deviated —
  <how>`, `missing`, or `unverified — <what the input lacked>`; an
  unlisted criterion is an unreviewed one.
  Edges is the open-edge check only — for each open criterion,
  `clear` when nothing was built over it or `filled — <what>` when
  something was, since a filled open edge is a decision the builder
  made alone. Instruments reads `none specified — OC-NNN
  unmeasurable until instrumentation-plan runs` when the spec's
  metric has no block, never `clean`; an instrument the input says
  nothing about is `silent`, with what the input lacked on the
  line, since only a confirmation is `firing`. Never a composite
  score: a number is how a review stops being argued with. Five
  sections and no more: the gate's outcome is read off Criteria and
  Decisions and reported in chat, never written as a sixth heading.
- **What the input can't show is unverified, never guessed.** A
  criterion the account is silent on is `unverified — <what the
  input lacked>`, and it holds the gate like `missing`; `deviated`
  claims the build was seen doing something else, and silence is
  not that. When the build is described rather than shown, every
  criterion the account does not cover is `unverified`, and a pass
  with every criterion `unverified` is still written: the file is
  the record that nothing was verified, and the report says what
  would verify it (a walkthrough, screenshots, the builder in the
  room). A decision the input cannot settle either way, with no
  contradiction found, is `cannot tell — <why>` under Decisions; it
  holds the slice like a contradiction, and it is a different thing
  from `undetermined`, which is only ever the user's answer once a
  contradiction is on the table. Say it in product terms ("the
  account gives a 24/48/72 cadence but not whether the manager set
  it, so D-001 can't clear from here").
- **A review is a dated record, never edited.** The next pass is a
  new file, suffixed `-2`, `-3` on the same day; the sequence is the
  build's audit trail. Fixes land in the build, and the next pass
  shows them landed.
- **A contradicted decision is the headline finding, and it holds
  the slice.** Written `contradicts D-NNN — <how>` plus one of three:
  `reason — <the limit found>, routed to decision-log`, when the
  builder hit something real (a constraint discovered in
  implementation, a rejected alternative that turned out necessary)
  — the user takes the limit to design's decision-log, which writes
  the new or reversing decision; the brief's validation lapses by
  its own rule, and a fresh spec follows; `mistake — S-NNN.N re-issued`, when the build simply
  diverged, and the slice is re-reviewed after the fix;
  `undetermined`, when the user can't say because the builder isn't
  in the room — the slice stays held and the next pass re-asks.
  Ask which it is during the pass, in product terms ("did they hit
  something that made the one-page layout impossible, or did it just
  come out different?"), never by citing the lens.
- **Findings route to owners; review never fixes.** A `missing` or
  `deviated` criterion goes back to the builder as its own line; a
  silent instrument to instrumentation-plan or the builder, whichever
  the finding names; leaked scaffolding to the builder with the
  spec's prototype line cited. This skill never edits the build, the
  spec, or any design artifact — a review that repairs what it found
  is an author reviewing itself.
- **The Scaffolding lens counts debt as well as leaks.** Sample data,
  placeholder copy, or incidental markup shipped as real is a
  finding; so is the census of the spec's `(assumption)` lines and
  its override notes — the missing critique behind an in-design brief
  specified on override, an assumption-led spec — named every pass
  until the owning artifact records the fix. Repetition is the point.
- **The gate is partial, and this skill holds it.** Criteria and
  Decisions clean lets the slice be recorded `shipped` (slice-plan
  writes that on the user's word). When, counting this pass and the
  review files on record, every slice not `dropped` has such a pass,
  write the spec's Status to `built (<date>, through SL-NNN)`; a
  slice cut later gets its own clean pass, which re-writes the
  pointer. A spec already `measured` keeps that Status, and the pass
  file is the record — say so. Edges, Instruments, and Scaffolding
  findings don't hold the slice — they're named, owned, and recur
  until fixed. A firing instrument gets its Status flipped to
  `firing (<date>, → reviews/<date>-S-NNN.md)` in the same pass; for
  a slice-boundary event that is the post-ship pass.

## After the review

Report per the voice contract: the file path, one line per lens with
its verdict, the headline finding if there is one, and the state
line ("review 2026-09-12, S-001 / SL-001 (connect a first source):
criteria 9 met, 1 deviated; decisions clean; 1 instrument silent").
Unverified criteria and cannot-tell decisions are counted there too
("criteria 1 deviated, 4 unverified; decisions 1 cannot tell"), with
one clause on what would verify them.
The decision this artifact exists for: ship, fix first, or log the
deviation as a decision — named per finding, in order of what holds
the slice. When the header says the spec is stale, the fresh spec is
the close, ahead of any per-finding call. When the gate cleared, the
close is the next step instead: slice-plan records it shipped, and
the window for reading the outcome starts from that date.

## What this skill refuses

- A score, grade, or any composite number standing in for verdicts.
- Editing the build, the spec, or any design artifact — the Status
  writes on a cleared gate and a confirmed instrument are the whole
  of its reach.
- Editing or superseding a past review — the next pass is a new file.
- Softening a contradicted decision into a suggestion, or writing
  `reason` or `mistake` without the user having said which.
- Reviewing code quality, architecture, or performance — this is
  fidelity to the design, and code review is someone else's tool.
- Dropping a standing finding because it was named last pass.
- A sixth section — the gate's outcome is read off Criteria and
  Decisions and reported in chat; check the headings against the
  five lenses before writing, and cut anything past Scaffolding.
- A verdict word the spec does not list, or `deviated` on a
  criterion the input never showed — silence is `unverified`.
