# Define spec — v1

Define turns discovery evidence into four artifacts, in sequence: a
product charter (challenges, vision, outcomes, metrics), user roles,
journey maps, and a prioritized opportunity backlog. Each artifact
exists to force a decision, and each section earns its place by being
cited downstream or by gating a write-time check — a section that does
neither is cut, not kept. Later stages cite these IDs the way define
cites `E-NNN`: point, don't re-argue.

## Files

Default root: `define/` in the user's project, next to `research/`. If
the user keeps definition work elsewhere, ask once, then reuse their
answer for the session.

```
define/
├── charter.md                 # challenges, vision, outcomes, metrics — one deliverable
├── charter-<agreed-date>.md   # archived superseded charters — one Status edit at archive time, never after
├── roles.md                   # all U-NNN role blocks
├── journeys/J-NNN-<slug>.md   # one journey per role × scope
└── opportunities.md           # all O-NNN blocks, ranked
```

`<slug>` is 2–5 lowercase hyphenated words. Skills create every file
and header themselves. Only opportunities.md carries a `Log:` pointer;
it does so on the whole set's behalf.

## ID table

| ID | Artifact | Lives in | Cited by |
|---|---|---|---|
| `CH-NNN` | Challenge | charter.md | outcomes, journeys, opportunities |
| `OC-NNN` | Desired outcome | charter.md | metrics, future-state shifts, opportunity Impact lines |
| `U-NNN` | User role | roles.md | charter `For:` lines, journeys, opportunity Who lines |
| `J-NNN` (stages `J-NNN.S`) | Journey | journeys/ | opportunity Journey lines |
| `O-NNN` | Opportunity | opportunities.md | the design stage |

All IDs follow the evidence log's discipline: sequential, zero-padded
to three digits (stage numbers `S` are plain integers), permanent —
never renumbered, reused, or deleted. The first ID is 001; next =
highest existing + 1 — scan the artifact's file(s) before writing,
creating files or directories if absent. For charter IDs, "the
artifact's files" includes every archived `charter-<date>.md`: a
superseding charter continues CH/OC numbering from the archive's
highest, never restarting — otherwise every downstream `Impact: moves
OC-002` silently re-points. Each kind counts independently. Dropped and
superseded items keep their IDs, and their files or blocks are never
deleted. Upstream IDs (`E-NNN`, `Q-NNN`, voices P/R/M) are discover's;
define cites them and never mints them.

## Uncertainty markers

One vocabulary, used identically by every define skill (discover's
unreachable-user fallbacks use `(unconfirmed)` the same way):

- `given (<source>)` — a constraint or fact with a source behind it;
  lives in the charter's Constraints section.
- `(assumption)` — believed but unevidenced; the honest label for
  mandate-driven claims and for stated guesses (including a user's
  unsized complexity guess).
- `(unconfirmed)` — a call made while the user was unreachable, or one
  the user could not settle, listed for their confirmation. A state to
  surface, not a reason to stall.
- `(ambition)` — a metric-target marker: the target is a stated
  aspiration, not derived from a benchmark or evidence.

## Confidence inheritance

Define consumes the evidence log; it never improves it. **Load-bearing**
means: the entries a claim would lose its support without. Corroborating
entries repeat what load-bearing ones establish and live on a
`Corroborates:` line, where they never move Confidence — so appending
weak corroboration can't make a strong claim look weaker. In order:

1. **Weakest link** — any define claim's Confidence is the weakest
   load-bearing entry it cites — the same floor rule discover's
   synthesis uses for themes.
2. **Only the evidence log raises a level** — new firsthand evidence,
   or a merge of independent firsthand entries, routed through
   discover's evidence-log. Writing define artifacts never changes an
   entry's level; if drafting surfaces stronger evidence, route it
   there first, then re-cite.
3. **Assumptions are labeled, not laundered** — an uncited claim is
   `(assumption)`; an uncited block's own Confidence line (challenge,
   role, or opportunity) reads `assumption-led — no evidence cited`;
   and a wholly uncited charter or journey additionally sets the
   header `- **Confidence:**` bullet as the at-a-glance flag — the
   bullet is required in that case and absent otherwise.
   Assumption-led is legitimate (mandates, greenfield); invisible is
   what it must never be.

Stakes carry over wherever the artifact has a Stakes field — challenge
and opportunity blocks; roles and journey stages read the cited
entries' `Stakes:` lines in place. Low confidence with high stakes
reads "verify cheaply before building", never "deprioritize". Retracted entries (see
Upstream contract) are never load-bearing.

## Charter format

```markdown
# Product charter — <product>
<!-- weaveworm product-charter v1 -->

- **Status:** draft
- **Owner:** <who carries this — or `unassigned`, never a guess>
- **Supersedes:** charter-<agreed-date>.md   (only when superseding; omit on a first charter)
- **Confidence:** assumption-led — no evidence cited   (only when wholly uncited)

## Challenges

### CH-001 <the challenge, one falsifiable sentence>
- **Evidence:** E-003, E-007
- **Corroborates:** E-011
- **Confidence:** medium — weakest load-bearing entry is E-007
- **Stakes:** high — carried from E-003
- **Contradicted by:** E-011 (→ CH-004)   (only on a contradicted challenge)

## Vision
<2–3 sentences: the future state the outcomes below add up to. No
feature names. Consumed as a write-time check: every outcome must serve
it, and it must promise nothing no outcome delivers.>

## Desired outcomes

### OC-001 <an observable state of the world, not a feature>
- **From:** CH-001
- **For:** U-002   (`(role tbd)` before roles exist; resolved by user-roles while draft)

### OC-002 <a second observable state>
- **From:** CH-002
- **For:** U-001

## Success metrics
<owned by the success-metrics skill; product-charter writes the stubs>
- **OC-001:** tbd (run success-metrics)
- **OC-002:** <metric> — <baseline> → <target> within <window> — <one-line why this target>
- **OC-003:** <metric> — 41% (measured 2026-09-10) → 60% within 30 days — <why> — result: 58% (measured 2026-10-28, E-041) — short
- **Guardrails:**
  - <metric that must not degrade> — currently <level, or `unmeasured`>
  - <guardrail> — currently 1.2% — result: held (measured 2026-10-28, E-042)
- **Secondary (requested):** <metric> — does not measure any outcome
- **Instrumented by:** <where the numbers come from>

## Constraints
<hard limits — platform, compliance, deadline, team — each marked
`given (<source>)` or `(assumption)`. Consumed by the design stage:
what it may not trade away.>

## Non-goals
<adjacent challenges the charter deliberately leaves alone, so scope
creep has to argue with a written line — opportunity-map checks new
opportunities against these. Challenges and outcomes cut at the 5-cap
land here (out of scope) or in Open questions (deferred), never only
in chat.>

## Open questions
<what define needs that no entry covers — each one a seed for a
research-plan Q-NNN block>
```

Charter field rules:

- **Challenges** are falsifiable problem sentences, same discipline as
  evidence-log claims — "trial users abandon setup before connecting a
  data source" can be proven wrong; "improve onboarding" cannot. At
  most 5; a sixth means the charter is a backlog, not a charter — cuts
  are recorded per the Non-goals note above. Evidence lines follow the
  inheritance rules; `Corroborates:` and `Stakes:` appear only when
  there's something to put in them.
- **A contradicted challenge** mirrors the opportunity rule: when new
  evidence contradicts the challenge sentence itself, the challenge
  keeps its ID and gains `- **Contradicted by:** E-NNN (→ CH-NNN)`,
  the corrected statement becomes a new `CH-NNN`, and every outcome
  whose `From:` names the old challenge is re-pointed or explicitly
  moved to Non-goals in the same pass — never left dangling. In a
  `draft` charter this is a direct edit; in an `agreed` one it runs
  through supersession.
- **Outcomes** are observable states, not features or activities:
  "new trial users reach a connected data source unaided" is an
  outcome; "ship a setup wizard" is a solution and "run onboarding
  research" is activity. Every outcome traces `From:` at least one
  challenge; a challenge no outcome addresses is either a Non-goal or
  an honest gap — say which. At most 5.
- **Success metrics** — exactly one metric line per outcome, keyed by
  its `OC-NNN`; a second metric on one outcome is an unresolved
  argument about what the outcome means. Guardrails are 1–3, shared
  across the charter, not per-outcome. An unknown baseline is written
  `baseline unknown (unmeasured)` — or `baseline unknown (→ Q-014)`
  only once that plan block actually exists; a bare `(→ Q-NNN)`
  placeholder is never written. With no baseline the target goes
  directional and an unknown window is written
  `within <window: set with the baseline>`, e.g.
  `- **OC-001:** 30-day setup completion — baseline unknown (unmeasured)
  → directional: up; number set when the baseline lands, within
  <window: set with the baseline> — target waits on measurement`. A
  backfilled baseline is written `<value> (measured YYYY-MM-DD)`. The
  target's one-line why is a benchmark, a cited E-ID, or `(ambition)`.
  **A result is the charter's answer to its own target**, appended to
  the metric line as `— result: <value> (measured YYYY-MM-DD, E-NNN)
  — reached | short | regressed`, judged against the target (deliver's
  outcome verdicts judge against the baseline, so a metric can have
  `moved` there and `short` here without contradiction — movement is
  the evidence, the target was the ambition). The `E-NNN` is the
  evidence-log entry holding the reading; a result with no entry is
  never written. A guardrail's result is `— result: held | breached
  (measured YYYY-MM-DD, E-NNN)`. A later reading replaces the result
  line; the history is the evidence log and deliver's outcome reviews.
  A directional target (no baseline when agreed) takes a result only
  after its baseline was backfilled; until then the reading *is* the
  baseline.
  **Secondary (requested)** exists only for a metric the user insisted
  on that measures no outcome; the line says so in as many words.

Charter lifecycle (transitions written by product-charter):

- `draft` — freely editable.
- `agreed (<date>)` — the team committed. The gate, both parts: every
  outcome has a filled metric line (measured baseline or the explicit
  unmeasured/directional forms; a stub or an `(assumption)`-marked
  figure never passes) **and** every outcome's `For:` names a `U-NNN`
  — an outcome still reading `(role tbd)` is an outcome for nobody,
  which is not something a team can commit to. From here the file is
  frozen. Two edits are allowed after `agreed`, both on metric and
  guardrail lines only: the baseline backfill, written `<value>
  (measured YYYY-MM-DD)`, and the result line per the Success metrics
  rules — filling in a promised measurement, or recording what the
  agreed target came to, is not changing the agreement. A result of
  `reached` or `regressed` is the standing prompt for supersession:
  an outcome that came true or went backwards is a charter whose
  challenges have moved, and product-charter is where that gets
  re-cut.
- `superseded (→ charter.md, <date>)` — written on the archived file's
  Status line at archive time, the one edit ever made to an archive.
  The supersession procedure: move the old file to
  `define/charter-<agreed-date>.md` (if that name is taken, suffix
  `-2`, `-3`… — an archive is never overwritten); flip its Status;
  write the new `charter.md` with a `Supersedes:` line naming it,
  continuing CH/OC numbering per the ID rules; re-validate every cited
  entry — drop retracted ones, name new contradictions; then sweep
  downstream: list every define/ file whose `OC-NNN`/`CH-NNN`
  citations changed meaning or died (journey shifts, opportunity
  Impact lines), and report that list in chat as required follow-up —
  the spec knows the dependents exist, so supersession walks them.

## Role block format (roles.md)

File header: `# Roles` + `<!-- weaveworm user-roles v1 -->`.

```markdown
## U-002 <role name>
- **Kind:** user | customer | stakeholder
- **Does:** <what they observably do with or around the system>
- **Needs:** <what they need from it>
- **Goals:** <what success looks like to them, in their terms>
- **Evidence:** E-004, E-009
- **Corroborates:** E-015
- **Confidence:** medium — weakest load-bearing entry is E-009
- **Voices:** P1, P3, R2
- **Distinct from:** U-001 — <the behavioral difference that makes this a separate role>
```

Role rules: roles split on what people do and need, never demographics
— two segments who behave identically are one role. `Kind` separates
the buyer from the operator from the bystander with veto power — a
write-time check against the classic buyer-operator miss. `Voices`
lists the log voices (P/R/M, carried as written) behind the role, so a
role built only on M-voices is visibly proxy-based. `Goals` are
consumed by journey-map: stages are the role's units of progress
toward them. Every role after the first carries `Distinct from:`. At
most ~7 roles; more means the splits stopped being behavioral. Allowed
edits: everything but the heading; a genuinely different role is a new
block.

## Journey file format (journeys/J-NNN-<slug>.md)

One journey per role × scope. Header:

```markdown
# J-003 <U-002 role name> — <scope>
<!-- weaveworm journey-map v1 -->
- **Role:** U-002
- **Scope:** <the slice of experience this maps>
- **State:** current+future | current-only
- **Confidence:** assumption-led — no evidence cited   (only when wholly uncited)
- **Superseded by:** J-007   (only on a superseded journey)
```

Then two sections:

- **Current state** — numbered stages, each headed
  `### J-003.1 <stage name>` with `- **Doing:**` (observed behavior,
  E-cited) and `- **Friction:**` (what breaks down, E-cited or
  `(assumption)`). At most 8 stages; finer grain belongs in a
  narrower-scoped journey.
- **Future state** — per-stage `Shifts`: what is different *for the
  user*, phrased as experience, never mechanism — "the user connects a
  data source without leaving the flow (OC-001)" describes an
  opportunity; "a wizard walks them through it" prescribes a solution.
  Every shift cites the `OC-NNN` it serves (or `CH-NNN` if the charter
  has the challenge but no outcome yet). Stages with no shift are
  listed under `Unchanged` — an all-shifts future state is a rewrite
  fantasy, not a map. Shifts are consumed by opportunity-map: a shift
  no opportunity addresses is a named gap, and an opportunity
  contradicting a shift is a flag, not a coincidence.

With no charter, `current-only` is the default `State:` — writing
shifts anyway is the user's explicit opt-in, every shift marked
`(assumption)`. `current-only` is also legitimate whenever the future
is genuinely undecided; never invent shifts to look finished.

Allowed edits: everything but the heading and existing stage IDs —
new evidence lands on its stage in place. A materially changed journey
(new stages, different order) is a fresh `J-NNN`; the old file gains
the header's `Superseded by:` bullet, never a heading edit — and every
opportunity `Journey:` line citing the old journey's stages is listed
in chat as required follow-up, the same dependent-sweep charter
supersession runs.

## Opportunity block format (opportunities.md)

File header:

```markdown
# Opportunities
<!-- weaveworm opportunity-map v1 -->
Log: <path to the evidence log — default research/evidence-log.md; `none — assumption-led` when no log exists>
```

File order: `pursued` blocks first, under a `<!-- pursued -->` marker
— they are the backlog's output, what the design stage pulls, and they
lead the file and the chat summary. Then `delivered` blocks under a
`<!-- delivered -->` marker — finished, with the outcome's verdict on
record, kept visible so the backlog shows what pursuing actually
bought. Then open blocks in rank order, best case first. Then
`deferred` and `dropped` blocks below a `<!-- parked -->` marker —
only dead blocks park, so they never compete for rank position.
Markers are written when first needed. At most ~10 open blocks; park
the tail as `deferred — below the line`.

```markdown
## O-003 <the opportunity as one problem-shaped sentence>
- **Status:** open
- **Evidence:** E-003, E-007
- **Corroborates:** E-011
- **Who:** U-002
- **Journey:** J-003.4
- **Confidence:** medium — weakest load-bearing entry is E-007
- **Stakes:** high — carried from E-003
- **Impact:** high — moves OC-001; 4 of 6 firsthand voices hit this (E-003)
- **Complexity:** medium — per eng input 2026-08-06
- **Rank rationale:** <one line — the impact-vs-complexity call, judgment labeled>
- **Score (requested):** <RICE or similar the user insisted on — arithmetic over the same entries; not the rank driver>
- **Candidate:** <solution idea>
```

- **Who** cites the role(s) affected once roles exist — a plain
  population phrase before that. **Journey** cites the stage the
  opportunity lives in, when a journey covers it; `—` when none does
  (and that's a journey-map gap worth naming).
- **Impact** names the `OC-NNN` outcome(s) the opportunity moves (or
  `CH-NNN` pre-outcomes; `unstated outcomes (assumption)` with no
  charter at all) plus the evidence-based reach/severity behind the
  level. **Complexity** is the team's stated call — `high|medium|low —
  per <who/when>`; a user's unsized guess is recorded
  `<level> (assumption) — <who>'s read, not sized`; unreachable or
  unknown → `unknown (unconfirmed)`. It is never invented, and neither
  unknown nor `(assumption)` complexity ever deprioritizes — both rank
  on impact with the gap flagged, because "probably hard" is how
  high-impact work dies quietly.
- **An opportunity is 2+ entries pointing at one problem**; a
  single-entry block is allowed but its rank rationale is flagged
  `(single source)`. **Assumption-led blocks** (no evidence in scope):
  `Evidence: none (assumption)`,
  `Confidence: assumption-led — no evidence cited`, ranked on stated
  belief with the gap named in the rank rationale.
- **Stakes** appears only when a cited entry carries it; **Candidate**
  only when the user insists on recording a solution idea — never in
  the heading; **Score (requested)** only when the user insisted on a
  composite score after pushback.
- Statuses: `open` → `pursued (<date>)` when the team commits it to
  the design stage, `deferred — <reason>`, or `dropped — <reason>` —
  all written by opportunity-map, including
  `dropped — contradicted by E-NNN (→ O-NNN)` when new evidence
  contradicts the statement itself and the corrected statement becomes
  a new block. `pursued` closes as `delivered (<date>) — OC-001 moved
  | flat | regressed (E-NNN, → <outcome review path>)`: written by
  opportunity-map on the user's word once a deliver outcome review
  exists for the brief that pulled the block and its reading is in
  the evidence log. The verdict is deliver's, baseline-relative,
  carried verbatim; the path is recorded as the user gives it — define
  never parses deliver's files. A `too early` reading writes nothing;
  the block stays `pursued`. `delivered` is terminal: a `flat` or
  `regressed` outcome the team wants to attack again is a fresh block
  whose `Evidence:` cites the reading, with the delivered block
  gaining `(→ O-NNN)` — the same shape as a contradiction. Allowed
  edits: everything but the heading sentence — a different statement
  is a new block.

## Upstream contract

Define reads `research/evidence-log.md` as written by the discover
plugin; the canonical format is discover's evidence-log spec
(`discover/references/evidence-log-spec.md` in the weaveworm repo). If
the user keeps research somewhere other than `research/`, ask once,
then reuse their answer for the session. Syntheses in
`research/synthesis/` are an optional secondary input — useful for
clustering, but themes are not evidence; only E-entries are citable.

The minimum define depends on: entries headed `## E-NNN <one
falsifiable claim>` with `**Evidence:**`, `**Source:**`,
`**Question:**`, and `**Confidence:** high|medium|low — <reason>`
bullets, plus optional `**Stakes:**` and `**Contradicts:**` lines.
Three edge cases carry over from discover:

- **Retracted entries** — strikethrough heading plus a `**Retracted:**`
  line. They still exist and still read as claims; define treats them
  as never load-bearing.
- **Entries without a `Question:` line** — discover's producer skills
  always write one, but older or hand-kept logs may lack it; scope
  those by matching their Source line, the same fallback discover's
  synthesis uses. Entries marked `Question: unplanned (<topic slug>)`
  are routine, not malformed — they're findings no plan anticipated,
  and clusters of them are prime challenge and opportunity material.
- **Voice IDs** — quotes are attributed P1… (firsthand participants),
  R1… (survey respondents), M1… (mined proxy voices). Carry them as
  written; the P/R/M distinction is what tells a firsthand count from
  a proxy one.

A log kept by hand in that shape works identically. Define skills
never write to the log — evidence flows in through discover only.

## Standalone fallback

When no evidence log exists (and the user, asked once, confirms there
is none elsewhere), define runs assumption-led rather than stalling.
The dependency is on information, not files: every upstream artifact
answers questions, and when the artifact is absent the skill asks the
user those questions directly — a short intake before any writing.

The doctrine, four rules:

1. **Ask the floor, not everything.** Each skill has a prerequisite
   set (below) of at most ~5 questions, asked in one pass. What the
   user can't answer becomes an Open question or research-plan seed —
   never a blocker.
2. **Answers land in the skill's own artifact**, as `(assumption)`
   lines — or `given (<source>)` when the user names a source. Define
   never mints `E-NNN`s to dress up intake answers; evidence IDs stay
   discover's.
3. **The debt stays visible** via the existing labels:
   `Evidence: none (assumption)`,
   `Confidence: assumption-led — no evidence cited`,
   `Log: none — assumption-led`.
4. **Promotion, not rewrite.** When a log exists later, re-cite:
   intake answers that evidence now supports gain `E-NNN` citations;
   contradicted ones follow the contradiction discipline. Backfilling
   citations is an allowed edit everywhere.

Prerequisite questions per skill — the intake floor, phrased for the
user, answers labeled per rule 2:

- **product-charter** — What problems have you seen, and how do you
  know each one is real? Who set this mandate, and what future are
  they committed to? What limits are non-negotiable, and who set them?
- **user-roles** — Who uses this, who pays for it, and who can veto
  it? What does each group observably do differently?
- **journey-map** — Walk one role through the scope today: what do
  they do at each step, and where does it break down?
- **opportunity-map** — Which problems matter most, and why do you
  believe that? What's the team's read on cost, and whose read is it?

The same doctrine governs gaps *between* define's own skills — the
artifact rules above already carry those fallbacks (`(role tbd)`
before roles exist, `current-only` journeys with no charter,
`unstated outcomes (assumption)`, a plain population phrase on Who).
A skill invoked out of sequence asks its floor questions about the
missing define artifact the same way, and the answer lines re-point to
real IDs once the upstream skill runs.

## Contradictions, everywhere

Discover's `Contradicts:` line lives only on the newer entry, so any
define skill citing entries checks both directions — the cited
entries' own lines, and entries anywhere in the log pointing at them.
A contested claim is cited with the contradiction named (counterpart
marked `(out of scope)` when it lies outside the cited set), which
side the artifact leans on, why, and what would settle it. Contested
can still rank high; it can't pretend to be settled.
