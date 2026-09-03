#!/usr/bin/env bash
# Sync the canonical voice contract into each stage plugin's references/,
# and the canonical plugin-root guard hook into each plugin's hooks/.
# The canonicals live at references/voice.md and hooks/; stage copies ship
# with the plugins and must never be edited directly.
set -euo pipefail
cd "$(dirname "$0")/.."
for stage in discover define design deliver; do
  cp references/voice.md "$stage/references/voice.md"
  mkdir -p "$stage/hooks"
  cp hooks/hooks.json hooks/guard-plugin-root.py "$stage/hooks/"
done
echo "synced references/voice.md and hooks/ -> discover, define, design, deliver"
