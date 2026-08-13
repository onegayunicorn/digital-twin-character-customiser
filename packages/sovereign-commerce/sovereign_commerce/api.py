"""Sovereign Commerce HTTP API (stdlib http.server)."""
from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class CommerceAPI:
    def __init__(self, kernel=None, jurisdiction=None, compliance=None,
                 entities=None, ledger=None, payments=None, procurement=None,
                 offgrid=None, escrow=None, twins=None):
        self.kernel = kernel
        self.jurisdiction = jurisdiction
        self.compliance = compliance
        self.entities = entities
        self.ledger = ledger
        self.payments = payments
        self.procurement = procurement
        self.offgrid = offgrid
        self.escrow = escrow
        self.twins = twins

    def health(self) -> dict:
        return {"status": "ok", "kernel_primitives": len(self.kernel.primitives())
                if self.kernel else 0,
                "domains": 14, "ledger_balanced": self.ledger.double_entry_balanced()
                if self.ledger else None}

    def jurisdiction_classify(self, tx: dict) -> dict:
        return self.jurisdiction.profile(tx) if self.jurisdiction else {}

    def compliance_gate(self, context: dict) -> dict:
        return self.compliance.run_gates(context.get("feature", "payments"),
                                         context) if self.compliance else {}

    def entity_summary(self) -> dict:
        return {"count": self.entities.count()} if self.entities else {}

    def ledger_status(self) -> dict:
        return {"balanced": self.ledger.double_entry_balanced(),
                "accounts": {a: self.ledger.balance(a) for a in
                             sorted(self.ledger._balances)} } if self.ledger else {}


def make_server(api: CommerceAPI, host: str = "127.0.0.1", port: int = 0):
    class Handler(BaseHTTPRequestHandler):
        def _json(self, code, payload):
            body = json.dumps(payload).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):  # noqa: N802
            if self.path == "/health":
                self._json(200, api.health())
            elif self.path == "/ledger":
                self._json(200, api.ledger_status())
            elif self.path == "/entities":
                self._json(200, api.entity_summary())
            else:
                self._json(404, {"error": "not found"})

        def do_POST(self):  # noqa: N802
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                self._json(400, {"error": "invalid json"})
                return
            if self.path == "/jurisdiction":
                self._json(200, api.jurisdiction_classify(payload))
            elif self.path == "/compliance":
                self._json(200, api.compliance_gate(payload))
            else:
                self._json(404, {"error": "not found"})

        def log_message(self, *args):
            pass

    return ThreadingHTTPServer((host, port), Handler)
