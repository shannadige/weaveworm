---
name: journey-map
description: Map one role's experience as a J-NNN journey file — current state as evidence-cited stages with friction, future state as per-stage shifts phrased as what changes for the user, describing the opportunity without prescribing solutions. Use when a designer asks "map the journey", "what does the current experience look like", "current state vs future state", "where does it break down for X", "what should the experience become", or after user-roles lands and a role needs its experience mapped. Do NOT use for defining who the roles are (use user-roles), turning friction into a ranked backlog (use opportunity-map), or recording findings (use discover's evidence-log).
---

# journey-map

The third stage of define: journeys turn roles plus evidence into the
before/after picture that opportunity-map prioritizes from. Input: one
`U-NNN` role from `define/roles.md`, a scope (the slice of experience to
map — from the user, or proposed from where the role's evidence
clusters), the evidence log, and the charter if one exists. Output: one
`define/journeys/J-NNN-<slug>.md` file (define root per the spec — ask
once if definition work lives elsewhere) per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/define-spec.md` — read it before
writing; it owns the file format, stage IDs, and confidence inheritance.
Project artifacts (`research/`, `define/`, `design/`, `deliver/`) live
under the working directory the session started in; read and write them
by those relative paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the
folder above it are not the project, even though that folder also has
stage-named subfolders: they hold only spec and voice files, are
read-only, and are never listed, searched, or written. If roles.md
doesn't exist, route to user-roles first — a journey without a role is a
flowchart of nobody; the quick path is running user-roles for just the
one role in question, assumption-led if it must be. Conversation runs
per the voice contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` —
register, translation, and question/report shape live there, not here.

## Mapping rules

- **Current state is observed, not imagined.** Every stage's `Doing:`
  and `Friction:` cites E-entries or carries `(assumption)` — the
  same citation discipline as everywhere in define (Corroborates for
  repeats, retracted never load-bearing, contradictions per the
  spec's rule). The best sources are behavioral: usability sessions,
  analytics entries, support tickets. A current state built wholly on
  `(assumption)` is legitimate and labeled: set the spec's header
  `Confidence: assumption-led — no evidence cited` bullet — and its
  stages are research-plan bait; say so.
- **Stages are the role's units of progress, not the product's
  screens.** Progress toward the role's `Goals:` line — that's what
  the field is for. "Realizes the data is stale" is a stage; "lands on
  the dashboard" is a screen. At most 8 — finer grain belongs in a
  narrower-scoped journey.
- **Future state describes the opportunity, never the solution.**
  Each shift says what is different for the user — what they achieve,
  skip, or no longer suffer — and cites the `OC-NNN` it serves
  (`CH-NNN` if the charter has the challenge but no outcome yet).
  With no charter, `current-only` is the default per the spec —
  writing shifts anyway is the user's explicit opt-in, every shift
  marked `(assumption)` with the missing charter flagged. Mechanism
  words are the tell: wizard, modal, AI, auto-anything. If the user
  offers a solution, hold it for the opportunity block's `Candidate:`
  line and write the shift as the experience it would produce — and
  say you did.
- **Not every stage shifts.** Stages listed under `Unchanged` are a
  feature of an honest map; an all-shifts future state is a rewrite
  fantasy. `current-only` is a legitimate `State:` when the future is
  still undecided — never invent shifts to look finished.
- **Re-mapping is a new file, not an edit war.** Small updates (new
  evidence on a stage) edit in place per the spec's journey
  allowed-edits rule; if the journey has materially changed — new
  stages, a different order — map it fresh as a new `J-NNN`, add the
  spec's `Superseded by:` header bullet to the old file, and list
  every opportunity `Journey:` line citing the old stages as required
  follow-up. Headings and existing stage IDs never change.

## After the journey

Report per the voice contract, in this shape and no other: the file
path; one line per stage (number, name, friction count); one line per
shift (stage, what changes for the user, the OC-ID with the outcome's
name); then one state line ("6 stages, 4 with friction, 3 shifts, 2
unchanged, State: current+future"). If the user offered a solution,
the report says in one plain clause where it went and why: it is held
for opportunity-map's `Candidate:` line, the shift was written as the
experience it would produce, and journeys have to outlive any one
mechanism, so solutions die in journey files. Saying only that
mechanisms don't belong in shifts reads as a refusal, and a parked
idea the user can't find reads as ignored. The decision to force:
name the moment that matters most — the stage whose friction is
best-evidenced or highest-stakes — with its one-line why, and offer
opportunity-map scoped to this journey. If friction clusters where
the charter has no challenge, that's a charter gap — name it.

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash inside a sentence (a comma, a parenthesis, or a second sentence
instead); every ID travels with its name, and a status or marker is
said in words rather than quoted as syntax; the state line this skill's
report names is the second-to-last line; the last line is the single
first step, stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## What this skill refuses

- Mapping a journey for a role that isn't in roles.md.
- Solutions in shifts — mechanisms route to `Candidate:` lines via
  opportunity-map.
- Inventing friction no entry or stated belief supports, or an
  invented future state for a `current-only` journey.
