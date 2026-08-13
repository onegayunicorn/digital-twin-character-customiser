import json
import threading
import urllib.request

import pytest

from sovereign_commerce import (ComplianceOS, CommerceTwinHub, EntityRegistry,
                                JurisdictionEngine, Ledger, LedgerError,
                                NfcEscrowBridge, OffGridNode,
                                PaymentOrchestrator, ProcurementEngine,
                                SovereignKernel, StripeClient, SupplyChain)
from sovereign_commerce.api import CommerceAPI, make_server


# --- kernel ----------------------------------------------------------------
def test_kernel_primitives():
    k = SovereignKernel()
    assert len(k.primitives()) == 12
    assert k.describe("ledger")["owner"] == "sovereign-commerce"
    k.attach("ledger", "sovereign_commerce.ledger")
    assert k.status()["ledger"] == "attached"
    with pytest.raises(KeyError):
        k.describe("nope")


# --- jurisdiction ----------------------------------------------------------
def test_jurisdiction_classify():
    j = JurisdictionEngine()
    p = j.profile({"user_jurisdiction": "AU", "asset_jurisdiction": "US"})
    assert p["classified"]["user"] == "AU"
    assert p["classified"]["asset"] == "US"
    assert p["primary"] in p["classified"].values()
    assert "digital_assets" in p["regulatory_profile"]


def test_jurisdiction_unknown_warns():
    j = JurisdictionEngine(default="AU")
    p = j.profile({"service_jurisdiction": "XX"})
    assert p["classified"]["service"] == "ZZ"
    assert any("unknown jurisdiction" in w for w in p["warnings"])


# --- compliance gates ------------------------------------------------------
def test_compliance_gate_block_missing_registration():
    c = ComplianceOS()
    res = c.run_gates("digital-asset-exchange", {"jurisdiction": "AU",
                                                 "classification": "VASP"})
    assert res["final"] == "BLOCK"
    assert "registration" in res["failed"]


def test_compliance_gate_enable_when_complete():
    c = ComplianceOS()
    ctx = {"jurisdiction": "AU", "classification": "VASP", "registered": True,
           "aml_program": True, "kyc": True, "transaction_monitoring": True,
           "travel_rule": True, "sanctions_ok": True, "record_keeping": True,
           "independent_evaluation": True}
    res = c.run_gates("digital-asset-exchange", ctx)
    assert res["final"] == "ENABLE"


def test_compliance_evidence_logged():
    c = ComplianceOS()
    c.run_gates("x", {"classification": "y"})
    assert any(e["type"] == "gate_chain" for e in c.evidence_log())


def test_kyc_and_sanctions():
    c = ComplianceOS()
    assert c.check_kyc("e1", {"verified": True, "id_document": "passport"})["ok"]
    assert not c.check_kyc("e2", {})["ok"]
    assert c.check_sanctions({"id": "e1"})["ok"]
    assert not c.check_sanctions({"id": "e2", "sanctions_list": "US-OFAC"})["ok"]


# --- entities --------------------------------------------------------------
def test_entity_registry():
    r = EntityRegistry()
    r.register("e1", "company", "Acme Pty Ltd")
    r.register("e2", "dao", "Protocol DAO")
    assert r.get("e1")["governance"] == ["directors", "officers",
                                         "signing-authority", "board-approvals"]
    assert "governance-token" in r.get("e2")["governance"]
    r.add_beneficial_owner("e1", "owner-1", 0.8)
    assert r.get("e1")["beneficial_owners"][0]["share_pct"] == 0.8
    with pytest.raises(ValueError):
        r.register("e3", "ufo", "x")


# --- ledger -----------------------------------------------------------------
def test_ledger_double_entry():
    l = Ledger()
    l.post("cash", 1000.0, "opening credit")
    l.post("equity", -1000.0, "opening debit")  # balanced contra entry
    l.transfer("cash", "buyer-wallet", 250.0)
    assert l.balance("cash") == pytest.approx(750.0)
    assert l.balance("buyer-wallet") == pytest.approx(250.0)
    assert l.double_entry_balanced()


def test_ledger_insufficient_funds():
    l = Ledger()
    with pytest.raises(LedgerError):
        l.transfer("a", "b", 100.0)


def test_escrow_hold_release_refund():
    l = Ledger()
    l.post("payer", 500.0, "opening credit")
    l.post("equity", -500.0, "opening debit")
    l.escrow_hold("e1", "payer", 200.0)
    assert l.balance("payer") == pytest.approx(300.0)
    assert l.escrow_state("e1")["state"] == "held"
    l.escrow_release("e1", "payee")
    assert l.balance("payee") == pytest.approx(200.0)
    assert l.escrow_state("e1")["state"] == "released"
    assert l.double_entry_balanced()


# --- payments ---------------------------------------------------------------
def test_stripe_client_test_mode():
    s = StripeClient()
    pi = s.create_payment_intent(1000, "aud")
    assert pi["test_mode"] is True
    assert pi["status"] == "requires_payment_method"


def test_payment_orchestrator_escrow_flow():
    l = Ledger()
    l.post("buyer", 500.0, "opening credit")
    l.post("equity", -500.0, "opening debit")
    orch = PaymentOrchestrator(ledger=l)
    res = orch.pay("buyer", "seller", 100.0)
    assert res["status"] == "settled"
    assert l.balance("seller") == pytest.approx(100.0)
    assert l.double_entry_balanced()


def test_payment_orchestrator_blocked_by_compliance():
    c = ComplianceOS()
    orch = PaymentOrchestrator(compliance=c)
    res = orch.pay("a", "b", 10.0, context={"jurisdiction": "AU"})
    assert res["status"] == "BLOCKED"


# --- procurement -------------------------------------------------------------
def test_tender_evaluation_and_three_way_match():
    p = ProcurementEngine()
    tid = p.create_tender("IT Hardware", "gov", [{"sku": "LAP", "qty": 10}])
    p.submit_bid(tid, "supplier-a", 9500.0, 0.8)
    p.submit_bid(tid, "supplier-b", 8800.0, 0.6)
    ev = p.evaluate(tid)
    # supplier-a: vf=0.926*0.5 + quality 0.8*0.5 = 0.863 > supplier-b: 0.5+0.3 = 0.8
    assert ev[0]["supplier"] == "supplier-a"
    po = p.create_po("supplier-b", "gov", [{"sku": "LAP", "qty": 10, "unit_price": 880.0}])
    grn = p.create_grn(po, [{"sku": "LAP", "qty": 10}])
    inv = p.create_invoice(po, "supplier-b", [{"sku": "LAP", "qty": 10, "unit_price": 880.0}])
    m = p.three_way_match(po, grn, inv)
    assert m["match"] is True and m["payable"] is True


def test_three_way_match_fails_on_price_mismatch():
    p = ProcurementEngine()
    po = p.create_po("s", "b", [{"sku": "X", "qty": 5, "unit_price": 10.0}])
    grn = p.create_grn(po, [{"sku": "X", "qty": 5}])
    inv = p.create_invoice(po, "s", [{"sku": "X", "qty": 5, "unit_price": 12.0}])
    m = p.three_way_match(po, grn, inv)
    assert m["match"] is False and m["payable"] is False
    assert any("price" in i for i in m["issues"])


# --- supply chain -------------------------------------------------------------
def test_supply_chain_custody_chain():
    sc = SupplyChain()
    sc.register_sku("LAP", "Laptop")
    serial = sc.serialise("LAP", "B1")[0]
    sc.add_event(serial, "manufactured", "factory")
    sc.add_event(serial, "shipped", "port")
    assert sc.verify_chain(serial)
    assert sc.chain_of_custody(serial)[-1]["event"] == "shipped"


# --- off-grid -----------------------------------------------------------------
def test_offgrid_queue_and_sync():
    n = OffGridNode("n1")
    n.local_transaction("local-buyer", -50.0, "offline purchase")
    assert n.queue.pending_count() == 1
    n.enter_disaster_mode()
    assert n.status()["disaster_mode"] is True
    pending = n.sync_outgoing()
    assert len(pending) == 1
    n2 = OffGridNode("n2")
    n2.merge_incoming(pending)
    assert n2.ledger.entries_since(0)[0]["memo"] == "offline purchase"


# --- NFC escrow ---------------------------------------------------------------
def test_nfc_escrow_release_on_condition():
    l = Ledger()
    l.post("tap-payer", 300.0)
    b = NfcEscrowBridge(ledger=l)
    tap = b.tap("TAG-001", "tap-payer", "shop", 100.0, condition="goods_received")
    assert tap["state"] == "held"
    b.verify_condition("TAG-001", True)
    assert b.tap_status("TAG-001")["state"] == "released"
    assert l.balance("shop") == pytest.approx(100.0)


def test_nfc_escrow_refund_when_condition_fails():
    l = Ledger()
    l.post("tap-payer", 300.0)
    b = NfcEscrowBridge(ledger=l)
    b.tap("TAG-002", "tap-payer", "shop", 100.0)
    b.verify_condition("TAG-002", False)
    assert b.tap_status("TAG-002")["state"] == "refunded"
    assert l.balance("tap-payer") == pytest.approx(300.0)


# --- twins ---------------------------------------------------------------------
def test_commerce_twins():
    t = CommerceTwinHub()
    twin = t.create_twin("order", "o1", {"status": "created", "total": 99.0})
    assert twin == "order:o1"
    t.update_twin("order", "o1", "status", "paid")
    state = t.twin_state("order", "o1")
    assert state["status"] == "paid" and state["total"] == 99.0
    assert t.snapshot("order:o1")["status"] == "paid"


# --- API ------------------------------------------------------------------------
def test_commerce_api():
    api = CommerceAPI(kernel=SovereignKernel(), jurisdiction=JurisdictionEngine(),
                      compliance=ComplianceOS(), entities=EntityRegistry(),
                      ledger=Ledger())
    server = make_server(api, port=0)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        with urllib.request.urlopen(f"{base}/health") as r:
            assert json.loads(r.read())["kernel_primitives"] == 12
        req = urllib.request.Request(f"{base}/jurisdiction", data=b'{}',
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            assert json.loads(r.read())["primary"] == "AU"
        req2 = urllib.request.Request(f"{base}/compliance",
                                      data=json.dumps({"feature": "payments",
                                                       "jurisdiction": "AU"}).encode(),
                                      headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req2) as r:
            assert json.loads(r.read())["final"] == "BLOCK"
    finally:
        server.shutdown()
        server.server_close()
