"""RepoAgent: per-repository steward agent."""
from __future__ import annotations

import re

from sovereign.agents import BaseAgent


def slugify(name: str) -> str:
    s = re.sub(r"[^0-9A-Za-z]+", "-", name).strip("-").lower()
    return s or "repo"


class RepoAgent(BaseAgent):
    def __init__(self, owner: str, name: str, domain: str = "misc",
                 agent_id: str | None = None):
        super().__init__(agent_id or f"repo-{slugify(name)}", "repo")
        self.owner = owner
        self.repo_name = name
        self.domain = domain
        self.url = f"https://github.com/{owner}/{name}"

    def execute(self, task: dict) -> dict:
        status = task.get("status", "inventoried")
        return {
            "agent": self.agent_id,
            "repo": {"owner": self.owner, "name": self.repo_name,
                     "url": self.url, "domain": self.domain},
            "sandbox_status": status,
            "note": "Repo facts only; contents not inspected unless analyzed.",
        }


def repo_agent_factory(owner: str, name: str, domain: str = "misc") -> RepoAgent:
    return RepoAgent(owner, name, domain)
