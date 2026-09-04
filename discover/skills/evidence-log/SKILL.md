---
name: evidence-log
description: Record, update, or query research findings in a project's evidence log. Use after any research session — interviews, usability tests, teardowns, analytics reviews — or when the user asks "what do we know about X". If the notes have no plan block yet (no research/plans.md, or no Q-NNN for their question), route to research-plan first so the entries have a question to cite, then log here. Do NOT use for planning research (use research-plan) or writing interview guides (use interview-kit).
---

# evidence-log

Maintain the project's evidence log per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`. Project
artifacts (`research/`) live under the
working directory the session started in; read and write them by those
relative paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder
above it are not the project: they hold only spec and voice files, are
read-only, and are never listed, searched, or written. Read the spec
before your first write in a session; it defines the file location,
entry format, ID rules, and confidence levels. Do not improvise fields.
Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here. One deliberate exception,
below: queried entries return verbatim, because downstream work cites
their IDs.

## Recording findings

1. Locate or create the log per the spec.
2. Turn the user's raw material (notes, transcript, observations) into
   entries: one falsifiable claim each, evidence with counts and verbatim
   quotes, source, confidence with reason, and the `Q-NNN` it answers —
   `Question: unplanned (<topic slug>)` when no plan block covers a real
   finding.
3. Before appending, scan existing headings for overlap:
   - Same claim, new evidence → add the evidence and source to the existing
     entry; raise confidence only if the new source is independent and
     firsthand — per the spec's confidence precedence, proxy corroboration
     is appended as evidence but never raises the level.
   - Conflicting claim → new entry with a `Contradicts:` line. Never edit
     the old entry to agree.
4. Append, then show the user only the new/changed entries and one line of
   log state: `Log: 14 entries, 2 contradictions open.`

Anonymize as you write: strip names, emails, and employers from quotes,
and label every voice by source type per the spec, never by the user's
own labels. Anyone interviewed firsthand is a P (a stakeholder or
manager interview is still a P), survey respondents are R, mined proxy
voices (reviews, forums, secondhand reports) are M. The user's raw notes
may carry their own scheme ("M1" for a manager, "S3" for a stakeholder,
a first name); when a label collides with the convention, relabel to the
next free ID of the right type and say so in chat in one clause ("the
manager you filed as M1 is P6 in the log; M is reserved for mined
voices, and a manager interview counts as firsthand"). Downstream skills
read the prefix as the evidence type, so a wrong prefix caps a role's
confidence for no reason.

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash anywhere in the reply, list lines and the state line included
(a comma, a colon, a parenthesis, or a second sentence instead); every
ID travels with its name, and a status or marker is said in words
rather than quoted as syntax; the state line this skill's report names
is the second-to-last line; the last line is the single first step,
stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->

## Querying

"What do we know about onboarding?" → return matching entries verbatim
(IDs and confidence included), contradictions flagged first, then one
sentence on where evidence is thin. Do not summarize entries into prose;
the IDs are the point — downstream work cites them.

If more than ~5 entries match, or the user isn't live in the chat, write
the answer to `research/queries/<date>-<topic-slug>.md` instead — header
`<!-- weaveworm evidence-query v1 -->`, plus a `Log state: <n> entries as
of <date>` line marking it a frozen snapshot (never edited later) — and
point at the file.

## What this skill refuses

- Inventing findings from no source material. If the user asks to log a
  hunch, record it at `low` confidence and say so.
- Deleting or renumbering entries. Retraction only, per the spec.
