# Live demo: Claude Code as a discovery agent, MACE as its physics tool

**Length:** about 5 minutes. **Setup:** VS Code with the Claude Code panel open on `demo/`.
**The story:** a blind genetic algorithm gets stuck. An agent that can reason *and* call MACE finds
the known answer in a couple of tool calls. Then the two work together.

---

## Night before (do not skip)

```bash
cd demo                # from the repo root
./setup.sh            # installs mace-torch + ase, downloads MACE-MP-0 weights, smoke-tests
```

- The model weights are cached in `~/.cache/mace`, so class Wi-Fi doesn't matter.
- Turn on auto-accept for Bash in Claude Code (or pre-approve `.venv/bin/python`) so you don't
  spend demo time clicking "allow".
- Bump the VS Code font size (`Cmd +` two or three times) and close every other panel.
- Run all three acts once as a rehearsal, then `/clear` the Claude Code chat.
- Open `backup/` in a Finder window: it has saved outputs for every act.

## Day of: before you start talking

- Open VS Code on `demo/`. Claude Code panel on the right, `CLAUDE.md` open on the left.
  It gives Claude the project context, so your prompts can stay short.

---

## Act 1: "What does a force field actually return?" (about 1 min)

**Say:** "MACE takes atoms in and gives energy and forces out. Let me ask the agent to show us."

**Type into Claude Code:**

> Run 01_hello_forces.py and explain the forces in one sentence each.

**What happens:** about 5 s of runtime. Stretched O–H bond (1.28 Å) → forces of ~5 eV/Å pull the
H back toward O → after relaxation both bonds are 0.974 Å (experiment ≈ 0.96 Å).

**Point at:** the O and the stretched H have equal and opposite forces (Newton's third law falls out of
F = −∇E). The unstretched H barely moves.

## Act 2: "Evolution with MACE as the fitness function" (about 1.5 min)

**Say:** "Now a real search problem. 32 sites, half copper and half gold: about 600 million ways to
arrange them. Which arrangement is most stable? Classic genetic algorithm, MACE scores each child."

**Type:**

> Run the genetic algorithm in 02_evolve_cuau.py, then open ga_progress.png and tell me whether it
> found the L1_0 phase.

**What happens:** about 20 s. 235 MACE evaluations. Best found ≈ **+18 meV/atom**, while the known
L1₀ CuAu ordering is **−18 meV/atom**. The GA improved a lot over random (+73) but stalled.

**Say:** "Blind mutation finds partial order, but it's stuck in a local minimum. What if the
mutation operator could *think*?"

## Act 3: "The agent becomes the mutation operator" (about 2 min)

**Type:**

> You are the evolutionary operator now. Propose 6 Cu/Au orderings based on physical intuition
> (layering, checkerboards, stripes), score them all with mace_tool.py in one call, then propose
> 4 improved ones based on what you learned and score those. Finish with a table of the best 3.

**What happens:** Claude reasons about layering, calls `mace_tool.py score ...` twice and should
land on `CCCCCCCC|AAAAAAAA|CCCCCCCC|AAAAAAAA` (−17.9 meV/atom), the L1₀ phase, within about two rounds.
`CCAACCAA` repeated four times scores the same −17.9: it is the same L1₀ phase layered along a
different axis, so either answer counts as finding it.

**Optional closer (if time remains):**

> Seed the GA with your two best structures using --init and run it. Does anything beat them?

The GA keeps L1₀ as its best through all 15 generations: an independent check that the agent's
answer is a real minimum, not a lucky guess.

**Closing line:** "The LLM brought hypotheses, MACE brought physics in milliseconds, and the GA
brought brute-force verification. That's the agentic discovery loop on one laptop."

---

## If something goes wrong

| Problem | Fix |
|---|---|
| Claude asks permission for every command | Click "always allow" for `.venv/bin/python` |
| A run is slow or hangs | `Esc` to stop it, then show the saved output: `cat backup/act2_output.txt`, `open backup/ga_progress.png` |
| Claude doesn't propose L1₀ | Nudge it: "What about alternating pure layers along z?" Even better: it shows the human stays in the loop |
| No internet | Fine, as long as `setup.sh` ran the night before. Claude Code itself needs internet, so tether to your phone if class Wi-Fi is down |
| Running long on time | Skip Act 1. Act 2 → Act 3 is the core story |

## Reference numbers (MACE-MP-0 small, CPU, from rehearsal)

| Structure | Genome (4 layers along z) | E_form (meV/atom) |
|---|---|---|
| L1₀ CuAu (known phase) | `CCCCCCCC\|AAAAAAAA\|CCCCCCCC\|AAAAAAAA` | −17.9 |
| GA best, seed 7, 15 gens | `CCACCACA\|AACCAACC\|CCAAACAA\|AACCAACC` | +18.4 |
| Random orderings (average) | (random) | ≈ +73 |
| In-plane half/half stripes | `CCCCAAAA\|CCCCAAAA\|CCCCAAAA\|CCCCAAAA` | +192.9 |

Caveat to mention if asked: these are fixed-lattice energies (no cell relaxation) from a universal
model. A real study would relax each structure and spot-check the winners with DFT.
