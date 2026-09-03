# Findings from the Nook second pass (2026-09-03)

Source: the seven skills the first run did not exercise, run one after
another on a copy of that run's final workspace, sonnet, 7 runs, $3.34.
Evidence under `.runs/2026-09-03-nook-run2/`: `ws/` (git history per
step), `logs/<step>.jsonl`, `prompts/`, `run2.out` (per-step summary
with each final reply). Three read-only audits checked each artifact
against its skill file and spec; their line-cited claims were spot
checked and hold. This note follows the shape of
`2026-09-03-nook-run-fixes.md`: fixes first, then decisions for Shan.

Headline: all seven skills fired, every kit went through research-plan
first, review-mining and outcome-review logged through evidence-log,
build-review held the gate, and outcome-review refused a ship date the
slice record did not support. Nothing was written outside the
workspace. The defects are in verdict vocabulary, counting, the
knowledge-only teardown, and chat shape.

Harness notes, so nobody chases them as skill bugs: the survey prompt
said 12 buildings where the workspace README says about 140 (the skill
caught it and proceeded on the user's figure, flagged); the outcome
prompt claimed a clean review and a ship date that no record backs (the
skill caught that too). `ws/research/raw/app-reviews-2026-08.md` is a
synthetic fixture written for review-mining.

## 1. Plugin-root reach is now a deliver problem too

build-review's second call was `find <repo> -maxdepth 2` over the
plugin's parent folder (`22-build-review.jsonl`); outcome-review read
the spec, slice, brief, and charter at `<repo>/{deliver,design,define}/…`
before recovering with `pwd` (`23-outcome-review.jsonl`, calls 5 to 9).
The five discover runs made no reach. The flow-map smoke case still
fails the same grader in about half of runs after four rewordings of
the shared sentence (see item 8a). Every reach was a read of a missing
file or a listing; no write.

Change: the prose lever is spent. Two remaining levers, one is a
decision (8a): a PreToolUse hook shipped with each plugin that denies
Read, Glob, Grep, and Bash paths under `${CLAUDE_PLUGIN_ROOT}/..`
outside `references/` and `skills/`; or a runner-side check only, and
accept the reads as harmless.

## 2. Chat shape across all seven replies

Bold phrases 2, 5, 9, 6, 9, 5, 4 per reply against a cap of one; em
dashes 2 to 10; every reply ends on a statement, but three end on a
second unresolved item or a bundle of actions rather than one next
step (survey-kit, usability-test-kit, outcome-review). Bare IDs
(`D-001`, `SL-001`, `E-010/E-011`) and backticked statuses (`low`,
`answered`) leak spec syntax into chat in five replies. The voice
contract's new "before you send" rule did not move this on its own.

Change: inline the three rules that break (one bold, no mid-sentence
em dashes, last line is the single first step) into each skill's
"After the write" section as a shared snippet that `scripts/sync-voice.sh`
stamps, the way it syncs voice.md; and add the state line each skill's
report contract already asks for to the same snippet. Then re-run the
smoke suite and read the three chat-shape graders, which are the
measure.

## 3. research-plan writes Fielded before anything ran

All three kit runs appended a Q block with `Fielded: Not yet, plan only`
(`ws/research/plans.md:26,38`) or asserted fielded because recruiting
was scheduled (`plans.md:50`). research-plan's rule is that Fielded is
the one line appended when the work actually runs; a real Fielded line
later would be a second one.

Change: `discover/skills/research-plan/SKILL.md`, the Fielded rule: the
line is absent until at least one session, send, or capture happened;
unfielded state lives in Status and Timeline. Add the same to the
plan-block template's comment so the kits inherit it.

## 4. The P/M label collision resurfaced in consent scripts

Item 3 fixed evidence-log; the kits still promise participants the
wrong prefix. interview-kit's consent says the manager will appear as
"M2" (`ws/research/kits/Q-002.md:53`); usability-test-kit numbers its
participants P6 to P10 while the log's firsthand manager is still M1
(`Q-004.md:75`), so the next free number is P7 once that relabel lands.

Change: interview-kit and usability-test-kit consent rules: firsthand
participants are P-numbered, M is mined voices only; read the log's
highest P before numbering and state the next; if the log carries a
firsthand voice under M, say so in chat in one clause.

## 5. Build-review invents verdict words when the build is described, not shown

The spec allows `met`, `deviated — <how>`, or `missing` per criterion;
the review wrote `unconfirmed` on three (`ws/deliver/reviews/2026-09-03-S-001.md:10,13,14`),
`unconfirmed` on an instrument (line 31, spec: `firing` or `silent`),
`undetermined` on D-001 with no contradiction found (line 26, spec
reserves it for after a contradiction), and added a sixth `## Gate`
section (spec fixes five). The gate outcome was right (S-001.3 does
call for a removal location) but three criteria are effectively
unreviewed under an undefined word.

Change, `deliver/references/deliver-spec.md` build review format and
`deliver/skills/build-review/SKILL.md`: add `unverified — <what the
input lacked>` as a criterion form that holds the gate like `missing`;
a Decisions form for "cannot tell whether D-NNN was honored", distinct
from post-contradiction `undetermined`; when the build is described
rather than shown, `Reviewed:` says so and uncovered criteria are
`unverified`, never `deviated`; no sections beyond the five lenses
(lint it); and a check that a spec still `open` was never handed off,
since a build was reviewed against one.

## 6. Outcome-review borrowed a verdict form for the no-shipped-slice case

`too early (no moving slice shipped)` is reserved for shipped slices
carrying `none alone`; here nothing had shipped and the skill's own
rule is to route to slice-plan before any reading, writing nothing.
The record (`ws/deliver/outcomes/2026-10-15-B-001.md`) also carries
prose in `Shipped:` and `Window:`, and a guardrail cited then marked
`unmeasured` because the spec offers no `too early` for guardrails.

Change: `deliver/skills/outcome-review/SKILL.md` no-shipped-slice
branch: nothing is written, readings may still be logged, the reply
routes to build-review then slice-plan. `deliver-spec.md`: add
`too early` as a guardrail verdict. Keep `no moving slice shipped` for
the `none alone` case only.

## 7. competitor-teardown narrated products it never opened

The skill's rule is absolute ("Never narrate a product you did not
open"); under a no-web-access prompt it wrote three teardowns from
recall, called it "a deliberate, user-directed exception" the skill
has no clause for, and marked Q-005 `answered` against a Done-when it
wrote for itself in the same pass (`ws/research/plans.md:54-59`). No
claim has a URL; evidence headings read "X is recalled as…", which is
unfalsifiable; E-016 is an inference from Amazon's business model, not
a remembered feature; the comparison says every cell is low and then
marks three moderate.

Change, `discover/skills/competitor-teardown/SKILL.md`: handle the
knowledge-only case explicitly, one of two ways (decision 8b). And
`research-plan`: `answered` requires at least one entry whose Source
resolves to a file, URL, or participant; a Done-when written in the
same pass as the fielding cannot be met without an observation from
outside the session. `evidence-log-spec.md`: hedges belong in
Confidence, never the heading.

## 8. review-mining counts are wrong where counting is the point

Per-app tally is Nook 8, Luxer One 3, Parcel Pending 4 (`ws/research/mining/Q-006.md:9`,
repeated at `plans.md:69` and `evidence-log.md:130`); the raw file has
9, 3, 3. Low-star count says 9 of 15; it is 10. E-021's base is 2 of 3,
not 2 of 4. E-021's `Contradicts: E-003` points the wrong way (both
want fewer reminders; E-019 is the one that contradicts E-003 and has
no link), holds prose instead of IDs, and bundles review 14 ("just send
me a second text first"), which supports the ladder, under the
"too many reminders" theme. E-022 bundles two causes the firsthand log
keeps apart. Cross-product separation, the review-6 outlier, and the
low cap were all handled correctly.

Change, `discover/skills/review-mining/SKILL.md` "Count, don't vibe":
tally per app from the item list before writing Sources, per-app
counts sum to n, each theme's cited items match the app it names; one
claim per entry; Contradicts holds IDs only with the test "the two
headings cannot both be true"; when the export has no URLs, Sources
says so; when the log already holds a non-mined M label, say so in
chat and keep numbering.

## 9. Kit-specific rules

- survey-kit (`ws/research/kits/Q-003.md`): fielding line assumed a
  10 to 20% response rate and a ~120 target the plan never set (line
  4); Q5 is an "if you knew X, would you Y" hypothetical (line 25); Q3
  has no skip for "I don't know" on Q2 (lines 22-23); no disqualifier
  list. Add: no n in the plan means target unresolved, ban assumed
  rates even labeled, name the hypothetical pattern as banned, require
  skip logic on confidence follow-ups.
- usability-test-kit (`Q-004.md`): T1's success criterion substitutes
  "doesn't say they'd email the manager" for the brief's "without the
  manager having to email anyone", a half a resident-only prototype
  cannot show (line 32); T1's scenario and success contradict (line
  31 vs 32); Mode was guessed as moderated without a marker (line 5);
  T2's heading echoes the button label (line 37); three tasks against
  the five-to-seven floor with the cut unnarrated. Add: Mode to the
  never-guess floor with `moderated (unconfirmed)` fallback; when
  Done-when has a half the artifact cannot exhibit, name it out of
  reach; headings count as task wording; fewer tasks allowed when
  length forces it, cut narrated.
- interview-kit (`Q-002.md`): Q4 names the pattern under validation
  ("like once a week", line 32); time-boxes sum to exactly 45 minutes
  with no slack (lines 24, 28, 47); the disqualify line omits
  UX/research workers. Add: for validation studies never name the
  pattern in the question; the guide fits with slack, cut a question
  rather than the buffer.

## Worth keeping, per skill

interview-kit opened with "tell me about the last time" and pressed on
"the week you skip it". survey-kit refused to narrow Participants to
locker users and said why, and split knowledge, confidence, and
enforcement belief into separate items. usability-test-kit read
fourteen files before drafting, fixed success, partial, failure, and
bound per task, and flagged that a local `index.html` cannot be
remote-tested without hosting. competitor-teardown capped everything
low and filled Not observable honestly. review-mining excluded the
annotated outlier from every tally and never counted competitor
reviews toward Nook. build-review named the secondhand account in
`Reviewed:`, cleared D-002 correctly, and left both statuses alone.
outcome-review refused the chat's ship claim, logged through
evidence-log first, minted no IDs, and spotted that the 2026-09-09
reading is a baseline candidate.

## Decisions, answered by Shan 2026-09-03

- a. Reach: ship a PreToolUse hook in each plugin that blocks Read,
  Glob, Grep, and Bash paths under the plugin's parent folder outside
  `references/` and `skills/`, returning one line the model can act
  on ("that path is inside the plugin checkout; project files live
  under the working directory, use a relative path"). Keep the
  grader; the hook is what makes it pass.
- b. Knowledge-only teardowns: forbid. competitor-teardown writes no
  teardown files, leaves the Q block `open` or `deferred — no web
  access`, adds a Fielded line saying it was attempted and nothing
  opened, and offers review-mining or captures the user supplies
  (screenshots, PDFs, pasted pages).
- c. `unverified — <what the input lacked>` joins the build review
  criterion forms and holds the gate like `missing`; a Decisions form
  `cannot tell — <why>` covers a decision the input cannot settle,
  distinct from post-contradiction `undetermined`. A review with
  every criterion unverified is still written; `Reviewed:` names the
  secondhand account.
- d. Chat-shape snippet: `scripts/sync-voice.sh` stamps a shared block
  into every SKILL.md's after-the-write section between marker
  comments (`<!-- voice:report-shape v1 -->`): one bold phrase at
  most, no mid-sentence em dashes, the skill's state line is the
  second-to-last line, the last line is the single first step as a
  statement. Lint checks the block is present and matches the
  canonical copy, as it does for voice.md.
