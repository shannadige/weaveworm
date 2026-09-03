---
name: research-plan
description: Turn a product question into a one-page research plan — method chosen via decision table, participants, timeline, and a definition of done. Plans accumulate in research/plans.md as Q-NNN blocks with open/answered/dropped status. Use when a designer or PM asks "how should I research X", "should I run interviews or a survey", adds a new question mid-project, wants to mark a question answered, or can't reach users directly and needs proxy sources. Also use when research has already been run but never planned: "I have interview notes but no plan", "we did six interviews last week and nothing is logged", "put the question on record". It still applies when the right answer is "log what you have": the plan block is what evidence-log entries cite, so it gets written first (marked as already fielded), and only then do the notes go to evidence-log. Never skip it to read the raw notes and advise directly. Do NOT use for recording findings themselves (use evidence-log, once a plan block exists).
---

# research-plan

Input: a product question in plain language. Output: the one-page plan
below, filled in and appended to the plan file. If the user's question
is really several questions, say so and plan for the one they confirm
matters most; the others can be appended later as their own `Q-NNN`
blocks. Conversation runs per the voice contract at
`${CLAUDE_PLUGIN_ROOT}/references/voice.md` — register, translation, and
question/report shape live there, not here. Project artifacts
(`research/`, `define/`, `design/`, `deliver/`) live under the working
directory the session started in; read and write them by those relative
paths and never `cd`. `${CLAUDE_PLUGIN_ROOT}` and the folder above it
are not the project, even though that folder also has stage-named
subfolders: they hold only spec and voice files, are read-only, and are
never listed, searched, or written.

## Plan file

- Default path: `research/plans.md`, next to the evidence log. If the user
  keeps research elsewhere, ask once, then reuse their answer for the session.
- If the file doesn't exist, create it with this header before appending:

  ```markdown
  # Research plans
  <!-- weaveworm research-plan v1 -->
  ```

- Each plan is one `Q-NNN` block, sequential (next ID = highest existing + 1,
  zero-padded). Append-only: a new question is a new block, never an edit to
  an old one.
- **Status** is always the first bullet under the heading, so heading + next
  line alone give a complete index of questions and their state.
- Two edits are allowed to an existing block: its **Status** line, and
  appending one **Fielded:** line when the work actually runs (actual
  dates, sessions completed, instrument version used) — Timeline stays
  the plan; Fielded records reality. The line is absent until at least
  one session, send, or capture has happened. Before that, "not yet
  fielded" is what Status and Timeline already say; scheduled recruiting
  is still a plan, and a placeholder Fielded line would leave a second
  one when the work runs. When the research ran before any plan existed (notes in
  `research/raw/`, no block), write the block from what happened and
  add its Fielded line in the same pass, so the evidence log has a
  question to cite. Status transitions:
  - `open` → `answered (→ E-014, E-015)` once the entries named in "Done
    when" exist in the evidence log — cite them by ID. Substantively
    answered but formally short of "Done when" (or the reverse) →
    `answered (→ …) — caveat: <one line>`, never a stretched claim and
    never an edited "Done when".
  - `answered` needs an observation from outside the session: at least
    one of the cited entries must have a Source that resolves to a file,
    a URL, or a participant. A "Done when" written in the same pass as
    the fielding cannot be met by that pass alone, however carefully its
    claims are hedged; recall is not evidence. Until something was
    opened, read, or heard, the block stays `open` or goes `deferred`.
  - `open` → `deferred — <reason>` for a question planned but knowingly
    not schedulable yet.
  - `open` → `dropped — <reason>` if the question is abandoned. Never delete
    the block.

## Method decision table

Pick the row that matches what the user wants to know. Show them the row and
the "why" — the choice must be inspectable, and they may overrule it.

| You want to know… | Method | Why this one |
|---|---|---|
| Why people do/don't do something | Interviews, 5–8 people | Motivation only surfaces in open conversation; small n is enough for patterns |
| Whether people can use the thing | Usability test, 5 people | 5 sessions find most usability problems; more adds little |
| How common a behavior or attitude is | Survey | Only counts generalize — but run it after interviews so you know what to ask |
| What alternatives users compare you to | Competitive teardown | Faster than asking users to describe competitors from memory |
| What users actually do in the product | Analytics / session recordings | Self-report diverges from behavior; logs don't |
| Whether people would want something that doesn't exist yet | Concept test — prototype, fake-door, or landing page | Stated interest is cheap; a small real commitment (click, signup) is the honest signal |
| How to organize navigation or content | Card sort / tree test, 10–15 people | Structure problems show up in sorting patterns; cheap and remote-friendly |
| Which of two live variants performs better | A/B test | Only works with real traffic — with under ~1k users/week, run a usability test instead |
| How behavior unfolds over days or weeks | Diary study, 6–10 people | One-shot sessions miss routines, workarounds, and drop-off; longitudinal self-logging catches them |
| What users say when you can't reach them | Review mining, 2+ source types | Real user language at zero recruiting cost — but self-selected and secondhand; findings cap at `low` confidence |

**No row fits?** Say so instead of force-fitting one. Propose the closest
method in the same shape — method, why, and what it *can't* tell you — and
mark the plan's Method line `(off-table)` so the reader knows it wasn't a
table pick.

## When you can't reach users

If the org gatekeeps customers, or there are no users yet, say so in the
plan and substitute proxy sources — never fake the Participants field.
In order of strength:

1. Support tickets and sales/CS call recordings — real user language,
   secondhand framing
2. Public reviews — your app-store/G2 page, or competitors' for pre-launch
3. Communities where target users talk — forums, Reddit, Discord
4. Interviews *about* users with customer-facing staff (support, sales) —
   last resort, twice-removed

Findings from proxies log at `low` confidence (per the evidence-log spec —
secondhand caps confidence at `low`), and the plan's Risks line must say
the evidence is indirect.

## Before filling the template

The intake floor — only what actually changes the plan: access to
users, hard deadlines, and what research already exists. If the user
hasn't told you, ask. Never invent Participants or Timeline
values; a plausible-looking guess reads as fact once it's in the plan.

Two flags to raise before planning:

- The question presumes its answer ("why do users love the new nav?") →
  reframe it neutrally first and confirm.
- The question is "how common" but nobody has done qualitative work yet →
  recommend the interview row first; a survey written on assumptions
  measures the wrong things precisely.

If the user can't be reached to confirm — a reframe, a primary-question
pick, or a batched default — act anyway, record in the block that the
call is unconfirmed, and list it for confirmation. A call this skill
makes is recorded as the skill's (on the Fielded line or beside the
reframed heading), never attributed to the user: "reframe made by
research-plan, unconfirmed" rather than "made by the PM". Unconfirmed
is a state to surface, not a reason to stall.

## Plan template

```markdown
## Q-001 <the question, reframed neutrally>

- **Status:** open
- **Question:** <one sentence — what decision this research informs>
- **Method:** <from table> — <the "why" from the table, adapted>
- **Participants:** <who counts, who's excluded, how many, where you'll find them>
- **Timeline:** <sessions + synthesis, in days — err on the long side>
- **Done when:** <the observable output, e.g. "8–12 entries appended to the
  evidence log, contradictions flagged, one recommendation drafted">
- **Risks:** <top 1–2 ways this could mislead, e.g. recruiting bias, leading question>
<!-- Fielded: appended only after the first session, send, or capture has
     happened; until then Status and Timeline carry the state -->
```

Keep the filled plan under one page. "Done when" must name the evidence log
(spec: `${CLAUDE_PLUGIN_ROOT}/references/evidence-log-spec.md`) so findings
land somewhere citable, not in a slide deck.

End by telling the user the concrete first step of their own plan — e.g.
"Draft the screener and message 10 candidates today."

<!-- voice:report-shape v1 -->
Before you send, the reply has this shape: one bold phrase at most; no
em dash inside a sentence (a comma, a parenthesis, or a second sentence
instead); every ID travels with its name, and a status or marker is
said in words rather than quoted as syntax; the state line this skill's
report names is the second-to-last line; the last line is the single
first step, stated as a sentence, never a question and never a menu.
<!-- /voice:report-shape -->
