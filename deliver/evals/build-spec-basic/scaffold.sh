#!/usr/bin/env bash
# Copies the define, design, and research layers only: no deliver/ exists yet, so build-spec creates it.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$HERE/../fixtures/define" "$HERE/../fixtures/design" "$HERE/../fixtures/research" .
