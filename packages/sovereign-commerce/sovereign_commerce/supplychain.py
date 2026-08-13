"""Supply chain: SKU registry, serialisation, batch tracking, provenance."""
from __future__ import annotations

import hashlib
import time
import uuid


class SupplyChain:
    def __init__(self):
        self._skus: dict[str, dict] = {}
        self._units: dict[str, dict] = {}

    def register_sku(self, sku: str, name: str, unit: str = "ea") -> dict:
        self._skus[sku] = {"sku": sku, "name": name, "unit": unit}
        return self._skus[sku]

    def serialise(self, sku: str, batch: str, qty: int = 1) -> list[str]:
        if sku not in self._skus:
            raise KeyError(f"unknown sku {sku!r}")
        serials = []
        root_hash = "0" * 64
        for _ in range(qty):
            serial = f"{sku}-{uuid.uuid4().hex[:10].upper()}"
            created = {"ts": time.time(), "event": "created", "prev_hash": root_hash}
            created["hash"] = hashlib.sha256(
                f"created||{root_hash}".encode()).hexdigest()
            self._units[serial] = {"sku": sku, "batch": batch, "events": [created]}
            serials.append(serial)
        return serials

    def add_event(self, serial: str, event: str, location: str = "") -> None:
        u = self._units.get(serial)
        if not u:
            raise KeyError(f"unknown serial {serial!r}")
        prev_hash = u["events"][-1].get("hash", "0" * 64)
        record = {"ts": time.time(), "event": event, "location": location,
                  "prev_hash": prev_hash}
        record["hash"] = hashlib.sha256(
            f"{event}|{location}|{prev_hash}".encode()).hexdigest()
        u["events"].append(record)

    def chain_of_custody(self, serial: str) -> list[dict]:
        u = self._units.get(serial)
        if not u:
            raise KeyError(f"unknown serial {serial!r}")
        return list(u["events"])

    def verify_chain(self, serial: str) -> bool:
        """Verify the custody hash chain is unbroken."""
        events = self.chain_of_custody(serial)
        prev = "0" * 64
        for e in events:
            if e.get("prev_hash") != prev:
                return False
            if e["hash"] != hashlib.sha256(
                    f"{e['event']}|{e.get('location','')}|{prev}".encode()).hexdigest():
                return False
            prev = e["hash"]
        return True
