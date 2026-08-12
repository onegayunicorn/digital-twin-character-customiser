"""Sandbox workspace generator for a repository."""
from __future__ import annotations

import json
import os

from .agent import slugify


def generate_sandbox(root: str, owner: str, name: str, domain: str = "misc") -> str:
    """Create sandboxes/<owner>/<slug>/ with manifest.json, sim stub, README.

    Returns the sandbox directory path.
    """
    slug = slugify(name)
    sandbox_dir = os.path.join(root, "sandboxes", owner, slug)
    os.makedirs(sandbox_dir, exist_ok=True)

    manifest = {
        "repo": {"owner": owner, "name": name,
                 "url": f"https://github.com/{owner}/{name}"},
        "domain": domain,
        "status": "sandboxed",
        "generated_by": "repo-agent",
        "sim_stub": "sim_stub.py",
    }
    with open(os.path.join(sandbox_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    with open(os.path.join(sandbox_dir, "sim_stub.py"), "w", encoding="utf-8") as fh:
        fh.write(f'''"""Simulation stub for {owner}/{name} (domain: {domain}).

Replace this stub with the repository's real simulation entry point.
All outputs are SIMULATED and carry no clinical/scientific claims.
"""
import json


def run() -> dict:
    return {{
        "repo": "{owner}/{name}",
        "domain": "{domain}",
        "status": "stub",
        "clinical_claim_level": "none",
    }}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
''')

    with open(os.path.join(sandbox_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# Sandbox — {owner}/{name}\n\n"
                 f"- Domain: {domain}\n- Status: sandboxed (stub)\n"
                 f"- Run: `python3 sim_stub.py`\n"
                 f"- Repo: https://github.com/{owner}/{name}\n")
    return sandbox_dir
