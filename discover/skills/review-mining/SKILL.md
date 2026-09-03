---
name: review-mining
description: Execute a Q-NNN plan that relies on proxy sources — mine app-store reviews, G2/Capterra, Reddit, forums, and support threads for voice-of-customer on the question, with counts and verbatim quotes in a dated mining file. Use when a designer asks "what are people saying about us on Reddit", "mine our app store reviews", "what do users complain about on G2", when users are unreachable, there are no users yet, or the plan's Participants line names proxy sources. Do NOT use for choosing the method (use research-plan), walking competitor products (use competitor-teardown), or recording conclusions (use evidence-log).
---

# review-mining

Input: a `Q-NNN` block from the plan file (default `research/plans.md`)
whose Participants or Method line names proxy sources (reviews,
communities, support archives). Output: the mining file below, then
evidence-log entries. If no plan block exists, say so and run
research-plan first — the question and target-user definition come from
the plan; without them, mining returns whatever the loudest reviewers
complain about. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory the session started in; read and write them by those relative
paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder above it
are not the project, even though that folder also has stage-named
subfolders: they hold only spec and voice files, are read-only, and are
never listed, searched, or written.

## Mining file

- One file per question: `research/mining/Q-NNN.md`.
- Create with this header:

  ```markdown
  # Review mining — Q-NNN <question>
  <!-- weaveworm review-mining v1 -->
  Plan: Q-NNN in research/plans.md
  Mined: <date>
  ```

- Sections, in order: **Sources**, **Themes**, **Outliers**, **Coverage**.

## Acquiring the material

In order of preference: (a) material the user points at — support export,
CSV, pasted dump; ask once for a path; (b) web search and fetch for
public review and community URLs. A source that won't load (bot-gated
store pages, private archives) is recorded in **Sources** as "attempted,
not retrievable" — move on; never substitute recalled or model-generated
reviews for material you couldn't fetch. If nothing can be retrieved or
supplied, stop and say so; a mining file written from prior knowledge is
fabrication.

## Mining rules

- **Sweep multiple source types**, not one: the plan's proxy-source ladder
  (support archives → public reviews → communities) ranks them by
  strength. Two or more types is the bar for an unqualified theme. If
  only one venue exists, still record the pattern, mark it "single-venue —
  may be an artifact of <venue>", and name in **Coverage** the second
  venue that would test it; never drop a counted pattern for missing the
  bar, and never present one as if it cleared it.
- **Bounded sweep.** Scan 40–60 items per source type, or the full set if
  smaller — record the n either way. Stop when the last 15 items scanned
  add no new theme, and say so; that's saturation, not laziness.
- **Count, don't vibe.** Every theme states the arithmetic with the item
  numbers inline: "11 of 60 reviews scanned mention export friction
  [#3, #7, #12, …]" — never "many users complain about export." An item
  supporting two themes is counted in both with the overlap said out
  loud; theme counts that sum past n with no overlap note read as
  fabrication. Repeat voices shrink the denominator — "7 of 12 posts
  (4 distinct users)" — state both numbers. Record what was scanned
  (source, date range, n, and the sort/filter applied — most recent,
  most helpful, 1-star only) in **Sources** so the denominator is
  auditable and its bias visible.
- **Capped output.** At most 5 themes, ranked by count, the remainder
  rolled into one "also mentioned" line; 1–2 quotes per theme, not a
  quote wall.
- **Verbatim quotes with URLs and dates.** Paraphrase loses the user's
  actual language — the point of proxy research. Anonymize handles to
  M1, M2… as you quote — M for mined voices; per the spec, P-numbers are
  firsthand participants and R-numbers survey respondents.
- **Name the skew.** Reviewers are self-selected extremes and complaints
  dominate; communities over-represent power users. **Coverage** must say
  who these sources structurally cannot speak for (e.g. churned users who
  never reviewed, non-English markets).
- **Outliers get a section, not deletion.** A single vivid contradicting
  review isn't a theme, but hiding it is curation bias.

## Confidence when logging

Proxy evidence is secondhand: per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md` and the plan's
proxy rules, **cap confidence at `low`** regardless of how many reviews
agree — the spec's 2+-independent-sources route to `high` does not apply
across proxy venues; venue independence does not make evidence firsthand. Volume raises confidence within a source's reach, not beyond
it, and mined corroboration never raises an existing firsthand entry's
level — append it as evidence, leave the level alone (spec: confidence
precedence).
If a mined theme matters, its evidence-log entry should end by naming
the firsthand method that would confirm it ("would rise with 5
interviews — see research-plan").

## After mining

Log themes in the evidence log — one falsifiable claim per entry, Source
citing the mining file (e.g. `Source: review-mining Q-004, mined
2026-08-05, 11/60 reviews`), `Question: Q-NNN` so synthesis can scope
it. Then check the plan's "Done when": if the mining was the last
evidence it named, remind the user to mark the question answered in
research-plan. Close by telling the user the one thing the mining could
not answer, so the next Q-NNN block is ready if they want it.

Report per the voice contract: the theme one-liners with their counts,
the new E-NNN headings, and one state line ("3 sources, 4 themes, 6
entries logged").
