# Conclusion

## What you can do now

You can now explain what a machine-learned interatomic potential does and why
molecular dynamics needs one at every timestep; describe MACE's mental model
well enough to predict, roughly, how it will behave on a system you have not
seen it run on; load a pretrained MACE foundation model into ASE and run a
molecular dynamics simulation with it; fine-tune that model on new DFT data
and read a committee's disagreement as a signal of when to trust it; and
describe how MACE, plus that uncertainty signal, serves as the fast, honest
"evaluate" step inside an agent's propose-evaluate-decide-refine discovery
loop.

## Where to go next

Start hands-on: the MACE repository and the ASE documentation are enough to
move from this tutorial's small example to a system you actually care about.
To see how today's foundation models compare and where they still fail,
Matbench Discovery tracks exactly that across the field
[@riebesell2023matbench]. If the architecture itself is what interested you,
NequIP and Allegro are close relatives worth reading for contrast — the same
equivariant idea, different design choices [@batzner2022nequip;
@musaelian2023allegro]. And if the agentic loop sketched in § Content is the
part you want to build for real, the natural next step is wiring MACE into
whichever agent framework your own project already uses; this tutorial
deliberately stopped at the shape of that loop, not an implementation of it.

## Open edges

Foundation models like MACE-MP-0 already cover most of the periodic table, but
coverage is not the same as reliability everywhere in it — some chemistry is
still better served by a fine-tuned, purpose-built model than by the
foundation model off the shelf, and that line moves with every new release.
Uncertainty quantification for these models — the committee approach used in §
Content among them — is genuinely useful but still an active research
question, not a standardized tool the way a p-value is. And the agentic loop
this tutorial describes is a shape, not a shipped product: end-to-end systems
that actually close propose-evaluate-decide-refine autonomously, safely, and
correctly are still mostly research prototypes. That gap, between "MACE makes
the loop possible" and "the loop is a solved problem," is exactly where the
interesting work is right now.
