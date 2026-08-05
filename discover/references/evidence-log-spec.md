# Evidence log spec — v1

The evidence log is one markdown file that accumulates research findings as
structured entries. Every discover skill appends to it; later design stages
cite entries by ID instead of re-quoting research.

## File

- Default path: `research/evidence-log.md` in the user's project. If the user
  keeps research elsewhere, ask once, then reuse their answer for the session.
- If the file doesn't exist, create it with the header below before appending.

```markdown
# Evidence log
<!-- weaveworm evidence-log v1 -->
```

## Entry format

```markdown
## E-014 Users abandon setup at the API-key step
- **Evidence:** 4 of 6 interviewees stalled here; P2: "I didn't know where to even get the key."
- **Source:** interviews 2026-08 (P1–P6), guide v2
- **Question:** Q-002
- **Confidence:** high — observed behavior, not opinion
- **Contradicts:** E-003
```

Field rules:

- **Heading** — `E-NNN` + the claim as one falsifiable sentence. A claim
  states something that could be proven wrong ("users abandon setup at the
  API-key step"), not a theme ("onboarding friction").
- **Evidence** — the observation that supports the claim. Counts and verbatim
  quotes beat paraphrase. Quote voices by ID, never by name — firsthand
  participants are P1, P2…, survey respondents R1, R2…, mined proxy voices
  M1, M2…, so one log can hold all three without collision.
- **Source** — where this came from, specific enough to relocate: session
  batch + date, teardown target + date, analytics query, etc.
- **Question** — the `Q-NNN` plan block this entry answers. Synthesis scopes
  entries by this field; an entry without one can only be found by
  Source-line matching, so producer skills always write it. A real finding
  no plan block covers — sessions reliably produce these — is written
  `Question: unplanned (<topic slug>)`, never omitted; clusters of
  `unplanned` entries on one topic are the seed of the next `Q-NNN` block.
- **Confidence** — one of three levels, with a short reason:
  - `high` — observed behavior, or the same finding from 2+ independent sources
  - `medium` — self-reported, or a single strong source
  - `low` — single anecdote, hunch, or secondhand
- **Stakes** — optional: `high` + one line, for claims whose cost-if-true is
  severe (safety, data loss, revenue). Stakes records importance; Confidence
  records evidence strength. `low` confidence with `Stakes: high` means
  "verify cheaply, soon", not "deprioritize".
- **Contradicts** — optional. IDs of entries this one conflicts with. Never
  delete or edit the older entry; the tension is data for synthesis.

## Confidence precedence

Three rules interact across skills; apply them in this order:

1. **Proxy cap** — an entry whose evidence is wholly proxy (mined reviews,
   forums, secondhand reports) is `low`, no matter how many venues agree.
2. **Corroboration raise** — new evidence raises an existing entry's level
   only if it is firsthand and independent of the entry's existing sources.
   Proxy material may be appended as evidence but never changes the level.
3. **Synthesis floor** — synthesis never raises a level; it reports the
   weakest load-bearing entry.

## ID rules

- Sequential: next ID = highest existing + 1. Zero-padded to three digits.
- IDs are permanent. Never renumber, reuse, or delete. A retracted finding
  gets a strikethrough heading and a `**Retracted:**` line explaining why.

## One claim per entry

If evidence supports two claims, write two entries and let them share a
Source line. Compound entries can't be cited or contradicted precisely.
