# design

> **Status: contracts settled; all six skills written.** Not yet
> registered in the marketplace.

Design toolkit for product designers, stage three of the stack. Six
skills, five artifact kinds, one discipline: pull a pursued
opportunity, diverge before converging, log every load-bearing
decision, map the flows, prototype what's testable — and critique the
result against the charter it must not betray. Design never re-argues
what define settled; it cites `O-NNN`, `OC-NNN`, `U-NNN`, and
`J-NNN.S` the way define cites `E-NNN`.

## The sequence

1. **design-brief** — turn a pursued `O-NNN` into a `B-NNN` brief:
   the design's job in one problem-shaped sentence, with roles,
   journey moment, outcomes, and inherited constraints cited — never
   restated.
2. **concept-sprint** — 3+ genuinely distinct `C-NNN` directions per
   brief, each a mechanism with its trades named. Ends by forcing the
   pick, recorded as a decision — parked concepts keep their IDs.
3. **decision-log** — `D-NNN` blocks for every load-bearing choice:
   rationale, rejected alternatives, and what would reverse it. The
   design stage's evidence log; the artifact critique argues with.
4. **flow-map** — `F-NNN` flows per brief × scope: steps, system
   states, and edge paths, each stage traced to the decision behind
   it.
5. **prototype** — a self-contained HTML prototype per brief, every
   screen annotated with the flow stage it renders, ending in the
   task seeds a usability test would run. Built to be tested, not
   admired.
6. **design-critique** — a dated pass against fixed lenses:
   constraints violated, non-goals crept, shifts dropped, decisions
   untraced, `(untested)` choices counted. Verdicts per lens, never
   a score.

The loop closes through discover: `(untested)` decisions seed
research-plan questions, usability-test-kit runs them, evidence lands
in the log, and decisions get re-cited with `E-NNN`s behind them.
That loop is also the validation gate: a clean critique marks a brief
`reviewed` (ready to test — deliberately not done), only cited test
evidence marks it `validated`, and a later design decision knocks it
back to needing revalidation.

No define artifacts yet? Design stands alone: design-brief asks the
prerequisite questions itself — problem, audience, constraints,
done-when — and writes the answers into the brief as labeled
assumptions. Critique counts the assumption debt instead of blocking
on it, and citations backfill once define runs (see the spec's
Standalone fallback).

## Files it creates

Everything lives under one `design/` root in your project, next to
`define/` and `research/` (say once if you keep it elsewhere; the
session remembers):

```
design/
├── briefs/B-NNN-<slug>.md      # one brief per pursued opportunity
├── concepts/B-NNN.md           # that brief's concept sprint
├── decisions.md                # all D-NNN decision blocks
├── flows/F-NNN-<slug>.md       # one flow per brief × scope
├── prototypes/B-NNN/           # self-contained HTML prototype
└── critiques/<date>-B-NNN.md   # dated critique passes
```

Skills create every file and header themselves — you never scaffold
anything.

The shared contract all six skills write against:
[design-spec.md](references/design-spec.md). How they talk while
writing it: [voice.md](references/voice.md), the conversation contract
shared across all weaveworm stages. Upstream:
[define spec](../define/references/define-spec.md) ·
[evidence-log spec](../discover/references/evidence-log-spec.md).
