"""Tool registry with ACL-gated execution."""
from __future__ import annotations


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, dict] = {}

    def register(self, name: str, fn, acl: str = "agent") -> None:
        self._tools[name] = {"fn": fn, "acl": acl}

    def can_call(self, name: str, caller_role: str) -> bool:
        tool = self._tools.get(name)
        if not tool:
            return False
        acl = tool["acl"]
        if acl == "admin":
            return caller_role == "admin"
        if acl == "agent":
            return caller_role in ("agent", "admin")
        return True

    def call(self, name: str, caller_role: str, **kwargs):
        if not self.can_call(name, caller_role):
            raise PermissionError(f"role {caller_role!r} cannot call tool {name!r}")
        return self._tools[name]["fn"](**kwargs)

    def names(self) -> list[str]:
        return sorted(self._tools)
