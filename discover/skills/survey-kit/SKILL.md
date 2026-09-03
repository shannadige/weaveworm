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
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory the session started in; read and write them by those relative
paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder above it
are not the project, even though that folder also has stage-named
subfolders: they hold only spec and voice files, are read-only, and are
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
  used the product < 1 week).
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
  recent behavior is the honest signal.
- **One idea per question** — no double-barreled ("How satisfied are you
  with speed and reliability?" is two questions).
- **No leading or loaded wording**, same discipline as the interview
  guide: "How do you feel about X?" not "How much do you like X?"
- **Scale hygiene**: balanced options, a genuine "not applicable / don't
  recall" escape, consistent direction across the questionnaire, 5 or 7
  points — pick one and keep it.
- **Order**: behavior questions before attitude questions (attitudes
  contaminate recall less than the reverse), demographics last, one
  screener-critical question early enough to disqualify cheaply. Cap the
  whole thing at ~10 questions; completion collapses past that.

## Fielding floor

State the arithmetic on the kit's Fielding line: target n from the plan's
Participants line, expected response rate, therefore invites needed. The
response rate must have a source — ask the user for their last survey's
rate; if they have none, write `unknown` and state invites as a range,
never a single guessed number. Below ~30 completes, report counts, not
percentages — "7 of 24" is honest, "29%" implies precision the sample
can't carry. Pilot with 2–3 people before fielding; their confusions are
wording bugs, and fixing them is what v1 → v2 is for.

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
Fielding: target <n> completes / response rate <rate or unknown> / invites <n or range>
Caveats: <e.g. "no prior qualitative work on this question — measures assumptions">

## Screener

| # | Question | Continue if | Else |
|---|---|---|---|
| S1 | <behavioral question> | <condition> | terminate |

Exclude at analysis: straightliners, speeders (< <s> seconds)

## Questionnaire v1

Changed: initial version

1. <behavior question>
2. <question>
   ...
D1. <demographics, last>

## Intro

<text>
```

## After writing the kit

Report per the voice contract: the file path, the fielding arithmetic
line, and the concrete first step ("pilot with 2 people this week").

## After fielding

Results go to the evidence log per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md` — one falsifiable
claim per entry with the counts ("18 of 42 respondents…"), Source citing
this kit's questionnaire version and field dates, `Question: Q-NNN` so
synthesis can scope it. Free-text answers are quoted verbatim and
anonymized. If completion or response rates were poor, log that too; a
survey nobody finished is itself a finding.
