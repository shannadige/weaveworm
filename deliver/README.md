# deliver

> **Status: spec v1, five skills written and audited.** Registered in
> the marketplace.

Delivery toolkit for product designers, stage four of the stack. Five
skills, three artifact kinds plus two dated records, one discipline:
hand a reviewed design to whoever builds it — a human engineer or a
coding agent — precisely enough that nothing load-bearing gets
decided by accident, then find out whether the outcome moved. Deliver
never re-argues what design settled and never manages the build; it
cites `B-NNN`, `D-NNN`, `F-NNN.S`, and `OC-NNN` the way design cites
`O-NNN` and `J-NNN.S`.

## The sequence

1. **build-spec** — turn a reviewed brief's flows, decisions, and
   prototype into an `S-NNN` build spec: one acceptance criterion per
   flow stage and per edge, each citing the decision behind it; the
   load-bearing decisions carried with what would reverse them; the
   prototype marked normative or incidental part by part. Asks once
   who receives it — a human engineer or an agent — and packages the
   open items to match: a handoff agenda, or stop conditions.
2. **slice-plan** — cut a spec into `SL-NNN` increments that each
   deliver a journey shift on their own and, where one can, move the
   metric. What ships first is a design decision, not a ticket.
3. **instrumentation-plan** — `I-NNN` blocks: the event behind each
   `OC-NNN` metric the brief moves, the flow stage it fires at, and
   the baseline. Without this the charter's metrics never get
   measured.
4. **build-review** — a dated pass over the build against the spec:
   criteria met, deviated, or missing; edges handled; decisions
   silently reversed; instruments present; prototype scaffolding
   leaked. Verdict per lens, never a score; deviations route to the
   owning skill, never fixed here.
5. **outcome-review** — after a slice ships and the window passes:
   did the metric move? Production numbers enter discover's evidence
   log, the reading is credited to the brief's Done when and never
   to one decision, and the record forces keep, iterate, or revert.

The loop closes through discover twice: `(untested)` decisions were
already seeds for usability tests; now shipped slices seed the
evidence that says whether the outcome the charter named actually
moved. Deliver mints no evidence and edits nothing upstream. The
reading reaches define through two writes deliver names and never
makes: success-metrics records the result on the charter's metric
line, judged against the agreed target, and opportunity-map closes
the pursued opportunity as delivered with the verdict. That is how
the objectives set in define learn what delivery bought.

## Who receives the handoff

The spec is written for the reader who can't ask: explicit gaps,
mandatory edges, decisions with their reversal conditions, and a
clear line between what in the prototype is the design and what is
scaffolding. A human engineer can skip precision they don't need; an
agent can't invent precision that isn't there. The one thing that
branches on the recipient is what happens to the open items — an
agenda for the handoff conversation, or a list of what the agent may
not decide alone. A design change after handoff is a fresh spec, the
way a changed flow is a fresh flow: the builder sees exactly what
moved, and the old spec stays on record.

## Files it creates

Everything lives under one `deliver/` root in your project, next to
`design/`, `define/`, and `research/` (say once if you keep it
elsewhere; the session remembers):

```
deliver/
├── specs/S-NNN-<slug>.md       # one build spec per brief
├── slices/S-NNN.md             # that spec's SL-NNN increments
├── instrumentation.md          # all I-NNN instrument blocks
├── reviews/<date>-S-NNN.md     # dated build review passes
└── outcomes/<date>-B-NNN.md    # dated outcome reviews
```

Skills create every file and header themselves — you never scaffold
anything.

The shared contract all five skills will write against:
[deliver-spec.md](references/deliver-spec.md). How they talk
while writing it: [voice.md](references/voice.md), the conversation
contract shared across all weaveworm stages. Upstream:
[design spec](../design/references/design-spec.md) ·
[define spec](../define/references/define-spec.md) ·
[evidence-log spec](../discover/references/evidence-log-spec.md).
