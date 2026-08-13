"""NFC-escrow bridge: NFC-tap conditional settlement.

Integrates the nfc-escrow-bridge repo concept (420-inventory: nfc-escrow-bridge,
nfc-escrow-bridge-omega/v2, universal-quantum-escrow): a tap on an NFC tag
creates a conditional hold; settlement releases only when the condition
verifies (e.g., goods-received event). Deterministic, ledger-controlled.
"""
from __future__ import annotations

import uuid


class NfcEscrowBridge:
    def __init__(self, ledger=None):
        from .ledger import Ledger
        self.ledger = ledger or Ledger()
        self._taps: dict[str, dict] = {}

    def tap(self, tag_id: str, payer: str, payee: str, amount: float,
            condition: str = "goods_received") -> dict:
        """NFC tap -> escrow hold with a named release condition."""
        escrow_id = f"nfc_{uuid.uuid4().hex[:10]}"
        self.ledger.escrow_hold(escrow_id, payer, amount, f"nfc tap {tag_id}")
        self._taps[tag_id] = {"escrow": escrow_id, "payer": payer, "payee": payee,
                              "amount": amount, "condition": condition,
                              "state": "held", "verified": False}
        return self._taps[tag_id]

    def verify_condition(self, tag_id: str, condition_met: bool) -> dict:
        tap = self._taps.get(tag_id)
        if not tap:
            raise KeyError(f"unknown tap {tag_id!r}")
        tap["verified"] = bool(condition_met)
        if condition_met and tap["condition"] == "goods_received":
            self.ledger.escrow_release(tap["escrow"], tap["payee"])
            tap["state"] = "released"
        elif not condition_met:
            self.ledger.escrow_refund(tap["escrow"])
            tap["state"] = "refunded"
        return dict(tap)

    def tap_status(self, tag_id: str) -> dict | None:
        t = self._taps.get(tag_id)
        return dict(t) if t else None
