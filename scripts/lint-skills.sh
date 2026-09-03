#!/usr/bin/env bash
# Static checks on every SKILL.md, no model calls. Exit 1 on any error.
#   frontmatter has name and description
#   the voice contract is cited
#   every ${CLAUDE_PLUGIN_ROOT}/... path resolves inside that plugin
#   stage copies of voice.md match the canonical references/voice.md
#   no banned words from the voice contract's Register section
#   plugin.json exists and the marketplace lists the plugin
set -uo pipefail
cd "$(dirname "$0")/.."
errors=0; warnings=0
err()  { echo "error   $*"; errors=$((errors+1)); }
warn() { echo "warning $*"; warnings=$((warnings+1)); }

banned='leverage|utili[sz]e|serves as|comprehensive|robust|crucial|pivotal|delve|seamless|streamline|empower|foster|actionable|holistic|deep dive|unpack|best practices|at its core|game-changer|transformative|moreover|furthermore|additionally|it'"'"'s worth noting|that said'
intensifiers='genuinely|truly'

for plugin in discover define design deliver; do
  [ -f "$plugin/.claude-plugin/plugin.json" ] || err "$plugin: missing .claude-plugin/plugin.json"
  grep -q "\"source\": \"./$plugin\"" .claude-plugin/marketplace.json || err "$plugin: not listed in .claude-plugin/marketplace.json"
  if ! cmp -s references/voice.md "$plugin/references/voice.md"; then
    err "$plugin/references/voice.md differs from references/voice.md (run scripts/sync-voice.sh)"
  fi
  for f in "$plugin"/skills/*/SKILL.md; do
    [ "$(head -1 "$f")" = "---" ] || err "$f: no frontmatter"
    grep -q '^name:' "$f" || err "$f: frontmatter lacks name"
    grep -q '^description:' "$f" || err "$f: frontmatter lacks description"
    grep -q 'references/voice.md' "$f" || err "$f: does not cite the voice contract"
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
