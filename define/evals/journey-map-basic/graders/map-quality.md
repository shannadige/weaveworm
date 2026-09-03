---
type: llm
target:
  source: file
  path: define/journeys/J-001-*.md
---
Judge the journey file against all of the following. Pass only if every point holds.

1. Stages are the analyst's units of progress toward a signed-off close (for example "discovers the bank data is stale"), not product screens or menu locations. Fail if two or more stages are named for a screen, page, or button.
2. Every `Doing:` and `Friction:` line carries a source: an `E-NNN` entry, the literal marker `(assumption)`, a citation of the role's block in roles.md (for what the role does by definition, such as submitting the close), or a charter constraint marked `given (...)`. A friction line reading `none observed` counts when it cites one of those. Fail on any line with none of these.
3. Where an `E-NNN` entry is cited, it supports the claim. A stage about stale data cites E-002; a stage about the personal checklist cites E-006; a stage about waiting on the ERP owner cites E-003 or E-007. Fail if an entry is cited for something it does not support.
4. The file has a current state section and a future state section. Every shift in the future state is phrased as what is different for the analyst or controller (what they achieve, skip, or no longer suffer) and cites `OC-001` or `OC-002`. Fail if any shift describes a feature or mechanism, or cites nothing.
5. At least one stage is listed as unchanged in the future state. An all-shifts future is a rewrite fantasy, not a map.
6. The header has `Role:`, `Scope:`, and `State:` bullets, and `State:` is `current+future`.
