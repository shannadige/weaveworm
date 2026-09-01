#!/usr/bin/env bash
# Sync the canonical voice contract into each stage plugin's references/.
# The canonical lives at references/voice.md; stage copies ship with the
# plugins and must never be edited directly.
set -euo pipefail
cd "$(dirname "$0")/.."
for stage in discover define design; do
  cp references/voice.md "$stage/references/voice.md"
done
echo "synced references/voice.md -> discover, define, design"
