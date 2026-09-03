# weaveworm

Claude Code plugins for product design. Each plugin covers one stage of the
design stack; skills produce fixed-shape artifacts, and stages hand off
through documents — not vibes. All stages share one conversation
contract, [references/voice.md](references/voice.md): canonical at the
repo root, synced into each plugin by `scripts/sync-voice.sh`, edited
only at the root.

## Plugins

- **discover** — research planning, study instruments, evidence logging, and
  synthesis. Skills: `research-plan`, `interview-kit`, `survey-kit`,
  `usability-test-kit`, `competitor-teardown`, `review-mining`,
  `evidence-log`, `synthesis`. Shared contract:
  [evidence log spec](discover/references/evidence-log-spec.md).
  Usage guide: [discover/README.md](discover/README.md).
- **define** — the product strategy workshop as a pipeline: product
  charter, user roles, journey maps, and impact-vs-complexity
  opportunity prioritization, built on discover's evidence log. Skills:
  `product-charter`, `success-metrics`, `user-roles`, `journey-map`,
  `opportunity-map`. Shared contract:
  [define spec](define/references/define-spec.md).
  Usage guide: [define/README.md](define/README.md).
- **design** — pursued opportunities into solutions a team can test:
  briefs, divergent concepts, a decision log, flows, and
  self-contained HTML prototypes, gated by recurring critique. Skills:
  `design-brief`, `concept-sprint`, `decision-log`, `flow-map`,
  `prototype`, `design-critique`. Shared contract:
  [design spec](design/references/design-spec.md).
  Usage guide: [design/README.md](design/README.md).
- **deliver** — a reviewed design into a build a human engineer or a
  coding agent produces without deciding anything load-bearing by
  accident, then a reading of whether the outcome moved: build specs,
  slices, instruments, build reviews, and outcome reviews. Skills:
  `build-spec`, `slice-plan`, `instrumentation-plan`, `build-review`,
  `outcome-review`. Shared contract:
  [deliver spec](deliver/references/deliver-spec.md).
  Usage guide: [deliver/README.md](deliver/README.md).

## Install

```
/plugin marketplace add shannadige/weaveworm
```

Then pick plugins from the `/plugin` menu. Each plugin ships a hook that
keeps the model out of the plugin checkout; it runs on `python3`, which
must be on your PATH (macOS and most Linux distributions have it). If it
is missing the hook stays quiet and the guard is simply off.

## Testing

Two tiers, both cheap. `scripts/lint-skills.sh` runs no model: it checks
every SKILL.md for frontmatter, a voice-contract citation, resolving
`${CLAUDE_PLUGIN_ROOT}` paths, banned words, and that each plugin's copy
of voice.md matches the root. `scripts/smoke.sh` runs the lint, then one
headless case per plugin (the mid-chain skill that reads upstream
artifacts: `synthesis`, `journey-map`, `flow-map`, `build-spec`) with
the plugin loaded and deterministic graders only, and prints one line
per case. Cases live at `<plugin>/evals/<case>/` in the `claude plugin
eval` layout, with shared fixtures under `<plugin>/evals/fixtures/`.

The runner behind it, `scripts/eval-pilot.py`, also does the full
ablation (no plugin, spec in the system prompt, plugin loaded) with LLM
judges. That is for a one-off benchmark claim, not for checking edits.

## License

MIT. See [LICENSE](LICENSE).
