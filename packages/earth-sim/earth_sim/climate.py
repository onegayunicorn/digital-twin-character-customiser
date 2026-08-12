"""Climate model for the Pangaea Proxima greenhouse world.

Documented equations:
  CO2(t)   = C0 * exp(ln(C_end/C0) * t/T)          exponential ramp
  dT       = alpha * log2(CO2 / 280)               alpha = 3.0 C per doubling
  sea level= dT * 2.0  +  30 * clip(dT/8, 0, 1)    thermal + ice melt
"""
from __future__ import annotations

import math

from dataclasses import dataclass

PREINDUSTRIAL_CO2 = 280.0  # ppm


@dataclass
class ClimateState:
    time_myr: float
    global_mean_temp_c: float
    co2_ppm: float
    sea_level_m: float
    precipitation_mm_yr: float
    ice_cover_pct: float


class ClimateModel:
    def __init__(self, start_co2: float = 420.0, end_co2: float = 950.0,
                 duration_myr: float = 250.0, co2_sensitivity: float = 3.0,
                 baseline_temp_c: float = 14.0):
        self.start_co2 = start_co2
        self.end_co2 = end_co2
        self.duration_myr = duration_myr
        self.alpha = co2_sensitivity
        self.baseline = baseline_temp_c

    def co2_at_time(self, t_myr: float) -> float:
        return self.start_co2 * math.exp(
            math.log(self.end_co2 / self.start_co2) * (t_myr / self.duration_myr)
        )

    def temp_anomaly(self, co2_ppm: float) -> float:
        return self.alpha * math.log2(co2_ppm / PREINDUSTRIAL_CO2)

    def sea_level(self, temp_anomaly_c: float) -> float:
        thermal = temp_anomaly_c * 2.0
        ice_melt = 30.0 * max(0.0, min(1.0, temp_anomaly_c / 8.0))
        return thermal + ice_melt

    def get_climate_state(self, t_myr: float) -> ClimateState:
        co2 = self.co2_at_time(t_myr)
        dT = self.temp_anomaly(co2)
        sl = self.sea_level(dT)
        precip = 1000.0 * (1.0 + dT * 0.03)
        ice = max(0.0, 15.0 - t_myr * 0.06)
        return ClimateState(
            time_myr=t_myr,
            global_mean_temp_c=self.baseline + dT,
            co2_ppm=co2,
            sea_level_m=sl,
            precipitation_mm_yr=precip,
            ice_cover_pct=ice,
        )
