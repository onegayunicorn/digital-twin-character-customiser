"""Photonic entanglement engine: Bell-state fidelity, concurrence, evolution.

Implements standard two-qubit entanglement metrics (pure-state closed form):
  Bell state |phi+> = (|00> + |11>)/sqrt(2)
  Fidelity   F(rho, |phi+>) = <phi+| rho |phi+>
  Concurrence C(rho) = max(0, sqrt(l1) - sqrt(l2) - sqrt(l3) - sqrt(l4))
    (Wootters 1998 formula for two-qubit states)
  Dephasing evolution: rho -> (1 - p) rho + p Z(rho) (dephasing channel)

HONESTY: metrics are standard quantum-information quantities (VERIFIED math).
They describe a modeled density matrix, not a measured photonic system.
"""
from __future__ import annotations

import math

import numpy as np

PHI_PLUS = np.array([1.0, 0.0, 0.0, 1.0]) / math.sqrt(2.0)  # |00>+|11>


def bell_state_fidelity(rho: np.ndarray) -> float:
    """F = <phi+| rho |phi+> for a 4x4 density matrix."""
    return float(np.real(PHI_PLUS.conj() @ rho @ PHI_PLUS))


def concurrence(rho: np.ndarray) -> float:
    """Wootters concurrence for a 2-qubit density matrix (0 = separable)."""
    # spin-flipped rho: (Y⊗Y) rho* (Y⊗Y)
    y = np.array([[0, -1j], [1j, 0]])
    yy = np.kron(y, y)
    rho_flip = yy @ rho.conj() @ yy
    m = rho @ rho_flip
    eigvals = np.sort(np.real(np.linalg.eigvals(m)))[::-1]
    c = max(0.0, math.sqrt(max(eigvals[0], 0.0))
            - math.sqrt(max(eigvals[1], 0.0))
            - math.sqrt(max(eigvals[2], 0.0))
            - math.sqrt(max(eigvals[3], 0.0)))
    return float(max(0.0, c))


def dephase_channel(rho: np.ndarray, p: float) -> np.ndarray:
    """Dephasing: with probability p the phase coherence Z is applied.

    rho' = (1-p) rho + p (Z⊗I) rho (Z⊗I)  -- simplified single-axis model.
    """
    z = np.diag([1.0, -1.0])
    zi = np.kron(z, np.eye(2))
    return (1.0 - p) * rho + p * (zi @ rho @ zi)


def entanglement_evolution(rho0: np.ndarray, dephase_steps: int = 50,
                           p_step: float = 0.02) -> dict:
    """Apply repeated dephasing; record fidelity + concurrence decay."""
    rho = rho0.astype(complex)
    fidelities, concurrences = [], []
    for _ in range(dephase_steps):
        rho = dephase_channel(rho, p_step)
        fidelities.append(bell_state_fidelity(rho))
        concurrences.append(concurrence(rho))
    return {"fidelity": fidelities, "concurrence": concurrences,
            "final_fidelity": fidelities[-1], "final_concurrence": concurrences[-1],
            "disclaimer": "Modeled density-matrix evolution; not a measurement."}


def pure_bell_rho() -> np.ndarray:
    """Density matrix of the |phi+> Bell state (unit-trace, Hermitian)."""
    return np.outer(PHI_PLUS, PHI_PLUS.conj())
