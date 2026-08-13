"""The 14 sovereign commerce domains (architecture master scope)."""
from __future__ import annotations

DOMAINS = [
    ("consumer", "Wallet / commerce / everyday payments"),
    ("merchant", "POS / checkout / invoicing / settlement"),
    ("procurement", "RFQ / RFP / tender / three-way matching"),
    ("government", "Agency portal / grants / credentials"),
    ("financial", "Payment rails / ledgers / treasury / FX"),
    ("blockchain", "Nodes / wallets / tokens / chain indexing"),
    ("defi", "AMM / lending / liquidation / yield"),
    ("identity", "DID / verifiable credentials / attestation"),
    ("offgrid", "Local mesh / offline queue / store-and-forward"),
    ("energy", "Solar / microgrid / energy trading"),
    ("supplychain", "Provenance / serialisation / custody"),
    ("entities", "Legal entity registry / ownership"),
    ("security", "IAM / PKI / zero-trust / SIEM"),
    ("compliance-os", "KYC / AML / sanctions / policy engine"),
]

DEFAULT_JURISDICTION = "AU"


def domain_by_name(name: str) -> dict:
    for n, desc in DOMAINS:
        if n == name:
            return {"name": n, "description": desc}
    raise KeyError(f"unknown domain {name!r}")
