"""Sovereign Kernel: the 12 shared primitives every vertical uses.

Identity, Trust, Policy, Permissions, Ledger, Events, Payments, Contracts,
Compliance, Audit, AI Agents, Interoperability — registered as a primitive
registry with ownership mapping to platform packages.
"""
from __future__ import annotations

PRIMITIVES = [
    ("identity", "DID / KYC / IAM / device identity", "governance"),
    ("trust", "Reputation, attestation, verification", "governance"),
    ("policy", "Rules engine (procurement, compliance)", "sovereign-commerce"),
    ("permissions", "RBAC/ABAC gates", "governance"),
    ("ledger", "Double-entry accounting, escrow", "sovereign-commerce"),
    ("events", "Event bus, audit trail", "digital-twin"),
    ("payments", "Payment orchestration, rails, payouts", "sovereign-commerce"),
    ("contracts", "Terms, agreements, digital signatures", "sovereign-commerce"),
    ("compliance", "Compliance OS: gates, KYC/CDD, AML", "sovereign-commerce"),
    ("audit", "Tamper-evident audit chain", "sovereign"),
    ("ai-agents", "Agent roster (governance, med, repo)", "governance"),
    ("interoperability", "Bridge registry, handshake, MCP", "bridge"),
]


class SovereignKernel:
    """Kernel primitive registry. Verticals request primitives; each
    primitive reports its owner package and readiness (registered only)."""

    def __init__(self):
        self._registry = {name: {"purpose": purpose, "owner": owner,
                                 "status": "registered"}
                          for name, purpose, owner in PRIMITIVES}

    def primitives(self) -> list[str]:
        return list(self._registry)

    def describe(self, name: str) -> dict:
        if name not in self._registry:
            raise KeyError(f"unknown primitive {name!r}")
        return self._registry[name]

    def attach(self, name: str, implementation: str) -> None:
        if name not in self._registry:
            raise KeyError(f"unknown primitive {name!r}")
        self._registry[name]["implementation"] = implementation
        self._registry[name]["status"] = "attached"

    def status(self) -> dict:
        return {k: v["status"] for k, v in self._registry.items()}
