# Agent runbook: preparing and running the MACE demo

For a Claude Code agent asked to **set up, verify, rehearse, or run** this demo.
(`CLAUDE.md` in this folder is different: it is the context Claude reads while *performing*
the demo in front of the class. Keep it short and don't add setup detail to it.)

## What the demo is

A ~5-minute live segment in a class talk (deck: `../presentation/`). Claude Code acts as a
discovery agent and uses MACE-MP-0, a machine-learned interatomic potential, as its physics tool.

| Act | Command | Shows |
| --- | --- | --- |
| 1 | `01_hello_forces.py` | MACE returns forces; a stretched O–H bond relaxes back |
| 2 | `02_evolve_cuau.py` | Genetic algorithm with MACE as fitness on 32 Cu/Au sites; stalls at +18 meV/atom |
| 3 | `mace_tool.py score ...` | Claude proposes orderings itself and finds L1₀ CuAu at −17.9 meV/atom |

The human presenter's run-of-show (what to say, which prompts to type) is `DEMO_SCRIPT.md`.

## Requirements

- macOS or Linux, CPU only (no GPU needed). About 2 GB of disk for PyTorch.
- [`uv`](https://docs.astral.sh/uv/) on PATH. It fetches Python 3.11 itself.
- Internet for setup only. Afterward MACE runs offline; weights are cached in `~/.cache/mace/`.

## 1. Set up

From this `demo/` directory:

```bash
./setup.sh
```

It creates `.venv/` (skipped if it already exists), installs `mace-torch ase matplotlib`,
downloads the MACE-MP-0 weights, and runs a smoke test. It ends with `Ready.`
First run takes a few minutes. Always call Python as `.venv/bin/python`, never the system Python.

## 2. Verify (expected numbers)

Run each command and compare with what you get. Values come from MACE-MP-0 `small`, float32, CPU;
the last digit can differ across machines. Anything far off means a broken setup.

```bash
.venv/bin/python 01_hello_forces.py
```
- Stretched bonds `1.282 Å, 0.969 Å`; |F| ≈ 5.3 eV/Å on O and the stretched H.
- Relaxed bonds `0.974 Å, 0.974 Å`; max |F| ≈ 0.002. Runtime ≈ 5 s.

```bash
.venv/bin/python 02_evolve_cuau.py
```
- Deterministic (seed 7): `Best found ... 18.4 meV/atom`, `L1_0 CuAu ... -17.9`,
  `Random avg ... 73.3`, `235 MACE evaluations` in ~20 s.
- Writes `ga_progress.png` and `ga_history.json` here (gitignored). Compare with `backup/`.

```bash
.venv/bin/python mace_tool.py score CCCCCCCC\|AAAAAAAA\|CCCCCCCC\|AAAAAAAA CCAACCAA\|CCAACCAA\|CCAACCAA\|CCAACCAA CACACACA\|ACACACAC\|CACACACA\|ACACACAC CCCCCCCC\|CCCCCCCC\|AAAAAAAA\|AAAAAAAA
```
- Prints JSON sorted by energy: −17.89, −17.89, +12.92, +192.9. Runtime ≈ 6 s.
- The first two are the same L1₀ phase in two orientations. Either one counts as "found it".

## 3. Run Act 3 the way the audience sees it

Act 3 is the part where the LLM does the work, so rehearse it by actually doing it:
propose about 6 orderings from physical intuition (layers, checkerboards, stripes), score them
all in **one** `mace_tool.py score` call, then propose about 4 refinements and score those.
Optionally seed the GA with the best results and confirm nothing beats them:

```bash
.venv/bin/python 02_evolve_cuau.py --init CCCCCCCC\|AAAAAAAA\|CCCCCCCC\|AAAAAAAA
```
Expected: best stays at −17.9 for all 15 generations.

## Genome format (needed for Act 3)

32 characters of `C` (Cu) and `A` (Au), written as 4 atomic layers stacked along z, 8 sites per
layer. `|` separators are optional but must be shell-escaped or quoted. Composition can vary
(the score is the formation energy vs. pure Cu + pure Au), but the demo uses 16/16. Lower is more stable.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `uv: command not found` | Install uv: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Model download fails | Needs github.com access once; then cached in `~/.cache/mace/` |
| `cuequivariance ... not available` warning | Harmless. Scripts already silence it on stdout |
| Slow (>2× the times above) | Another process is using the CPU; MACE uses all cores |
| Broken `.venv` | `rm -rf .venv && ./setup.sh` |

## Don't

- Edit or regenerate files in `backup/`. They are the presenter's fallback, and
  `../presentation/build_deck.py` charts `backup/ga_history.json` on slide 7.
- Commit `.venv/`, `ga_progress.png`, `ga_history.json` or `*_relaxed.xyz` (already gitignored).
- Change defaults in `02_evolve_cuau.py` (seed, population, generations) or `cuau.py`
  (`MODEL`, `A_LATTICE`). The deck, `DEMO_SCRIPT.md` and the numbers above all assume them.
- Hand-compute or estimate energies. Every number shown must come from a MACE call.
