# Content — spine

## Purpose

Teach the HOW: the physics that makes a potential necessary, the ML mental
model that makes MACE work, worked use (basic run, then fine-tuning/active
learning), and how it plugs into an agent loop — then the failure modes.

## Claims

- A molecular dynamics step needs energy and force at the current atomic
  positions; force is (minus) the gradient of energy with respect to position,
  and MD moves atoms forward by integrating that force over time.
- DFT is the physically correct way to get that energy and force, but it
  solves a hard problem from scratch every call, which is why it is slow and
  why a machine-learned shortcut is worth building.
- MACE turns a neighborhood of atoms into a graph (atoms = nodes, proximity =
  edges) and passes messages between neighbors, iterated over several layers,
  to build a many-body description before reading off energy and forces.
- MACE's messages are equivariant (rotate the atoms and the predicted forces
  rotate the same way, unforced) and higher-order (each message already
  encodes multi-atom, not just pairwise, information) — this is what the
  Atomic Cluster Expansion buys over a plain graph neural network.
- Running MD with a pretrained MACE foundation model is loading the model into
  ASE as a calculator and letting ASE's existing integrators do the
  timestepping — no training required to get started.
- Fine-tuning adapts a foundation model to new chemistry with a small DFT
  dataset; a committee of MACE models (or a model's own uncertainty estimate)
  gives a confidence signal an agent can use to decide when to trust a
  prediction versus flag it for a real DFT check — active learning.
- The agentic tie-in: MACE, plus its uncertainty signal, is the "evaluate" step
  of a propose → evaluate → decide → refine loop; the fine-tuning/active-learning
  cycle is what lets the agent's own decisions expand the model's competence
  over time.

## Decisions

- Chose a water molecule for the worked examples over an exotic material, so
  every reader — regardless of major — recognizes the system and can judge
  whether the output looks right.
- Put the physics-first-principles and ML-first-principles bridges in their
  own `##` units rather than folding them into "how it works," so a reader
  missing either background has a named place to stand.
- Split "using it" into two worked cases (basic MD run, then
  fine-tuning/active learning) rather than one, because the jump from "run a
  pretrained model" to "adapt and trust a model" is exactly the jump an
  agentic loop needs and a single example would hide it.
- Added one figure (`figures/mace-mental-model.svg`) for § MACE's mental model
  — the graph → message-passing → readout relationship is the one thing the
  prose leaves most abstract.

## Open questions

- Whether "equivariance" reads clearly from the figure and one analogy, or
  needs a second, more worked example.
- How much ASE/Python code to show verbatim vs. describe, given the
  slide-width constraint.

## Not doing

- Not deriving the Atomic Cluster Expansion's tensor algebra or the
  equivariance group theory — cited, not rederived.
- Not implementing a real agent framework around the loop — described in
  shape, not in code.
- Not covering distributed or multi-GPU training of MACE from scratch.
