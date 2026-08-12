import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "packages", "sovereign"))

from sovereign.agents import AgentFactory  # noqa: E402
from sovereign.api import OrchestratorAPI, make_server  # noqa: E402
from sovereign.governance import AuditLogger  # noqa: E402
from sovereign.handshake import HandshakeRegistry  # noqa: E402
from sovereign.memory import MemoryManager  # noqa: E402
from sovereign.queue import TaskQueue  # noqa: E402
from sovereign.scheduler import Scheduler  # noqa: E402
from sovereign.tools import ToolRegistry  # noqa: E402


def _ready_agents():
    agents = {r: AgentFactory.create(r, r) for r in ("reasoner", "coder", "tool", "coordinator")}
    for a in agents.values():
        a.transition("ready")
    return agents


def test_agent_factory_and_states():
    a = AgentFactory.create("r1", "reasoner")
    assert a.state == "idle"
    a.transition("ready")
    a.transition("busy")
    a.transition("done")  # busy -> done is valid
    with pytest.raises(ValueError):
        a.transition("busy")  # cannot go busy from done
    with pytest.raises(ValueError):
        AgentFactory.create("x", "nope")


def test_queue_priority_order():
    q = TaskQueue()
    q.push({"id": "low", "prompt": "x"}, priority=5)
    q.push({"id": "high", "prompt": "y"}, priority=0)
    first = q.pop()
    assert first["id"] == "high"
    q.complete("high")
    assert q.queued_count() == 1  # low still queued


def test_scheduler_dispatches_all():
    q = TaskQueue()
    agents = _ready_agents()
    for i in range(4):
        q.push({"id": f"t{i}", "prompt": f"task {i}"})
    sched = Scheduler(q, agents, tick_s=0.0)
    dispatched = sched.run(max_ticks=100)
    assert dispatched == 4
    assert q.queued_count() == 0
    for i in range(4):
        assert q.get(f"t{i}")["status"] == "done"


def test_scheduler_state_machine_valid():
    q = TaskQueue()
    agents = _ready_agents()
    q.push({"id": "t1", "prompt": "hello"})
    sched = Scheduler(q, agents, tick_s=0.0)
    assert sched.tick() == 1
    for a in agents.values():
        assert a.state == "ready"  # back to ready after done


def test_memory_manager(tmp_path):
    m = MemoryManager(str(tmp_path / "mem.json"), max_working=3)
    for i in range(5):
        m.write_working({"n": i})
    assert len(m.recent_working(10)) == 3  # trimmed
    m.write_episodic({"e": 1})
    m.write_semantic("key", {"v": 1})
    assert m.read_semantic("key")["v"] == 1
    m2 = MemoryManager(str(tmp_path / "mem.json"))
    assert m2.episodic_count() == 1  # persisted


def test_tool_registry_acl():
    t = ToolRegistry()
    t.register("read", lambda: "ok", acl="agent")
    t.register("admin_only", lambda: "secret", acl="admin")
    assert t.call("read", "agent") == "ok"
    with pytest.raises(PermissionError):
        t.call("admin_only", "agent")
    assert t.call("admin_only", "admin") == "secret"


def test_audit_logger_chain(tmp_path):
    p = str(tmp_path / "audit.jsonl")
    a = AuditLogger(p)
    a.log({"event": "one"})
    a.log({"event": "two"})
    assert a.entry_count == 2
    assert AuditLogger.verify_chain(p)


def test_handshake_registry():
    reg = HandshakeRegistry(stale_after_s=10.0)
    ack = reg.hello("agent-1", "reasoner")
    assert ack["ack"] == "ok"
    assert reg.beat("agent-1", ack["token"])
    assert reg.alive() == ["agent-1"]
    assert not reg.beat("agent-1", "wrong-token")


def test_http_api_endpoints():
    q = TaskQueue()
    agents = _ready_agents()
    api = OrchestratorAPI(queue=q, agents=agents, memory=MemoryManager(),
                          audit=AuditLogger(), handshake=HandshakeRegistry())
    server = make_server(api, port=0)
    import threading
    import urllib.request
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        with urllib.request.urlopen(f"{base}/health") as r:
            assert json.loads(r.read())["status"] == "ok"
        req = urllib.request.Request(f"{base}/tasks", data=b'{"prompt": "hi"}',
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            assert r.status == 201
        with urllib.request.urlopen(f"{base}/status") as r:
            st = json.loads(r.read())
            assert st["queued"] == 1
    finally:
        server.shutdown()
        server.server_close()
