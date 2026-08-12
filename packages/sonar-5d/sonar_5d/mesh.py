"""Diamond-cubic crystal lattice mesh generation + OBJ export."""
from __future__ import annotations

import math

import numpy as np

# Diamond cubic: two interpenetrating FCC lattices offset by (1/4, 1/4, 1/4)
BASIS = [
    (0.0, 0.0, 0.0), (0.5, 0.5, 0.0), (0.5, 0.0, 0.5), (0.0, 0.5, 0.5),
    (0.25, 0.25, 0.25), (0.75, 0.75, 0.25), (0.75, 0.25, 0.75), (0.25, 0.75, 0.75),
]

BOND_OFFSETS = [
    (0.25, 0.25, 0.25), (-0.25, -0.25, 0.25), (-0.25, 0.25, -0.25),
    (0.25, -0.25, -0.25),
]


def diamond_cubic_lattice(cells: int = 2) -> tuple[np.ndarray, list[tuple[int, int]]]:
    """Generate atom positions (N, 3) and bond edges for a (cells^3) supercell.
    Each unit cell contributes 8 atoms; bonds connect the 4 nearest neighbours
    of every atom at distance sqrt(3)/4 * a (a = 1)."""
    atoms = []
    for i in range(cells):
        for j in range(cells):
            for k in range(cells):
                for (bx, by, bz) in BASIS:
                    atoms.append((i + bx, j + by, k + bz))
    atoms = np.array(atoms)
    n = len(atoms)
    bond_len2 = 3.0 / 16.0  # (sqrt(3)/4)^2
    bonds: list[tuple[int, int]] = []
    for a_i in range(n):
        for b_i in range(a_i + 1, n):
            d2 = float(np.sum((atoms[a_i] - atoms[b_i]) ** 2))
            if abs(d2 - bond_len2) < 1e-6:
                bonds.append((a_i, b_i))
    return atoms, bonds


def lattice_metrics(cells: int = 2) -> dict:
    atoms, bonds = diamond_cubic_lattice(cells)
    return {
        "cells": cells,
        "n_atoms": len(atoms),
        "n_bonds": len(bonds),
        "atoms_per_cell": len(atoms) / cells ** 3,
        "bond_length": math.sqrt(3.0) / 4.0,
    }


def export_obj(atoms: np.ndarray, bonds: list[tuple[int, int]],
               path: str, scale: float = 1.0) -> int:
    """Write an OBJ mesh (vertices + line segments). Returns vertex count."""
    lines = ["# sonar-5d diamond-cubic lattice mesh"]
    for (x, y, z) in atoms:
        lines.append(f"v {x * scale:.6f} {y * scale:.6f} {z * scale:.6f}")
    for (a, b) in bonds:
        lines.append(f"l {a + 1} {b + 1}")  # OBJ is 1-indexed
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return len(atoms)
