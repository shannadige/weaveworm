#!/usr/bin/env bash
# Copies this case's fixtures into the run workspace: the Nook README and the
# raw interview notes and ticket summary from the 2026-09-03 end-to-end run.
# Deliberately no research/plans.md and no research/evidence-log.md: the
# research ran before anyone planned it, and the question is not on record.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$HERE/fixtures/." .
