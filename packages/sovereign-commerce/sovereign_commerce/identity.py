"""Identity & wallets: DID, Knox Bio-Node attestation binding, PQC signing
stub, Gaya Wallet (SYS-002) MPC-style m-of-n signing, Quantum Lineage Bridge.

HONESTY NOTICE:
- The PQC (Dilithium) signer is an INTERFACE STUB: real post-quantum signing
  requires an external pqcrypto library. The stub uses HMAC and MUST NOT be
  presented as actual PQC security (claims register I1).
- Knox Bio-Node binding records attestation data supplied by the caller;
  hardware verification is the device's responsibility (register I2).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import secrets
import time
import uuid

PQC_DISCLAIMER = ("PQC interface stub: HMAC stand-in, NOT real Dilithium. "
                  "Integrate a pqcrypto library for production.")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


# --- DID -------------------------------------------------------------------
class DidRegistry:
    def __init__(self):
        self._dids: dict[str, dict] = {}

    def create(self, entity_id: str, method: str = "key") -> str:
        did = f"did:{method}:{_sha(entity_id + secrets.token_hex(4))[:32]}"
        self._dids[did] = {"entity": entity_id, "created": time.time(),
                           "bindings": []}
        return did

    def bind(self, did: str, target: str) -> None:
        if did not in self._dids:
            raise KeyError(f"unknown did {did!r}")
        self._dids[did]["bindings"].append(target)

    def verify(self, did: str, entity_id: str) -> bool:
        d = self._dids.get(did)
        return bool(d and d["entity"] == entity_id)

    def count(self) -> int:
        return len(self._dids)


# --- Knox Bio-Node ---------------------------------------------------------
class KnoxBinding:
    """Records device attestation bindings. Hardware state is caller-supplied."""

    def __init__(self):
        self._bindings: dict[str, dict] = {}

    def attest(self, device_id: str, attestation: dict) -> str:
        binding_id = f"knox_{uuid.uuid4().hex[:10]}"
        record = {"binding_id": binding_id, "device": device_id,
                  "attestation": attestation, "ts": time.time(),
                  "verified": bool(attestation.get("enclave_ok"))}
        self._bindings[binding_id] = record
        return binding_id

    def verify_binding(self, binding_id: str) -> dict | None:
        b = self._bindings.get(binding_id)
        return dict(b) if b else None


# --- PQC signing stub ------------------------------------------------------
class PqcSigner:
    """Dilithium-labeled interface. STUB: HMAC-based, NOT real PQC."""

    def __init__(self, secret: str | None = None):
        self._secret = (secret or secrets.token_hex(32)).encode()
        self.disclaimer = PQC_DISCLAIMER

    def sign(self, message: str) -> dict:
        sig = hmac.new(self._secret, message.encode(), hashlib.sha256).hexdigest()
        return {"algorithm": "dilithium-interface-stub", "signature": sig,
                "disclaimer": self.disclaimer}

    def verify(self, message: str, signature: str) -> bool:
        expected = hmac.new(self._secret, message.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)


# --- Gaya Wallet (SYS-002, MPC m-of-n) -------------------------------------
class GayaWallet:
    """MPC-style wallet: keys held as n shares; signing requires m shares."""

    def __init__(self, wallet_id: str, n_shares: int = 3, m_required: int = 2):
        self.wallet_id = wallet_id
        self.n = n_shares
        self.m = m_required
        self._shares: dict[str, str] = {}

    def split(self, master_key: str) -> list[str]:
        """Deterministic share splitting: share_i = sha256(master + i)."""
        self._shares = {f"s{i}": _sha(f"{master_key}|{i}") for i in range(self.n)}
        return list(self._shares.values())

    def partial_sign(self, share_id: str, message: str) -> str:
        if share_id not in self._shares:
            raise KeyError(f"unknown share {share_id!r}")
        return hmac.new(self._shares[share_id].encode(), message.encode(),
                        hashlib.sha256).hexdigest()

    def aggregate(self, partials: list[str], message: str) -> dict:
        if len(partials) < self.m:
            raise ValueError(f"need {self.m} shares, got {len(partials)}")
        joined = "|".join(sorted(partials))
        return {"wallet": self.wallet_id, "signature": _sha(f"{joined}|{message}"),
                "shares_used": len(partials), "threshold": f"{self.m}-of-{self.n}"}


# --- Quantum Lineage Bridge ------------------------------------------------
class LineageBridge:
    """Device activation + lineage tracking (activation counter)."""

    def __init__(self):
        self._activations: dict[str, int] = {}
        self._lineage: list[dict] = []

    def activate(self, device_id: str) -> int:
        n = self._activations.get(device_id, 0) + 1
        self._activations[device_id] = n
        self._lineage.append({"device": device_id, "activation": n,
                              "ts": time.time()})
        return n

    def generation_depth(self, device_id: str) -> int:
        return self._activations.get(device_id, 0)
