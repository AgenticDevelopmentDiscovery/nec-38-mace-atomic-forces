"""Act 1: MACE in 10 lines. Stretch a water molecule, read the forces, let it relax."""
import numpy as np
from ase.build import molecule
from ase.optimize import BFGS

from cuau import calc

water = molecule("H2O")
water.positions[1] *= 1.35          # stretch one O-H bond by ~35%
water.calc = calc()


def oh(a):
    return a.get_distance(0, 1), a.get_distance(0, 2)


print(f"Stretched  O-H bonds: {oh(water)[0]:.3f} Å, {oh(water)[1]:.3f} Å")
print(f"Energy: {water.get_potential_energy():.3f} eV\nForces (eV/Å):")
for s, f in zip(water.get_chemical_symbols(), water.get_forces()):
    print(f"  {s:2s} [{f[0]:+7.3f} {f[1]:+7.3f} {f[2]:+7.3f}]   |F| = {np.linalg.norm(f):.3f}")

BFGS(water, logfile=None).run(fmax=0.01)
print(f"\nRelaxed    O-H bonds: {oh(water)[0]:.3f} Å, {oh(water)[1]:.3f} Å   (experiment ≈ 0.96 Å)")
print(f"Energy: {water.get_potential_energy():.3f} eV   max |F| = {np.abs(water.get_forces()).max():.3f} eV/Å")
