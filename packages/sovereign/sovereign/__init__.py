"""Sovereign orchestrator core (stdlib-only, local-first).

Model-agnostic orchestration layer (the 'DeepSeek v4' name in the source doc
is aspirational; no such model family exists — see claims register O1):

  agents     - base agent + factory + lifecycle state machine
  queue      - persistent task queue (FIFO + priority)
  scheduler  - tick loop dispatching tasks to agents
  memory     - working / episodic / semantic stores (JSON)
  tools      - registry with ACL-gated execution
  governance - append-only audit log
  handshake  - agent registration (hello/ack) with heartbeats
  api        - minimal HTTP API: /health /status /tasks /agents

Design: no mandatory external calls, tamper-evident audit, full data ownership.
"""
from .agents import BaseAgent, AgentFactory
from .queue import TaskQueue
from .scheduler import Scheduler
from .memory import MemoryManager
from .tools import ToolRegistry
from .governance import AuditLogger
from .handshake import HandshakeRegistry
from .api import make_server

__all__ = [
    "BaseAgent", "AgentFactory", "TaskQueue", "Scheduler", "MemoryManager",
    "ToolRegistry", "AuditLogger", "HandshakeRegistry", "make_server",
]
