"""TransceivingRouter: 3-cell resonance routing with engram storage.

Reimplementation of the document's CellModule/TransceivingRouter without
NLTK/qutip dependencies. The 'quantum pulse' is a resonance-coherence metric:
    pulse = 0.5 + 0.5 * emotion   (0..1)
"""
from __future__ import annotations

from datetime import datetime, timezone

import numpy as np

from .sentiment import sentiment_score

BASE_FREQ = 1.0  # Hz


class CellModule:
    def __init__(self, name: str):
        self.name = name
        self.state = {"freq": BASE_FREQ, "fluct": 0.0, "signal": None, "engram": []}

    def store(self, signal, freq: float, emotion_score: float = 0.0):
        self.state["signal"] = signal
        self.state["freq"] = freq
        self.state["fluct"] = float(np.std(signal)) if signal is not None else 0.0
        self.state["engram"].append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "emotion": round(emotion_score, 4),
        })
        self.state["freq"] *= (1.0 + 0.05 * emotion_score)

    def retrieve_engram(self):
        return self.state["engram"][-1] if self.state["engram"] else None


class TransceivingRouter:
    def __init__(self):
        self.cells = {
            "resonance": CellModule("resonance"),
            "adaptive": CellModule("adaptive"),
            "static": CellModule("static"),
        }
        self.t = np.linspace(0.0, 1.0, 100)

    def route_intent(self, intent_text: str) -> tuple[float, float]:
        emotion = sentiment_score(intent_text)
        ambient = np.sin(2.0 * np.pi * BASE_FREQ * self.t) * (len(intent_text) / 100.0)
        self.cells["resonance"].store(ambient, BASE_FREQ, emotion)
        sig = ambient
        for _ in range(3):
            sig = sig * (1.0 + 0.1 * emotion)
            self.cells["adaptive"].store(sig, 1.2, emotion)
            self.cells["static"].store(sig * 1.1, 1.1, emotion)
            self.cells["resonance"].store(sig * 1.05, 1.05, emotion)
        return round(emotion, 4), round(self.cells["static"].state["freq"], 4)


def resonance_pulse(emotion: float) -> float:
    """Coherence-style pulse metric in [0, 1]: 0.5 unbiased, tilted by emotion."""
    return round(0.5 + 0.5 * emotion, 4)
