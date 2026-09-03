# Fix plan from the 2026-09-03 Nook end-to-end run

Source: one use case (Nook, parcel lockers for apartment buildings) driven
through 17 of the 24 skills headlessly on sonnet, 20 runs, $7.05. Every
artifact, trace, and prompt is under `.runs/2026-09-03-nook-e2e/`:
`ws/` is the final workspace, `logs/<step>.jsonl` the stream-json trace
per run, `prompts/<step>.md` what the user said, `run.sh` the runner.
Read a trace with `python3 -c` over the `assistant` events; the
`tool_use` blocks carry every path a skill touched.

Work the items in order. Items 1 to 5 are fixes; item 6 is voice; item 7
is verification; item 8 lists decisions that need Shan and must not be
"fixed" unilaterally, because the current behavior is spec'd.

Conventions that bind this work: `references/voice.md` is canonical and
each plugin's copy is synced by `scripts/sync-voice.sh`, never edited
directly. Run `scripts/lint-skills.sh` after every SKILL.md edit. Chat
prose follows the voice contract. Commit per item, not one blob.

## 1. Skills reach into the plugin repo for project files (highest)

Finding: 11 of 20 runs tried to read or list project artifacts under the
plugin checkout (`<repo>/define/charter.md`, `<repo>/research/...`,
`<repo>/design`), then recovered. journey-map ran `mkdir -p
<repo>/define/journeys` and then removed it (trace `07-journey.jsonl`).
flow-map ran `git log --oneline --all` inside the repo hunting for the
brief (`11-flow.jsonl`). Cause: every SKILL.md names the spec at
`${CLAUDE_PLUGIN_ROOT}/references/...`, and the model generalizes that
root to the project. Only `define/skills/journey-map/SKILL.md:16-19`
says the define root lives under the working directory and the plugin
root is never written to; it still slipped.

Change:
- Add one shared sentence to every SKILL.md's intro paragraph, right
  after the spec citation, worded the same everywhere: project
  artifacts (`research/`, `define/`, `design/`, `deliver/`) live under
  the working directory; `${CLAUDE_PLUGIN_ROOT}` holds only the spec
  and voice files, is read-only, and is never listed, searched, or
  written. Apply to all 24 skills (`*/skills/*/SKILL.md`).
- Add the same rule once to each stage spec's file-location section
  (`discover/references/evidence-log-spec.md`,
  `define/references/define-spec.md`, `design/references/design-spec.md`,
  `deliver/references/deliver-spec.md`).
- Extend `scripts/lint-skills.sh` to fail when a SKILL.md lacks the
  sentence (grep for a fixed phrase, the way it greps for
  `references/voice.md` at line 28).
- Add a trace grader to each of the four smoke cases
  (`<plugin>/evals/<case>/graders/no-plugin-root-reach.md`): type
  `regex`, `target: trace`, `match: none`, pattern along the lines of
  `weaveworm/(research|define|design|deliver)/(?!references/|skills/)`
  plus `weaveworm[^"]*git log`. Tune the pattern against
  `.runs/2026-09-03-nook-e2e/logs/07-journey.jsonl` (must hit) and
  `02-evidence-log.jsonl` (must not hit) before trusting it.

Verify: `scripts/smoke.sh`; the new grader passes on all four cases and
`wrote_outside` stays empty. Re-run `07-journey` with
`.runs/2026-09-03-nook-e2e/run.sh` against a copy of `ws/` rolled back
to before that step (git history was stripped from the copy, so
recreate by deleting `define/journeys/`, `define/opportunities.md`,
`design/`, `deliver/`) and confirm no plugin-root paths in the trace.

## 2. research-plan does not trigger when the user already has notes

Finding: prompt `prompts/01-research-plan.md` asks "How should I
research this?" and mentions unlogged raw notes. sonnet skipped the
skill, read the raw files, advised against more research, and ended on a
menu (`01-research-plan.jsonl`, no `Skill` tool use). It triggered on
the follow-up (`01b-research-plan.jsonl`).

Change: strengthen the description in
`discover/skills/research-plan/SKILL.md:3`. Name the case: research
already run but unplanned, "I have notes but no plan", "put the question
on record", and say the skill still applies when the answer will be
"log what you have". Keep the Do NOT clause. Consider the same pass over
`evidence-log`'s description so the pair route cleanly: notes with no
plan go to research-plan first, then evidence-log.

Verify: re-run `prompts/01-research-plan.md` three times on sonnet with
the discover plugin; the `Skill` tool fires with
`discover:research-plan` in at least two. Check with the smoke runner's
`tool_used` grader (`tool: Skill`, `input_match: research-plan`) if you
add it as a case, `discover/evals/research-plan-notes-first/`.

## 3. evidence-log carries the user's participant labels into the log

Finding: the raw manager interview was filed as "M1" by the PM. The log
kept `M1` (`ws/research/evidence-log.md`, E-002, E-005, E-012, E-014).
`discover/references/evidence-log-spec.md:36` reserves M for mined proxy
voices, so user-roles capped U-002 to low confidence and spent a
paragraph explaining the collision (`ws/define/roles.md`, U-002
Confidence line).

Change: in `discover/skills/evidence-log/SKILL.md:36` (the anonymize
step) say voices are labelled by source type per the spec, not by the
user's own labels: interview participants become P-n, survey respondents
R-n, mined proxy voices M-n, and a stakeholder interview is still a P.
When a user's label collides with the convention, relabel and narrate
the translation in chat (voice contract: translations are narrated).
Mirror one sentence in the spec at line 36.

Verify: re-run `prompts/02-evidence-log.md` on the run's raw notes; the
manager appears as P6 (or similar), and user-roles on the result gives
U-002 a confidence above the proxy cap.

## 4. prototype writes its README to a nested path

Finding: `ws/design/prototypes/B-001/design/prototypes/B-001/README.md`
(trace `12-prototype.jsonl`: a `cd ./design/prototypes/B-001` in Bash,
then a relative Write). `index.html` landed correctly. design-critique
noticed and reported it as an aside without repairing; build-spec read
the nested file silently (`14-spec.jsonl`).

Change:
- `design/skills/prototype/SKILL.md` around lines 12-13: state both
  files are written to `design/prototypes/B-NNN/` from the project
  root, with no `cd`, and that the skill lists the folder after writing
  and fixes any misplacement before reporting.
- Critique not repairing is spec'd
  (`design/skills/design-critique/SKILL.md:46`), so route the repair:
  in the critique skill, a misplaced or missing prototype README is a
  Traceability finding owned by prototype, not an aside. In
  `deliver/skills/build-spec/SKILL.md`, a README found anywhere other
  than `design/prototypes/B-NNN/README.md` is reported as a design-side
  defect in the spec's `For the builder` paragraph rather than read
  silently.
- Add a `file_exists` grader for `design/prototypes/*/README.md` to a
  prototype eval case if one is added; the smoke suite has none today.

Verify: re-run `prompts/12-prototype.md`; README lands beside
`index.html`; no nested `design/` directory appears.

## 5. design-brief edits a define artifact

Finding: to mark O-001 pursued, design-brief read
`define/skills/opportunity-map/SKILL.md` from the sibling directory and
edited `ws/define/opportunities.md` (`09b-brief.jsonl`). Correct result,
but it only works because all four plugins share one checkout; an
installed design plugin may not have define beside it.

Change (after item 8a is decided): either
- sanction it: add to `design/references/design-spec.md` (Standalone
  fallback or Upstream contract section) that design-brief may set
  `pursued` on the user's explicit say-so, using the exact form
  opportunity-map writes (`Status: pursued (<date>)`, block moved under
  the `<!-- pursued -->` marker), and record the write in chat; or
- forbid it: design-brief stops and asks the user to run
  opportunity-map, with the override form it already offers
  (`Pulls: O-NNN — open, designed on user override (assumption)`) as the
  only alternative.
Either way, `design/skills/design-brief/SKILL.md:25-32` gets the rule
and stops depending on the define skill file being on disk.

## 6. Chat voice: formatting rules slip even when the skill fires

Finding, across the 20 final replies (see `logs/*.jsonl`, `result`
event): em dashes averaged about eight per reply, bold phrases exceeded
one in 14 replies, five replies ended on a question. Register,
translation, and IDs-with-names held. Worst case was the untriggered
research-plan reply (item 2).

Change: the contract already bans these
(`references/voice.md`, Register). Two levers:
- Add a short "before you send" line to the Reporting section of
  `references/voice.md`: one bold at most, no mid-sentence em dashes,
  close on the decision or next action as a statement, never a
  question. Then `scripts/sync-voice.sh`.
- Add a `last_message` regex grader to each smoke case: `match: none`
  on `\?\s*$` (ends on a question) and a count-style check on `—` if
  the runner grows one (today `regex` only supports contains/none; a
  `max` count would be a small addition to `grade()` in
  `scripts/eval-pilot.py`).

Verify: smoke suite; eyeball three final replies.

## 7. Verification pass

1. `scripts/lint-skills.sh` clean.
2. `scripts/smoke.sh` clean, including the new graders from items 1 and
   6.
3. Targeted re-runs named under items 1 to 4, using
   `.runs/2026-09-03-nook-e2e/run.sh` (edit `SP` at the top to point at a
   fresh copy of `ws/`).
4. `git status` on the plugin repo clean of anything but the intended
   edits after every headless run.

## 8. Decisions for Shan, not fixes

These are current spec choices the run surfaced. Do not change them
without an answer.

- a. Cross-stage writes (item 5): sanctioned with a named form, or
  forbidden.
- b. Critique gate scope: `design/references/design-spec.md:446` makes
  the gate partial (Constraints and Non-goals only). The run passed
  B-001 to `reviewed` while U-002, named in `For:` and load-bearing for
  half of `Done when`, had no flow or screen. Decide whether an unserved
  named role blocks `reviewed`, or whether design-brief should instead
  force the user to narrow `For:` when scope is one-sided.
- c. Metric placeholder form: `define/references/define-spec.md:193-197`
  prescribes the literal `within <window: set with the baseline>`. In
  the charter (`ws/define/charter.md`, Success metrics) it reads as
  template leakage, four times. Options: keep, or replace with prose
  ("window set with the baseline") that the spec still recognizes.
- d. Metric line length: each metric line in the run is 80 to 120 words
  because baseline reasoning, proxies, and caveats all sit on one
  bullet. Decide whether the spec should split caveats onto a
  sub-bullet.
- e. Whether to run the five study-instrument skills, build-review, and
  outcome-review on this use case next; they were not exercised.

## Smaller items, fold into the nearest commit

- `design/skills/flow-map/SKILL.md`: a stage is a user step;
  `ws/design/flows/F-001-resident-parcel-escalation.md` F-001.1 ("Parcel
  remains uncollected") is a state. Add a one-line check mirroring
  journey-map's "stages are units of progress" rule.
- `discover/skills/synthesis/SKILL.md`: scheduling words in the user's
  ask ("Thursday's meeting") are not an unresolved item for the readout;
  the synthesis listed it as one (`ws/research/synthesis/`).
- `discover/skills/research-plan/SKILL.md` Fielded line: the run
  attributed the question reframe to the PM when the skill made it
  (`ws/research/plans.md`, Fielded). Say that a call the skill makes is
  recorded as the skill's, flagged for confirmation.
