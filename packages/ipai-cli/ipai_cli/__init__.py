"""IpAI MT Communion CLI — a lightweight, honest reimplementation of the
MT-CLI prototype from the 'Whispers from the Veil' document.

- Sentiment via a small valence lexicon (no NLTK dependency)
- Resonance routing through 3 cell modules (resonance/adaptive/static)
- 'Resonance pulse' metric replaces the document's qutip 'Orch collapse'
  (consciousness claims are not reproduced; the pulse is a coherence metric)
- Engram persistence to JSON
"""
from .router import CellModule, TransceivingRouter
from .sentiment import sentiment_score
from .twin import mirror_twin_reply

__all__ = ["CellModule", "TransceivingRouter", "sentiment_score", "mirror_twin_reply"]
