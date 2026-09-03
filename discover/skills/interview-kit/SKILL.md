---
name: interview-kit
description: Turn a Q-NNN research plan into interview instruments — a screener, a versioned discussion guide, and a consent script, kept in one kit file per question. Use when a designer has a plan and asks "write the interview guide", "draft a screener", "what should I ask", or wants to revise the guide between sessions. Do NOT use for choosing a method (use research-plan), usability tests (use usability-test-kit), surveys (use survey-kit), or recording what sessions revealed (use evidence-log).
---

# interview-kit

Input: a `Q-NNN` block from the plan file (default `research/plans.md`)
whose Method is interviews or another open-ended conversational method —
not usability tests or surveys, which have their own kits. Output: the
kit file below. If no plan block exists for the question, say so and run
research-plan first — never improvise Participants or the research
question here; the kit inherits them. Conversation runs per the voice
contract at `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register,
translation, and question/report shape live there, not here. Project
artifacts (`research/`, `define/`, `design/`, `deliver/`) live under the
working directory the session started in; read and write them by those
relative paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder
above it are not the project, even though that folder also has
stage-named subfolders: they hold only spec and voice files, are
read-only, and are never listed, searched, or written.

## Kit file

- One file per question: `research/kits/Q-NNN.md` (same `research/` root as
  the plan and evidence log; if the user keeps research elsewhere, ask once,
  then reuse their answer for the session). If a kit already exists for this
  question under a different method, the plan and kit disagree — flag it,
  don't overwrite; never overwrite a kit containing a frozen version.
- Create with this header, citing the plan block it serves:

  ```markdown
  # Interview kit — Q-NNN <question>
  <!-- weaveworm interview-kit v1 -->
  Plan: Q-NNN in research/plans.md
  ```

- Three sections, in order: **Screener**, **Guide**, **Consent**.

## Before drafting

The plan doesn't carry everything the kit needs. The intake floor:
session length (default
45 minutes if they have no preference) and whether sessions are recorded.
If not recorded, the consent script drops the recording clause and keeps
the rest. Never improvise either value mid-draft. If the user can't be
reached, take the defaults (45 minutes, recorded), mark them `(unconfirmed)`
in the kit header, and flag them for confirmation before session 1.

## Guide versioning

The evidence log cites guides by version (`Source: interviews 2026-08
(P1–P6), guide v2`), so versions must stay resolvable:

- Guide sections are headed `## Guide v1`, `## Guide v2`, … — sequential,
  append-only.
- A version that has run at least one session is frozen. Revisions between
  sessions = append the next version with a one-line `Changed:` note saying
  what moved and why ("Changed: dropped Q3, everyone answered it in Q2").
- Typo-level fixes to a never-used version may edit in place; anything a
  participant has heard may not.

## Screener rules

- Qualify on **behavior, not demographics or self-assessment**: "How many
  times in the last month did you X?" beats "Are you an experienced X-er?"
- Every screener question needs a stated pass condition; list disqualifiers
  explicitly (e.g. works in UX/market research, used the product < 1 week).
- Mirror the plan's Participants line — who counts, who's excluded, how
  many. If the screener drifts from the plan, flag it, don't silently widen.

## Guide rules

- Funnel order: warm-up (context, rapport) → core (the plan's question) →
  wrap (anything missed, referrals).
- Past behavior over hypotheticals: "Tell me about the last time you…"
  beats "Would you use…". Stated intent about imaginary products is not
  evidence.
- No leading or presuming questions — same discipline research-plan applies
  to the research question itself. "How do you feel about the new nav?"
  not "What do you love about the new nav?"
- Every core question gets 1–2 probes underneath ("What happened next?",
  "What did you do instead?") so silence has a follow-up ready.
- Time-box each section; the whole guide must fit the session length with
  slack. Cut questions, not the wrap.

## Consent

Short script, read at session start. Must cover: purpose in one sentence,
recording permission (explicit yes before recording starts), how the data
is used and anonymized — participants become P1, P2… per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`, and quotes are
stripped of names and employers — and that they can
stop or skip any question. Keep it plain language, not legalese.

## Kit template

```markdown
# Interview kit — Q-001 <question>
<!-- weaveworm interview-kit v1 -->
Plan: Q-001 in research/plans.md

## Screener

| # | Question | Pass if |
|---|---|---|
| S1 | <behavioral question> | <condition> |

Disqualify: <explicit disqualifiers>
Quota: <n> participants — <who, from the plan's Participants line>

## Guide v1

Session length: <minutes>

### Warm-up (<min>)
1. <question>

### Core (<min>)
2. <question>
   - Probe: <follow-up>
3. <question>
   - Probe: <follow-up>

### Wrap (<min>)
4. Is there anything about <topic> I should have asked and didn't?

## Consent

<script>
```

## After writing the kit

Report per the voice contract: the file path, the Quota line, and the
concrete first step ("message 10 candidates today").

## After each session

The kit ends where evidence-log begins: remind the user to log findings
after every session — one falsifiable claim per entry, Source citing this
kit's guide version, `Question: Q-NNN` so synthesis can scope it, per the
spec at `${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`. The
plan's table row expects patterns from 5–8 interviews: if sessions 4 and
5 produce no new claims, stop and say so before recruiting more — that's
saturation, not laziness.
