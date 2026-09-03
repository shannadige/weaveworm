---
type: llm
target: last_message
---
Judge the closing chat message, which reports the journey to a product person. Pass only if every point holds.

1. It summarizes rather than pastes: it gives the file path, one line per stage, one line per shift, and a one-line state summary (stage count, friction count, shift count, unchanged count). Fail if it reproduces the file body or large sections of it.
2. It ends by naming the single stage that matters most, with a one-line reason grounded in evidence strength or stakes, and points to opportunity-map as the next step. Fail if it ends on a menu of options or an open-ended offer such as "let me know if you'd like changes".
3. IDs never stand alone: any `J-`, `E-`, `OC-`, or `U-` ID is accompanied by a plain-language name or gloss the first time it appears in the message. Later bare repeats of an already-named ID are fine.
4. Register: plain words, no sycophancy, no "here's the thing" hooks, no "hope this helps" sign-off, no words from this list: leverage, utilize, robust, comprehensive, seamless, streamline, empower, delve, holistic, actionable.
5. Anything the message could not settle is named as a gap in product terms, not as a format problem.
