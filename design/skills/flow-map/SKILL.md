---
name: flow-map
description: "The articulation stage of design — turn a brief's chosen concept into F-NNN flow files: numbered stages of user step, system state, and edge paths, each stage traced to the D-NNN decision behind it, the flow as a whole to the J-NNN.S journey moment it redesigns. Use when a designer says \"map the flow\", \"what are the steps\", \"detail the happy path\", \"what happens when it fails\", or a concept was just chosen and they want it concrete. Do NOT use for current-state journeys (use define's journey-map), choosing the concept (use concept-sprint), or building screens (use prototype)."
---

# flow-map

The articulation stage of design: where the chosen direction stops being
a phrase and becomes stages a prototype can render and a test can walk.
Input: a brief with a concept-sprint pick on record — any post-pick
Status qualifies, since each carries the pick pointer (`in-design (→
D-NNN)`, `reviewed (<date>, → D-NNN)`, `in-design — revalidation needed
(→ D-NNN)`, `validated (…through D-NNN…)`), and the concept file's
`chosen (→ D-NNN)` line is the cross-check — plus the chosen `C-NNN` and
the journey moment the brief cites. No pick on record means nothing to
articulate — route to concept-sprint; a flow drawn from an unchosen
concept launders the pick. Output: `design/flows/F-NNN-<slug>.md` per
the spec's flow file format, one flow per brief × scope. Read the spec
at `${CLAUDE_PLUGIN_ROOT}/references/design-spec.md` before your first
write in a session — it owns the file format, the stage cap, the Edges
section, and tracing rules; do not improvise fields. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory; `${CLAUDE_PLUGIN_ROOT}` holds only the spec and voice files,
is read-only, and is never listed, searched, or written. Conversation
runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here.

## Mapping rules

- **The intake floor, one batched pass at mapping start:** where
  this flow starts and stops (its scope boundary against sibling
  flows), and which stages the user already sees in their head. One
  named exception to the voice contract's batched-pass rule: edges
  are walked per stage as each is mapped, below, because "what
  breaks here" is only answerable with the stage in front of the
  user.
- **One flow per brief × scope, 8 stages at most.** The cap matches
  journey-map's, and for the same reason: past eight stages a flow is
  hiding either bloat or two scopes. Finer grain is the escape hatch,
  not a bigger file — a narrower-scoped flow with its own `F-NNN`
  ("connect a source" and "recover a failed sync" are two flows, not
  twelve stages). Propose the split; never silently truncate.
- **`Step:` is what the user does; `State:` is content and behavior,
  never visual style.** "Shows the three most recent sources, newest
  first, with a retry affordance on any that failed" is a state; "a
  card grid with blue accents" is prototype's call, made later and
  traced to its own decision if contested. A state written as visuals
  gets rewritten as what it communicates and lets the user do — and
  you say so.
- **Every stage traces to a decision.** Its `Decision:` line names
  the `D-NNN` behind it, and most stages inherit the concept's
  choosing decision. A stage resting on a choice no block covers gets
  one routed through decision-log at the moment it surfaces — the
  choice is load-bearing by definition, a stage now traces to it —
  never improvised inline. When the user can't make the call yet,
  write `— (needs one)` per the spec: an honest gap critique will
  flag, not a placeholder rationale.
- **The Edges section is required, anchored per stage.** Error,
  empty, and interrupted at minimum, each naming the `F-NNN.S` it
  branches from and what the user sees and can do there. An edge
  nobody has designed is written `not handled (open)` — a line,
  never a silence, because a silent edge reads as handled to
  everyone downstream. Edge handling that's load-bearing (retry
  semantics, data loss on interrupt) gets its own `D-NNN` like any
  stage. Walk the edges with the user stage by stage; "what breaks
  here" is a question they can always answer.
- **Assumption-led briefs pass their stand-ins down.** When the
  brief carries no `U-NNN` or `J-NNN.S` to cite, the flow header's
  `Role:` and `Journey:` lines carry the brief's population phrase
  and prose moment verbatim, `(assumption)`-labeled, per the spec's
  Standalone fallback — never an invented ID — and gain their
  citations when define's backfill lands.
- **The flow must deliver the shift the brief cites.** The brief's
  `J-NNN.S` names the journey moment this design changes; the
  mapped flow either produces that changed experience or names why
  it diverged, on the record. A flow that quietly serves a different
  moment than its brief is scope creep wearing stage numbers —
  surface it, and route a real divergence back through the brief's
  open questions or a `D-NNN` with the judgment labeled.
- **Material change supersedes; it never edits in place.** Re-pointing
  a `Decision:` line, upgrading an open edge to handled, tightening a
  `State:` — those are edits, expected as decisions land. Reordered
  or re-scoped stages, or a re-picked concept, make a different flow:
  a fresh `F-NNN` citing the new decision, the old file's header
  gaining `Status: superseded (→ F-NNN)` per the spec's flow
  lifecycle (mirroring decision reversal — the old record stays). Then sweep: prototype screens whose `data-flow`
  names the old stages and test seeds citing them are stale; name
  that blast radius in the same pass, in product terms, for
  prototype to re-point.

## After the mapping

Report per the voice contract: the file path, one line per stage
(number, the step in a phrase), the edge tally, and the state line
("F-002, 5 stages, edges: 2 handled, 1 open, 1 stage needs a
decision"). The decision this artifact exists for: which flow gets
prototyped first — name it with the one-line why, which is usually
the riskiest untested edge, the one whose failure costs the brief's
`Done when:`. When a stage sits at `(needs one)` or an
edge at `not handled (open)`, fold it into the close: the single next
action is the decision-log run or edge conversation that clears it
before the prototype hardens the gap.

## What this skill refuses

- Mapping a flow for an unchosen concept — no `D-NNN` pick, no flow;
  concept-sprint is the route.
- Visual prescription inside `State:` lines — it gets rewritten as
  content and behavior, narrated.
- A ninth stage — scope splits into a narrower flow instead.
- Omitting the Edges section, or leaving an unhandled edge silent
  instead of written open.
- Improvising a stage's rationale inline — decisions route through
  decision-log or the stage reads `(needs one)`.
- Editing a materially changed flow in place — supersession keeps the
  old record and names what it breaks.
