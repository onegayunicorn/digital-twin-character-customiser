import math
import os

import numpy as np
import pytest

from sonar_5d.mesh import diamond_cubic_lattice, export_obj, lattice_metrics
from sonar_5d.sweep import peak_response, sonar_field, sweep_plane


def test_atom_count_formula():
    # 8 atoms per unit cell -> cells^3 * 8
    for cells in (1, 2, 3):
        atoms, bonds = diamond_cubic_lattice(cells)
        assert len(atoms) == cells ** 3 * 8
        assert len(bonds) > 0


def test_bond_length_invariant():
    atoms, bonds = diamond_cubic_lattice(2)
    d = math.sqrt(3.0) / 4.0
    for a, b in bonds[:50]:
        assert np.linalg.norm(atoms[a] - atoms[b]) == pytest.approx(d)


def test_lattice_metrics():
    m = lattice_metrics(2)
    assert m["n_atoms"] == 64
    assert m["atoms_per_cell"] == pytest.approx(8.0)
    assert m["bond_length"] == pytest.approx(math.sqrt(3.0) / 4.0)


def test_obj_export(tmp_path):
    atoms, bonds = diamond_cubic_lattice(1)
    p = tmp_path / "mesh.obj"
    n = export_obj(atoms, bonds, str(p))
    assert n == len(atoms)
    text = p.read_text()
    assert text.count("v ") == len(atoms)
    assert text.count("l ") == len(bonds)


def test_sonar_field_peak_at_origin():
    origin = np.array([0.0, 0.0, 0.0])
    targets = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
    t = 0.25  # wave peaks at integer distances: sin(pi/2 - 2*pi*r) = 1
    i = sonar_field(origin, targets, t, freq=1.0)
    # envelope decays with distance
    assert abs(i[0]) > abs(i[1]) > abs(i[2])


def test_sweep_plane_finds_atoms():
    atoms, _ = diamond_cubic_lattice(2)
    res = sweep_plane(atoms, plane_z=0.5, t=0.25)
    assert res["atoms_in_plane"] > 0
    assert res["max_intensity"] > 0


def test_peak_response_positive():
    times = np.linspace(0, 2, 200)
    origin = np.array([0.0, 0.0, 0.0])
    target = np.array([1.0, 0.0, 0.0])
    p = peak_response(times, origin, target, freq=1.0)
    assert p > 0.0
