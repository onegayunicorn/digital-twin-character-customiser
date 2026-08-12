#!/usr/bin/env python3
"""Build docs/repo-inventory.csv + docs/repo-inventory.md from repo_list.py
(source of record, 420 repos) merged with GitHub API metadata for the public
subset (data/repos/*.json).

Domain classification is a name heuristic for grouping purposes only.
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from repo_list import REPOS  # noqa: E402

DOMAIN_RULES = [
    ("quantum", r"quant|qubit|bell|entangl|bloch|spdc|teleport|photonic"),
    ("sovereign", r"sovereign|sov(erign)?|command-core|taka|aether|omega"),
    ("genesis-cure", r"genesis|genosync|dna|kaleidoscope|dmd|cure|lineage|chromagene"),
    ("bci-neuro", r"bci|neural|neuro|brain|eeg|muse|zenith|particle.?bender|plasma"),
    ("escrow-payments", r"escrow|stripe|payment|financial|s2h|ledger|mubits|tibits|gaya"),
    ("teleos-os", r"tele|os-|quantum-os|computercations"),
    ("mesh-network", r"mesh|bluejay|blujay|network|node|hub|bridge|mesh"),
    ("dashboard-ui", r"dashboard|dash|ui|app|mobile|web|flutter|frontend"),
    ("hardware-drivers", r"driver|firmware|kernel|device|sensor|hardware|g35|a17|aosp|opencl"),
    ("orchestrator-agent", r"orchestrat|agent|command|orchestrator|controller|bot"),
    ("ai-chat-llm", r"ai|chat|llm|gpt|gemma|deepseek|kimi|nexus|claude|copilot"),
    ("misc", r".*"),
]


def classify(name: str) -> str:
    low = name.lower()
    for domain, pattern in DOMAIN_RULES:
        if re.search(pattern, low):
            return domain
    return "misc"


def load_public_meta() -> dict:
    """{(owner, name): {language, stars, description, url}} from API dumps."""
    meta = {}
    data_dir = os.path.join(ROOT, "data", "repos")
    if not os.path.isdir(data_dir):
        return meta
    for fn in os.listdir(data_dir):
        if not fn.endswith(".json"):
            continue
        try:
            with open(os.path.join(data_dir, fn), encoding="utf-8") as fh:
                repos = json.load(fh)
        except Exception:
            continue
        if not isinstance(repos, list):
            continue
        for r in repos:
            owner = r.get("owner", {}).get("login", "?")
            meta[(owner, r.get("name", ""))] = {
                "language": r.get("language") or "",
                "stars": r.get("stargazers_count", 0),
                "description": (r.get("description") or "")[:120],
                "url": r.get("html_url", ""),
            }
    return meta


def main() -> int:
    meta = load_public_meta()
    rows = []
    for owner, name in REPOS:
        m = meta.get((owner, name))
        visibility = "public" if m else "private/unknown"
        rows.append({
            "owner": owner,
            "name": name,
            "url": f"https://github.com/{owner}/{name}",
            "domain": classify(name),
            "visibility": visibility,
            "language": m["language"] if m else "",
            "stars": m["stars"] if m else 0,
            "description": m["description"] if m else "",
        })

    out_csv = os.path.join(ROOT, "docs", "repo-inventory.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    domains: dict[str, list] = {}
    for r in rows:
        domains.setdefault(r["domain"], []).append(r)
    public_count = sum(1 for r in rows if r["visibility"] == "public")
    lang_stats: dict[str, int] = {}
    for r in rows:
        if r["language"]:
            lang_stats[r["language"]] = lang_stats.get(r["language"], 0) + 1

    md_lines = [
        "# Repository Inventory — 420 Repos",
        "",
        f"**Total:** {len(rows)} repositories · **Public (API-confirmed):** {public_count} "
        f"· **Private/unknown:** {len(rows) - public_count}",
        "",
        "**Owners:** onegayunicorn, PIXELATED-Pty-ltd, Shadowbyteinc. Source of record: "
        "user's Copilot session list; public metadata merged from the GitHub API "
        "(anonymous, `data/repos/*.json`).",
        "",
        "## Domain grouping (name-heuristic, for routing only)",
        "",
        "| Domain | Count | Example repos |",
        "|---|---|---|",
    ]
    for domain in sorted(domains, key=lambda d: -len(domains[d])):
        examples = ", ".join(r["name"] for r in domains[domain][:3])
        md_lines.append(f"| {domain} | {len(domains[domain])} | {examples} |")

    md_lines += [
        "",
        "## Language breakdown (public subset)",
        "",
        "| Language | Repos |",
        "|---|---|",
    ]
    for lang, n in sorted(lang_stats.items(), key=lambda x: -x[1])[:10]:
        md_lines.append(f"| {lang or '(none)'} | {n} |")
    md_lines += [
        "",
        "## Use with the platform",
        "",
        "- Full CSV: [`repo-inventory.csv`](repo-inventory.csv)",
        "- Per-repo agents/sandboxes: `packages/repo-agent` (generated on demand)",
        "- Repo adjacency matrix: `python3 -m matrix_core --mode integrate --inventory docs/repo-inventory.csv`",
    ]
    with open(os.path.join(ROOT, "docs", "repo-inventory.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md_lines) + "\n")

    print(f"inventory: {len(rows)} repos -> docs/repo-inventory.csv + .md "
          f"(public={public_count}, domains={len(domains)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
