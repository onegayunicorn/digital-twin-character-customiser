"""Tectonic plate motion engine (Pangaea Proxima assembly)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Plate:
    name: str
    present_centroid: tuple[float, float]  # (lat, lon) degrees
    velocity_vector: tuple[float, float]   # (deg/Myr lat, deg/Myr lon)
    area_km2: float


DEFAULT_PLATES = [
    Plate("North America", (40.0, -100.0), (-0.3, 0.25), 24_700_000),
    Plate("South America", (-15.0, -60.0), (-0.2, 0.3), 17_840_000),
    Plate("Eurasia", (50.0, 60.0), (0.15, -0.1), 54_750_000),
    Plate("Africa", (5.0, 20.0), (0.05, 0.15), 30_370_000),
    Plate("Australia", (-25.0, 135.0), (0.4, 0.2), 7_692_000),
    Plate("Antarctica", (-80.0, 0.0), (0.2, 0.0), 14_200_000),
    Plate("Indian", (20.0, 78.0), (0.3, 0.1), 11_900_000),
]

COLLISION_PAIRS = [
    ("Africa", "Eurasia", "Mediterranean Orogeny"),
    ("North America", "Africa", "Atlantic Suture Belt"),
    ("Australia", "Eurasia", "Austral-Asian Orogeny"),
]

# Narrative boundary conditions from the source document's parameters.yaml.
# NOTE: the document's linear plate velocities (~0.05-0.4 deg/Myr) are ~10x
# slower than real plate rates, so the motion engine alone does NOT assemble
# the supercontinent within 250 Myr (verified: derived collisions = 0). These
# scheduled events therefore encode the document's *narrative timeline* as
# boundary conditions, not as outputs of the motion model.
NARRATIVE_EVENTS = [
    ("Atlantic spreading cessation", 150.0),
    ("Himalaya orogeny peak", 180.0),
    ("Mediterranean closure", 210.0),
    ("Pangaea Proxima final assembly", 250.0),
]


class TectonicSimulation:
    """Plate-motion simulation over 250 Myr (deterministic) + narrative events."""

    def __init__(self, plates: list[Plate] | None = None,
                 time_step_myr: float = 2.5,
                 collision_distance_deg: float = 15.0,
                 orogeny_peak_elevation_m: float = 9500.0):
        self.plates = plates or list(DEFAULT_PLATES)
        self.dt = time_step_myr
        self.collision_distance = collision_distance_deg
        self.orogeny_peak = orogeny_peak_elevation_m
        self.orogeny_events: list[dict] = []

    def step(self, time_myr: float) -> dict[str, dict[str, float]]:
        positions: dict[str, dict[str, float]] = {}
        for plate in self.plates:
            dlat = plate.velocity_vector[0] * time_myr
            dlon = plate.velocity_vector[1] * time_myr
            positions[plate.name] = {
                "lat": plate.present_centroid[0] + dlat,
                "lon": plate.present_centroid[1] + dlon,
            }
        self._detect_orogenies(positions, time_myr)
        return positions

    def _detect_orogenies(self, positions: dict, time_myr: float) -> None:
        for p1, p2, event in COLLISION_PAIRS:
            if self._distance(positions[p1], positions[p2]) < self.collision_distance:
                self.orogeny_events.append({
                    "event": event,
                    "time_myr": round(time_myr, 1),
                    "peak_elevation_m": self.orogeny_peak,
                    "source": "derived (motion engine)",
                })

    def _narrative_events_up_to(self, time_myr: float) -> list[dict]:
        out = []
        for name, t in NARRATIVE_EVENTS:
            if abs(time_myr - t) < 1e-6:
                out.append({
                    "event": name,
                    "time_myr": t,
                    "peak_elevation_m": self.orogeny_peak,
                    "source": "narrative boundary condition (document parameters.yaml)",
                })
        return out

    @staticmethod
    def _distance(pos1: dict, pos2: dict) -> float:
        return ((pos1["lat"] - pos2["lat"]) ** 2
                + (pos1["lon"] - pos2["lon"]) ** 2) ** 0.5

    def run_full(self, total_myr: float = 250.0) -> dict:
        history = {"time": [], "positions": [], "orogenies": []}
        t = 0.0
        while t <= total_myr:
            history["time"].append(round(t, 1))
            history["positions"].append(self.step(t))
            t += self.dt
        history["orogenies"] = self.orogeny_events + [
            {"event": name, "time_myr": t_event,
             "peak_elevation_m": self.orogeny_peak,
             "source": "narrative boundary condition (document parameters.yaml)"}
            for name, t_event in NARRATIVE_EVENTS if t_event <= total_myr
        ]
        return history
