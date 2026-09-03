#!/usr/bin/env bash
# Copies the shared fixtures (evidence log, roles, agreed charter) into the run workspace.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$HERE/../fixtures/." .
