import math

import numpy as np
import pytest

from theory_sim.galaxy_rotation import (KPC_M, MSUN_KG, NGC3198,
                                        compare_rotation_models,
                                        exponential_disk_v, isothermal_pressure_v,
                                        nfw_halo_v, point_mass_v,
                                        total_v_squared)


def test_point_mass_matches_kepler():
    v = point_mass_v(1e11, 10.0)  # 1e11 Msun at 10 kpc
    expected = math.sqrt(6.67430e-11 * 1e11 * MSUN_KG / (10.0 * KPC_M)) / 1e3
    assert v == pytest.approx(expected)

