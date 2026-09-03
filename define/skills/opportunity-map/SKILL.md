---
name: opportunity-map
description: The last stage of define — cluster evidence and journey friction into a prioritized opportunity backlog: O-NNN blocks, each one problem-shaped sentence with its evidence, the role and journey moment it lives in, impact against the charter's outcomes, and the team's stated complexity. Use when a designer asks "what should we work on", "turn the research into opportunities", "prioritize what we learned", "help me prioritize the roadmap", "impact vs effort on these", wants to mark an opportunity pursued, deferred, dropped, or delivered, or a journey map just landed and they want next steps. Do NOT use for writing the charter (use product-charter), mapping journeys (use journey-map), writing the stakeholder readout (use discover's synthesis), or recording findings (use discover's evidence-log).
---

# opportunity-map

The fourth stage of define, and its handoff: a ranked backlog the design
stage pulls from. Input: the evidence log (default
`research/evidence-log.md`; ask once if research lives elsewhere),
journey files in `define/journeys/`, the charter, and syntheses as
secondary input — optionally scoped to a journey, a `Q-NNN`, or a topic.
Scoping covers `Question: unplanned` entries whose slug matches and
Question-less entries by Source-line matching, per the spec's Upstream
contract. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/define-spec.md` before your first
write in a session — it owns the block format, file order, ID rules,
statuses, and confidence inheritance; do not improvise fields. Project
artifacts (`research/`, `define/`, `design/`, `deliver/`) live under the
working directory the session started in; read and write them by those
relative paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder
above it are not the project, even though that folder also has
stage-named subfolders: they hold only spec and voice files, are
read-only, and are never listed, searched, or written. Output:
`define/opportunities.md` (define root per the spec — ask once if
definition work lives elsewhere) created with the spec's header — `Log:
none — assumption-led` when no log exists — or updated. Conversation
runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Mapping rules

- **Problem-shaped, not solution-shaped.** "Trial users can't connect
  a data source without help" is an opportunity; "add a setup wizard"
  is a solution wearing an opportunity's clothes. Solutions the user
  insists on recording go on the block's `Candidate:` line — never in
  the heading, which downstream design work inherits.
- **Cluster from entry bodies and journeys — friction and shifts
  both.** Re-read the entries; entries and friction moments describing
  the same struggle belong together even when their wording differs,
  and every future-state shift should map to an opportunity — a shift
  none addresses is a named gap, and an opportunity that contradicts a
  shift is a flag to surface, not a coincidence. An opportunity is 2+
  entries pointing at one problem; single-entry opportunities are
  flagged `(single source)` in the rank rationale. Cite the journey
  moment (`Journey: J-003.4`) when one covers it — `—` when none
  does, itself a journey-map gap worth naming. `Who:` cites the
  affected `U-NNN` role(s) once roles exist — a plain population
  phrase before that.
- **Assumption-led path.** No evidence in scope but upstream artifacts
  exist (a greenfield run arriving from assumption-led journeys):
  write blocks with the spec's forms — `Evidence: none (assumption)`,
  `Confidence: assumption-led — no evidence cited` — ranked on stated
  belief with the gap named in each rank rationale. If there's no log
  *and* no upstream artifacts at all, stop and say so — the honest
  route is charter and roles first, then back here.
- **Confidence per the spec's inheritance rules** — weakest
  load-bearing entry; Corroborates never moves it; retracted entries
  never load-bearing; contradictions checked both directions and
  named; merges of independent firsthand entries route through
  discover's evidence-log before re-citing.
- **Impact is outcome-anchored.** The Impact line names the `OC-NNN`
  the opportunity moves (or `CH-NNN` pre-outcomes; `unstated outcomes
  (assumption)` with no charter — and say the charter is the missing
  stage) plus the evidence behind the level: reach as counts from
  cited entries, severity from `Stakes:` lines. Proxy entries don't
  add reach however many venues they come from — the same logic
  behind discover's proxy cap on confidence.
- **Non-goals are a gate.** Before writing a block, check the
  charter's Non-goals: an opportunity landing inside one is either
  dropped with that reason or the Non-goal is explicitly challenged
  back to product-charter — never both kept silently. The written
  line exists to be argued with, not walked past.
- **Complexity is the team's call, never yours.** Ask once, batched,
  for the team's read on the candidates (`high|medium|low` with one
  line of why — what it touches); record `Complexity: <level> — per
  <who/when>`. A user's unsized guess ("probably high, skip asking
  eng") is recorded honestly as `<level> (assumption) — <who>'s read,
  not sized`; unreachable or unknown → `unknown (unconfirmed)`. Per
  the spec, neither unknown nor `(assumption)` complexity ever
  deprioritizes — both rank on impact with the gap flagged, because
  "probably hard" is how high-impact work dies quietly.
- **Rank is the impact-vs-complexity call, stated as judgment.** High
  impact + low complexity rises; the interesting calls (high/high,
  low/low) get their reasoning in the rank rationale. Ties on impact
  break by reach counts from cited entries, then `Stakes:`; when
  neither discriminates, say the intra-tier order is arbitrary rather
  than implying one. Strategic fit the user states is a legitimate
  input, labeled as theirs. If the user asks for a RICE (or similar)
  score: push back once, concretely — RICE's Reach and Confidence
  multiply the same weak entries twice, so the number restates the
  inputs with extra confidence — and propose the rank rationale
  instead. If they insist, record it on the spec's
  `Score (requested):` line, never as the rank driver.
- **Statuses close the loop.** `pursued (<date>)` when the team
  commits an opportunity to design — pursued blocks move to the top
  of the file under the spec's `<!-- pursued -->` marker; they're the
  backlog's output, not its dead weight. Design-brief may write that
  same status, in the same form, when the user commits at the pull;
  read it as this skill's own write. `deferred`/`dropped` on
  instruction park below the `<!-- parked -->` marker, and
  `dropped — contradicted by E-NNN (→ O-NNN)` fires without
  instruction when new evidence contradicts the statement itself —
  the corrected statement becomes a new block.
- **Delivered is the loop actually closing.** When the user says a
  pursued opportunity shipped and its outcome was read (deliver's
  outcome-review ends by sending them here), write the spec's
  `delivered` form: the date, the outcome's verdict as deliver gave
  it, the `E-NNN` holding the reading, and the outcome review's path
  as the user states it. The block moves under the `<!-- delivered
  -->` marker. No reading in the log, or a `too early` verdict, means
  it stays `pursued` — say what's missing. `delivered` is terminal:
  when a `flat` or `regressed` outcome is worth another go, that's a
  fresh block whose `Evidence:` cites the reading, ranked like any
  other, with the delivered block gaining `(→ O-NNN)`; the first
  attempt's record stays intact.
- **Re-runs update, never duplicate; keep the backlog workable.**
  Same opportunity, fresh evidence → append per the spec's allowed
  edits. More than ~10 open blocks means the map stopped helping
  anyone choose — merge near-duplicates, park the tail as
  `deferred — below the line`, and say you did. Above ~50 entries in
  scope, propose scoping before clustering rather than silently
  sampling.

## After the mapping

Report per the voice contract: pursued blocks first (one line each —
they're the handoff), delivered blocks next (one line each with the
verdict — they're what pursuing bought), then the top 5 open
opportunities as one line each — ID, statement, impact, complexity —
plus the state line covering the rest ("10 opportunities: 1 pursued,
1 delivered, 6 open, 2 dropped").
The decision this artifact exists for: which
opportunity gets pursued — name your top pick and the one-line why.
If the top pick is `(single source)`, contested, or carries
`unknown`/`(assumption)` complexity, say what one cheap step (a
research-plan question, an eng sizing conversation) would firm it up
first. If any shift or Non-goal check surfaced a gap, name it here.

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash inside a sentence (a comma, a parenthesis, or a second sentence
instead); every ID travels with its name, and a status or marker is
said in words rather than quoted as syntax; the state line this skill's
report names is the second-to-last line; the last line is the single
first step, stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## What this skill refuses

- Inventing an opportunity nothing supports, or padding Evidence
  lines with tangential E-IDs for weight.
- Inventing a complexity level — it's recorded from the team, marked
  `(assumption)` as a stated guess, or marked unknown.
- A composite score as the rank driver — the insist path is the
  `Score (requested):` line.
- Raising confidence during mapping.
- Writing `delivered` with no evidence-log entry for the reading, or
  re-opening a delivered block instead of writing a fresh one.
- Deleting or renumbering blocks, or editing a heading sentence —
  other edits per the spec's allowed list.
