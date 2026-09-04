#!/usr/bin/env bash
# Sync the canonical voice contract into the plugin's references/,
# the canonical plugin-root guard hook into each plugin's hooks/, and the
# canonical report-shape block into every SKILL.md between its marker
# comments. The canonicals live at references/voice.md,
# references/report-shape.md, and hooks/; stage copies ship with the
# plugins and must never be edited directly. A SKILL.md without the
# marker pair is an error: the block belongs in its after-the-write
# section, and placing the markers is a one-time edit by hand.
set -euo pipefail
cd "$(dirname "$0")/.."
for stage in discover; do
  cp references/voice.md "$stage/references/voice.md"
  mkdir -p "$stage/hooks"
  cp hooks/hooks.json hooks/guard-plugin-root.py "$stage/hooks/"
done
echo "synced references/voice.md and hooks/ -> discover"
python3 - */skills/*/SKILL.md <<'PY'
import re, sys
open_m, close_m = '<!-- voice:report-shape v1 -->', '<!-- /voice:report-shape -->'
body = open('references/report-shape.md').read().strip()
pat = re.compile(re.escape(open_m) + r'.*?' + re.escape(close_m), re.S)
missing, stamped = [], 0
for path in sys.argv[1:]:
    s = open(path).read()
    if len(pat.findall(s)) != 1:
        missing.append(path); continue
    new = pat.sub(lambda m: f'{open_m}\n{body}\n{close_m}', s)
    if new != s:
        open(path, 'w').write(new); stamped += 1
print(f'stamped references/report-shape.md into {stamped} SKILL.md file(s)')
if missing:
    print('error: no single report-shape marker pair in: ' + ', '.join(missing)); sys.exit(1)
PY
