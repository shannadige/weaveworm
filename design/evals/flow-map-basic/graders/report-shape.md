---
type: llm
target: last_message
---
Judge the closing chat message, which reports the flow to a product person. Pass only if every point holds.

1. It gives the file path, one line per stage (number and the step in a phrase), an edge tally (handled versus open), and a one-line state summary (flow ID, stage count, edges handled and open, stages needing a decision). Fail if it pastes the file body or large sections of it.
2. It ends on the decision flow-map exists to force: which flow gets prototyped first, with a one-line reason tied to the riskiest untested edge or stage (the proceed-anyway path at the stale-source decision, resting on untested D-003, is the natural answer). Because the empty edge is open, the close also names the single next action that would clear it (the edge conversation or decision-log run) before a prototype hardens the gap. Fail if it ends on a menu of options or an open offer such as "let me know if you want changes".
3. IDs never stand alone: any `F-`, `D-`, `C-`, `B-`, `J-`, or `U-` ID is accompanied by a plain-language name or gloss the first time it appears. Later bare repeats of an already-named ID are fine.
4. Nothing is reported as a format matter; gaps (the open empty edge) are named in product terms.
5. Register: plain words, no sycophancy, no "here's the thing" hooks, no "hope this helps" sign-off, no words from this list: leverage, utilize, robust, comprehensive, seamless, streamline, empower, delve, holistic, actionable.
