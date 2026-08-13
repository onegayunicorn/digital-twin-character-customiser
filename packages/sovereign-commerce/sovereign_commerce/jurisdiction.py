"""Jurisdiction engine: every transaction is classified across six
jurisdiction dimensions before any regulatory profile applies."""
from __future__ import annotations

DIMENSIONS = ["user", "entity", "transaction", "asset", "service", "data"]

# Coarse regulatory profiles per jurisdiction (architecture map; not legal advice)
PROFILES = {
    "AU": {"aml": "AUSTRAC enrolment/registration applicable for designated services",
           "kyc": "KYC/CDD required", "digital_assets": "VASP registration (2026 reforms)"},
    "US": {"aml": "FinCEN BSA; MSB registration for money services",
           "kyc": "KYC/CDD required", "digital_assets": "State-by-state classification"},
    "EU": {"aml": "AMLD6; registers required", "kyc": "KYC/CDD required",
           "digital_assets": "MiCA regime"},
    "GB": {"aml": "FCA registration", "kyc": "KYC/CDD required",
           "digital_assets": "FCA cryptoasset regime"},
    "SG": {"aml": "MAS licensing", "kyc": "KYC/CDD required",
           "digital_assets": "PSA licensing"},
    "ZZ": {"aml": "jurisdiction-specific analysis required",
           "kyc": "KYC/CDD required", "digital_assets": "unknown"},
}


class JurisdictionEngine:
    def __init__(self, default: str = "AU"):
        self.default = default

    def classify(self, transaction: dict) -> dict:
        """Classify a transaction across the six dimensions. Unknown/missing
        jurisdiction resolves to the default with a warning flag."""
        classified = {}
        warnings = []
        for dim in DIMENSIONS:
            j = (transaction.get(f"{dim}_jurisdiction") or self.default).upper()
            if j not in PROFILES:
                j = "ZZ"
                warnings.append(f"{dim}: unknown jurisdiction -> ZZ")
            classified[dim] = j
        return {"classified": classified, "warnings": warnings}

    def profile(self, transaction: dict) -> dict:
        c = self.classify(transaction)
        # The most restrictive jurisdiction (lowest in PROFILES order wins)
        order = ["ZZ", "US", "EU", "GB", "SG", "AU"]
        primary = min(c["classified"].values(), key=lambda j: order.index(j))
        return {"classified": c["classified"], "primary": primary,
                "regulatory_profile": PROFILES[primary], "warnings": c["warnings"]}
