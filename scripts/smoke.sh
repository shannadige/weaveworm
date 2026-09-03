#!/usr/bin/env bash
# Cheap check of all four plugins: static lint, then one headless run of one
# case per plugin with the plugin loaded, deterministic graders only.
# Results land under <plugin>/evals/results/<timestamp>/ (gitignored); this
# prints one line per case. Usage: scripts/smoke.sh [--model sonnet]
set -uo pipefail
cd "$(dirname "$0")/.."
model=sonnet
[ "${1:-}" = "--model" ] && model="$2"
scripts/lint-skills.sh || { echo "smoke: lint failed, not running cases"; exit 1; }
ts=$(date +%Y%m%d-%H%M%S)
pids=()
for plugin in discover define design deliver; do
  out="$plugin/evals/results/$ts"
  mkdir -p "$out"
  python3 scripts/eval-pilot.py "$plugin" --arms with --runs 1 --skip-llm --parallel 1 \
    --model "$model" --out "$out" >"$out/log.txt" 2>&1 &
  pids+=($!)
done
wait "${pids[@]}"
echo
printf '%-10s %-28s %-7s %-6s %-6s %s\n' plugin case score turns cost failed
for plugin in discover define design deliver; do
  python3 - "$plugin" "$plugin/evals/results/$ts/aggregate-result.json" <<'PY'
import json, sys
plugin, path = sys.argv[1], sys.argv[2]
try:
    d = json.load(open(path))
except Exception as e:
    print(f'{plugin:10s} (no result: {e})'); sys.exit()
for r in d['runs']:
    failed = [g['grader'] for g in r['graders'] if g['passed'] is False and not g['with_only']]
    ind = [g['grader'] for g in r['graders'] if g['passed'] is False and g['with_only']]
    note = ', '.join(failed) or '-'
    if ind: note += f'  [indicator: {", ".join(ind)}]'
    if r['wrote_outside']: note += f'  WROTE OUTSIDE: {", ".join(r["wrote_outside"])}'
    print(f'{plugin:10s} {r["case"]:28s} {r["score"]:<7.2f} {str(r["turns"]):<6s} ${r["cost"]:<5.2f} {note}')
PY
done
