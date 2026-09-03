---
name: user-roles
description: Build the picture of users, customers, and stakeholders as U-NNN role blocks — each defined by what they observably do and need from the system, grounded in evidence-log voices, never demographics. Use when a designer asks "who are our users", "map the stakeholders", "what roles are we designing for", "who's the buyer vs the operator", "build personas" (this skill is the evidence-grounded version), or the charter's outcomes still say "(role tbd)". Do NOT use for writing the charter (use product-charter), mapping what a role experiences step by step (use journey-map), or recording findings (use discover's evidence-log).
---

# user-roles

The second stage of define: roles are who the charter's outcomes are for
and whose journeys get mapped next. Input: the evidence log (default
`research/evidence-log.md`; ask once if research lives elsewhere) and
the charter if one exists. Output: `define/roles.md` (define root per
the spec — ask once if definition work lives elsewhere) per the spec at
`${CLAUDE_PLUGIN_ROOT}/references/define-spec.md` — read it before
writing; it owns the block format, ID rules, and confidence inheritance.
Project artifacts (`research/`, `define/`, `design/`, `deliver/`) live
under the working directory: a path like `define/roles.md` resolves
against the working directory, never against `${CLAUDE_PLUGIN_ROOT}`,
whose folder is named after a stage but holds only the spec and voice
files, is read-only, and is never listed, searched, or written. Do not
improvise fields. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Role rules

- **Roles split on behavior and need, never demographics.** Two
  segments who do and need the same things are one role, whatever
  their title, company size, or industry — and one job title can hide
  two roles ("admin who sets up" vs "admin who audits"). Every role
  after the first carries `Distinct from:` naming the behavioral
  difference; if you can't write that line, it isn't a separate role.
- **Built from voices, and visibly so.** Cluster the log's voices
  (P/R/M, carried as written) by what they do and need; the `Voices:`
  line is the role's receipts. A role whose voices are all M-voices is
  proxy-based — visibly so on its `Voices:` line, with its Confidence
  inheriting the capped `low` per the spec's rules, `Corroborates:`
  holding repeating entries, and retracted entries never load-bearing. Contradictions per the spec's
  Contradictions-everywhere rule.
- **Kind does the org-chart work.** `user` operates the system,
  `customer` pays for it, `stakeholder` can veto or redirect it —
  one person may be all three, but the *role* is one Kind, because
  what they need from the system differs by hat. The buyer-operator
  split is the classic miss; check for it explicitly.
- **Goals are theirs, not yours.** What success looks like in the
  role's terms ("close the books by day 3"), not the product's
  ("adopts the integration"). An outcome-shaped goal belongs in the
  charter; route it there.
- **At most ~7 roles.** More means the splits stopped being
  behavioral — merge, or name the long tail in one line as
  out-of-scope bystanders.
- **Assumption-led path.** No evidence: write the roles the user
  believes exist, every claim `(assumption)`, Confidence
  `assumption-led — no evidence cited`, and offer research-plan — an
  interview study per assumed role is the classic next question.
- **Re-runs update, never duplicate.** Same role, fresh entries →
  append per the spec's allowed edits; a different role → a
  new block. The heading is fixed.
- **Single-role mode.** Called from journey-map for one role: write
  that block only (assumption-led if it must be), skip the
  which-role-matters question, and hand straight back to journey-map
  with the new `U-NNN`.

## After the roles

If the charter has `(role tbd)` outcomes, resolve them now — write the
`U-NNN` into each outcome's `For:` line (a charter `draft` edit; the
agreed gate makes `(role tbd)` in an `agreed` charter impossible
plugin-side, but on a hand-kept charter that skipped the gate, list
the mapping in chat for product-charter's supersession instead). Report per the voice contract: each role as one
line — ID, name, Kind, confidence — plus the state line ("4 roles: 2
user, 1 customer, 1 stakeholder; U-003 is proxy-based"). The decision
to force: name the role whose experience you'd map first and
the one-line why (most evidence behind it, most friction in it, or the
charter's outcomes point at it) — and offer journey-map for that role.

## What this skill refuses

- Demographic splits, or a role no voice or stated belief supports.
- A role block without `Does:` and `Needs:` filled — a name and a
  quote is a character, not a role.
- Raising confidence during clustering; per the spec, only the
  evidence log raises levels.
