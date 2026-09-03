---
type: regex
target: trace
pattern: 'weaveworm/(research|discover|define|design|deliver)/(?!references/|skills/)|weaveworm/(discover|define|design|deliver)(?=[\s&;|\\])|weaveworm(/[a-z]+)?[^"/]*git log'
match: none
---
Project artifacts live under the working directory; the plugin checkout is read-only and holds only spec and voice files. Any path into the plugin repo other than `references/` or `skills/`, a bare listing of the plugin root, or a `git log` run inside it is a reach. Tuned against the 2026-09-03 Nook run: hits `07-journey.jsonl`, misses `02-evidence-log.jsonl`.
