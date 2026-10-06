"""Act 2: a genetic algorithm with MACE as the fitness function.

Search the 601-million possible 50/50 Cu/Au orderings of a 32-site fcc cell
for the most stable one, then check it against L1_0 (the known ordered phase).

  python 02_evolve_cuau.py [--generations 15] [--pop 16] [--seed 7]
  python 02_evolve_cuau.py --init GENOME,GENOME   # seed with agent-proposed structures
"""
import argparse
import json
import random
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import cuau

p = argparse.ArgumentParser()
p.add_argument("--generations", type=int, default=15)
p.add_argument("--pop", type=int, default=16)
p.add_argument("--seed", type=int, default=7)
p.add_argument("--init", default="", help="comma-separated genomes to seed the population")
args = p.parse_args()
rng = random.Random(args.seed)

cache = {}


def fitness(g):
    if g not in cache:
        cache[g] = cuau.formation_energy(g)
    return cache[g]


def random_genome():
    sites = list("C" * 16 + "A" * 16)
    rng.shuffle(sites)
    return "".join(sites)


def mutate(g):
    """Swap one Cu with one Au (keeps composition fixed)."""
    g = list(g)
    i = rng.choice([k for k, s in enumerate(g) if s == "C"])
    j = rng.choice([k for k, s in enumerate(g) if s == "A"])
    g[i], g[j] = g[j], g[i]
    return "".join(g)


def crossover(a, b):
    """Take whole layers from each parent, then repair to 16 Cu / 16 Au."""
    child = list("".join(a[k:k + 8] if rng.random() < 0.5 else b[k:k + 8] for k in range(0, 32, 8)))
    while child.count("A") != 16:
        want, have = ("A", "C") if child.count("A") < 16 else ("C", "A")
        k = rng.choice([i for i, s in enumerate(child) if s == have])
        child[k] = want
    return "".join(child)


def tournament(pop):
    return min(rng.sample(pop, 3), key=fitness)


t0 = time.time()
cuau.refs()
seeds = [g.replace("|", "").upper() for g in args.init.split(",") if g.strip()]
pop = (seeds + [random_genome() for _ in range(args.pop)])[: args.pop]
history = []
for gen in range(args.generations + 1):
    pop.sort(key=fitness)
    scores = [fitness(g) for g in pop]
    history.append({"gen": gen, "best": scores[0], "mean": sum(scores) / len(scores), "best_genome": pop[0]})
    print(f"gen {gen:2d}  best {scores[0]:7.1f}  mean {history[-1]['mean']:7.1f} meV/atom   {cuau.pretty(pop[0])}")
    if gen == args.generations:
        break
    children = pop[:2]  # elitism
    while len(children) < args.pop:
        child = crossover(tournament(pop), tournament(pop)) if rng.random() < 0.7 else tournament(pop)
        for _ in range(rng.choice([1, 1, 2])):
            child = mutate(child)
        children.append(child)
    pop = children

best = pop[0]
e_l10 = fitness(cuau.L10)
random_avg = sum(fitness(random_genome()) for _ in range(8)) / 8
print(f"\nBest found : {cuau.pretty(best)}  {fitness(best):7.1f} meV/atom")
print(f"L1_0 CuAu  : {cuau.pretty(cuau.L10)}  {e_l10:7.1f} meV/atom  (known ordered phase)")
print(f"Random avg : {'':35s}  {random_avg:7.1f} meV/atom")
print(f"{len(cache)} MACE evaluations in {time.time() - t0:.0f} s")

json.dump({"history": history, "best": best, "L10": e_l10, "random_avg": random_avg},
          open("ga_history.json", "w"), indent=2)

fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
gens = [h["gen"] for h in history]
ax.plot(gens, [h["mean"] for h in history], color="#C9A0A0", lw=2, marker="o", ms=4, label="population mean")
ax.plot(gens, [h["best"] for h in history], color="#500000", lw=2.5, marker="o", ms=5, label="best")
ax.axhline(e_l10, color="#1E293B", ls="--", lw=1.2, label="L1$_0$ CuAu (known phase)")
ax.set_xlabel("generation")
ax.set_ylabel("formation energy (meV/atom)")
ax.set_title("MACE-scored evolution of Cu/Au orderings", color="#500000", weight="bold")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("ga_progress.png")
print("wrote ga_progress.png, ga_history.json")
