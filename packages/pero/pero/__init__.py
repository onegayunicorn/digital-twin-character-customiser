"""PERO — Photonic Entanglement Research Orchestrator (analysis toolkit).

Two clearly separated layers (per the honest framing of the source document):

  classical - splitting efficiency, spatial coherence, spectral decomposition,
              FFT oscillation, tilt/polarization coherence prediction
  quantum   - Bell S-parameter model, SPDC coincidence model, verdict helper

The archive's 'entanglement' results are classical optics by its own analysis;
this package implements both the classical metrics and the *requirements* for
genuine quantum evidence (SPDC probability, Bell violation, coincidence counting).
"""
from .classical import (fft_dominant_frequency, spatial_coherence,
                        spectral_decomposition, splitting_efficiency,
                        tilt_coherence_prediction)
from .quantum import (bell_s_parameter, classify_quantum_evidence,
                      spdc_coincidence_rate, spdc_pair_rate)
from .engine import (bell_state_fidelity, concurrence, dephase_channel,
                     entanglement_evolution, pure_bell_rho)

__all__ = [
    "splitting_efficiency", "spatial_coherence", "spectral_decomposition",
    "fft_dominant_frequency", "tilt_coherence_prediction",
    "bell_s_parameter", "classify_quantum_evidence", "spdc_coincidence_rate",
    "spdc_pair_rate", "bell_state_fidelity", "concurrence", "dephase_channel",
    "entanglement_evolution", "pure_bell_rho",
]
