#!/usr/bin/env bash
# Static checks on every SKILL.md, no model calls. Exit 1 on any error.
#   frontmatter has name and description
#   the voice contract is cited
#   the shared plugin-root sentence is present (plugin root never listed, searched, or written)
#   every ${CLAUDE_PLUGIN_ROOT}/... path resolves inside that plugin
#   stage copies of voice.md match the canonical references/voice.md
#   each plugin's hooks/ (plugin-root guard) matches the canonical hooks/
#   the report-shape block is present once and matches references/report-shape.md
#   no banned words from the voice contract's Register section
#   plugin.json exists and the marketplace lists the plugin
set -uo pipefail
cd "$(dirname "$0")/.."
errors=0; warnings=0
err()  { echo "error   $*"; errors=$((errors+1)); }
warn() { echo "warning $*"; warnings=$((warnings+1)); }

banned='leverage|utili[sz]e|serves as|comprehensive|robust|crucial|pivotal|delve|seamless|streamline|empower|foster|actionable|holistic|deep dive|unpack|best practices|at its core|game-changer|transformative|moreover|furthermore|additionally|it'"'"'s worth noting|that said'
intensifiers='genuinely|truly'

for plugin in discover; do
  [ -f "$plugin/.claude-plugin/plugin.json" ] || err "$plugin: missing .claude-plugin/plugin.json"
  grep -q "\"source\": \"./$plugin\"" .claude-plugin/marketplace.json || err "$plugin: not listed in .claude-plugin/marketplace.json"
  if ! cmp -s references/voice.md "$plugin/references/voice.md"; then
    err "$plugin/references/voice.md differs from references/voice.md (run scripts/sync-voice.sh)"
  fi
  for h in hooks.json guard-plugin-root.py; do
    if ! cmp -s "hooks/$h" "$plugin/hooks/$h"; then
      err "$plugin/hooks/$h differs from hooks/$h (run scripts/sync-voice.sh)"
    fi
  done
  for f in "$plugin"/skills/*/SKILL.md; do
    [ "$(head -1 "$f")" = "---" ] || err "$f: no frontmatter"
    grep -q '^name:' "$f" || err "$f: frontmatter lacks name"
    grep -q '^description:' "$f" || err "$f: frontmatter lacks description"
    grep -q 'references/voice.md' "$f" || err "$f: does not cite the voice contract"
    tr -s '\n' ' ' <"$f" | grep -q 'never listed, searched, or written' || err "$f: lacks the plugin-root sentence (project artifacts live under the working directory; the plugin root is never listed, searched, or written)"
    if [ "$(grep -c '<!-- voice:report-shape v1 -->' "$f")" != 1 ] || [ "$(grep -c '<!-- /voice:report-shape -->' "$f")" != 1 ]; then
      err "$f: report-shape block missing or duplicated (one marker pair, stamped by scripts/sync-voice.sh)"
    elif ! sed -n '/<!-- voice:report-shape v1 -->/,/<!-- \/voice:report-shape -->/p' "$f" | sed '1d;$d' | cmp -s - references/report-shape.md; then
      err "$f: report-shape block differs from references/report-shape.md (run scripts/sync-voice.sh)"
    fi
    for ref in $(grep -o '\${CLAUDE_PLUGIN_ROOT}/[A-Za-z0-9_./-]*' "$f" | sort -u); do
      path="$plugin/$(printf '%s' "$ref" | sed 's|^\${CLAUDE_PLUGIN_ROOT}/||')"
      [ -e "$path" ] || err "$f: $ref does not resolve"
    done
    hits=$(grep -niwE "$banned" "$f" || true)
    if [ -n "$hits" ]; then while IFS= read -r hit; do err "$f:$hit"; done <<<"$hits"; fi
    n=$(grep -ciwE "$intensifiers" "$f"); [ "$n" -gt 0 ] && warn "$f: $n intensifier(s) (genuinely/truly)"
  done
done
echo "lint: $errors error(s), $warnings warning(s) across $(ls -d */skills/*/ | wc -l | tr -d ' ') skills"
[ "$errors" -eq 0 ]
