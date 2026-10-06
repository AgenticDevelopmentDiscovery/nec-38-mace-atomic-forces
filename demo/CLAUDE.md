# MACE agentic demo

This folder is a live classroom demo: Claude Code acts as a discovery agent and uses
MACE-MP-0 (a machine-learned interatomic potential) as its physics tool.

## Environment
- Always run Python with `.venv/bin/python` (MACE, ASE, matplotlib are installed there).
- CPU only. One 32-atom MACE evaluation takes ~0.1 s.
- Keep answers short: the audience is watching the terminal.

## Files
- `cuau.py`: shared helpers. A Cu/Au structure is a 32-character "genome" of `C` (Cu) and `A` (Au),
  written as 4 atomic layers stacked along z, 8 sites each: `CCCCCCCC|AAAAAAAA|CCCCCCCC|AAAAAAAA`.
  `|` separators are optional. The score is the formation energy in meV/atom vs. pure Cu + pure Au
  on a fixed fcc lattice (a = 3.85 Å). Lower = more stable.
- `mace_tool.py`: the agent's tool. Prints JSON.
  - `.venv/bin/python mace_tool.py score GENOME [GENOME ...]` (several genomes per call is faster)
  - `.venv/bin/python mace_tool.py forces FILE.xyz`
  - `.venv/bin/python mace_tool.py relax FILE.xyz [OUT.xyz]`
- `01_hello_forces.py`: stretches a water molecule, prints MACE forces, relaxes it.
- `02_evolve_cuau.py`: genetic algorithm with MACE as the fitness function. Writes
  `ga_progress.png` and `ga_history.json`. `--init G1,G2` seeds the population with given genomes.

## Rules for the agent
- Never hand-compute energies; every number must come from a MACE call.
- When proposing structures, state the physical idea behind each (layering, checkerboard, etc.).
