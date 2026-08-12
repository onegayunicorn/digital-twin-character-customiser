"""repo-agent CLI.

Usage:
  python3 -m repo_agent --repo onegayunicorn/quantum-hub [--domain quantum] [--sandbox .]
"""
from __future__ import annotations

import argparse
import json
import sys

from .agent import repo_agent_factory
from .sandbox import generate_sandbox


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="repo_agent")
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--domain", default="misc")
    ap.add_argument("--sandbox", default=".", help="root for sandbox workspaces")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    owner, name = args.repo.split("/", 1)
    agent = repo_agent_factory(owner, name, args.domain)
    sandbox_path = generate_sandbox(args.sandbox, owner, name, args.domain)
    res = agent.execute({"status": "sandboxed"})
    res["sandbox_path"] = sandbox_path
    if args.quiet:
        print(f"repo-agent ok: {owner}/{name} domain={args.domain} sandbox={sandbox_path}")
        return 0
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
