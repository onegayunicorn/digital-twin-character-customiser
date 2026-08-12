"""Bridge capability registry."""
from __future__ import annotations

from sovereign.handshake import HandshakeRegistry


class BridgeRegistry:
    def __init__(self):
        self._routes: dict[str, dict] = {}
        self.handshake = HandshakeRegistry(stale_after_s=30.0)

    def register(self, module: str, capability: str, endpoint, role: str = "bridge") -> None:
        """Register a module serving a capability through an endpoint callable."""
        self._routes[capability] = {
            "module": module, "endpoint": endpoint, "role": role,
        }
        return None

    def route(self, capability: str):
        """Resolve and return the endpoint for a capability."""
        route = self._routes.get(capability)
        if not route:
            raise KeyError(f"capability {capability!r} not registered")
        return route

    def call(self, capability: str, **kwargs):
        route = self.route(capability)
        return route["endpoint"](**kwargs)

    def capabilities(self) -> list[str]:
        return sorted(self._routes)

    def health(self) -> dict:
        return {
            "capabilities": len(self._routes),
            "modules": sorted({r["module"] for r in self._routes.values()}),
            "handshake_alive": self.handshake.alive(),
        }
