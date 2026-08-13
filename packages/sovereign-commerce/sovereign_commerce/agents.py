"""Accio Work agents: 13 autonomous execution agents (sovereign BaseAgent).

Each agent has minimal deterministic behavior; heavier logic delegates to the
commerce modules. All outputs carry decision-support framing where relevant.
"""
from __future__ import annotations

from sovereign.agents import BaseAgent

LOCALES = {"en-AU": "AUD", "en-US": "USD", "en-GB": "GBP",
           "ja-JP": "JPY", "zh-CN": "CNY"}


class AdGenAgent(BaseAgent):
    """Generates creative assets from templates."""

    def __init__(self, agent_id: str = "adgen", role: str = "adgen"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        template = task.get("template", "default")
        return {"agent": self.agent_id, "template": template,
                "creative": {"headline": f"{template} headline",
                             "body": f"{template} body copy"}, "status": "generated"}


class LocalizationAgent(BaseAgent):
    """Regional language/currency adaptation."""

    def __init__(self, agent_id: str = "localization", role: str = "localization"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        locale = task.get("locale", "en-AU")
        currency = LOCALES.get(locale, "AUD")
        return {"agent": self.agent_id, "locale": locale, "currency": currency,
                "status": "localized"}


class ComplianceAgent(BaseAgent):
    """Runs the regulatory gate chain."""

    def __init__(self, agent_id: str = "compliance", role: str = "compliance"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .compliance import ComplianceOS
        res = ComplianceOS().run_gates(task.get("feature", "payments"),
                                       task.get("context", {}))
        return {"agent": self.agent_id, "gate": res}


class PaymentAgent(BaseAgent):
    """Stripe-style payment orchestration (test-mode)."""

    def __init__(self, agent_id: str = "payment", role: str = "payment"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .ledger import Ledger
        from .payments import PaymentOrchestrator
        ledger = Ledger()
        ledger.post(task.get("payer", "buyer"), 500.0, "opening credit")
        ledger.post("equity", -500.0, "opening debit")
        orch = PaymentOrchestrator(ledger=ledger)
        return {"agent": self.agent_id,
                "result": orch.pay(task.get("payer", "buyer"),
                                   task.get("payee", "seller"),
                                   task.get("amount", 100.0))}


class EscrowAgent(BaseAgent):
    """NFC-tap conditional settlement."""

    def __init__(self, agent_id: str = "escrow", role: str = "escrow"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .ledger import Ledger
        from .nfc_escrow import NfcEscrowBridge
        ledger = Ledger()
        ledger.post(task.get("payer", "tap-payer"), 300.0, "opening credit")
        ledger.post("equity", -300.0, "opening debit")
        bridge = NfcEscrowBridge(ledger=ledger)
        tap = bridge.tap(task.get("tag", "TAG-1"), task.get("payer", "tap-payer"),
                         task.get("payee", "shop"), task.get("amount", 100.0))
        if task.get("condition_met", False):
            bridge.verify_condition(task.get("tag", "TAG-1"), True)
        return {"agent": self.agent_id, "tap": bridge.tap_status(task.get("tag", "TAG-1"))}


class IdentityAgent(BaseAgent):
    """DID verification + Knox binding."""

    def __init__(self, agent_id: str = "identity", role: str = "identity"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .identity import DidRegistry
        reg = DidRegistry()
        did = reg.create(task.get("entity", "user-1"))
        reg.bind(did, task.get("device", "device-1"))
        return {"agent": self.agent_id, "did": did,
                "verified": reg.verify(did, task.get("entity", "user-1"))}


class TwinAgent(BaseAgent):
    """Digital twin state updates."""

    def __init__(self, agent_id: str = "twin", role: str = "twin"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .twins import CommerceTwinHub
        hub = CommerceTwinHub()
        twin = hub.create_twin(task.get("entity_type", "order"),
                               task.get("entity_id", "o1"),
                               task.get("initial", {"status": "created"}))
        if task.get("update"):
            for field, value in task["update"].items():
                hub.update_twin(task.get("entity_type", "order"),
                                task.get("entity_id", "o1"), field, value)
        return {"agent": self.agent_id, "twin": twin,
                "state": hub.twin_state(task.get("entity_type", "order"),
                                        task.get("entity_id", "o1"))}


class AnalyticsAgent(BaseAgent):
    """Metrics aggregation."""

    def __init__(self, agent_id: str = "analytics", role: str = "analytics"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        metrics = task.get("metrics", {})
        return {"agent": self.agent_id, "metrics": metrics,
                "total": sum(metrics.values()), "status": "recorded"}


class GovernanceAgent(BaseAgent):
    """Policy enforcement + licensing checks."""

    def __init__(self, agent_id: str = "governance", role: str = "governance"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .governance import ContributorLicense
        lic = ContributorLicense(revenue_share_pct=task.get("share_pct", 10.0))
        return {"agent": self.agent_id,
                "license": lic.terms(),
                "contribution_allowed": lic.contribution_ok(
                    task.get("opted_in", True))}


class ProcurementAgent(BaseAgent):
    """Tender evaluation + three-way matching."""

    def __init__(self, agent_id: str = "procurement", role: str = "procurement"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .procurement import ProcurementEngine
        p = ProcurementEngine()
        tid = p.create_tender(task.get("title", "T"), task.get("buyer", "b"),
                              [{"sku": "S", "qty": task.get("qty", 10)}])
        for bid in task.get("bids", [{"supplier": "s1", "price": 100.0}]):
            p.submit_bid(tid, bid["supplier"], bid["price"],
                         bid.get("quality", 0.5))
        return {"agent": self.agent_id, "evaluation": p.evaluate(tid)}


class SupplyChainAgent(BaseAgent):
    """Serialisation + custody trail."""

    def __init__(self, agent_id: str = "supply-chain", role: str = "supply-chain"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .supplychain import SupplyChain
        sc = SupplyChain()
        sc.register_sku(task.get("sku", "LAP"), task.get("name", "Laptop"))
        serial = sc.serialise(task.get("sku", "LAP"), task.get("batch", "B1"))[0]
        for ev in task.get("events", [{"event": "shipped", "location": "port"}]):
            sc.add_event(serial, ev["event"], ev.get("location", ""))
        return {"agent": self.agent_id, "serial": serial,
                "chain_ok": sc.verify_chain(serial)}


class OffgridAgent(BaseAgent):
    """Offline queue + disaster mode."""

    def __init__(self, agent_id: str = "offgrid", role: str = "offgrid"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        from .offgrid import OffGridNode
        node = OffGridNode(task.get("node", "edge-1"))
        node.local_transaction(task.get("account", "local-buyer"),
                               task.get("amount", -50.0), task.get("memo", "offline"))
        if task.get("disaster", False):
            node.enter_disaster_mode()
        return {"agent": self.agent_id, "status": node.status()}


AGENT_FACTORY = {
    "orchestrator": None,  # provided by governance package
    "adgen": AdGenAgent, "localization": LocalizationAgent,
    "compliance": ComplianceAgent, "payment": PaymentAgent,
    "escrow": EscrowAgent, "identity": IdentityAgent, "twin": TwinAgent,
    "analytics": AnalyticsAgent, "governance": GovernanceAgent,
    "procurement": ProcurementAgent, "supply-chain": SupplyChainAgent,
    "offgrid": OffgridAgent,
}


def make_agent(name: str) -> BaseAgent:
    cls = AGENT_FACTORY.get(name)
    if cls is None or name == "orchestrator":
        raise KeyError(f"agent {name!r} not available here (orchestrator lives in governance)")
    return cls()
