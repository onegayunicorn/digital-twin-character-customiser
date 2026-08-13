"""Autonomous trigger bus: declarative topic -> agent routing.

Agents wake up automatically when fire_trigger(topic, payload) is called.
Mirrors the blueprint's trigger map (identity/payment/escrow/compliance/
governance/twin/offgrid events).
"""
from __future__ import annotations

from .agents import make_agent

# Blueprint trigger map: topic -> agent(s)
DEFAULT_TRIGGERS = {
    "did.verified": ["identity", "compliance"],
    "knox.attested": ["identity", "orchestrator"],
    "payment.intent_created": ["payment", "compliance"],
    "payment.webhook": ["payment", "twin", "analytics"],
    "payment.expiry": ["payment"],
    "escrow.nfc_tap": ["escrow", "compliance"],
    "escrow.condition_met": ["escrow", "payment"],
    "compliance.entity": ["compliance", "governance"],
    "compliance.jurisdiction": ["compliance"],
    "governance.template": ["governance"],
    "governance.marketplace": ["governance"],
    "twin.state_changed": ["twin", "analytics"],
    "twin.payment_event": ["twin", "compliance"],
    "offgrid.network_loss": ["offgrid"],
    "offgrid.network_restore": ["offgrid"],
    "ads.generate": ["adgen", "localization"],
}


class TriggerBus:
    def __init__(self, triggers: dict | None = None):
        self._triggers = dict(triggers or DEFAULT_TRIGGERS)
        self._log: list[dict] = []

    def register(self, topic: str, agents: list[str]) -> None:
        self._triggers[topic] = agents

    def topics(self) -> list[str]:
        return sorted(self._triggers)

    def fire(self, topic: str, payload: dict | None = None) -> list[dict]:
        """Wake the agents registered for a topic; returns their results."""
        payload = payload or {}
        deliveries = []
        for name in self._triggers.get(topic, []):
            try:
                agent = make_agent(name)
                agent.transition("ready")
                agent.transition("busy")
                result = agent.execute(payload)
                delivery = {"topic": topic, "agent": name, "ok": True,
                            "result": result}
            except Exception as exc:  # noqa: BLE001
                delivery = {"topic": topic, "agent": name, "ok": False,
                            "error": str(exc)}
            deliveries.append(delivery)
            self._log.append(delivery)
        return deliveries

    def last_events(self, n: int = 10) -> list[dict]:
        return self._log[-n:]
