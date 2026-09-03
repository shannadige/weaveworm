---
name: design-brief
description: "The first stage of design — turn a pursued O-NNN opportunity into a B-NNN design brief: the design's job as one problem-shaped sentence, with roles, journey moment, outcomes, and inherited constraints cited from define, never restated. Use when a designer says \"let's design this\", \"start on O-003\", \"write the design brief\", \"kick off design for the pursued opportunity\", or an opportunity was just marked pursued and they want next steps. Do NOT use for choosing what to pursue (use define's opportunity-map), exploring solutions (use concept-sprint), or recording design decisions (use decision-log)."
---

# design-brief

The first stage of design, and the assumption boundary: concepts,
decisions, flows, and prototypes all cite the brief and never reach past
it. Input: a `pursued` block in `define/opportunities.md`, plus the
charter, roles, and journeys it cites, and the evidence log where cited
directly (ask once if define or research work lives elsewhere). Output:
`design/briefs/B-NNN-<slug>.md` (design root per the spec — ask once if
design work lives elsewhere) per the spec's brief format, Status `open`.
Read the spec at `${CLAUDE_PLUGIN_ROOT}/references/design-spec.md`
before your first write in a session — it owns the brief format, ID
rules, lifecycle, uncertainty markers, and the Standalone fallback; do
not improvise fields. Project artifacts (`research/`, `define/`,
`design/`, `deliver/`) live under the working directory the session
started in; read and write them by those relative paths and never `cd`.
`${CLAUDE_PLUGIN_ROOT}` and the folder above it are not the project,
even though that folder also has stage-named subfolders: they hold only
spec and voice files, are read-only, and are never listed, searched, or
written. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Brief rules

- **Only `pursued` blocks are pull-able.** An open opportunity isn't
  designable — the team hasn't chosen it, and a brief would launder
  that. Ask once, in the intake pass: is the team committing to this
  one? On a yes, record the pursue call yourself per the spec's
  Upstream contract — the block's Status becomes `pursued (<date>)`
  and the block moves under the `<!-- pursued -->` marker, the exact
  write opportunity-map would make, from this spec alone and never
  from the define skill file — then say in chat that the backlog was
  edited on the user's say-so, and cite `Pulls: O-NNN (pursued
  <date>)`. When the user wants the backlog left alone, proceed on
  explicit override per the spec — `Pulls: O-NNN — open, designed on
  user override (assumption)`, opportunities.md untouched — and say
  that critique will name the unpursued pull in every pass until
  someone records the call.
- **One brief per pursued opportunity, or one per coherent cluster.**
  Pursued blocks sharing one problem and one journey moment can share
  a brief; propose the cluster and let the user confirm it, never
  merge silently. Distinct problems get distinct briefs even when
  pursued together.
- **The heading restates the opportunity as the design's job** — one
  problem-shaped sentence, no solution named. "Trial users can reach
  a connected data source unaided" is a job; "a setup wizard" is a
  concept that hasn't earned a `C-NNN` yet. A solution the user leads
  with gets held as the first concept-sprint candidate and the job
  written as the problem it assumes — and say you did.
- **Cite, never restate.** `For:`, `Journey:`, `Moves:` carry
  `U-NNN`, `J-NNN.S`, and `OC-NNN` IDs — duplicated prose drifts
  from its source; an ID can't. In chat, IDs travel with names per
  the voice contract. A brief serving no journey shift names that
  gap on its own `Journey:` line rather than citing the nearest
  moment for cover.
- **`For:` is who the scope serves, checked at intake.** Before
  writing, hold `For:` against the shifts and `Done when:`: a role
  named on either with no shift in scope is a gap the brief would
  carry into every concept and flow. Ask in the intake pass, plainly
  ("Done when says the manager stops emailing, but every shift here is
  the resident's — keep the manager and name what changes for them,
  or narrow this to residents and reword Done when?"), and don't
  write until one is chosen; a dropped role with a real need becomes
  an Open question. Critique reports drift from this line; it does
  not gate on it, so the fix belongs here.
- **Constraints are inherited first, then local.** Every charter
  constraint that binds this brief comes over citing the charter and
  carrying its `given (<source>)`. Brief-local limits the intake
  surfaces are marked `(brief)` plus `given (<source>)` or
  `(assumption)`. Never invent a constraint the user didn't state
  and no artifact carries — a plausible-sounding limit nobody set is
  scope theater.
- **Non-goals gate at write time.** Before writing, check the brief's
  scope against the charter's Non-goals: a brief landing inside one
  is either stopped with that reason or the Non-goal is explicitly
  challenged back to product-charter — never both kept silently. The
  Non-goals bordering this brief go on `Out of scope:`, with any
  brief-local exclusions, so concept-sprint inherits the fence.
- **`Done when:` is an observable state**, tied to the metric of the
  `OC-NNN` the brief moves — the state a usability test would
  confirm, never a deliverable list. "The prototype ships" is a
  deliverable; "a first-run user reaches a connected source without
  help" is done. This line is the brief's contract with validation;
  write it like a test will read it, because one will.
- **`Charter:` records what was read at pull time** — `agreed
  <date>`, `draft (as read <date>)`, or `none — assumption-led`. A
  draft charter is usable; teams design against moving strategy all
  the time. What it can't provide is charter-agreement, so record
  the draft state plainly and say critique will recheck against the
  charter as it stands at critique time.
- **Standalone fallback.** Missing define artifacts never stall the
  brief — the dependency is on information, not files. Per missing
  artifact, ask the spec's intake floor in one batched pass: no
  opportunities.md → the problem, for whom, why now (`Pulls: none —
  assumption-led`, heading `(assumption)`-labeled); no charter →
  what can't be traded away and who set each limit, what's not this
  design's job, what observable state means done; no roles or
  journeys → who it's for and which moment of their workflow it
  changes, as a plain population phrase and a prose moment. What the
  user can't answer becomes an Open question — a research-plan seed,
  never a blocker or a re-ask.
- **Open questions are seeds, not residue.** Each one is phrased so
  research-plan could lift it into a `Q-NNN` unchanged — what the
  brief needs that nothing upstream answers.
- **Re-runs update, never duplicate.** Same job, new upstream state →
  edit per the spec's allowed list: everything but the heading, and
  backfilling citations when define artifacts land is the expected
  edit, not an exception. A different job is a new brief.
  This skill writes `open`, and `parked` on the user's call —
  recording the prior Status per the spec's `(was <status>)` form and
  restoring it verbatim when the user unparks, so a brief parked
  mid-design comes back mid-design; `in-design`, `reviewed`, and
  `validated` belong to concept-sprint, design-critique, and
  decision-log.

## After the brief

Report per the voice contract: the file path, the job sentence, then
one line each for what it pulls, who it serves, what it moves, and
the constraint set — plus the state line ("B-003 open: pulls O-003
(trial users reach a connected source unaided), 4 constraints (1
brief-local), 2 open questions"). The decision this
artifact exists for: is this brief's scope one concept sprint or two,
and what's the first question that sprint has to answer — name your
read and the one-line why. If the brief is assumption-led or
override-pulled, say which single step (a research-plan question,
recording the pursue call) would firm it up before concepts start.

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash inside a sentence (a comma, a parenthesis, or a second sentence
instead); every ID travels with its name, and a status or marker is
said in words rather than quoted as syntax; the state line this skill's
report names is the second-to-last line; the last line is the single
first step, stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## What this skill refuses

- Designing from an open opportunity without either the user's
  pursue call recorded per the spec or the explicit override path,
  and any edit to opportunities.md other than that one pursue write.
- Inventing constraints, or restating upstream prose the brief should
  cite.
- A solution in the heading — it's held as a concept-sprint candidate
  and the job written problem-shaped, and you say so.
- Minting upstream IDs — an absent artifact gets labeled assumptions
  per the Standalone fallback, never a fabricated citation.
- Editing a brief heading — a different job is a new brief.
