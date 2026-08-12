"""Pangaea Proxima — Earth in 250 million years, simulation package.

Implements the documented models from the 'Earth in 250 Million Years'
synthesis: a Wilson-cycle tectonic engine and an IPCC-style climate model
(exponential CO2 ramp, logarithmic temperature forcing with alpha=3.0 C per
CO2 doubling, thermal+ice-melt sea level).

HONESTY: the model is SIMULATED. Its outputs (end CO2 ~950 ppm, delta-T
~+5.3 C, sea level ~+30 m) follow from the documented equations; the source
document's narrative claims (+7.5 C, +65 m) do not match its own model and
are recorded as UNVERIFIED in the claims register.
"""
