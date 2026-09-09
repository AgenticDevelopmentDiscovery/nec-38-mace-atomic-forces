# Context — spine

## Purpose

Say WHAT MACE is and where it came from — a machine-learned interatomic
potential — before arguing why it matters for agentic discovery or how it
works internally.

## Claims

- MACE is a program that predicts the potential energy of a set of atoms and
  the force on each one, trained to reproduce quantum-mechanical (DFT)
  calculations.
- Molecular dynamics needs energy and forces recomputed at every timestep,
  which is why simulation speed is the bottleneck DFT cannot clear and MACE
  can.
- MACE descends from a lineage: classical (fixed-form) force fields → DFT as
  the accuracy ground truth → machine-learned potentials (Behler–Parrinello
  neural network potentials, GAP, the Atomic Cluster Expansion) → MACE, which
  folds the Atomic Cluster Expansion's many-body features into an equivariant
  graph neural network.
- "Foundation model" MACE variants (e.g. MACE-MP-0) are pretrained across most
  of the periodic table, so a reader can use one without training anything
  first.

## Decisions

- Defined MACE by what it does (predicts energy/forces fast, at near-DFT
  accuracy) rather than by its architecture — the architecture is
  `03-content`'s job, not context's.
- Stated the classical-FF → DFT → ML-potential lineage briefly rather than as a
  literature survey, because it explains why MACE's speed/accuracy trade-off is
  the whole point, not a footnote.

## Open questions

- How much detail on DFT belongs here versus assumed — see `topic.md` open
  questions.

## Not doing

- Not explaining the Atomic Cluster Expansion math or equivariance here —
  that's `03-content`'s "how it works."
- Not covering agentic workflows here — that's `02-motivation`'s job.
