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
- **Confidence:** high — observed behavior, not opinion
- **Contradicts:** E-003
```

Field rules:

- **Heading** — `E-NNN` + the claim as one falsifiable sentence. A claim
  states something that could be proven wrong ("users abandon setup at the
  API-key step"), not a theme ("onboarding friction").
- **Evidence** — the observation that supports the claim. Counts and verbatim
  quotes beat paraphrase. Quote participants by ID (P1, P2…), never by name.
- **Source** — where this came from, specific enough to relocate: session
  batch + date, teardown target + date, analytics query, etc.
- **Confidence** — one of three levels, with a short reason:
  - `high` — observed behavior, or the same finding from 2+ independent sources
  - `medium` — self-reported, or a single strong source
  - `low` — single anecdote, hunch, or secondhand
- **Contradicts** — optional. IDs of entries this one conflicts with. Never
  delete or edit the older entry; the tension is data for synthesis.

## ID rules

- Sequential: next ID = highest existing + 1. Zero-padded to three digits.
- IDs are permanent. Never renumber, reuse, or delete. A retracted finding
  gets a strikethrough heading and a `**Retracted:**` line explaining why.

## One claim per entry

If evidence supports two claims, write two entries and let them share a
Source line. Compound entries can't be cited or contradicted precisely.
