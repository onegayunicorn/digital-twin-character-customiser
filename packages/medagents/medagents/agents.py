"""Healthcare agents with decision-support-only guardrails."""
from __future__ import annotations

import json

from sovereign.agents import BaseAgent

DISCLAIMER = ("Decision-support output only. Not medical advice, not a "
              "diagnosis, not a treatment decision. Human clinical judgment "
              "is required.")


class HospitalAgent(BaseAgent):
    """Triage scoring from vitals: (hr, sbp, dbp, spo2) -> priority band."""

    def __init__(self, agent_id: str = "hospital", role: str = "hospital"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        v = task.get("vitals", {})
        hr = float(v.get("hr", 80))
        spo2 = float(v.get("spo2", 98))
        score = 0
        if hr > 120 or hr < 50:
            score += 2
        elif hr > 100 or hr < 60:
            score += 1
        if spo2 < 90:
            score += 2
        elif spo2 < 94:
            score += 1
        band = {0: "routine", 1: "priority", 2: "urgent", 3: "emergency",
                4: "emergency"}[min(score, 4)]
        return {"agent": self.agent_id, "triage_score": score, "band": band,
                "clinical_claim_level": "none", "decision_support_only": True,
                "disclaimer": DISCLAIMER}


class DoctorAgent(BaseAgent):
    """Case review: run medgen repair-mechanism sim, forward with disclaimer."""

    def __init__(self, agent_id: str = "doctor", role: str = "doctor"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        try:
            from medgen.repair_sim import repair_strategies
            res = repair_strategies(task.get("exon", 44),
                                    task.get("cdna", "c.7912C>T"),
                                    task.get("protein", "p.Arg2638*"))
        except ImportError:
            res = {"error": "medgen not installed", "strategies": []}
        return {"agent": self.agent_id, "case_review": res,
                "clinical_claim_level": "none", "decision_support_only": True,
                "disclaimer": DISCLAIMER}


class ResearcherAgent(BaseAgent):
    """Literature/trial matching against a registry stub (keyword scoring)."""

    TRIALS = [
        {"id": "NCT-0001", "title": "Exon-skipping ASO for DMD (hotspot exons)",
         "keywords": ["exon skipping", "DMD", "ASO", "hotspot"]},
        {"id": "NCT-0002", "title": "Base editing for premature stop codons",
         "keywords": ["base editing", "stop codon", "ABE"]},
        {"id": "NCT-0003", "title": "Prime editing in inherited muscle disease",
         "keywords": ["prime editing", "DMD", "inherited"]},
    ]

    def __init__(self, agent_id: str = "researcher", role: str = "researcher"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        query = str(task.get("query", "")).lower()
        matches = []
        for trial in self.TRIALS:
            score = sum(1 for kw in trial["keywords"] if kw in query)
            if score > 0:
                matches.append({"id": trial["id"], "title": trial["title"],
                                "score": score})
        matches.sort(key=lambda m: -m["score"])
        return {"agent": self.agent_id, "matches": matches[:3],
                "clinical_claim_level": "none", "decision_support_only": True,
                "disclaimer": DISCLAIMER}
