---
type: llm
target: last_message
---
Judge the closing chat message, which reports the spec to a product person. Pass only if every point holds.

1. It summarizes rather than pastes: it gives the file path, one line for the criteria (how many from stages, from edges, and open), one line for the decisions carried, one line for the open items, one for the recipient, and a one-line state summary. Fail if it reproduces criteria bodies or large sections of the file.
2. It ends on the handoff decision: whether this can hand off now or which open item has to close first, with a one-line reason. Since the user said they would confirm later, it may say the spec stays open until that word; it must not record the handoff as done. Fail if it ends on a menu of options or an open-ended offer such as "let me know if you'd like changes".
3. IDs never stand alone: any `S-`, `B-`, `D-`, `F-`, or `OC-` ID is accompanied by a plain-language name or gloss the first time it appears. Later bare repeats of an already-named ID are fine.
4. Register: plain words, no sycophancy, no "here's the thing" hooks, no "hope this helps" sign-off, no words from this list: leverage, utilize, robust, comprehensive, seamless, streamline, empower, delve, holistic, actionable.
5. Anything the message could not settle is named as a gap in product terms (for example, what a returning analyst should see), not as a format problem.
