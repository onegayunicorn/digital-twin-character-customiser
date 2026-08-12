"""Minimal HTTP API over the orchestrator (stdlib http.server)."""
from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class OrchestratorAPI:
    """Injectable state bundle: queue, agents, memory, audit, handshake."""

    def __init__(self, queue=None, agents=None, memory=None, audit=None,
                 handshake=None, pipelines=None, matrix=None, gatekeeper=None):
        self.queue = queue
        self.agents = agents or {}
        self.memory = memory
        self.audit = audit
        self.handshake = handshake
        self.pipelines = pipelines
        self.matrix = matrix
        self.gatekeeper = gatekeeper

    def health(self) -> dict:
        return {"status": "ok", "agents": len(self.agents),
                "queued": self.queue.queued_count() if self.queue else 0}

    def run_pipeline(self, pipeline: dict) -> dict:
        if not self.pipelines:
            return {"error": "pipeline runner not configured"}
        return self.pipelines.run_pipeline(pipeline)

    def matrix_status(self) -> dict:
        if self.matrix:
            return {"domains": self.matrix.get("domains", []),
                    "metrics": self.matrix.get("metrics", {})}
        return {"error": "matrix not configured"}

    def gatecheck(self, text: str, caller_role: str = "agent",
                  resource: str = "reports") -> dict:
        if not self.gatekeeper:
            return {"error": "gatekeeper not configured"}
        return self.gatekeeper.execute({"text": text, "caller_role": caller_role,
                                        "resource": resource})

    def status(self) -> dict:
        return {
            "status": "ok",
            "agents": {aid: {"role": a.role, "state": a.state}
                       for aid, a in self.agents.items()},
            "queued": self.queue.queued_count() if self.queue else 0,
            "memory": {"episodic": self.memory.episodic_count() if self.memory else 0},
            "audit_entries": self.audit.entry_count if self.audit else 0,
            "handshake_alive": self.handshake.alive() if self.handshake else [],
        }


def make_handler(api: OrchestratorAPI):
    class Handler(BaseHTTPRequestHandler):
        def _json(self, code: int, payload: dict) -> None:
            body = json.dumps(payload).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):  # noqa: N802
            if self.path == "/health":
                self._json(200, api.health())
            elif self.path == "/status":
                self._json(200, api.status())
            elif self.path == "/tasks":
                tasks = api.queue.all() if api.queue else []
                self._json(200, {"tasks": [
                    {"id": t["id"], "status": t["status"], "priority": t["priority"]}
                    for t in tasks]})
            elif self.path == "/agents":
                self._json(200, {"agents": list(api.agents)})
            elif self.path == "/matrix":
                self._json(200, api.matrix_status())
            elif self.path == "/gatecheck":
                self._json(200, api.gatecheck(""))
            else:
                self._json(404, {"error": "not found"})

        def do_POST(self):  # noqa: N802
            if self.path in ("/tasks", "/pipelines", "/gatecheck"):
                length = int(self.headers.get("Content-Length", 0))
                raw = self.rfile.read(length) if length else b"{}"
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    self._json(400, {"error": "invalid json"})
                    return
                if self.path == "/tasks":
                    tid = api.queue.push(payload)
                    self._json(201, {"id": tid, "status": "queued"})
                elif self.path == "/pipelines":
                    self._json(200, api.run_pipeline(payload))
                else:
                    self._json(200, api.gatecheck(
                        payload.get("text", ""),
                        payload.get("caller_role", "agent"),
                        payload.get("resource", "reports")))
            else:
                self._json(404, {"error": "not found"})

        def log_message(self, *args):  # silence request logs
            pass

    return Handler


def make_server(api: OrchestratorAPI, host: str = "127.0.0.1", port: int = 0):
    """Create (but do not start) a ThreadingHTTPServer; port 0 = ephemeral."""
    handler = make_handler(api)
    server = ThreadingHTTPServer((host, port), handler)
    return server


def serve(api: OrchestratorAPI, host: str = "127.0.0.1", port: int = 8787) -> None:
    server = make_server(api, host, port)
    print(f"Sovereign API on http://{host}:{server.server_address[1]}")
    server.serve_forever()
