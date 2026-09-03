---
name: product-charter
description: Write and steward the product charter — challenges as falsifiable CH-NNN claims cited from the evidence log, a vision, OC-NNN desired outcomes phrased as observable states, and constraints, with success metrics delegated to its sibling skill; owns the charter lifecycle (draft, agreed, superseded). Use when a designer asks to "run the define process", "let's do product strategy", "write the strategy doc", "write the charter", "what are we actually trying to solve", "define the challenges and outcomes", "what's the vision", starts a product strategy workshop, says "mark the charter agreed", or needs to revise an agreed charter because evidence changed. Do NOT use for defining the metrics themselves (use success-metrics), mapping who the users are (use user-roles), or recording findings (use discover's evidence-log).
---

# product-charter

The first stage of define: everything downstream — roles, journeys,
opportunity impact — traces back to the charter's challenges and
outcomes. Input: the evidence log (default `research/evidence-log.md`;
ask once if research lives elsewhere), syntheses as secondary input, and
the user's knowledge of mandates and constraints. Output:
`define/charter.md` (define root per the spec — ask once if definition
work lives elsewhere) per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/define-spec.md`. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory; `${CLAUDE_PLUGIN_ROOT}` holds only the spec and voice files,
is read-only, and is never listed, searched, or written. Read the spec
before writing — it owns the format, ID rules, confidence inheritance,
and the charter lifecycle. Do not improvise sections. Conversation runs
per the voice contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` —
register, translation, and question/report shape live there, not here.

## Before writing

The intake floor — only what changes the charter: what
the org already believes the product is for (mandates, stated
strategy), hard constraints (these land in the Constraints section,
each `given (<source>)` or `(assumption)`), who owns the charter, and
any challenges leadership has already committed to. If the user is
unreachable, write `Owner: unassigned`, mark unknowns `(unconfirmed)`,
and list them at the end for confirmation.

## Writing rules

- **Challenges come from the log, stated falsifiably.** Cluster
  entries the way opportunity-map does — from entry bodies, not
  headings — and re-read every entry you cite; an entry that doesn't
  support the challenge sentence gets dropped or the sentence
  rewritten, never kept for weight. Supporting-but-repeating entries
  go on `Corroborates:`. Retracted entries are never load-bearing.
  Contradictions per the spec's Contradictions-everywhere rule. At
  most 5 challenges — the charter is where you choose, not where you
  list — and cuts are recorded, not narrated: an out-of-scope cut goes
  to Non-goals, a deferred one to Open questions, so the next run
  doesn't re-derive what was already rejected.
- **Assumption-led path.** No evidence — a mandate or greenfield:
  still write the charter, every uncited claim `(assumption)`, the
  header's `Confidence: assumption-led — no evidence cited` bullet
  set, and Open questions doubling as the research backlog; offer to
  take the top one to discover's research-plan as a `Q-NNN` block. A
  mandate deserves a charter; it doesn't deserve to look researched.
- **Outcomes are observable states, not features or activity.** Per
  the spec: "new trial users reach a connected data source unaided" is
  an outcome; "ship a setup wizard" and "run onboarding research" are
  not. Solution-shaped input gets reframed as the outcome the solution
  assumes, and you say you did. Every outcome traces `From:` a
  challenge; name any challenge left unaddressed as a Non-goal or a
  gap. `For:` cites a `U-NNN` role once roles.md exists — before
  that, `(role tbd)`, which user-roles resolves while the charter is
  draft.
- **Vision is the sum, not a slogan.** 2–3 sentences a skeptic could
  check the outcomes against: if an outcome doesn't serve the vision
  or the vision promises what no outcome delivers, one of them is
  wrong — say which. That check is what the section is for.
- **Metrics stubbed, not skipped.** Write the spec's stub line per
  outcome — `- **OC-NNN:** tbd (run success-metrics)`; the section
  itself belongs to success-metrics.
- **Non-goals do real work.** At least one, each a plausible adjacent
  scope someone will eventually argue for — opportunity-map checks new
  opportunities against them. "None" is a smell.

## Lifecycle

All transitions per the spec's charter lifecycle; this skill writes
them.

- **Agreeing.** "Mark it agreed" → check both gate parts: every
  outcome's metric filled (stubs and `(assumption)` figures fail) and
  every `For:` resolved to a `U-NNN` — `(role tbd)` fails; an outcome
  for nobody isn't something a team can commit to. Gate passed →
  `agreed (<YYYY-MM-DD>)`, and say the file is now frozen. Gate failed
  → say exactly what's missing (which metrics, which roles) and offer
  success-metrics or user-roles accordingly. Never write `agreed`
  anyway.
- **Superseding.** Revising an agreed charter runs the spec's
  procedure in full: archive to `charter-<agreed-date>.md` (suffix
  `-2`, `-3`… on collision — never overwrite an archive), flip the archive's
  Status to `superseded (→ charter.md, <date>)` — the one edit an
  archive ever gets — write the new charter with its `Supersedes:`
  line, continue CH/OC numbering from the archive's highest,
  re-validate every cited entry, then sweep downstream: list every
  journey shift and opportunity Impact line citing a changed or dead
  `CH`/`OC` ID and report that list in chat as required follow-up.
- **Contradicted challenges** follow the spec's rule: keep the ID, add
  `Contradicted by: E-NNN (→ CH-NNN)`, mint the corrected statement as
  a new challenge, and re-point or explicitly retire every outcome
  tracing `From:` the old one — direct edit in draft, supersession
  once agreed.

## After the charter

Report per the voice contract; the lines: each challenge with its
confidence, each outcome, and the state line ("4 challenges, 3
outcomes, metrics stubbed, 2 open questions"). The decisions to force:
the challenge you'd put first and the one-line why, and the gate
distance — "metrics stubbed and roles unresolved; success-metrics and
user-roles stand between this draft and `agreed`" — recommending which
to run next. If open questions outnumber cited entries, the honest
move is research-plan first; the product is still discovery-shaped.

## What this skill refuses

- Citing an E-ID that doesn't exist, doesn't say what the challenge
  claims, or is retracted.
- Outcomes that are features or activities wearing outcome clothes.
- A sixth challenge or outcome — cut to Non-goals or Open questions,
  and say what was cut.
- Marking the charter `agreed` past a failed gate, or editing an
  `agreed` charter beyond the spec's baseline-backfill.
