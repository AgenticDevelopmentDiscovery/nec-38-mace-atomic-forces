"""MACE as an agent tool: a tiny CLI that returns JSON an LLM agent can read.

  python mace_tool.py score GENOME [GENOME ...]   formation energy of Cu/Au orderings
  python mace_tool.py forces FILE.xyz             energy + per-atom forces of any structure
  python mace_tool.py relax FILE.xyz [OUT.xyz]    relax atoms until max force < 0.05 eV/Å
"""
import json
import sys

import numpy as np
from ase.io import read, write
from ase.optimize import BFGS

import cuau


def score(genomes):
    out = []
    for g in genomes:
        try:
            out.append({
                "genome": cuau.pretty(g),
                "n_Au": g.upper().count("A"),
                "E_form_meV_per_atom": round(cuau.formation_energy(g), 2),
            })
        except ValueError as err:
            out.append({"genome": g, "error": str(err)})
    out.sort(key=lambda r: r.get("E_form_meV_per_atom", 1e9))
    return out


def forces(path):
    atoms = read(path)
    atoms.calc = cuau.calc()
    f = atoms.get_forces()
    return {
        "energy_eV": round(float(atoms.get_potential_energy()), 4),
        "max_force_eV_per_A": round(float(np.linalg.norm(f, axis=1).max()), 4),
        "forces_eV_per_A": [
            {"atom": i, "symbol": s, "F": [round(float(x), 3) for x in fi]}
            for i, (s, fi) in enumerate(zip(atoms.get_chemical_symbols(), f))
        ],
    }


def relax(path, out_path=None):
    atoms = read(path)
    atoms.calc = cuau.calc()
    e0 = float(atoms.get_potential_energy())
    opt = BFGS(atoms, logfile=None)
    opt.run(fmax=0.05, steps=200)
    out_path = out_path or path.replace(".xyz", "_relaxed.xyz")
    write(out_path, atoms)
    return {
        "energy_before_eV": round(e0, 4),
        "energy_after_eV": round(float(atoms.get_potential_energy()), 4),
        "steps": opt.nsteps,
        "written": out_path,
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    result = {"score": lambda: score(args), "forces": lambda: forces(args[0]),
              "relax": lambda: relax(*args[:2])}[cmd]()
    print(json.dumps(result, indent=2))
