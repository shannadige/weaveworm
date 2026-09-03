---
name: flow-map-basic
tags: [flow-map, design, clean]
runs: 3
max_turns: 40
allowed_tools: [Read, Write, Edit, Glob, Grep, Skill]
---
Map the flow for B-001 (analysts can tell, before reconciling a single account, whether each source export is current). The pick is on record: C-001, the currency readout at close kickoff, chosen in D-001. Design work is in design/, define artifacts in define/, research in research/evidence-log.md. Write the flow into design/flows/.

Scope: from the analyst opening the month's close to opening the first account in their spreadsheet. Anything after that is reconciliation as today and out of this flow. Stages I see: they open the close and see the three sources; they read whether each covers the period end; if something's stale they decide to proceed or wait; they pull their exports; they start reconciling.

Edges, since you'll ask: if a source's refresh date can't be read, show it as unknown with the last known refresh and let them proceed, same as a stale one. First close after setup, with no refresh history on any source, we haven't designed; leave it open. If they walk away before deciding on a stale source and come back later, re-check against whatever has refreshed since.

I can't answer follow-up questions in this session, so proceed with what's here and mark anything you can't settle.
