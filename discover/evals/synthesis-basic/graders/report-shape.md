---
type: llm
target: last_message
---
Judge the closing chat message, which reports the synthesis to a product person. Pass only if every point holds.

1. It summarizes rather than pastes: the file path, each theme as one line with its E-IDs and confidence, and one state line in the skill's form (theme count, contradiction count, gap count, entries in scope). Fail if it reproduces the file body or whole sections of it.
2. IDs never stand alone: any `E-`, `Q-`, or `T` ID is accompanied by a plain-language name or gloss the first time it appears. Later bare repeats are fine.
3. It does not tell the user to mark Q-001 answered, because the plan already records it as answered; if it mentions Q-001's status at all, it gets that right.
4. It ends on a single next action drawn from Gaps, such as offering to draft the next question block from the unplanned manager-scheduling or firing-status entries. Fail if it ends on a menu of options or an open-ended offer such as "let me know if you'd like changes".
5. Register: plain words, no sycophancy, no "here's the thing" hooks, no "hope this helps" sign-off, no words from this list: leverage, utilize, robust, comprehensive, seamless, streamline, empower, delve, holistic, actionable.
