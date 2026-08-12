"""repo-agent — one agent + sandbox per repository.

Given any repo from the 420-repo inventory, this package:
  1. Creates a RepoAgent (sovereign BaseAgent) with a role by domain.
  2. Generates a sandbox workspace (manifest.json, sim stub, README) under
     sandboxes/<owner>/<slug>/.
  3. Reports repo facts and sandbox status.

Statuses are honest: inventoried | sandboxed | analyzed — never "complete"
without verification (see agents/prompts/repo-agent.md).
"""
from .agent import RepoAgent, repo_agent_factory
from .sandbox import generate_sandbox

__all__ = ["RepoAgent", "repo_agent_factory", "generate_sandbox"]
