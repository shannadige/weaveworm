# define

Definition toolkit for product designers, stage two of the stack — the
product strategy workshop as a pipeline. Five skills, four artifacts,
one sequence: charter the challenges and outcomes, map who the roles
are, map their journeys, then prioritize opportunities by impact
against complexity. Every artifact cites upstream by ID — charters and
journeys cite `E-NNN` entries; the design stage cites `OC-NNN`
outcomes and `O-NNN` opportunities instead of re-arguing them.

## The sequence

1. **product-charter** — challenges as falsifiable `CH-NNN` claims
   cited from the evidence log, a vision, and `OC-NNN` desired
   outcomes phrased as observable states — never features. Owns the
   charter lifecycle: draft, agreed (frozen), superseded.
2. **success-metrics** — fills the charter's metrics section: one
   metric per outcome with baseline, target, and window, plus
   guardrails. The charter can't be `agreed` until every outcome's
   metric is filled and its role resolved — and unknown baselines stay
   visibly unknown, never replaced with invented numbers. (Three
   skills touch `charter.md`: product-charter owns it, success-metrics
   owns the metrics section, user-roles resolves `(role tbd)` while
   it's draft.)
3. **user-roles** — `U-NNN` blocks for users, customers, and
   stakeholders, split by what they observably do and need — never
   demographics — each grounded in the log's P/R/M voices.
4. **journey-map** — one `J-NNN` file per role × scope: current state
   as evidence-cited stages with friction, future state as per-stage
   shifts describing what changes *for the user* — the opportunity,
   never the solution.
5. **opportunity-map** — the handoff: `O-NNN` blocks ranked by impact
   (which outcomes they move, per evidence) against complexity (the
   team's stated call, never invented), each tied to the role and
   journey moment it lives in.

You don't invoke skills by name — just ask naturally. "What are we
actually trying to solve?" triggers product-charter; "who are our
users?" triggers user-roles; "where does it break down for admins?"
triggers journey-map; "what should we work on?" triggers
opportunity-map.

## Files it creates

Everything lives under one `define/` root in your project, next to
`research/` (say once if you keep it elsewhere; the session remembers):

```
define/
├── charter.md                 # challenges, vision, outcomes, metrics
├── charter-<agreed-date>.md   # archived superseded charters
├── roles.md                   # all U-NNN role blocks
├── journeys/J-NNN-<slug>.md   # one journey per role × scope
└── opportunities.md           # all O-NNN blocks, ranked
```

Skills create every file and header themselves — you never scaffold
anything.

## Getting the most out of it

- **Run the sequence in order the first time.** Outcomes anchor
  metrics and impact; roles anchor journeys; journeys anchor
  opportunities. Each skill works standalone, but skipping a stage
  surfaces as `(role tbd)`, `unstated outcomes (assumption)`, or a
  `—` journey line — honest gaps that point back at the skipped
  stage.
- **No research yet? Every stage has an assumption-led path.**
  With no evidence log, each skill opens with a short intake — at most
  ~5 prerequisite questions — and writes your answers as
  `(assumption)`-labeled claims. Mandates and greenfield work get
  charters, roles, and journeys too, with the open questions doubling
  as your first research backlog for discover's research-plan. When
  evidence lands later, claims get re-cited — promotion, not rewrite.
- **`agreed` means frozen.** While the charter is `draft`, edit
  freely. Once the team commits, changes go through supersession — the
  record of what was agreed never silently changes. (One exception:
  backfilling a measured baseline that was promised as unknown.)
- **Outcomes over artifacts.** Each skill ends by forcing the decision
  its artifact exists for — which role matters most, which moment
  hurts, which opportunity gets pursued — and every artifact is
  capped (5 challenges, 5 outcomes, ~7 roles, 8 stages, ~10 open
  opportunities) so it stays a decision tool, not a document.
- **Trust the inheritance rules.** Confidence is the weakest
  load-bearing entry, corroboration never inflates it, complexity is
  never invented, and define never raises a level — only firsthand
  evidence recorded or merged through discover's evidence-log does.

The shared contract all five skills write against:
[define-spec.md](references/define-spec.md). How they talk while
writing it: [voice.md](references/voice.md), the conversation contract
shared across all weaveworm stages. The upstream format it
consumes:
[discover's evidence-log spec](../discover/references/evidence-log-spec.md).
