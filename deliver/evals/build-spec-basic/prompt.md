---
name: build-spec-basic
tags: [build-spec, deliver, clean]
runs: 3
max_turns: 40
allowed_tools: [Read, Write, Edit, Glob, Grep, Skill]
---
Write the build spec for B-001, the brief in design/briefs/ about analysts knowing whether each export is current before they reconcile. Its flow is F-001 in design/flows/, the decisions are in design/decisions.md, the prototype and its README are in design/prototypes/B-001/, the critique that passed it is in design/critiques/, and the charter is define/charter.md. Write the spec into deliver/specs/.

It is going to a coding agent, not a person. All of the brief's current flows are in scope, which is just F-001. I can't settle any of the critique's findings right now; carry them. Leave the status as open: I'll confirm the handoff after I've read it.

I can't answer follow-up questions in this session, so proceed with what's here and mark anything you can't settle.
