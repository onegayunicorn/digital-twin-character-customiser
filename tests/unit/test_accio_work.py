import pytest

from sovereign_commerce.identity import (DidRegistry, GayaWallet, KnoxBinding,
                                         LineageBridge, PqcSigner)
from sovereign_commerce.payments_ext import (ExpiryScheduler, ReplayProtector,
                                             WebhookValidator)
from sovereign_commerce.tenants import TenantRegistry
from sovereign_commerce.governance import (AdvisoryCouncil, ContributorLicense,
                                           GovernanceCharter, Marketplace,
                                           PolicyLibrary, RevenueShare)
from sovereign_commerce.agents import make_agent
from sovereign_commerce.triggers import TriggerBus


# --- identity ----------------------------------------------------------------
def test_did_create_verify_bind():
    r = DidRegistry()
    did = r.create("user-1")
    assert did.startswith("did:")
    assert r.verify(did, "user-1")
    assert not r.verify(did, "user-2")
    r.bind(did, "device-1")
    assert "device-1" in r._dids[did]["bindings"]


def test_knox_binding_records_attestation():
    k = KnoxBinding()
    bid = k.attest("dev-1", {"enclave_ok": True})
    assert k.verify_binding(bid)["verified"] is True
    bid2 = k.attest("dev-2", {"enclave_ok": False})
    assert k.verify_binding(bid2)["verified"] is False


def test_pqc_stub_sign_verify_and_disclaimer():
    p = PqcSigner(secret="test-secret")
    sig = p.sign("message")
    assert "dilithium-interface-stub" in sig["algorithm"]
    assert "NOT real Dilithium" in sig["disclaimer"]
    assert p.verify("message", sig["signature"])
    assert not p.verify("other", sig["signature"])


def test_gaya_wallet_m_of_n():
    w = GayaWallet("w1", n_shares=3, m_required=2)
    shares = w.split("master-key")
    assert len(shares) == 3
    p1 = w.partial_sign("s0", "msg")
    p2 = w.partial_sign("s1", "msg")
    agg = w.aggregate([p1, p2], "msg")
    assert agg["threshold"] == "2-of-3"
    with pytest.raises(ValueError):
        w.aggregate([p1], "msg")  # need >= m shares


def test_lineage_bridge_activation():
    lb = LineageBridge()
    assert lb.activate("dev-1") == 1
    assert lb.activate("dev-1") == 2
    assert lb.generation_depth("dev-1") == 2


# --- payments hardening --------------------------------------------------------
def test_expiry_scheduler_ticks_after_ttl():
    s = ExpiryScheduler(ttl_seconds=100)
    s.register("a1", created_at=0.0)
    s.register("a2", created_at=200.0)
    expired = s.tick(now=101.0)
    assert expired == ["a1"]
    assert s.status("a1") == "expired"
    assert s.status("a2") == "active"
    assert s.expires_in("a2", now=201.0) == pytest.approx(99.0)


def test_webhook_validator_hmac():
    v = WebhookValidator()
    v.set_secret("tenant-1", "secret")
    sig = v.sign("tenant-1", '{"event":"payment"}')
    assert v.validate("tenant-1", '{"event":"payment"}', sig)
    assert not v.validate("tenant-1", '{"event":"other"}', sig)
    assert not v.validate("tenant-1", '{"event":"payment"}', "bad")


def test_replay_protector_rejects_replays_and_stale():
    rp = ReplayProtector(max_age_seconds=300)
    import time
    now = time.time()
    assert rp.accept("n1", now)
    assert not rp.accept("n1", now)  # replay
    assert not rp.accept("n2", now - 400)  # stale


# --- multi-tenancy -------------------------------------------------------------
def test_tenant_registry_isolation():
    t = TenantRegistry(master_secret="master")
    t.create("t1", currency="AUD")
    t.create("t2", currency="USD", locale="en-US")
    assert t.isolation_ok()  # distinct keys + webhook secrets
    assert t.get("t1")["currency"] == "AUD"
    assert t.get("t2")["locale"] == "en-US"
    t.bind_did("t1", "did:key:abc")
    assert t.get("t1")["did_binding"] == "did:key:abc"
    t.set_expiry("t1", 3600)
    assert t.get("t1")["expiry_ttl_seconds"] == 3600
    # per-tenant state stores are isolated dicts
    t.state("t1")["x"] = 1
    assert "x" not in t.state("t2")


# --- governance ---------------------------------------------------------------
def test_charter_and_license():
    c = GovernanceCharter()
    c.set_section("purpose", "open governance")
    pub = c.publish()
    assert pub["sections"]["purpose"] == "open governance"
    lic = ContributorLicense(revenue_share_pct=12.5)
    assert lic.terms()["revenue_share_pct"] == 12.5
    assert lic.contribution_ok(True)
    assert not lic.contribution_ok(False)


def test_policy_library_publish_amend():
    p = PolicyLibrary()
    p.publish("data-usage", "consent-first")
    p.amend("data-usage", "consent-first + retention 90d")
    assert "retention" in p.get("data-usage")["body"]


def test_advisory_council_approval_flow():
    c = AdvisoryCouncil(approve_threshold=0.6)
    for m in ("a", "b", "c", "d", "e"):
        c.add_member(m)
    pid = c.propose("Enable marketplace", "open templates")
    for m in ("a", "b", "c", "d"):
        c.vote(pid, m, True)
    c.vote(pid, "e", False)
    assert c.status(pid) == "approved"  # 4/5 = 0.8 >= 0.6


def test_revenue_share_and_marketplace():
    rs = RevenueShare()
    split = rs.split(100.0, 10.0)
    assert split["contributor"] == pytest.approx(10.0)
    assert split["platform"] == pytest.approx(90.0)
    m = Marketplace(revenue_share=rs)
    m.list_item("tpl-1", "creator", price=50.0)
    res = m.purchase("tpl-1", "buyer-1", share_pct=20.0)
    assert res["split"]["contributor"] == pytest.approx(10.0)
    assert m.revenue.ledger.double_entry_balanced()


# --- agents + trigger bus -------------------------------------------------------
def test_agent_factory_all_agents():
    for name in ("adgen", "localization", "compliance", "payment", "escrow",
                 "identity", "twin", "analytics", "governance", "procurement",
                 "supply-chain", "offgrid"):
        a = make_agent(name)
        a.transition("ready")
        a.transition("busy")
        assert a.execute({}) is not None
    with pytest.raises(KeyError):
        make_agent("orchestrator")


def test_trigger_bus_routes_and_wakes():
    bus = TriggerBus()
    results = bus.fire("did.verified", {"entity": "user-1"})
    assert {r["agent"] for r in results} == {"identity", "compliance"}
    assert all(r["ok"] for r in results)
    assert bus.fire("payment.webhook", {"payer": "buyer", "payee": "seller",
                                        "amount": 50.0})[0]["ok"]


def test_trigger_bus_unknown_topic_empty():
    bus = TriggerBus()
    assert bus.fire("no.such.topic") == []


def test_trigger_bus_offgrid_flow():
    bus = TriggerBus()
    res = bus.fire("offgrid.network_loss", {"node": "edge-9", "amount": -20.0})
    assert res[0]["agent"] == "offgrid"
    assert res[0]["result"]["status"]["disaster_mode"] is False
