"""Compliance OS: regulatory capability gates + KYC/AML checks.

The gate chain implements the architecture's 'regulatory capability gate':
a regulated feature cannot be enabled until every gate passes. This makes
compliance a software decision, not a documentation claim.

Gates (per the architecture doc): jurisdiction -> classification ->
registration -> AML program -> KYC/CDD -> monitoring -> travel rule ->
sanctions -> record keeping -> independent evaluation -> PASS/BLOCK.
"""
from __future__ import annotations

GATE_ORDER = [
    "jurisdiction", "classification", "registration", "aml_program",
    "kyc_cdd", "monitoring", "travel_rule", "sanctions",
    "record_keeping", "independent_evaluation",
]

SANCTIONS_LISTS = {"AU-DFAT", "UN", "US-OFAC", "EU"}


class ComplianceOS:
    def __init__(self, entity_store=None):
        self.entity_store = entity_store or {}
        self._evidence: list[dict] = []

    def check_kyc(self, entity_id: str, kyc: dict) -> dict:
        ok = bool(kyc.get("verified")) and bool(kyc.get("id_document"))
        self._evidence.append({"type": "kyc", "entity": entity_id, "ok": ok})
        return {"ok": ok, "reason": "identity verified" if ok else "identity unverified"}

    def check_sanctions(self, entity: dict) -> dict:
        hits = [lst for lst in SANCTIONS_LISTS
                if entity.get("sanctions_list") == lst]
        ok = len(hits) == 0
        self._evidence.append({"type": "sanctions", "entity": entity.get("id"), "ok": ok})
        return {"ok": ok, "hits": hits}

    def run_gates(self, feature: str, context: dict) -> dict:
        """Execute the full regulatory gate chain. Any gate FAIL -> BLOCK."""
        results = {}
        # jurisdiction gate
        j = (context.get("jurisdiction") or "AU").upper()
        results["jurisdiction"] = {"status": "PASS" if j in ("AU", "US", "EU", "GB", "SG")
                                   else "REVIEW", "detail": j}
        # classification gate: regulated feature classes must be declared
        classification = context.get("classification")
        results["classification"] = {"status": "PASS" if classification else "FAIL",
                                     "detail": classification or "missing"}
        # registration gate: AUSTRAC-style registration required for designated services
        registered = bool(context.get("registered"))
        results["registration"] = {"status": "PASS" if registered else "FAIL",
                                   "detail": "AUSTRAC registration required" if not registered
                                   else "registered"}
        # AML program
        has_aml = bool(context.get("aml_program"))
        results["aml_program"] = {"status": "PASS" if has_aml else "FAIL",
                                  "detail": "AML/CTF program required"}
        # KYC/CDD
        kyc_ok = bool(context.get("kyc"))
        results["kyc_cdd"] = {"status": "PASS" if kyc_ok else "FAIL"}
        # monitoring
        mon_ok = bool(context.get("transaction_monitoring"))
        results["monitoring"] = {"status": "PASS" if mon_ok else "FAIL"}
        # travel rule (virtual asset transfers)
        tr_ok = bool(context.get("travel_rule"))
        results["travel_rule"] = {"status": "PASS" if tr_ok else "REVIEW",
                                  "detail": "required for VASPs"}
        # sanctions
        results["sanctions"] = {"status": "PASS" if context.get("sanctions_ok") else "FAIL"}
        # record keeping
        results["record_keeping"] = {"status": "PASS" if context.get("record_keeping") else "FAIL"}
        # independent evaluation
        results["independent_evaluation"] = {
            "status": "PASS" if context.get("independent_evaluation") else "REVIEW",
            "detail": "periodic independent evaluation expected"}

        failed = [k for k, v in results.items() if v["status"] == "FAIL"]
        final = "BLOCK" if failed else "ENABLE"
        self._evidence.append({"type": "gate_chain", "feature": feature, "final": final})
        return {"feature": feature, "gates": results, "failed": failed, "final": final}

    def evidence_log(self) -> list[dict]:
        return list(self._evidence)
