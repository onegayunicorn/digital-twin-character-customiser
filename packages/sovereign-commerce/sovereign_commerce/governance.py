"""Governance & licensing: charter, contributor licenses, policy library,
advisory council workflow, revenue-sharing hooks, marketplace.

Implements the Gamma governance draft structure as working records.
NOT legal advice (register M4/X3).
"""
from __future__ import annotations

import time
import uuid

CHARTER_SECTIONS = [
    "purpose", "scope", "governance-structure", "decision-process",
    "licensing-and-ip", "data-and-compliance", "monetization-and-marketplace",
    "risk-and-dispute", "review-and-amendments",
]


class GovernanceCharter:
    def __init__(self):
        self._sections = {s: "" for s in CHARTER_SECTIONS}
        self._version = "0.1.0"

    def set_section(self, name: str, text: str) -> None:
        if name not in self._sections:
            raise KeyError(f"unknown charter section {name!r}")
        self._sections[name] = text

    def publish(self) -> dict:
        return {"version": self._version, "sections": dict(self._sections),
                "published": time.time()}


class ContributorLicense:
    """Starter contributor license terms (Gamma draft)."""

    def __init__(self, revenue_share_pct: float = 10.0,
                 attribution_required: bool = False):
        self.revenue_share = revenue_share_pct
        self.attribution_required = attribution_required

    def terms(self) -> dict:
        return {
            "ownership": "contributor retains ownership of their IP",
            "platform_license": "non-exclusive, royalty-free license for platform operation",
            "revenue_share_pct": self.revenue_share,
            "attribution": "opt-in" if not self.attribution_required else "required",
            "termination": "contributors may withdraw non-core content with reasonable notice",
            "disputes": "mediation-first, escalation to arbitration",
        }

    def contribution_ok(self, opted_into_license: bool) -> bool:
        return opted_into_license


class PolicyLibrary:
    def __init__(self):
        self._policies: dict[str, dict] = {}

    def publish(self, policy_id: str, body: str, version: str = "1.0") -> None:
        self._policies[policy_id] = {"body": body, "version": version,
                                     "updated": time.time()}

    def amend(self, policy_id: str, body: str) -> None:
        if policy_id not in self._policies:
            raise KeyError(f"unknown policy {policy_id!r}")
        self._policies[policy_id]["body"] = body
        self._policies[policy_id]["updated"] = time.time()

    def get(self, policy_id: str) -> dict | None:
        p = self._policies.get(policy_id)
        return dict(p) if p else None

    def list_policies(self) -> list[str]:
        return sorted(self._policies)


class AdvisoryCouncil:
    """Proposal -> vote (threshold) -> approve/deny -> escalate to review."""

    def __init__(self, approve_threshold: float = 0.6):
        self.threshold = approve_threshold
        self._proposals: dict[str, dict] = {}
        self._members: list[str] = []

    def add_member(self, member: str) -> None:
        self._members.append(member)

    def propose(self, title: str, body: str) -> str:
        pid = f"prop_{uuid.uuid4().hex[:8]}"
        self._proposals[pid] = {"title": title, "body": body, "votes": {},
                                "status": "open", "created": time.time()}
        return pid

    def vote(self, proposal_id: str, member: str, approve: bool) -> dict:
        p = self._proposals[proposal_id]
        if p["status"] != "open":
            raise ValueError(f"proposal {proposal_id} not open")
        p["votes"][member] = approve
        votes = list(p["votes"].values())
        if len(self._members) > 0 and len(votes) >= len(self._members):
            approval = sum(1 for v in votes if v) / len(votes)
            if approval >= self.threshold:
                p["status"] = "approved"
            elif approval <= (1 - self.threshold):
                p["status"] = "denied"
            else:
                p["status"] = "escalated-review"
        return dict(p)

    def status(self, proposal_id: str) -> str | None:
        p = self._proposals.get(proposal_id)
        return p["status"] if p else None


class RevenueShare:
    """Transparent contribution-ledger splits."""

    def __init__(self, ledger=None):
        from .ledger import Ledger
        self.ledger = ledger or Ledger()

    def split(self, revenue: float, contributor_share_pct: float) -> dict:
        contributor = revenue * contributor_share_pct / 100.0
        platform = revenue - contributor
        return {"revenue": revenue, "contributor": round(contributor, 2),
                "platform": round(platform, 2),
                "contributor_pct": contributor_share_pct}

    def record_split(self, item_id: str, revenue: float,
                     contributor_share_pct: float, contributor_acct: str,
                     platform_acct: str) -> dict:
        res = self.split(revenue, contributor_share_pct)
        self.ledger.post(platform_acct, res["platform"], f"revenue share: {item_id}")
        self.ledger.post(contributor_acct, res["contributor"], f"contributor share: {item_id}")
        return res


class Marketplace:
    def __init__(self, revenue_share: RevenueShare | None = None):
        self.revenue = revenue_share or RevenueShare()
        self._items: dict[str, dict] = {}

    def list_item(self, item_id: str, contributor: str, price: float,
                  license_ok: bool = True) -> dict:
        item = {"id": item_id, "contributor": contributor, "price": price,
                "license_ok": bool(license_ok), "sales": 0}
        self._items[item_id] = item
        return dict(item)

    def purchase(self, item_id: str, buyer: str, share_pct: float = 10.0) -> dict:
        item = self._items.get(item_id)
        if not item:
            raise KeyError(f"unknown item {item_id!r}")
        if not item["license_ok"]:
            raise ValueError("item not license-cleared")
        item["sales"] += 1
        res = self.revenue.record_split(item_id, item["price"], share_pct,
                                        contributor_acct=item["contributor"],
                                        platform_acct="platform")
        return {"item": item_id, "buyer": buyer, "sales": item["sales"],
                "split": res}
