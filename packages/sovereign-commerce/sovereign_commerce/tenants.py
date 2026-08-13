"""Multi-tenancy: isolation, per-tenant keys/DID/webhook secrets/expiry/state."""
from __future__ import annotations

import hashlib
import secrets


def _derive(secret: str, tenant: str, purpose: str) -> str:
    """Deterministic per-tenant key derivation (HKDF-style, sha256)."""
    return hashlib.sha256(f"{secret}|{tenant}|{purpose}".encode()).hexdigest()


class TenantRegistry:
    def __init__(self, master_secret: str | None = None):
        self._master = master_secret or secrets.token_hex(32)
        self._tenants: dict[str, dict] = {}

    def create(self, tenant_id: str, currency: str = "AUD",
               locale: str = "en-AU", compliance_profile: str = "AU") -> dict:
        webhook_secret = secrets.token_hex(32)
        tenant = {
            "id": tenant_id,
            "currency": currency,
            "locale": locale,
            "compliance_profile": compliance_profile,
            "encryption_key": _derive(self._master, tenant_id, "enc"),
            "webhook_secret": webhook_secret,
            "did_binding": None,
            "expiry_ttl_seconds": 7 * 24 * 3600,
            "state": {},  # isolated per-tenant state store
        }
        self._tenants[tenant_id] = tenant
        return self._summary(tenant)

    def get(self, tenant_id: str) -> dict | None:
        t = self._tenants.get(tenant_id)
        return dict(t) if t else None

    def _summary(self, t: dict) -> dict:
        return {"id": t["id"], "currency": t["currency"], "locale": t["locale"],
                "compliance_profile": t["compliance_profile"],
                "did_binding": t["did_binding"],
                "expiry_ttl_seconds": t["expiry_ttl_seconds"]}

    def bind_did(self, tenant_id: str, did: str) -> None:
        self._tenants[tenant_id]["did_binding"] = did

    def state(self, tenant_id: str) -> dict:
        return self._tenants[tenant_id]["state"]

    def set_expiry(self, tenant_id: str, ttl_seconds: int) -> None:
        self._tenants[tenant_id]["expiry_ttl_seconds"] = ttl_seconds

    def list_tenants(self) -> list[str]:
        return sorted(self._tenants)

    def isolation_ok(self) -> bool:
        """Each tenant has a distinct derived key and webhook secret."""
        keys = {t["encryption_key"] for t in self._tenants.values()}
        secrets_ = {t["webhook_secret"] for t in self._tenants.values()}
        return len(keys) == len(self._tenants) and len(secrets_) == len(self._tenants)
