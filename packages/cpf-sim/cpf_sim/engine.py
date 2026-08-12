"""CPF engine: 2D grid simulation of crystal planet formation."""
from __future__ import annotations

import math

import numpy as np

KB = 1.380649e-23  # J/K


def nucleation_probability(dg_star: float, temperature: float) -> float:
    """P = exp(-dG* / (kB * T)) — classical nucleation theory."""
    if temperature <= 0:
        return 0.0
    return math.exp(-dg_star / (KB * temperature))


class CPFEngine:
    def __init__(self, size: int = 64, seed: int = 42,
                 t_sun: float = 6000.0, t_void: float = 60.0,
                 t_crit: float = 300.0, dg_star: float = 5e-21,
                 density_seed: float = 0.6, growth_rate: float = 0.15,
                 stabilize_fraction: float = 0.25):
        self.size = size
        self.seed = seed
        self.t_sun = t_sun
        self.t_void = t_void
        self.t_crit = t_crit
        self.dg_star = dg_star
        self.growth_rate = growth_rate
        self.stabilize_fraction = stabilize_fraction

        rng = np.random.default_rng(seed)
        self.density = density_seed + rng.uniform(-0.15, 0.15, (size, size))
        self.density = np.clip(self.density, 0.1, 1.0)
        self.crystal_mass = np.zeros((size, size))
        self.crystal_state = np.zeros((size, size), dtype=bool)
        self.thermal = self._thermal_field()
        self._n_steps = 0

    def _thermal_field(self) -> np.ndarray:
        """Linear hot->cold gradient along the x axis (sun left, void right)."""
        x = np.linspace(0.0, 1.0, self.size)
        row = self.t_void + (self.t_sun - self.t_void) * (1.0 - x)
        return np.repeat(row[:, None], self.size, axis=1)

    def step(self, rng: np.random.Generator | None = None) -> dict:
        """One simulation step: nucleate, grow, feedback. Returns metrics."""
        rng = rng or np.random.default_rng(self.seed + self._steps)
        # 1. Nucleation in cold traps
        cold = self.thermal < self.t_crit
        candidates = cold & ~self.crystal_state
        for idx in np.argwhere(candidates):
            i, j = int(idx[0]), int(idx[1])
            p = nucleation_probability(self.dg_star, self.thermal[i, j])
            if rng.random() < p:
                self.crystal_state[i, j] = True
                self.crystal_mass[i, j] = 1.0
        # 2. Growth of existing crystals (local density feedback)
        growing = np.argwhere(self.crystal_state)
        for idx in growing:
            i, j = int(idx[0]), int(idx[1])
            self.crystal_mass[i, j] += self.growth_rate * self.density[i, j]
        # 3. Feedback: crystals draw in surrounding density (smoothing inward)
        kernel = np.array([[0.05, 0.1, 0.05], [0.1, 0.0, 0.1], [0.05, 0.1, 0.05]])
        density_influx = np.zeros_like(self.density)
        for idx in np.argwhere(self.crystal_state):
            i, j = int(idx[0]), int(idx[1])
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.size and 0 <= nj < self.size:
                        density_influx[ni, nj] += kernel[di + 1, dj + 1]
        self.density = np.clip(self.density + density_influx * 0.05, 0.1, 2.0)
        self._steps += 1
        return self.metrics()

    def metrics(self) -> dict:
        total_mass = float(self.crystal_mass.sum())
        grid_capacity = float(self.density.sum())
        return {
            "step": self._steps,
            "n_crystals": int(self.crystal_state.sum()),
            "crystal_mass": total_mass,
            "mass_fraction": total_mass / grid_capacity if grid_capacity else 0.0,
            "stabilized": total_mass / grid_capacity >= self.stabilize_fraction,
        }

    def run(self, max_steps: int = 200) -> dict:
        rng = np.random.default_rng(self.seed + 1000)
        history = []
        for _ in range(max_steps):
            m = self.step(rng)
            history.append(m)
            if m["stabilized"]:
                break
        self.history = history
        return history[-1]

    @property
    def _steps(self):
        return self._n_steps

    @_steps.setter
    def _steps(self, v):
        self._n_steps = v
