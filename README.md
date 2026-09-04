# weaveworm

A Claude Code plugin for product designers doing discovery. Its skills
produce fixed-shape artifacts (a research plan, study instruments, an
evidence log, a synthesis readout) and hand off through documents, not
vibes. Chat follows one conversation contract,
[references/voice.md](references/voice.md): canonical at the repo root,
synced into the plugin by `scripts/sync-voice.sh`, edited only at the
root.

## The plugin

**discover** — research planning, study instruments, evidence logging,
and synthesis. Skills: `research-plan`, `interview-kit`, `survey-kit`,
`usability-test-kit`, `competitor-teardown`, `review-mining`,
`evidence-log`, `synthesis`. Shared contract:
[evidence log spec](discover/references/evidence-log-spec.md).
Usage guide: [discover/README.md](discover/README.md).

Earlier versions carried three more stages (define, design, deliver).
They were removed on 2026-09-04 to keep the work on discovery; the git
history has them.

## Install

```
/plugin marketplace add shannadige/weaveworm
```

Then pick `discover` from the `/plugin` menu. The plugin ships a hook that
keeps the model out of the plugin checkout; it runs on `python3`, which
must be on your PATH (macOS and most Linux distributions have it). If it
is missing the hook stays quiet and the guard is simply off.

## Testing

Two tiers, both cheap. `scripts/lint-skills.sh` runs no model: it checks
every SKILL.md for frontmatter, a voice-contract citation, resolving
`${CLAUDE_PLUGIN_ROOT}` paths, banned words, and that the plugin's copy
of voice.md matches the root. `scripts/smoke.sh` runs the lint, then the
headless cases under `discover/evals/` (`research-plan-notes-first` and
`synthesis`) with the plugin loaded and deterministic graders only, and
prints one line per case. Cases use the `claude plugin eval` layout,
with shared fixtures under `discover/evals/fixtures/`.

The runner behind it, `scripts/eval-pilot.py`, also does the full
ablation (no plugin, spec in the system prompt, plugin loaded) with LLM
judges. That is for a one-off benchmark claim, not for checking edits.

## License

MIT. See [LICENSE](LICENSE).
