"""Shared helpers: a 32-site fcc Cu/Au lattice scored by MACE-MP-0.

A structure is a "genome": a 32-character string of C (copper) and A (gold).
Sites are ordered as 4 atomic layers stacked along z, 8 sites per layer,
so the genome reads layer by layer:  CCCCCCCC|AAAAAAAA|CCCCCCCC|AAAAAAAA
(that example is L1_0 CuAu, the known ordered phase).
"""
import contextlib
import io
import logging
import os
import warnings

import numpy as np
from ase.build import bulk

warnings.filterwarnings("ignore")

MODEL = os.environ.get("MACE_MODEL", "small")
A_LATTICE = 3.85  # Å, roughly Vegard's-law average of Cu (3.61) and Au (4.08)
N_SITES = 32

_calc = None
_refs = None


def calc():
    """Load MACE-MP-0 once (quietly) and reuse it."""
    global _calc
    if _calc is None:
        logging.disable(logging.WARNING)  # hide MACE/cuequivariance startup chatter
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            from mace.calculators import mace_mp

            _calc = mace_mp(model=MODEL, device="cpu", default_dtype="float32")
    return _calc


def lattice():
    atoms = bulk("Cu", "fcc", a=A_LATTICE, cubic=True).repeat((2, 2, 2))
    order = np.lexsort((atoms.positions[:, 0], atoms.positions[:, 1], np.round(atoms.positions[:, 2], 3)))
    return atoms[order]


def build(genome):
    genome = genome.replace("|", "").replace(" ", "").upper()
    if len(genome) != N_SITES or set(genome) - {"C", "A"}:
        raise ValueError(f"genome must be {N_SITES} characters of C/A, got {genome!r}")
    atoms = lattice()
    atoms.set_chemical_symbols(["Cu" if g == "C" else "Au" for g in genome])
    return atoms


def _pure_energy(symbol):
    """Per-atom energy of pure fcc metal at its own MACE-optimal lattice constant."""
    best = None
    for a in np.linspace(3.5, 4.2, 29):
        atoms = bulk(symbol, "fcc", a=a, cubic=True)
        atoms.calc = calc()
        e = atoms.get_potential_energy() / len(atoms)
        best = e if best is None else min(best, e)
    return best


def refs():
    global _refs
    if _refs is None:
        _refs = {"C": _pure_energy("Cu"), "A": _pure_energy("Au")}
    return _refs


def formation_energy(genome):
    """Formation energy in meV/atom vs. pure Cu + pure Au. Lower = more stable."""
    atoms = build(genome)
    atoms.calc = calc()
    e = atoms.get_potential_energy()
    g = genome.replace("|", "").replace(" ", "").upper()
    r = refs()
    e_ref = g.count("C") * r["C"] + g.count("A") * r["A"]
    return 1000 * (e - e_ref) / N_SITES


def pretty(genome):
    g = genome.replace("|", "").replace(" ", "").upper()
    return "|".join(g[i : i + 8] for i in range(0, N_SITES, 8))


L10 = "CCCCCCCC" "AAAAAAAA" "CCCCCCCC" "AAAAAAAA"
