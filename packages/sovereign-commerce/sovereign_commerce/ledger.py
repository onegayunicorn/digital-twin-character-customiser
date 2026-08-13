"""Double-entry ledger with escrow-style conditional settlement."""
from __future__ import annotations

import time


class LedgerError(Exception):
    pass


class Ledger:
    def __init__(self):
        self._entries: list[dict] = []
        self._balances: dict[str, float] = {}
        self._escrows: dict[str, dict] = {}

    def post(self, account: str, amount: float, memo: str = "") -> int:
        """Debit/credit convention: positive = credit, negative = debit."""
        self._balances[account] = self._balances.get(account, 0.0) + amount
        entry = {"account": account, "amount": amount, "memo": memo,
                 "ts": time.time(), "seq": len(self._entries)}
        self._entries.append(entry)
        return entry["seq"]

    def transfer(self, from_acct: str, to_acct: str, amount: float,
                 memo: str = "") -> tuple[int, int]:
        if amount <= 0:
            raise LedgerError("amount must be positive")
        if self._balances.get(from_acct, 0.0) < amount:
            raise LedgerError(f"insufficient funds in {from_acct}")
        a = self.post(from_acct, -amount, f"transfer out: {memo}")
        b = self.post(to_acct, amount, f"transfer in: {memo}")
        return a, b

    def balance(self, account: str) -> float:
        return self._balances.get(account, 0.0)

    def double_entry_balanced(self) -> bool:
        """Sum of all posted amounts must be zero (every debit has a credit)."""
        return abs(sum(e["amount"] for e in self._entries)) < 1e-9

    # --- escrow (conditional settlement) ---------------------------------
    def escrow_hold(self, escrow_id: str, payer: str, amount: float,
                    memo: str = "") -> int:
        if amount <= 0:
            raise LedgerError("amount must be positive")
        if self._balances.get(payer, 0.0) < amount:
            raise LedgerError(f"insufficient funds in {payer}")
        seq = self.post(payer, -amount, f"escrow hold: {memo}")
        self._escrows[escrow_id] = {"amount": amount, "payer": payer,
                                    "state": "held", "hold_seq": seq}
        return seq

    def escrow_release(self, escrow_id: str, payee: str) -> int:
        esc = self._escrows.get(escrow_id)
        if not esc or esc["state"] != "held":
            raise LedgerError(f"escrow {escrow_id} not held")
        seq = self.post(payee, esc["amount"], f"escrow release: {escrow_id}")
        esc["state"] = "released"
        return seq

    def escrow_refund(self, escrow_id: str) -> int:
        esc = self._escrows.get(escrow_id)
        if not esc or esc["state"] != "held":
            raise LedgerError(f"escrow {escrow_id} not held")
        seq = self.post(esc["payer"], esc["amount"], f"escrow refund: {escrow_id}")
        esc["state"] = "refunded"
        return seq

    def escrow_state(self, escrow_id: str) -> dict | None:
        esc = self._escrows.get(escrow_id)
        return dict(esc) if esc else None
