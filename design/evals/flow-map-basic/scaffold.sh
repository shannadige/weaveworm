#!/usr/bin/env bash
# Copies the define layer, the evidence log, and the design layer through the pick: brief in-design, concepts with C-001 chosen, decisions D-001 to D-003. No flows yet.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$HERE/../fixtures/define" "$HERE/../fixtures/research" .
mkdir -p design
cp -R "$HERE/../fixtures/design/briefs" "$HERE/../fixtures/design/concepts" design/
cp "$HERE/../fixtures/design/decisions.md" design/
