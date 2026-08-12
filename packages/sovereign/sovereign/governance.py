"""Append-only audit logger (tamper-evident JSONL)."""
from __future__ import annotations

import hashlib
import json
import time


class AuditLogger:
    def __init__(self, path: str | None = None):
        self.path = path
        self._prev_hash = "0" * 64
        self._entries = 0

    def log(self, event: dict) -> str:
        """Append an event with a chained SHA-256 hash of the previous entry."""
        entry = {
            **event,
            "ts": time.time(),
            "prev_hash": self._prev_hash,
        }
        payload = json.dumps(entry, sort_keys=True).encode("utf-8")
        entry["hash"] = hashlib.sha256(payload).hexdigest()
        self._prev_hash = entry["hash"]
        self._entries += 1
        if self.path:
            with open(self.path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry) + "\n")
        return entry["hash"]

    @property
    def entry_count(self) -> int:
        return self._entries

    @staticmethod
    def verify_chain(path: str) -> bool:
        """Verify the hash chain in an audit JSONL file."""
        prev = "0" * 64
        try:
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    entry = json.loads(line)
                    if entry.get("prev_hash") != prev:
                        return False
                    payload = {k: v for k, v in entry.items() if k != "hash"}
                    if hashlib.sha256(json.dumps(payload, sort_keys=True)
                                      .encode()).hexdigest() != entry["hash"]:
                        return False
                    prev = entry["hash"]
        except FileNotFoundError:
            return False
        return True
