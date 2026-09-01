---
name: design-critique
description: "The gate stage of design — run a dated critique pass over a brief's artifacts against fixed lenses: charter constraints violated, non-goals crept into, journey shifts dropped or contradicted, roles unserved, decisions untraced, (untested) choices counted. Verdicts per lens with cited IDs, never a score. Use when a designer says \"critique this\", \"review the design\", \"does this hold up\", \"are we still on charter\", or before handing work to testing or delivery. Do NOT use for code review, reviewing research instruments (use discover), or fixing what it finds (route fixes through the owning skill)."
---

# design-critique

The gate stage of design: the recurring pass that checks the work
against the charter it must not betray. Input: a brief and every
design artifact citing it — concepts, decisions, flows, prototype —
plus the charter, journeys, roles, and the pulled opportunity's
block in opportunities.md upstream, read as they stand now, not as
they stood at pull time. This skill's intake floor is empty: it asks
the user nothing; its input is the artifacts as they stand. Output:
`design/critiques/<date>-B-NNN.md` per the spec's critique format,
and the one write this skill makes outside its own file: the brief's
Status to `reviewed (<date>, → D-NNN)` when the gate clears, the
pick pointer carried forward per the brief lifecycle. Read the spec at
`${CLAUDE_PLUGIN_ROOT}/references/design-spec.md` before your first
write in a session — it owns the lens set, the verdict form, and the
gate; do not improvise lenses. Conversation runs per the voice
contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register,
translation, and question/report shape live there, not here.

## Critique rules

- **Fixed lenses, fixed order, verdict per lens.** Constraints,
  Non-goals, Shifts, Roles, Traceability, Debt census — all six run
  every pass, in that order, each closing `clean` or with findings
  citing IDs. Never a composite score: a number is how a critique
  stops being argued with, and a finding without cited IDs is an
  opinion, not a finding. The constraint lens rechecks against the
  charter as it stands at critique time, naming any constraint that
  shifted since the brief's pull — a draft charter's drift is exactly
  what this catches.
- **A critique is a dated record, never edited.** The next pass is a
  new file; the sequence of files is the design's audit trail, and
  an amended critique is a critique that never happened. Fixes land
  in the artifacts, and the next pass shows them landed.
- **Findings name owners; critique never fixes.** A traded-away
  constraint points at the brief or decision that traded it; a
  dropped shift at flow-map; an untraced screen at decision-log
  (which mints the missing block) or prototype (which cuts the
  screen); a decision nothing traces to is flagged as noise — it
  keeps its ID, flagged, never deleted. The critique that quietly
  repairs what it found has stopped being a gate and started being
  an author reviewing itself.
- **The debt census is priced, not just counted.** Count the
  `(untested)` decisions and the brief's `(assumption)` lines, then
  weight by stakes: for each high-stakes item — hard to reverse, or
  load-bearing for the brief's `Done when:` — name the cheapest test
  or intake question that would clear it, phrased as a research-plan
  seed. An assumption-led brief gets its debt named in the verdict
  with define as the pointed-to fix; the census prices the debt, it
  never blocks on it.
- **Standing findings recur until resolved, every pass.** An
  override-pulled brief (its `O-NNN` still open), a draft or absent
  charter, and a `reviewed` brief with no `Q-NNN` plan naming its
  test seeds each stay a named finding in every subsequent pass
  until the owning artifact records the fix. Repetition is the
  point: a debt that stops being named becomes a decision nobody
  made.
- **The gate is partial, and this skill holds it.** Lenses 1 and 2
  clean — no constraint traded, no non-goal crept — writes the
  brief's Status to `reviewed (<date>, → D-NNN)`, the pick pointer
  carried forward: coherent and charter-true,
  ready to put in front of users, deliberately not done. Critique
  never writes `validated`; it mints no evidence, and only cited
  test entries clear that bar, through decision-log. Findings on
  lenses 3 through 6 don't block `reviewed` — they're named,
  owned, and priced instead.

## After the critique

Report per the voice contract: the file path, one line per lens with
its verdict, the census in plain terms, and the state line
("critique 2026-09-14, B-001: 4 lenses clean, 1 constraint finding,
5 untested / 2 assumptions"). The decision this artifact exists for:
disposition on what it found — for each finding, fix, test, or accept
with the debt named, forced in order of what blocks the gate. When
the gate cleared, the close is the bridge instead: `reviewed` is not
a resting place, so the single next action is the research-plan run
that lifts the prototype's test seeds into `Q-NNN`s — and say
plainly that until it exists, the missing plan is itself a standing
finding.

## What this skill refuses

- A score, grade, or any composite number standing in for verdicts.
- Editing the artifacts it critiques — the Status write on a cleared
  gate, plus `parked` on the user's call per the spec, is the whole
  of its reach; fixes route to owners.
- Editing or superseding a past critique — the next pass is a new
  file.
- Softening a violation into a suggestion — a traded constraint is
  named as traded, whoever traded it.
- Writing `validated`, ever — critique mints no evidence.
- Dropping a standing finding because it was named last pass.
