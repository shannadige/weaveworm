# weaveworm

Claude Code plugins for product design. Each plugin covers one stage of the
design stack; skills produce fixed-shape artifacts, and stages hand off
through documents — not vibes.

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

## Install

```
/plugin marketplace add shannadige/weaveworm
```

Then pick plugins from the `/plugin` menu.
