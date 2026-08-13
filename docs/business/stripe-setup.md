# Stripe Integration & Account Setup

**Account email (user-provided):** t.j.power1986@gmail.com · **Status:** UNVERIFIED (user-supplied; Stripe account state must be confirmed in the Stripe dashboard)
**Source docs:** "Gpt stripe account help.pdf" (architecture), "《Stripe account 》 (1).pdf" (financial-systems overview: GAYA Wallet SYS-002, Samsung Wallet DID + Knox Bio-Node, RWA tokenization)

## 1. What the platform uses Stripe for

| Function | Module | Mode |
|---|---|---|
| Payment intents / capture / refund | `sovereign-commerce/payments.py` | test-mode client (no live keys in repo) |
| Payment orchestration + payouts | `payments.py` | orchestration layer |
| Escrow-like conditional settlement | `nfc_escrow.py` + ledger | holds/releases (ledger-controlled) |
| Payments kiosk | `apps/commerce-portal/kiosk.html` | portal surface |

## 2. Setup checklist (user action — not verifiable from here)

1. Confirm account at dashboard.stripe.com (email t.j.power1986@gmail.com) — verify KYC/business verification status.
2. Create test-mode API keys; **never** commit live keys (`payments.py` reads `STRIPE_SECRET_KEY` env only).
3. Configure webhook signing secret; endpoint URL once deployed.
4. For AU region: confirm ABN/company details + GST registration before going live.
5. Payouts: verify bank account details in the Stripe dashboard.

## 3. Regulatory posture (from the architecture doc)

- The commerce platform treats Stripe as the **payment rails** layer; the platform's own
  Compliance OS (AUSTRAC-style gates) sits in front of feature enablement.
- Australia: AML/CTF regime expanded 31 Mar 2026 (changes) and 1 Jul 2026 (additional
  businesses); virtual-asset service providers require AUSTRAC registration/enrolment —
  this drives the regulatory capability gates in `compliance.py`.
- **Claims register note (S7):** account operational status, fees, and approval states are
  user-reported and unverified; do not present as fact externally.

## 4. Related repos in the 420-inventory

- `nfc-escrow-bridge`, `nfc-escrow-bridge-omega`, `nfc-escrow-bridge-v2`,
  `universal-quantum-escrow` — the NFC-escrow lineage that `nfc_escrow.py` integrates;
  `gaya-wallet` / `Gaya-ecosystem-` — wallet lineage referenced in the second PDF.
