#!/usr/bin/env python3
"""Repo connectivity: sandbox all public repos + connectivity report + matrix.

Reads docs/repo-inventory.csv, generates a repo-agent sandbox for every
API-confirmed PUBLIC repo, and writes docs/repo-connectivity.md with the
domain adjacency summary (via matrix-core integration).
"""
from __future__ import annotations

import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "packages", "repo-agent"))


def main() -> int:
    from repo_agent.sandbox import generate_sandbox

    inv = os.path.join(ROOT, "docs", "repo-inventory.csv")
    rows = []
    with open(inv, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    public = [r for r in rows if r["visibility"] == "public"]
    sandbox_root = os.path.join(ROOT, "sandboxes")

    sandboxed = []
    for r in public:
        try:
            path = generate_sandbox(sandbox_root, r["owner"], r["name"], r["domain"])
            sandboxed.append((r, path))
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {r['owner']}/{r['name']}: {exc}")

    # matrix integration on the full inventory
    try:
        sys.path.insert(0, os.path.join(ROOT, "packages", "matrix-core"))
        from matrix_core.integration import integrate_inventory
        mx = integrate_inventory(inv)
    except Exception as exc:  # noqa: BLE001
        mx = {"domains": [], "metrics": {"nodes": 0}, "error": str(exc)}

    lines = [
        "# Repository Connectivity",
        "",
        f"**Public repos (API-confirmed):** {len(public)} · **Sandboxes generated:** {len(sandboxed)}",
        "",
        "Each public repo has a sandbox workspace under `sandboxes/<owner>/<repo>/` "
        "(manifest.json + sim stub) via the repo-agent. Completion status is **unknown** "
        "for all repos until inspected — sandbox status is `sandboxed`, never `complete`.",
        "",
        "## Domain adjacency (matrix integration)",
        "",
        f"- Domains: {len(mx.get('domains', []))}",
        f"- Graph: nodes={mx.get('metrics', {}).get('nodes', 0)} "
        f"edges={mx.get('metrics', {}).get('edges', 0)} "
        f"density={mx.get('metrics', {}).get('density', 0):.3f}",
        "",
        "## Public repo list",
        "",
        "| # | Repo | Domain | Language | Sandbox |",
        "|---|---|---|---|---|",
    ]
    for i, (r, path) in enumerate(sorted(sandboxed, key=lambda x: x[0]["name"].lower()), 1):
        lines.append(f"| {i} | [{r['owner']}/{r['name']}]({r['url']}) | {r['domain']} "
                     f"| {r['language'] or '—'} | `sandboxes/{r['owner']}/{r['name']}/` |")

    with open(os.path.join(ROOT, "docs", "repo-connectivity.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"connectivity: {len(public)} public repos -> {len(sandboxed)} sandboxes; "
          f"matrix nodes={mx.get('metrics', {}).get('nodes', 0)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
