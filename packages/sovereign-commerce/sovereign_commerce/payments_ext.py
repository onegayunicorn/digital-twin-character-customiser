"""Payments hardening: seven-day authorization expiry + hourly scheduler,
webhook HMAC validation, replay protection."""
from __future__ import annotations

import hashlib
import hmac
import time

DEFAULT_EXPIRY_SECONDS = 7 * 24 * 3600  # seven days
HOURLY_SECONDS = 3600


class ExpiryScheduler:
    """Tracks authorizations; hourly tick expires those past their TTL."""

    def __init__(self, ttl_seconds: int = DEFAULT_EXPIRY_SECONDS):
        self.ttl = ttl_seconds
        self._auths: dict[str, dict] = {}
        self._expired: list[str] = []

    def register(self, auth_id: str, created_at: float | None = None) -> None:
        self._auths[auth_id] = {"created_at": created_at if created_at is not None
                                else time.time(), "status": "active"}

    def tick(self, now: float | None = None) -> list[str]:
        """One scheduler tick (call hourly). Returns newly expired ids."""
        now = now or time.time()
        newly = []
        for auth_id, rec in list(self._auths.items()):
            if rec["status"] == "active" and now - rec["created_at"] > self.ttl:
                rec["status"] = "expired"
                newly.append(auth_id)
                self._expired.append(auth_id)
        return newly

    def status(self, auth_id: str) -> str | None:
        rec = self._auths.get(auth_id)
        return rec["status"] if rec else None

    def expires_in(self, auth_id: str, now: float | None = None) -> float | None:
        rec = self._auths.get(auth_id)
        if not rec:
            return None
        return max(0.0, self.ttl - ((now or time.time()) - rec["created_at"]))


class WebhookValidator:
    """HMAC-SHA256 signature validation with per-tenant secrets."""

    def __init__(self, secrets: dict[str, str] | None = None):
        self._secrets = secrets or {}

    def set_secret(self, tenant: str, secret: str) -> None:
        self._secrets[tenant] = secret

    def sign(self, tenant: str, payload: str) -> str:
        secret = self._secrets.get(tenant, "").encode()
        return hmac.new(secret, payload.encode(), hashlib.sha256).hexdigest()

    def validate(self, tenant: str, payload: str, signature: str) -> bool:
        secret = self._secrets.get(tenant, "").encode()
        expected = hmac.new(secret, payload.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)


class ReplayProtector:
    """Nonce + timestamp store: rejects replays and stale events."""

    def __init__(self, max_age_seconds: float = 300.0, max_entries: int = 10_000):
        self.max_age = max_age_seconds
        self.max_entries = max_entries
        self._seen: dict[str, float] = {}

    def accept(self, nonce: str, timestamp: float) -> bool:
        now = time.time()
        if abs(now - timestamp) > self.max_age:
            return False
        if nonce in self._seen:
            return False
        self._seen[nonce] = timestamp
        if len(self._seen) > self.max_entries:  # prune oldest
            oldest = min(self._seen, key=self._seen.get)
            del self._seen[oldest]
        return True
