import json
import os

from repo_agent.agent import RepoAgent, repo_agent_factory, slugify
from repo_agent.sandbox import generate_sandbox


def test_slugify():
    assert slugify("Quantum-Hub!") == "quantum-hub"
    assert slugify("---") == "repo"  # degenerate fallback


def test_repo_agent_facts():
    a = repo_agent_factory("onegayunicorn", "quantum-hub", "quantum")
    assert a.owner == "onegayunicorn"
    assert a.url == "https://github.com/onegayunicorn/quantum-hub"
    res = a.execute({"status": "inventoried"})
    assert res["repo"]["domain"] == "quantum"
    assert res["sandbox_status"] == "inventoried"
    assert "not inspected" in res["note"]


def test_sandbox_generation(tmp_path):
    d = generate_sandbox(str(tmp_path), "onegayunicorn", "Tele-OS", "teleos-os")
    assert os.path.isdir(d)
    manifest = json.loads(open(os.path.join(d, "manifest.json")).read())
    assert manifest["repo"]["name"] == "Tele-OS"
    assert manifest["status"] == "sandboxed"
    stub = open(os.path.join(d, "sim_stub.py")).read()
    assert "clinical_claim_level" in stub


def test_repo_agent_extends_sovereign():
    from sovereign.agents import BaseAgent
    assert issubclass(RepoAgent, BaseAgent)
