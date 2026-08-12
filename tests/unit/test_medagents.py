import pytest

from medagents.agents import DoctorAgent, HospitalAgent, ResearcherAgent


def test_hospital_triage_bands():
    a = HospitalAgent()
    a.transition("ready")
    a.transition("busy")
    r_ok = a.execute({"vitals": {"hr": 80, "spo2": 98}})
    r_crit = a.execute({"vitals": {"hr": 130, "spo2": 88}})
    assert r_ok["band"] == "routine"
    assert r_crit["band"] == "emergency"
    assert r_crit["triage_score"] > r_ok["triage_score"]
    assert r_crit["clinical_claim_level"] == "none"
    assert r_crit["decision_support_only"] is True


def test_doctor_agent_forward_with_disclaimer():
    a = DoctorAgent()
    res = a.execute({"exon": 44, "cdna": "c.7912C>T", "protein": "p.Arg2638*"})
    assert res["case_review"]["clinical_claim_level"] == "none"
    assert "disclaimer" in res and "disclaimer" in res["case_review"]
    assert any(s["mechanism"] == "exon_skipping"
               for s in res["case_review"]["strategies"])


def test_researcher_matching():
    a = ResearcherAgent()
    res = a.execute({"query": "exon skipping DMD ASO"})
    assert res["matches"] and res["matches"][0]["id"] == "NCT-0001"
    assert res["decision_support_only"] is True


def test_agents_extend_sovereign_base():
    from sovereign.agents import BaseAgent
    assert issubclass(HospitalAgent, BaseAgent)
    assert issubclass(DoctorAgent, BaseAgent)
    assert issubclass(ResearcherAgent, BaseAgent)
