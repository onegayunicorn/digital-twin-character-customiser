import pytest

from governance.agents import (ChatAgent, GatekeeperAgent, OrchestratorAgent,
                               TallymanAgent, WatcherAgent)


def test_gatekeeper_blocks_unverified_claims():
    g = GatekeeperAgent()
    res = g.execute({"text": "our 100% cure is guaranteed", "caller_role": "agent",
                     "resource": "reports"})
    assert res["status"] == "blocked"
    assert "100%" in res["claims_gate"]["flagged"]


def test_gatekeeper_allows_clean_text():
    g = GatekeeperAgent()
    res = g.execute({"text": "simulated mechanism analysis with disclaimer",
                     "caller_role": "agent", "resource": "reports"})
    assert res["status"] == "allowed"


def test_gatekeeper_acl():
    g = GatekeeperAgent()
    assert g.check_acl("admin", "admin:secrets")
    assert not g.check_acl("agent", "admin:secrets")
    assert not g.check_acl("guest", "reports")


def test_orchestrator_routes_batch():
    o = OrchestratorAgent()
    res = o.execute({"tasks": [{"id": "a", "role": "reasoner"},
                               {"id": "b", "role": "coder"}]})
    assert res["total"] == 2
    assert res["routed"]["reasoner"] == ["a"]


def test_watcher_health_and_attention():
    w = WatcherAgent()
    ok = w.execute({"stale_entities": [], "spec_counts": {"protocols": 131},
                    "tests": {"passed": 98, "failed": 0}})
    assert ok["status"] == "healthy"
    bad = w.execute({"stale_entities": ["node-1"],
                     "spec_counts": {"protocols": 131},
                     "tests": {"passed": 1, "failed": 2}})
    assert bad["status"] == "attention"


def test_tallyman_sums():
    t = TallymanAgent()
    res = t.execute({"metrics": {"tasks": 4, "tests": 98}})
    assert res["total"] == 102
    assert res["status"] == "tallied"


def test_chat_router():
    c = ChatAgent()
    assert c.execute({"message": "show tally"})["intent"] == "tallyman"
    assert c.execute({"message": "gate this claim"})["intent"] == "gatekeeper"
    assert c.execute({"message": "hello"})["intent"] == "direct"


def test_agents_extend_sovereign():
    from sovereign.agents import BaseAgent
    for cls in (OrchestratorAgent, GatekeeperAgent, WatcherAgent,
                TallymanAgent, ChatAgent):
        assert issubclass(cls, BaseAgent)
