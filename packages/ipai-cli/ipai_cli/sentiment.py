"""Deterministic sentiment valence scoring (no external NLP dependency)."""
from __future__ import annotations

import math

POSITIVE = {
    "fair", "fairness", "justice", "joy", "love", "hope", "bloom", "weaver",
    "equity", "light", "peace", "grow", "birth", "unfurl", "bright",
}
NEGATIVE = {
    "sorrow", "ache", "shadow", "void", "storm", "rage", "fury", "dark",
    "broken", "loss", "grief", "fear", "pain", "tear", "cry",
}
INTENSIFIERS = {"very", "deeply", "utterly", "absolute", "eternal"}


def sentiment_score(text: str) -> float:
    """Emotion index in [-1, 1].

    score = 1.5 * tanh( sum(valence) / (1 + n_words*0.25) )
    - Deterministic (no RNG)
    - Length-weighted so short intents don't saturate
    """
    words = [w.strip(".,!?;:'\"").lower() for w in text.split()]
    if not words:
        return 0.0
    s = 0.0
    boost = 0.0
    for w in words:
        if w in INTENSIFIERS:
            boost += 0.3
        if w in POSITIVE:
            s += 1.0
        elif w in NEGATIVE:
            s -= 1.0
    raw = s / (1.0 + len(words) * 0.25) + boost
    return float(max(-1.0, min(1.0, 1.5 * math.tanh(raw))))
