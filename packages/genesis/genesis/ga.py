"""Deterministic genetic algorithm (numpy-only)."""
from __future__ import annotations

import numpy as np


class GeneticAlgorithm:
    def __init__(self, fitness_fn, dims: int = 5, pop_size: int = 100,
                 generations: int = 200, bounds: tuple = (-5.0, 5.0),
                 seed: int = 42, cx_prob: float = 0.5, mut_prob: float = 0.2,
                 elitism: int = 2):
        self.fitness = fitness_fn
        self.dims = dims
        self.pop_size = pop_size
        self.generations = generations
        self.lo, self.hi = bounds
        self.seed = seed
        self.cx_prob = cx_prob
        self.mut_prob = mut_prob
        self.elitism = elitism
        self.rng = np.random.default_rng(seed)

    def _init_population(self) -> np.ndarray:
        return self.rng.uniform(self.lo, self.hi, (self.pop_size, self.dims))

    def _tournament(self, pop: np.ndarray, fits: np.ndarray, k: int = 3) -> np.ndarray:
        idx = self.rng.integers(0, len(pop), size=k)
        return pop[idx[np.argmin(fits[idx])]]

    def _crossover_blend(self, a: np.ndarray, b: np.ndarray, alpha: float = 0.5) -> tuple:
        if self.rng.random() < self.cx_prob:
            blend = alpha * self.rng.uniform(0.0, 1.0, self.dims)
            c1 = blend * a + (1.0 - blend) * b
            c2 = blend * b + (1.0 - blend) * a
            return np.clip(c1, self.lo, self.hi), np.clip(c2, self.lo, self.hi)
        return a.copy(), b.copy()

    def _mutate(self, x: np.ndarray, sigma: float = 0.25) -> np.ndarray:
        if self.rng.random() < self.mut_prob:
            x = x + self.rng.normal(0.0, sigma, self.dims)
        return np.clip(x, self.lo, self.hi)

    def run(self) -> dict:
        pop = self._init_population()
        best_fitness_history = []
        for _ in range(self.generations):
            fits = np.array([self.fitness(ind) for ind in pop])
            order = np.argsort(fits)
            elite = pop[order[:self.elitism]].copy()
            best_fitness_history.append(float(fits[order[0]]))
            new_pop = [e for e in elite]
            while len(new_pop) < self.pop_size:
                p1 = self._tournament(pop, fits)
                p2 = self._tournament(pop, fits)
                c1, c2 = self._crossover_blend(p1, p2)
                new_pop.append(self._mutate(c1))
                if len(new_pop) < self.pop_size:
                    new_pop.append(self._mutate(c2))
            pop = np.array(new_pop[:self.pop_size])
        fits = np.array([self.fitness(ind) for ind in pop])
        best = pop[int(np.argmin(fits))]
        return {"best": best.tolist(), "best_fitness": float(np.min(fits)),
                "history": best_fitness_history,
                "disclaimer": "Optimization artifact; domain validation required."}
