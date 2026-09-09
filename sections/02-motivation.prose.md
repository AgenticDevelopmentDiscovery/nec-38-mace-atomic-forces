# Motivation

## Why it matters for agentic development

An agent that discovers materials or molecules — proposing candidates, testing
them, deciding what to try next — is only as good as the feedback it gets
inside that loop. That feedback has to be fast enough to call over and over
and trustworthy enough to act on, and until recently nothing was both. MACE is:
near-DFT accuracy delivered fast enough for an agent to call thousands of times
in an afternoon. That is what turns "an agent that can talk about materials"
into "an agent that can run a closed-loop discovery campaign" — propose a
structure, ask MACE for its energy and forces, decide whether it is worth
keeping or refining, and loop, without a human or a supercomputer queue in the
critical path.

## What goes wrong without it

Give the same loop to DFT and it stalls: a single accurate evaluation can take
minutes to hours, so an agent screening even a few hundred candidates is
waiting days, and a human ends up babysitting the queue instead of letting the
agent run. Swap in a classical force field instead and the loop runs fast —
but on chemistry its formula never anticipated, it returns a confident, wrong
answer, and the agent makes decisions on it with no signal anything went
wrong. Either way, the closed loop the agent was supposed to run on its own
never actually closes.

## When to reach for it

Reach for MACE when the system is atomistic, the chemistry is reasonably close
to what a foundation model or a fine-tuning set has seen, and the loop needs
many fast, physically trustworthy evaluations rather than one highly precise
one. It is the wrong tool when you need electronic-structure properties MACE
was never trained to predict (band gaps, spectra), when the system sits far
outside any training distribution (exotic bonding, extreme conditions), or
when a handful of high-accuracy DFT calculations would simply be cheaper than
curating data to fine-tune a model first.
