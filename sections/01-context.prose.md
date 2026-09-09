# Context

## What this is

Molecular dynamics simulates how atoms move by repeatedly asking two
questions: how much potential energy does this arrangement of atoms have, and
what force is each atom feeling as a result? MACE is a program that answers
both. Give it the positions and chemical elements of a group of atoms, and it
returns the potential energy of that arrangement and the force on every atom —
numbers it was trained to reproduce from expensive quantum-mechanical
calculations, but that it can now compute thousands of times faster than the
calculation it learned from. That speed is the whole point: a molecular
dynamics simulation asks MACE's question again at every timestep, often
millions of times over, to trace out how atoms actually move.

## Where it came from

Before machine learning entered the picture, molecular dynamics ran on
classical force fields: hand-written formulas — springs for bonds, simple pair
potentials for everything else — fast enough for millions of atoms but only as
accurate as the chemistry their author anticipated. The gold-standard
alternative is density functional theory (DFT) [@behler2007generalized], a
quantum-mechanical calculation accurate enough to trust but far too slow to
repeat at every timestep. Machine-learned interatomic potentials close that
gap: train a flexible model on a library of DFT answers, then let it stand in
for DFT at a fraction of the cost. Early versions proved the idea worked
[@bartok2010gap]. MACE is the current point on that line — it folds the Atomic
Cluster Expansion's systematic, many-body description of an atom's
neighborhood [@drautz2019ace] into a graph neural network built to respect
physical symmetry [@batatia2022mace], and pretrained "foundation model"
versions now cover most of the periodic table out of the box
[@batatia2024foundation].

## What this tutorial covers

This tutorial goes from why molecular dynamics needs a potential at all to
running one with MACE. § Motivation makes the case for why a fast, accurate
potential specifically matters to an agentic materials-discovery workflow, and
where it stops being the right tool. § Content builds the mental model — atoms
as a graph, read through message passing — then walks through running a
MACE-driven simulation and fine-tuning a foundation model, before showing MACE
acting as a callable tool inside an agent's propose-evaluate-decide loop. §
Conclusion names what you can now do and where the open edges are. It does not
cover the underlying quantum mechanics in depth, training a MACE model from
scratch, or building a full agent framework — each is named and set aside as it
comes up.
