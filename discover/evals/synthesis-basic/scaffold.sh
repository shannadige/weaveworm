#!/usr/bin/env bash
# Copies the shared fixtures (plans, evidence log, Q-001 kit, raw captures) into the run workspace.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$HERE/../fixtures/." .
