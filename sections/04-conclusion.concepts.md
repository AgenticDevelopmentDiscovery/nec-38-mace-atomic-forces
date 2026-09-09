# Conclusion — spine

## Purpose

Say what the reader can now do, point at what comes next, and name what is
still open.

## Claims

- The reader can now explain what a machine-learned interatomic potential does
  and why MD needs one, run a MACE-driven MD simulation, fine-tune a
  foundation model, and describe how MACE and its uncertainty signal serve as
  the "evaluate" step of an agentic discovery loop — this must match
  `topic.md`'s "what the reader will be able to do" and § What this tutorial
  covers exactly.
- Natural next steps: the MACE codebase/docs and ASE for hands-on
  continuation; Matbench Discovery as the place foundation models are
  benchmarked against each other; other equivariant MLIP families
  (NequIP/Allegro) for architectural contrast; an actual agent framework for
  wiring the loop sketched in § MACE as a tool for real.
- What's still open: foundation-model coverage and reliability across the
  periodic table is improving but incomplete; uncertainty quantification for
  MLIPs is an active research area, not a standardized tool; agentic
  frameworks that close the discovery loop end-to-end are still mostly
  research prototypes.

## Decisions

- Ordered "where to go next" as MACE/ASE hands-on first, then
  benchmarking/alternatives, then agent frameworks — mirrors the tutorial's own
  arc (use it, compare it, then loop it into an agent) rather than listing
  resources by category.

## Open questions

- Whether to name a specific agent framework in "where to go next" or keep it
  generic, given `topic.md` scopes out evaluating agent frameworks.

## Not doing

- Not recommending a specific agent framework by name — out of scope per
  `topic.md`, and specific frameworks move too fast to endorse in a static
  document.
