---
name: competitor-teardown
description: Execute a Q-NNN plan whose method is competitive teardown — use web search and browsing to walk competitor products and record what they do, in a dated teardown file per competitor. Use when a designer asks "what are competitors doing", "tear down X", "run a competitive analysis", "compare us to X", "how does X handle onboarding", "what does X charge", or the plan's method row is competitive teardown. Do NOT use for choosing the method (use research-plan), mining user reviews of competitors (use review-mining), or recording conclusions (use evidence-log).
---

# competitor-teardown

Input: a `Q-NNN` block from the plan file (default `research/plans.md`)
whose Method is competitive teardown, plus the competitors to examine —
from the plan or the user. Output: one teardown file per competitor, a
comparison file, then evidence-log entries. If no plan block exists, offer
the one-line version: confirm the question and axes inline, run the
teardown, and append the Q-NNN block afterward so the evidence stays
citable. Either way the axes come from the question, never from whatever
the competitor's homepage happens to emphasize.

## Run order

1. Read the plan's Q-NNN block, or take the one-line version above.
2. Ask once, as one batched question: which competitors (default cap 3 —
   more only if the user asks) and whatever the capability check below
   needs (e.g. is an account available). If the user is unreachable, take
   the plan's named competitors (cap 3) in fetch-only mode, marked
   `(unconfirmed)`.
3. Derive the 3–5 comparison axes from the question and show them.
4. Walk one competitor at a time: one dated file each, cross-competitor
   axes table in the comparison file.
5. Log evidence entries and close per "After the teardown".

## Teardown file

- One file per competitor per question:
  `research/teardowns/Q-NNN-<competitor-slug>-<YYYY-MM-DD>.md`. Re-tearing
  down the same competitor later creates a new dated file, never an
  overwrite — the diff between snapshots is itself a finding.
- One cross-competitor file per question:
  `research/teardowns/Q-NNN-comparison.md`, holding the axes table.
  Comparison is inherently cross-competitor; it lives once, not repeated
  per file.
- Create each teardown with this header:

  ```markdown
  # Teardown — <competitor> (Q-NNN)
  <!-- weaveworm competitor-teardown v1 -->
  Plan: Q-NNN in research/plans.md
  Captured: <date> — competitor sites change; a teardown is a snapshot, not a fact sheet
  ```

- Sections, in order, each with a fixed contract so two teardowns stay
  comparable:
  - **Positioning** — verbatim headline, subhead, and stated target user.
  - **Walkthrough** — the steps actually observed, numbered, one line each.
  - **Pricing & packaging** — tiers, pricing unit, and what gates each tier.
  - **Read** — this-competitor-only interpretation, explicitly marked as
    inference.
  - **Not observable** — what couldn't be seen and why.

## Before walking anything

Check what you can actually reach, and say which mode applies:

- Browser automation plus an account — full walkthrough.
- Fetch-only (no clicking, no signup) — restrict Walkthrough to public
  surfaces (marketing site, docs, changelog, pricing page) and put every
  post-signup flow in **Not observable**.
- Neither, or the competitor is a desktop/mobile/sales-gated product you
  can't open — say so and stop. Never narrate a product you did not open.

## Teardown rules

- **Observe, don't infer motive.** Record what the product does and says —
  verbatim headlines, flow steps, screenshots when browsing allows, prices.
  "Their onboarding asks for a team size before showing the product" is
  evidence; "they're targeting enterprise" is interpretation and belongs in
  the **Read** section, marked as such.
- **Axes come from the question.** Compare on the 3–5 dimensions the plan's
  question needs, not a feature-matrix of everything. A teardown that
  inventories every feature answers no question.
- **Every claim gets a source**: URL + capture date. If it came from a
  review site or press coverage rather than the product itself, say so —
  secondhand description of a competitor is weaker than walking the flow.
- **Name what you couldn't see.** Gated flows (post-signup, paid tiers,
  sales-only demos) go in **Not observable** — an empty section here is a
  smell, not a virtue.

## Confidence when logging

Teardown findings split into two kinds; log them differently per the
spec at `${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`:

- Claims about *the competitor's product* ("X charges per seat, captured
  2026-08-05") — direct observation, `medium` is typical; `high` if
  verified across two independent sources.
- Claims about *what users want*, inferred from competitor choices
  ("competitors all offer Y, so users must need it") — inference, cap at
  `low`. Competitors copy each other; convergence is not demand.

## After the teardown

Log findings in the evidence log — one falsifiable claim per entry,
Source citing the teardown file and capture date (e.g.
`Source: teardown Q-003 acme, captured 2026-08-05`), `Question: Q-NNN`
so synthesis can scope it. Then check the plan's "Done when": if the
teardown was the last evidence it named, remind the user to mark the
question answered in research-plan.

In chat, show only the comparison axes, the new E-NNN headings, and one
state line ("2 teardowns, 5 entries logged"). Never paste teardown
bodies into the conversation — point at the files.
