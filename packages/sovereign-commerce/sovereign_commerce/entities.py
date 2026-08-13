"""Legal entity registry: person -> sole trader -> company -> trust ->
partnership -> non-profit -> government -> cooperative -> DAO/protocol."""
from __future__ import annotations

ENTITY_TYPES = [
    "person", "sole-trader", "company", "trust", "partnership",
    "non-profit", "government", "cooperative", "dao",
]

# Entity type -> governance requirements (architecture map)
GOVERNANCE = {
    "company": ["directors", "officers", "signing-authority", "board-approvals"],
    "trust": ["trustee", "beneficiaries", "trust-deed"],
    "partnership": ["partners", "partnership-agreement"],
    "government": ["agency", "delegations", "procurement-rules"],
    "dao": ["governance-token", "voting", "treasury"],
}


class EntityRegistry:
    def __init__(self):
        self._entities: dict[str, dict] = {}

    def register(self, entity_id: str, entity_type: str, name: str,
                 jurisdiction: str = "AU", **fields) -> dict:
        if entity_type not in ENTITY_TYPES:
            raise ValueError(f"unknown entity type {entity_type!r}")
        entity = {"id": entity_id, "type": entity_type, "name": name,
                  "jurisdiction": jurisdiction, "beneficial_owners": [],
                  "governance": GOVERNANCE.get(entity_type, []), **fields}
        self._entities[entity_id] = entity
        return entity

    def get(self, entity_id: str) -> dict | None:
        e = self._entities.get(entity_id)
        return dict(e) if e else None

    def add_beneficial_owner(self, entity_id: str, owner_id: str,
                             share_pct: float) -> None:
        e = self._entities[entity_id]
        e["beneficial_owners"].append({"owner": owner_id, "share_pct": share_pct})

    def entity_types(self) -> list[str]:
        return list(ENTITY_TYPES)

    def count(self) -> int:
        return len(self._entities)
