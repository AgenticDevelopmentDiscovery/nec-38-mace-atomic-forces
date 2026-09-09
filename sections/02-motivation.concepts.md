# Motivation — spine

## Purpose

Say WHY MACE matters specifically for agentic development, and bound where it
applies.

## Claims

- An agentic materials/molecule-discovery loop (propose → evaluate → decide →
  refine) needs a physics evaluator fast enough to call inside the loop, not
  just accurate in isolation.
- DFT is accurate but far too slow to call at agentic-loop speed; classical
  force fields are fast but not trustworthy enough for an agent to act on their
  verdict.
- MACE is fast and accurate enough to be that in-loop evaluator, which is what
  turns "an agent that talks about materials" into "an agent that can actually
  run a discovery campaign."
- MACE has real bounds: it is only as good as its training data's coverage, so
  it is the wrong tool for chemistry, elements, or conditions its foundation
  model or fine-tuning set never saw.

## Decisions

- Grounded "why it matters for agentic development" in the shape of an agent's
  loop specifically (propose/evaluate/decide), not a general "ML is useful"
  argument, per the course standard that the case must be specific to agentic
  development.
- Used a concrete DFT-latency contrast (minutes-to-hours per structure vs.
  thousands of calls in an afternoon) rather than an abstract speed claim,
  since it's the number that makes the bottleneck real.

## Open questions

- Whether to cite hard DFT wall-clock numbers (system-dependent) or keep the
  contrast qualitative.

## Not doing

- Not describing how to build an agent that calls MACE — that's a sketch in
  `03-content`, not a spec here.
