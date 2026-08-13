"""Payment orchestration + Stripe-style client (test-mode, no secrets).

The client reads STRIPE_SECRET_KEY from the environment only; live keys are
never stored in the repo. In test mode (no key) it returns deterministic
mock payment results with an explicit test-mode flag.
"""
from __future__ import annotations

import os
import uuid


class StripeClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ.get("STRIPE_SECRET_KEY")
        self.test_mode = not self.api_key or self.api_key.startswith("sk_test")

    def create_payment_intent(self, amount_cents: int, currency: str = "aud",
                              description: str = "") -> dict:
        if self.test_mode:
            return {"id": f"pi_test_{uuid.uuid4().hex[:12]}",
                    "amount": amount_cents, "currency": currency,
                    "status": "requires_payment_method", "test_mode": True,
                    "description": description}
        # live path would call the Stripe API here
        raise NotImplementedError("live Stripe API call not wired (add SDK)")

    def capture(self, payment_intent_id: str) -> dict:
        return {"id": payment_intent_id, "status": "succeeded", "test_mode": self.test_mode}

    def refund(self, payment_intent_id: str, amount_cents: int | None = None) -> dict:
        return {"id": f"re_{payment_intent_id}", "status": "succeeded",
                "test_mode": self.test_mode}


class PaymentOrchestrator:
    """Orchestrates: gate -> intent -> escrow hold -> capture -> escrow release."""

    def __init__(self, client: StripeClient | None = None, ledger=None,
                 compliance: ComplianceOS | None = None):
        from .ledger import Ledger
        self.client = client or StripeClient()
        self.ledger = ledger or Ledger()
        self.compliance = compliance

    def pay(self, payer: str, payee: str, amount: float, currency: str = "aud",
            escrow: bool = True, context: dict | None = None) -> dict:
        """Run the full payment flow with optional escrow settlement."""
        if self.compliance:
            gate = self.compliance.run_gates("payments", context or {})
            if gate["final"] != "ENABLE":
                return {"status": "BLOCKED", "gates": gate["gates"], "failed": gate["failed"]}
        intent = self.client.create_payment_intent(int(round(amount * 100)), currency)
        if escrow:
            escrow_id = f"esc_{uuid.uuid4().hex[:10]}"
            self.ledger.escrow_hold(escrow_id, payer, amount, "payment escrow")
            self.client.capture(intent["id"])
            self.ledger.escrow_release(escrow_id, payee)
            return {"status": "settled", "escrow": escrow_id,
                    "payment_intent": intent["id"], "test_mode": intent["test_mode"]}
        self.ledger.transfer(payer, payee, amount, "direct payment")
        return {"status": "settled", "payment_intent": intent["id"],
                "test_mode": intent["test_mode"]}
