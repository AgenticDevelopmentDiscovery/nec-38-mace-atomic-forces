# Content

## Atoms, energy, and forces

Every arrangement of atoms has a potential energy — how strained or how
comfortable the atoms are in that particular configuration, the way a
stretched spring holds more energy than a relaxed one. The force on any one
atom is how steeply that energy would drop if you nudged the atom in each
direction; atoms move toward lower energy the way a ball rolls downhill. A
molecular dynamics simulation repeats one step: compute the energy and forces
for the atoms' current positions, nudge every atom slightly along its force,
advance time by a tiny increment, and repeat — often millions of times.
Whatever answers that step, energy and forces in, next positions out, has to
be both right and fast, because it is asked the same question over and over.

## From a quantum calculation to a machine-learned shortcut

The physically correct way to compute an arrangement's energy is to solve the
quantum mechanics of its electrons; density functional theory (DFT) is the
standard way to do this well enough to trust. DFT is accurate, but it solves a
genuinely hard problem from scratch every time it is asked — one evaluation
can take minutes to hours even for a small system, which is why running a
million-step simulation directly on DFT is not realistic. A machine-learned
interatomic potential is a shortcut around that cost: train a model on a
library of DFT answers, energy and forces for many atomic arrangements, until
it reproduces them closely, then use the trained model in DFT's place. MACE is
one such model [@batatia2022mace]; the next section describes what it is
doing internally to earn that reproduction.

## MACE's mental model: a graph, read in many-body messages

MACE looks at a group of atoms as a graph: each atom is a node, and an edge
connects two atoms close enough to plausibly interact. To predict energy and
forces, each atom "listens" to its neighbors — passing messages along the
edges, several rounds in a row, so that after a few rounds an atom's message
reflects the shape of its whole local neighborhood, not just its nearest
neighbor. Two details set MACE's messages apart from an ordinary graph neural
network. Each message already encodes many-body information — how several
neighbors sit relative to one another, not just one pair at a time — borrowed
from the Atomic Cluster Expansion [@drautz2019ace]. And the whole calculation
is equivariant: rotate the input atoms and the predicted forces rotate the
same way, automatically, because the model is built to respect that symmetry
rather than learn it from data [@batzner2022nequip].

![Atoms become a graph, the graph passes many-body, equivariant messages between neighbors, and the model reads off a total energy and a force on every atom.](figures/mace-mental-model.svg){#fig:mental-model width=95%}

## Using it: running your first MACE molecular dynamics simulation

Getting from zero to a running simulation does not require training anything:
pretrained "foundation model" versions of MACE, such as MACE-MP-0, already
cover most of the periodic table [@batatia2024foundation]. In practice this
means loading a MACE model as a calculator inside ASE, the Atomic Simulation
Environment, attaching it to a small structure — a water molecule is enough to
see the idea work — and handing it to one of ASE's existing molecular dynamics
integrators. From there, every step is the loop from § Atoms, energy, and
forces: ASE asks the MACE calculator for energy and forces at the current
positions, moves the atoms, and asks again. Setup, MD loop, and a trajectory
file to inspect afterward is a few dozen lines of Python, built on a model you
never had to train yourself.

## Using it: fine-tuning and active learning

A foundation model is broad but not infallible on your specific chemistry, so
MACE supports fine-tuning: starting from the pretrained weights and continuing
training on a small set of DFT calculations for the system you actually care
about, far cheaper than training from scratch. The harder question is knowing
when to trust the model versus when to go get more DFT data, and this is where
a committee — several MACE models trained slightly differently — earns its
keep: close agreement suggests a reliable prediction, and disagreement is a
usable signal that the model is being asked about something outside what it
has learned. Feeding that disagreement back into which structures get a real
DFT calculation next, and then back into fine-tuning, is active learning —
and it is also exactly the shape an agentic loop needs.

## MACE as a tool in an agentic discovery loop

Put the pieces together and MACE is the "evaluate" step of an agent's propose
→ evaluate → decide → refine loop: the agent proposes a candidate structure,
calls MACE for its energy, forces, and, via a committee, a confidence signal,
then decides whether to keep it, discard it, or flag it for a real DFT
calculation. Because MACE is fast enough to call thousands of times and honest
enough about its own uncertainty to know when it is guessing, the agent can
run that loop largely unattended — and the active-learning cycle from the
previous section means every DFT calculation the agent triggers makes the next
round of MACE predictions a little more trustworthy. This is the loop that was
out of reach when the only fast option was inaccurate and the only accurate
option was slow.

## Pitfalls

The most common failure is trusting a MACE prediction outside what it was
trained on: the model still returns a confident-looking number for chemistry
it has never seen, and nothing in the output flags that it is extrapolating
unless you check a committee's disagreement or the structure's distance from
the training data. A close second is letting a molecular dynamics run "blow
up" — atoms placed too close together at the start, or a timestep too large
for the fastest motion in the system, produces forces large enough to send the
simulation to nonsense positions within a handful of steps. Finally, treating a
foundation model's units and conventions (energy per atom versus total, eV
versus kcal/mol) as obvious rather than checking them is a fast way to build an
agentic loop that is confidently wrong.
