import math

import numpy as np
import pytest

from pero.engine import (bell_state_fidelity, concurrence, dephase_channel,
                         entanglement_evolution, pure_bell_rho)


def test_bell_state_fidelity_perfect():
    rho = pure_bell_rho()
    assert bell_state_fidelity(rho) == pytest.approx(1.0, abs=1e-9)


def test_bell_state_fidelity_orthogonal():
    # |00> state has zero overlap with |phi+>
    rho00 = np.zeros((4, 4), dtype=complex)
    rho00[0, 0] = 1.0
    assert bell_state_fidelity(rho00) == pytest.approx(0.5)  # (1/sqrt2)^2


def test_concurrence_bell_pair_is_maximally_entangled():
    c = concurrence(pure_bell_rho())
    assert c == pytest.approx(1.0, abs=1e-6)


def test_concurrence_separable_state_zero():
    rho00 = np.zeros((4, 4), dtype=complex)
    rho00[0, 0] = 1.0
    assert concurrence(rho00) == pytest.approx(0.0, abs=1e-9)


def test_dephase_channel_preserves_trace():
    rho = pure_bell_rho()
    for p in (0.0, 0.3, 1.0):
        r = dephase_channel(rho, p)
        assert np.trace(r).real == pytest.approx(1.0, abs=1e-9)


def test_entanglement_decays_under_dephasing():
    res = entanglement_evolution(pure_bell_rho(), dephase_steps=100, p_step=0.05)
    # dephasing drives fidelity toward the 0.5 mixed-state floor and concurrence to 0
    assert res["final_fidelity"] < 0.55
    assert res["final_fidelity"] > 0.5  # floor, not below
    assert res["final_concurrence"] < 0.5  # decays from 1.0
    assert "disclaimer" in res


def test_fidelity_decay_is_monotonic():
    res = entanglement_evolution(pure_bell_rho(), dephase_steps=30, p_step=0.02)
    f = res["fidelity"]
    assert all(f[i] >= f[i + 1] - 1e-9 for i in range(len(f) - 1))
