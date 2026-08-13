"""Off-grid layer: offline transaction queue, store-and-forward sync,
local ledger, and disaster mode. Technical sovereignty — not legal
sovereignty (the architecture doc's explicit distinction)."""
from __future__ import annotations

import json
import time


class OfflineQueue:
    def __init__(self):
        self._queue: list[dict] = []

    def enqueue(self, op: dict) -> int:
        op = {**op, "queued_at": time.time()}
        self._queue.append(op)
        return len(self._queue)

    def pending(self) -> list[dict]:
        return list(self._queue)

    def pending_count(self) -> int:
        return len(self._queue)


class LocalLedger:
    """Append-only local ledger with sync cursor."""

    def __init__(self):
        self._entries: list[dict] = []
        self._cursor = 0

    def append(self, entry: dict) -> int:
        entry = {**entry, "seq": len(self._entries), "ts": time.time()}
        self._entries.append(entry)
        return entry["seq"]

    def entries_since(self, cursor: int) -> list[dict]:
        return self._entries[cursor:]

    @property
    def cursor(self) -> int:
        return self._cursor

    def advance_cursor(self, to: int) -> None:
        self._cursor = max(self._cursor, to)


class OffGridNode:
    """A sovereign edge node: offline operations + eventual-consistency sync."""

    def __init__(self, node_id: str):
        self.node_id = node_id
        self.queue = OfflineQueue()
        self.ledger = LocalLedger()
        self.disaster_mode = False

    def local_transaction(self, account: str, amount: float, memo: str = "") -> int:
        seq = self.ledger.append({"type": "local_tx", "account": account,
                                  "amount": amount, "memo": memo,
                                  "node": self.node_id})
        self.queue.enqueue({"op": "tx", "seq": seq, "account": account,
                            "amount": amount, "memo": memo, "node": self.node_id})
        return seq

    def sync_outgoing(self) -> list[dict]:
        """Store-and-forward: hand the pending queue to the mesh/cloud."""
        pending = self.queue.pending()
        self._last_sync = time.time()
        return pending

    def merge_incoming(self, remote_entries: list[dict]) -> dict:
        """Merge remote ledger entries (append-only, seq monotonic)."""
        merged, skipped = 0, 0
        existing = {e["seq"] for e in self.ledger._entries}
        for e in remote_entries:
            if e["seq"] not in existing:
                self.ledger._entries.append(e)
                merged += 1
            else:
                skipped += 1
        self.ledger._entries.sort(key=lambda e: e["seq"])
        return {"merged": merged, "skipped": skipped}

    def enter_disaster_mode(self) -> None:
        self.disaster_mode = True
        self.ledger.append({"type": "disaster_mode", "node": self.node_id})

    def exit_disaster_mode(self) -> None:
        self.disaster_mode = False

    def status(self) -> dict:
        return {"node": self.node_id, "disaster_mode": self.disaster_mode,
                "pending": self.queue.pending_count(),
                "ledger_entries": len(self.ledger._entries),
                "cursor": self.ledger.cursor,
                "last_sync": getattr(self, "_last_sync", None)}
