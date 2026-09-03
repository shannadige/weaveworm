---
name: synthesis
description: Compose evidence-log entries into a stakeholder-ready synthesis — themes built strictly from cited E-NNN entries, contradictions surfaced, gaps named, recommendations separated from findings. Use when a designer asks "what did we learn", "pull this together for the team", "write the readout", or a question's research sessions are done. Do NOT use for recording raw findings (use evidence-log) or planning the next study (use research-plan).
---

# synthesis

Input: the evidence log (default `research/evidence-log.md`, per the
spec at `${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`) and the
plan file (default `research/plans.md`; if the user keeps research
elsewhere, ask once, then reuse their answer for the session), scoped to
one or more `Q-NNN` questions or a topic the user names. Select in-scope
entries by their `Question:` field — `unplanned` entries whose topic
slug matches the named scope are in scope; for older entries without one, fall
back to matching the Source line against the question's kit, teardown,
or mining artifacts and the plan block's "Done when". Output: the
synthesis file below. If the log has no entries in scope, say so — a
synthesis of zero entries is a pitch, not research, and this skill
refuses to write one. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation,
and question/report shape live there, not here.

## Synthesis file

- One file per readout: `research/synthesis/<date>-<topic-slug>.md`
  (date-stamped because syntheses go stale as the log grows; a new
  readout is a new file, never an edit that silently changes what the
  team was told).
- Create with this header:

  ```markdown
  # Synthesis — <topic> (<date>)
  <!-- weaveworm synthesis v1 -->
  Scope: Q-NNN, Q-NNN — E-entries as of <date> (log: <n> entries)
  ```

- Sections, in order: **Themes**, **Contradictions**, **Gaps**,
  **Recommendations**.

## Synthesis rules

- **Every theme cites its entries.** A theme is 2+ entries pointing the
  same way, stated as one sentence with its E-IDs inline: "Users abandon
  setup at the integrations step (E-003, E-007, E-011)." A sentence with
  no E-ID doesn't belong in Themes — if it's worth saying, it's either a
  missing log entry (log it first, via evidence-log) or an opinion
  (Recommendations, labeled as such).
- **Theme confidence = its weakest load-bearing entry** — load-bearing
  means every entry cited in the theme sentence. Three `low` proxy entries
  don't sum to `medium`, and volume within one source type never upgrades
  a theme. State each theme's confidence and why. One escape hatch: if 2+
  in-scope entries make the same claim from independent firsthand sources,
  that's an evidence-log merge — route to evidence-log, let confidence
  rise there, then re-cite the merged entry. Proxy-sourced entries stay
  `low` no matter how many venues agree. If a cited entry carries
  `Stakes: high`, the theme states both — "confidence low, stakes high —
  cheap to verify" — so a low label can't read as low importance.
- **Contradictions are findings, not noise.** The spec's `Contradicts:`
  line lives only on the newer entry, so collect in both directions:
  in-scope entries carrying one, plus entries anywhere in the log whose
  `Contradicts:` line names an in-scope entry — pull the counterpart into
  the section even when out of scope, marked `(out of scope)`. Both sides
  cited, never resolved by silently picking the side that fits the story.
  If one side is stronger, say why (source independence, confidence,
  recency) and what would settle it. If the log's open-contradiction
  count exceeds what you surfaced, say so.
- **Retracted entries are never load-bearing.** A struck-through entry
  carries no theme, no side of a contradiction, and no recommendation.
  It may be named in the gaps only to say what its retraction left
  uncovered ("the one entry that asked was retracted, so there is no
  valid evidence yet on what members want instead").
- **Name the gaps.** What the question needed that no entry covers, and
  which populations the evidence structurally missed (screener limits,
  proxy-source skew). Clusters of `Question: unplanned` entries are named
  here too — each is a question the plan never asked, and the seed of the
  next `Q-NNN` block. An honest Gaps section is what stops a readout
  from being read as more complete than the log is.
- **Recommendations are downstream of themes, and separate.** Each one
  names the theme(s) it follows from and its cost if the theme is wrong.
  No recommendation may rest solely on a `low`-confidence theme without
  saying so.

## Synthesis template

```markdown
# Synthesis — <topic> (<date>)
<!-- weaveworm synthesis v1 -->
Scope: Q-NNN, Q-NNN — E-entries as of <date> (log: <n> entries)

## Themes

### T1 <one-sentence claim> (E-003, E-007)
- **Confidence:** <level> — weakest cited entry is E-007
- **So what:** <one line>

## Contradictions

### <claim A> (E-011) vs <claim B> (E-014)
- **Stronger:** <side, and why — independence, confidence, recency>
- **Would settle it:** <the study or entry that would>

## Gaps

- <what the question needed that no entry covers, and who the evidence
  structurally missed; a retracted entry appears here only as the reason
  for a hole>

## Recommendations

### R1 <action>
- **From:** T1
- **Cost if wrong:** <one line>
```

At most 5 themes and 5 recommendations. If more clusters exist, state
the count and roll the rest into one line rather than listing them.

## What this skill refuses

- Building on a retracted entry: it never heads a theme, sits on a
  contradiction, or backs a recommendation.
- Inventing or upgrading claims: nothing enters a theme that isn't in
  the log, and no confidence rises during synthesis. If synthesis makes
  the user realize an entry is missing or wrong, route through
  evidence-log first, then re-cite.
- Smoothing contradictions out of the story.

## After the synthesis

Report per the voice contract: the file path, each theme as one line
with its E-IDs and confidence, and one state line ("3 themes, 1
contradiction, 2 gaps — 14 entries in scope"). The readout itself is
for stakeholders to read in the file.

Then check each in-scope plan block's "Done when" against the log: if
it's now satisfied, remind the user to mark the question
`answered (→ E-NNN, …)` via research-plan. If Gaps names something a
stakeholder will ask about, that's the seed of the next Q-NNN block —
offer to draft it. End on that single next action.
