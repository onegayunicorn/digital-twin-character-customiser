import math

import pytest

from earth_sim.climate import ClimateModel, PREINDUSTRIAL_CO2
from earth_sim.tectonics import TectonicSimulation, DEFAULT_PLATES


def test_co2_exponential_ramp_endpoints():
    m = ClimateModel()
    assert m.co2_at_time(0.0) == pytest.approx(420.0)
    assert m.co2_at_time(250.0) == pytest.approx(950.0, rel=1e-3)


def test_temp_anomaly_logarithmic():
    m = ClimateModel()
    # at pre-industrial 280 ppm the anomaly is exactly 0
    assert m.temp_anomaly(280.0) == pytest.approx(0.0)
    # doubling -> alpha
    assert m.temp_anomaly(560.0) == pytest.approx(3.0)


def test_model_end_state_matches_its_own_equations():
    # The document's narrative claims +7.5C / +65m; its own model gives ~+5.3C / ~30m.
    m = ClimateModel()
    s = m.get_climate_state(250.0)
    assert s.co2_ppm == pytest.approx(950.0, rel=1e-3)
    assert s.global_mean_temp_c == pytest.approx(14.0 + 3.0 * math.log2(950.0 / 280.0), rel=1e-6)
    assert s.global_mean_temp_c < 21.5  # below the narrative's 21.5C claim
    assert s.sea_level_m < 65.0         # below the narrative's 65m claim


def test_ice_vanishes_by_250_myr():
    m = ClimateModel()
    assert m.get_climate_state(250.0).ice_cover_pct == pytest.approx(0.0)


def test_tectonic_simulation_runs_and_finds_collisions():
    sim = TectonicSimulation()
    history = sim.run_full(250.0)
    assert history["time"][0] == 0.0
    assert history["time"][-1] == pytest.approx(250.0)
    assert len(history["positions"]) == len(history["time"])
    # Narrative boundary conditions from the document's parameters.yaml fire:
    events = [e["event"] for e in history["orogenies"]]
    assert any("Mediterranean closure" in e for e in events)
    assert any("Atlantic spreading cessation" in e for e in events)
    assert any("Pangaea Proxima final assembly" in e for e in events)
    # Honest note: with the documented (too-slow) velocities, the motion engine
    # derives zero collisions on its own — verified, not asserted away.
    derived = [e for e in history["orogenies"] if e.get("source") == "derived (motion engine)"]
    assert len(derived) == 0


def test_plate_positions_advance():
    sim = TectonicSimulation()
    p0 = sim.step(0.0)
    p250 = sim.step(250.0)
    # Antarctica drifts north (lat increases from -80)
    assert p250["Antarctica"]["lat"] > p0["Antarctica"]["lat"]
    # Australia moves north-east
    assert p250["Australia"]["lat"] > p0["Australia"]["lat"]


def test_default_plates_present():
    names = {p.name for p in DEFAULT_PLATES}
    assert {"Africa", "Eurasia", "Australia", "Antarctica"} <= names
