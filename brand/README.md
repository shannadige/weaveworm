# weaveworm brand specification

Sekiguchi violet · rev 04 · approved 2026-08-06.

The rendered, self-demonstrating spec is [`spec.html`](spec.html) (self-contained,
fonts embedded — open it locally or see the
[live artifact](https://claude.ai/code/artifact/1e92a54c-914c-43a7-bb7e-0cc72f348435)).
Tokens for reuse: [`tokens.css`](tokens.css) · faces: [`fonts.css`](fonts.css) + [`fonts/`](fonts/).

## Premise

weaveworm is named for the weaveworms of Marathon — the organisms whose thread
Sekiguchi winds into the biomatic shells runners wear. The name does the
storytelling; the brand never illustrates it. No mascot, no worm drawings, no
jokes in the copy. The worm survives as a line with an equation.

```
worm  → thread   → shell
skill → artifact → product
```

The **colony** — several worms winding one shell, each on its own detuned,
precessing orbit — is the brand's source system. Every image is the same colony
observed through a different instrument.

## Laws

1. **One thread each.** Every pattern is a continuous path or an interlacing of
   continuous threads — several may work at once, but each is one unbroken line.
   Threads bend; they never break, and they never freehand. If a line can't
   state its equation, it doesn't ship.
2. **Violet marks the living.** While work is under way, violet rides every
   moving tip; at rest it contracts to a single point. Points and lines, never
   floods.
3. **Nothing rectangular but the page.** Patterns, imagery and motion live
   entirely in curves. The only right angles belong to typography, hairlines and
   the sheet itself. If a figure resolves into cells or pixels, it is rejected.

## Color

Light is canonical; dark values serve explicit dark mode only. Share = the
color's permitted proportion of a composition (the violets together hold under
8%). The violet is calibrated by eye against in-game Sekiguchi material — a
fitting, not a fact; correct it against captured reference when available.
Marathon's acid green belongs to the master brand and never appears.

| token          | light     | dark      | role                              | share  |
|----------------|-----------|-----------|-----------------------------------|--------|
| shell          | `#F2F0EC` | `#141118` | ground — pearl, faint lilac cast  | ~36%   |
| silk           | `#E9E6E0` | `#1C1822` | recessed panels, figure grounds   | ~19%   |
| lilac          | `#E4DEEC` | `#251F31` | violet's only ambient trace       | ~12%   |
| weft           | `#C9C3CE` | `#4C4457` | secondary thread tone             | ~10%   |
| chitin         | `#211C26` | `#EBE8F0` | ink                               | ~10%   |
| muted          | `#7B7480` | `#97909F` | secondary text                    | ~6%    |
| violet         | `#6847C9` | `#A78FFF` | the corporation's voice           | ~5%    |
| violet-deep    | `#4A3096` | `#8A70EC` | pressed/hover of violet           | ~2%    |

Violet marks: moving tips, the presence behind the cloth, the crest, the
primary action, the shipped state, one glyph of the wordmark, link underlines.
Violet never marks: fills, grounds, laid thread at rest, headings, borders,
body emphasis (that job belongs to weight).

## Type

All faces SIL OFL or free licenses, self-hosted — **nothing from the Google or
Adobe libraries**, including library-listed faces served elsewhere.

- **CMU Serif** (Computer Modern) — display and headings. Thin hairlines drawn
  by Knuth's equations; the provenance is the point. Italic for asides.
  Tracking: −0.022em at display, −0.018em large specimens, −0.012em at text sizes.
- **Overused Grotesk** 400/500/700 — body. It never performs; it testifies.
- **Departure Mono** — specification only: formulas, tokens, tables of record,
  the terminal.
- Candidates on file (rendered live in spec.html): Libertinus Serif Display,
  ET Book. Redaction was considered and retired to the portfolio.

## Pattern

Weaving notation is Boolean algebra: `D = Th · Tu · Tr` over `({0,1}, ∨, ∧)`;
warp surfaces where `D(i,j) = 1`. Each stage owns a draft — the pattern system
is an org chart, not wallpaper:

| stage    | draft       | state   |
|----------|-------------|---------|
| discover | plain weave | shipped |
| define   | 2/2 twill   | shipped |
| design   | 5-end satin | planned |
| deliver  | 2×2 basket  | planned |

Drafts render as thin laid threads that dive and surface (same hand as the
colony: layered passes at low alpha). Shipped drafts carry a violet shuttle
working the weft boustrophedon; planned stages hold cloth no one is weaving yet.

## Imagery & motion

No photography, no stock, no gradients, no stills pretending to be figures.
Fields are expressed through thread — displacement, weight, spacing. Every
published figure carries its function and its motion law in its caption; an
image that can't be regenerated doesn't exist.

Reference figures (formulas in spec.html captions):

- **The colony** — `pₖ(θ) = R(εₖθ)·(aₖ·sin fₖθ, bₖ·sin gₖθ)`, `fₖ:gₖ ≈ 1:2`
  detuned; parameters drawn fresh each winding, so no two shells are alike.
- **The membrane** — counter-travelling waves under a breathing envelope;
  violet rides the crest.
- **The presence** — a curtain of threads bowing around a body on a 3:2
  Lissajous orbit; violet marks its center.

Motion law: continuous travel or precession, periods 4–20 s, visible at a
glance — never easing snaps. Laid thread accumulates incrementally on an
offscreen buffer and is never redrawn (each figure holds under ~2 ms/frame).
Animation pauses off-screen and renders static under `prefers-reduced-motion`.

## Editorial conventions

Headings sit directly — no eyebrow labels, no `[ 01 ]` markers. No pill chips,
no card grids, no scattered uppercase micro-labels. Structure is carried by
serif hierarchy, hairline-ruled lists and tables, and plates with captions.
Copy is restrained and declarative; the metaphor is stated once, never performed.
