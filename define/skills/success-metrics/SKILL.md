---
name: success-metrics
description: Fill or revise the product charter's Success metrics section — one metric per OC-NNN desired outcome with baseline, target, and window, plus guardrails; every metric measures an outcome, not activity. Use when a designer asks "how do we measure this", "define success criteria", "what's the target", "what are our KPIs", "what's the north star metric" (the vision itself is product-charter), or the charter still stubs its metrics. Do NOT use for writing the charter's challenges and outcomes (use product-charter) or logging measurement findings (use discover's evidence-log).
---

# success-metrics

Input: the charter (`define/charter.md`; define root per the spec —
ask once if definition work lives elsewhere) plus whatever the user
knows about current instrumentation. Output: the charter's Success metrics
section, filled per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/define-spec.md`. This skill owns
exactly that section: while the charter is `draft` it may rewrite it
freely; once `agreed`, the only allowed edit is the spec's baseline
backfill, and anything else means the supersession procedure via
product-charter. If no charter exists yet, route to product-charter
first — metrics without outcomes have nothing to measure.

## Before writing

Ask once, as one batched question: what's instrumented today (events,
dashboards, warehouse queries), any baseline numbers already known,
and any targets handed down from above. If the user is unreachable,
write `Instrumented by: <best guess> (unconfirmed)`, use the spec's
unknown-baseline forms, and list everything unconfirmed at the end.

## Metric rules

- **One metric per outcome, keyed by its `OC-NNN`.** Read each
  outcome; its metric must be a number that moves if and only if that
  observable state comes true. For "new trial users reach a connected
  data source unaided", setup-completion rate measures the outcome;
  signups measure marketing. Two metrics on one outcome is an
  unresolved argument about what the outcome means — send it back to
  product-charter rather than papering over it with a dashboard.
- **Non-tracing metrics get pushback, then a labeled line.** Activity
  metrics (shipped, launched, story points) and any metric that
  measures no outcome: push back once, concretely — name what the
  requested metric would still show if every outcome failed
  ("engagement can rise while churn rises — power users churning
  slower mask it"), and propose the tracing alternative. If the user
  insists, record it as the spec's `- **Secondary (requested):**` line
  — never keyed to an outcome.
- **Baselines are measured, never invented.** Unknown baseline → the
  spec's `baseline unknown (unmeasured)` form, and offer to draft the
  measurement question through discover's research-plan (its analytics
  row); cite `(→ Q-NNN)` only once that plan block actually exists.
  The target then goes directional per the spec's worked example — a
  precise target over an unknown baseline is a guess wearing precision
  — and an unknown window is written
  `within <window: set with the baseline>`. On an assumption-led
  charter this is the expected shape: unknowns stay visible, never
  replaced with plausible numbers so the section looks finished. When
  a measurement later lands, the backfill — the one edit allowed after
  `agreed` — is written `<value> (measured YYYY-MM-DD)`.
- **Targets carry a why.** Per the spec: a benchmark, a cited E-ID, or
  explicit ambition marked `(ambition)`. A naked number invites
  hitting it by any means.
- **Guardrails name the damage the charter could do.** The tempting
  degradations: speed bought with error rate, activation bought with
  support load, conversion bought with trust. 1–3, shared across the
  charter (not per-outcome), each with `currently <level>` — or
  `unmeasured`, honestly; a guardrail nobody can read the current
  value of is a wish.

## After the section

Update the section in place. In chat, show one line per outcome metric,
the guardrail count, and anything routed to research-plan — never the
whole charter. If every outcome's metric now passes its half of the
spec's agreed gate, say so — and check the other half: outcomes still
reading `(role tbd)` mean user-roles stands between this charter and
`agreed`. product-charter writes that transition, and agreeing freezes
the file. End on the single next action, whichever it is.

## What this skill refuses

- A metric that measures no outcome — the insist path yields a
  Secondary (requested) line, never an outcome-keyed metric.
- Inventing a baseline, or a precise target with no stated why.
- Two metrics on one outcome.
- Editing the section of an `agreed` charter beyond the spec's
  baseline backfill.
