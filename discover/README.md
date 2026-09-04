# discover

Discovery toolkit for product designers. Eight skills, one pipeline: plan a
question, run the study, log the evidence, synthesize the readout. Every
artifact has a fixed shape and a citable ID, so any later work can point
at `E-014` instead of re-quoting research.

## The loop

1. **research-plan** — turn a product question into a `Q-NNN` plan block
   (method, participants, timeline, definition of done) in `research/plans.md`.
2. **Run the method skill** the plan chose:
   - `interview-kit` — screener, discussion guide, consent
   - `survey-kit` — screener, questionnaire, intro/consent
   - `usability-test-kit` — tasks with success criteria, facilitator script
   - `competitor-teardown` — walks competitor products, axes comparison
   - `review-mining` — mines app stores, G2, Reddit, support threads
3. **evidence-log** — after each session, record findings as `E-NNN` entries:
   one falsifiable claim each, with counts, quotes, source, and confidence.
4. **synthesis** — compose logged entries into a stakeholder readout. Themes
   cite entry IDs; contradictions and gaps are named, not smoothed over.

Repeat 2–3 per session; run 4 when a question's sessions are done.

You don't invoke skills by name — just ask naturally. "How should I research
onboarding drop-off?" triggers research-plan; "write the interview guide"
triggers interview-kit; "what did we learn?" triggers synthesis.

## Files it creates

Everything lives under one `research/` root in your project (say once if you
keep research elsewhere; the session remembers):

```
research/
├── plans.md                              # all Q-NNN plan blocks
├── evidence-log.md                       # all E-NNN findings (shared spec)
├── kits/Q-NNN.md                         # interview / survey / usability kits
├── teardowns/Q-NNN-<competitor>-<date>.md
├── teardowns/Q-NNN-comparison.md         # cross-competitor axes table
├── mining/Q-NNN.md                       # review-mining output
├── queries/<date>-<topic>.md             # answers to "what do we know about X"
└── synthesis/<date>-<topic>.md           # dated readouts
```

Skills create every file and header themselves — you never scaffold anything.

## Getting the most out of it

- **Start with research-plan.** Downstream skills inherit the question and
  participants from the plan block and will refuse to improvise them. A
  question skipped at planning time resurfaces as a mid-study argument.
- **Log evidence right after every session.** Synthesis reads only the log —
  a finding that stays in your head or a transcript doesn't exist to it.
- **Let contradictions stand.** Conflicting findings become linked entries
  (`Contradicts: E-003`), never edits. The tension is data for synthesis.
- **Trust the confidence rules.** `high` means observed behavior or 2+
  independent sources; proxy sources (reviews, forums) corroborate but never
  raise confidence. If a claim is cheap-to-be-wrong-about but severe if true,
  mark `Stakes: high`.
- **No users yet?** Say so — research-plan routes to proxy sources and
  review-mining instead of stalling on "recruit participants".

The shared contract all skills write against:
[evidence-log-spec.md](references/evidence-log-spec.md). How they talk
while writing it: [voice.md](references/voice.md), the conversation
contract shared across all weaveworm stages.
