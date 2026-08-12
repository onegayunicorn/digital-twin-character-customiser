"""Genesis Engine (cleaned reimplementation of the 'new code' framework).

A deterministic, numpy-only optimizer stack:
  ga    - genetic algorithm (tournament selection, blend crossover, gaussian
          mutation, elitism)
  spsa  - SPSA coordinate optimizer (simultaneous perturbation)
  fitness - pluggable objectives: sphere, rastrigin, molecule-score stub

NOT a cure finder: the engine optimizes whatever fitness function the user
provides. Any domain conclusion requires domain validation. No medical
efficacy claims.
"""
from .ga import GeneticAlgorithm
from .spsa import spsa_optimize
from .fitness import sphere, rastrigin, molecule_score_stub

__all__ = ["GeneticAlgorithm", "spsa_optimize", "sphere", "rastrigin",
           "molecule_score_stub"]
