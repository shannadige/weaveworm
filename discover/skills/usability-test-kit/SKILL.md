---
name: usability-test-kit
description: Turn a Q-NNN research plan whose method is a usability test into session instruments — a screener, versioned task scenarios with pre-defined success criteria, a facilitator script, and consent, in one kit file per question. Use when a designer has a usability-test plan and asks "write the test tasks", "what should I have them do", or wants to revise tasks between sessions. Do NOT use for choosing a method (use research-plan), open-ended interviews (use interview-kit), or recording findings (use evidence-log).
---

# usability-test-kit

Input: a `Q-NNN` block from the plan file (default `research/plans.md`)
whose Method is a usability test. Output: the kit file below. If no plan
block exists, say so and run research-plan first — the kit inherits the
question and the Participants line from the plan. Conversation runs per
the voice contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` —
register, translation, and question/report shape live there, not here.
Project artifacts (`research/`, `define/`, `design/`, `deliver/`) live
under the working directory the session started in; read and write them
by those relative paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the
folder above it are not the project, even though that folder also has
stage-named subfolders: they hold only spec and voice files, are
read-only, and are never listed, searched, or written.

## Before writing the kit

The plan doesn't name the artifact. The intake floor: what exactly is
being tested (URL, build, or prototype link) and its
version or date; whether sessions are moderated or unmoderated; and the
session length. Never guess a build identifier — a wrong one silently
pools results across different artifacts. If the user is unreachable,
stop rather than draft against an unnamed build. Mode is on the same
never-guess floor: a plan that says "remote" has not said moderated,
and the two modes need different success criteria and a different
script. If the build is named but the user can't be reached on mode,
write `Mode: moderated (unconfirmed)`, draft for a moderated session,
and flag it for confirmation before session 1.

## Kit file

- One file per question: `research/kits/Q-NNN.md` (same `research/` root
  as the plan and evidence log). If a kit already exists for this
  question under a different method, flag the mismatch with the plan
  instead of overwriting.
- Create with this header:

  ```markdown
  # Usability test kit — Q-NNN <question>
  <!-- weaveworm usability-test-kit v1 -->
  Plan: Q-NNN in research/plans.md
  Testing: <the artifact — live product, prototype link, build — and its state/version>
  Mode: <moderated | unmoderated | moderated (unconfirmed)>
  ```

- Four sections, in order: **Screener**, **Tasks**, **Facilitator
  script**, **Consent**.

## Screener rules

- Qualify on **behavior, not demographics or self-assessment**, mirroring
  the plan's Participants line — who counts, who's excluded, how many.
  Every question states a pass condition; if the screener drifts from the
  plan, flag it, don't silently widen.
- Usability-specific disqualifiers, stated explicitly: has already seen
  this build or prototype, works in UX/design/research.
- Access checks: the device, OS, and browser the test needs, and — for
  moderated remote sessions — screen-share capability.

## Task versioning

The evidence log cites `tasks v1`,
so versions are append-only (`## Tasks v1`, `## Tasks v2`, …) with a
one-line `Changed:` note, and a version any participant has attempted
is frozen. If the *artifact* changes between sessions (new build,
edited prototype), that also forces a new version — results against
different artifacts don't pool.

## Task rules

- **Scenarios, not instructions.** Give the goal and the context, never
  the route: "You want to split last night's dinner bill with your
  roommate" — not "tap Payments, then Split." If the task names a
  button, the task does the finding, not the participant.
- **No UI vocabulary in the task wording.** Using the interface's own
  labels ("add a *workspace*") tests reading, not navigation. Describe
  the goal in the participant's words from the screener or prior
  interviews. The task heading is task wording too: it gets read aloud,
  or shown in an unmoderated run, and a heading that echoes the
  option's label ("Tell the app you'll be away" above an "I'll be away"
  button) hands over the answer before the scenario starts. Head each
  task with the goal in the participant's words.
- **Success criteria fixed before session 1.** Each task states, in the
  kit: success (observable end state), partial, and failure — plus a
  time or give-up bound. Deciding after watching is how every session
  becomes a success.
- **Criteria test what the artifact can show.** When the brief's Done
  when has a half this artifact cannot exhibit (a resident-only
  prototype cannot show whether the manager had to email anyone), the
  kit names that half as out of reach next to the task and says what
  the session can observe instead. It never substitutes a criterion
  that sounds like the Done when ("participant doesn't say they'd email
  the manager") and calls it a direct test; a criterion worded to match
  the brief hides that the session never checked it. The half out of
  reach goes to chat as a gap the plan still owes.
- **Scenario and success point the same way.** A scenario that ends
  "do what you'd actually do" cannot have a success line that counts
  one honest answer as failure. Either the scenario sets up a goal the
  disallowed route cannot reach, or the criterion observes the path
  taken rather than what the participant says they would do. Read each
  scenario against its success line before session 1 and change
  whichever is wrong.
- **5–7 tasks, realistic order** (as a real user would encounter them),
  first task easy to settle nerves. Each fits the session length with
  slack; cut tasks, not the debrief. Fewer than five is allowed when
  the session length forces it (three bounded tasks plus consent and
  debrief is what 30 minutes holds); the cut is narrated in chat,
  naming which parts of the plan's Done when the remaining tasks leave
  uncovered, so the user can lengthen the session or accept the gap
  rather than discover it in the log.

## Facilitator script

The rules below assume a moderated session. For unmoderated tests (Maze,
UserTesting, and similar), set `Mode: unmoderated` in the header, replace
the script with per-task written instructions plus one post-task question,
make every success criterion observable from the recording alone, and drop
the rescue rule — an abandoned task is a failed task.

The script is what keeps five sessions comparable:

- Think-aloud setup: ask the participant to narrate as they go, with a
  one-line practice ("While you work, say what you're looking at and
  expecting to happen").
- **Neutral probes only** — "What are you looking for?", "What did you
  expect there?"; never "Did you see the menu?" A hint invalidates the
  task; if you must rescue a stuck participant to reach later tasks,
  mark the task failed first, then help.
- Same wording every session: read tasks verbatim, deflect questions
  with "What would you do if I weren't here?"
- It's the interface on trial, not the participant — say so at the
  start; "you can't do anything wrong here."

## Consent

Short script, read at session start: purpose in one sentence, explicit
yes before recording (screen and voice — name both), anonymization to
P1, P2… per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`, and the right
to stop or skip any task. Plain language, not legalese.

Every participant in a session is a P, whatever their role; M is for
mined proxy voices only and R for survey respondents. Before the script
names a number, read the evidence log's highest P and write the next one
into the consent section (no log yet means P1). If the log already holds
a firsthand voice under an M label, say so in chat in one clause and
leave it the next P, since the relabel will claim that number;
evidence-log owns the relabel itself.

## Kit template

```markdown
# Usability test kit — Q-001 <question>
<!-- weaveworm usability-test-kit v1 -->
Plan: Q-001 in research/plans.md
Testing: <artifact + version/date>
Mode: <moderated | unmoderated | moderated (unconfirmed)>

## Screener

| # | Question | Pass if |
|---|---|---|
| S1 | <behavioral question> | <condition> |

Disqualify: <seen this build, works in UX/research, …>
Access: <device/OS/browser, screen share>
Quota: <n> participants — <from the plan's Participants line>

## Tasks v1

Session length: <minutes>
Changed: initial version

### T1 <scenario — goal and context, no UI vocabulary>
- Success: <observable end state>
- Partial: <condition>
- Failure: <condition>
- Bound: <minutes or give-up signal>

## Facilitator script

<script — or per-task written instructions if unmoderated>

## Consent

<script>
```

## After writing the kit

Report per the voice contract: the file path, the task count with
session length, and the concrete first step ("dry-run the tasks on a
teammate today").

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash anywhere in the reply, list lines and the state line included
(a comma, a colon, a parenthesis, or a second sentence instead); every
ID travels with its name, and a status or marker is said in words
rather than quoted as syntax; the state line this skill's report names
is the second-to-last line; the last line is the single first step,
stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## After each session

Log per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`: one falsifiable
claim per entry, with the counts against the pre-defined criteria ("3 of
5 participants failed task 2 at the same step"), Source citing this
kit's tasks version, `Question: Q-NNN` so synthesis can scope it.
The plan's table row expects most usability problems to surface by
session 5: if sessions 4–5 are finding nothing new, say so; if they're
still surfacing new failures, that's a signal the design has more
problems than one round will catch, so raise it rather than quietly
recruiting more.
