---
name: survey-kit
description: Turn a Q-NNN research plan whose method is a survey into fielding instruments — a screener, a versioned questionnaire, and an intro/consent text, kept in one kit file per question. Use when a designer has a survey plan and asks "write the survey", "draft the questionnaire", or wants to revise questions between waves. Do NOT use for choosing a method (use research-plan), interview guides (use interview-kit), or recording results (use evidence-log).
---

# survey-kit

Input: a `Q-NNN` block from the plan file (default `research/plans.md`)
whose Method is a survey. Output: the kit file below. If no plan block
exists, say so and run research-plan first — the kit inherits the
question and Participants line; never improvise them here. Conversation
runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here. Project artifacts
(`research/`) live under the working
directory the session started in; read and write them by those relative
paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder above it
are not the project: they hold only spec and voice files, are read-only, and are
never listed, searched, or written.

One check before drafting: research-plan warns that a survey written
before any qualitative work measures assumptions precisely. If the
evidence log has no interview-sourced entries touching this question,
raise that once — the user may proceed, but the flag goes on the kit's
Caveats line.

## Kit file

- One file per question: `research/kits/Q-NNN.md` (same `research/` root
  as the plan and evidence log; if the user keeps research elsewhere, ask
  once, then reuse their answer for the session). If a kit already exists
  for this question under a different method, split two cases: the plan
  says survey but an interview kit exists — that's the normal
  interviews-then-quantify sequence, so route back to research-plan for a
  new Q-NNN block citing the old one, don't stack a second kit on the same
  ID; the plan's Method line contradicts the existing kit —
  flag it, don't overwrite.
- Create with this header:

  ```markdown
  # Survey kit — Q-NNN <question>
  <!-- weaveworm survey-kit v1 -->
  Plan: Q-NNN in research/plans.md
  ```

- A header preamble (Fielding, Caveats), then three sections, in order:
  **Screener**, **Questionnaire**, **Intro**.

## Screener rules

Screener questions are answered unsupervised — no facilitator judges the
answer, so each needs a terminate-vs-continue branch, not a judgment call:

- Qualify on **behavior, not demographics or self-assessment**: "How many
  times in the last month did you X?" beats "Are you an experienced X-er?"
- Every screener question states its continue condition; everything else
  terminates. List disqualifiers explicitly (works in UX/market research,
  used the product < 1 week) on a `Disqualify:` line under the screener
  table; the line is part of the kit even when the plan's Participants
  line is wide. "Residents across all buildings" still excludes research
  workers and the product's own team, and a screener without the line
  lets them through.
- Mirror the plan's Participants line — who counts, who's excluded. If the
  screener drifts from the plan, flag it, don't silently widen.
- Name the analysis-time checks in the kit: straightliners (same answer
  down a scale block) and speeders (completion far under the pilot median)
  are excluded from counts, and the exclusion is reported.

## Questionnaire versioning

Same contract as interview guides — the evidence log cites
`questionnaire v1`, so versions must stay resolvable:

- Sections headed `## Questionnaire v1`, `## Questionnaire v2`, … —
  sequential, append-only, each with a one-line `Changed:` note.
- A version any respondent has answered is frozen. Changing a question's
  wording mid-field creates two incomparable datasets; a new version means
  results are reported per version, never pooled silently.

## Question rules

- **Behavior over intent**: "How many times in the last month did you X?"
  beats "How likely are you to X?" Stated intent inflates; recall of
  recent behavior is the honest signal. The hypothetical form ("If you
  knew X for certain, would you Y?") is banned outright: it asks the
  respondent to imagine a fact and then predict themselves, and the
  answer measures neither what they know nor what they do. Ask what
  they believe X is, and read the behavior question already in the
  questionnaire against it at analysis.
- **One idea per question** — no double-barreled ("How satisfied are you
  with speed and reliability?" is two questions).
- **No leading or loaded wording**, same discipline as the interview
  guide: "How do you feel about X?" not "How much do you like X?"
- **Scale hygiene**: balanced options, a genuine "not applicable / don't
  recall" escape, consistent direction across the questionnaire, 5 or 7
  points — pick one and keep it.
- **Follow-ups skip what the previous answer ruled out.** A confidence
  question after a knowledge question ("How sure are you about that?")
  skips when the answer was "I don't know"; how sure someone is of not
  knowing is a number with no meaning, and it lands in the count as if
  it had one. Write the skip on the question itself (`skip if Q2 = I
  don't know`) so the survey tool enforces it and the analysis base is
  the people who gave an answer.
- **Order**: behavior questions before attitude questions (attitudes
  contaminate recall less than the reverse), demographics last, one
  screener-critical question early enough to disqualify cheaply. Cap the
  whole thing at ~10 questions; completion collapses past that.

## Fielding floor

State the arithmetic on the kit's Fielding line: target n from the plan's
Participants line, expected response rate, therefore invites needed. If
the Participants line names a population and no n ("residents across
all 12 buildings"), the target is `unresolved`, not a round number the
kit picks; a target the plan never set is the kit widening the plan,
and the reply asks for the n. The response rate must have a source —
ask the user for their last survey's rate; if they have none, write
`unknown` for the rate and `unresolved` for invites. An assumed rate is
banned even when labeled as an assumption or written as a range ("10 to
20%, placeholder"): a range built on a guessed rate is the guess with
wider margins, and the invite count computed from it reads as sized.
With no rate on record, the first send produces one: send to a known
count, measure the return, then size the rest. Below ~30 completes,
report counts, not percentages — "7 of 24" is honest, "29%" implies
precision the sample can't carry. Pilot with 2–3 people before fielding;
their confusions are wording bugs, and fixing them is what v1 → v2 is
for.

## Intro

Short text atop the survey: purpose in one sentence, length honestly
stated in minutes, anonymity and data use in plain language, and that
they can stop at any point. Respondents become R1, R2… if any free-text
answer is quoted in the evidence log — R is the survey-respondent prefix
per the spec; P-numbers are firsthand session participants.

## Kit template

```markdown
# Survey kit — Q-001 <question>
<!-- weaveworm survey-kit v1 -->
Plan: Q-001 in research/plans.md
Fielding: target <n from the plan, or unresolved> completes / response rate <sourced rate or unknown> / invites <n, or unresolved>
Caveats: <e.g. "no prior qualitative work on this question — measures assumptions">

## Screener

| # | Question | Continue if | Else |
|---|---|---|---|
| S1 | <behavioral question> | <condition> | terminate |

Disqualify: <explicit disqualifiers>
Exclude at analysis: straightliners, speeders (< <s> seconds)

## Questionnaire v1

Changed: initial version

1. <behavior question>
2. <question>
3. <confidence follow-up> (skip if 2 = I don't know)
   ...
D1. <demographics, last>

## Intro

<text>
```

## After writing the kit

Report per the voice contract: the file path, the fielding arithmetic
line, and the concrete first step ("pilot with 2 people this week").

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash anywhere in the reply, list lines and the state line included
(a comma, a colon, a parenthesis, or a second sentence instead); every
ID travels with its name, and a status or marker is said in words
rather than quoted as syntax; the state line this skill's report names
is the second-to-last line; the last line is the single first step,
stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## After fielding

Results go to the evidence log per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`: one falsifiable
claim per entry with the counts ("18 of 42 respondents…"), Source citing
this kit's questionnaire version and field dates, `Question: Q-NNN` so
synthesis can scope it. Free-text answers are quoted verbatim and
anonymized. If completion or response rates were poor, log that too; a
survey nobody finished is itself a finding.
