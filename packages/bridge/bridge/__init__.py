"""ipp-bridge — the software bridge between platform modules.

A capability routing table: each module registers the capabilities it serves
and the endpoint (function) that implements them. Handshake/re-registration
reuses the sovereign HandshakeRegistry. The bridge gives the platform a single
routing surface for flows and triggers defined in platform/extensions/.
"""
from .registry import BridgeRegistry

__all__ = ["BridgeRegistry"]
