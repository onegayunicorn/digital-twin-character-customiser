import pytest

from sovereign.agents import AgentFactory
from sovereign.pipelines import PipelineRunner
from sovereign.queue import TaskQueue


def _agents():
    agents = {r: AgentFactory.create(r, r) for r in ("reasoner", "coder")}
    for a in agents.values():
        a.transition("ready")
    return agents


def test_pipeline_executes_ordered_steps():
    q = TaskQueue()
    agents = _agents()
    runner = PipelineRunner(q, agents)
    res = runner.run_pipeline({
        "id": "p1",
        "steps": [
            {"id": "s1", "task": {"prompt": "analyze"}, "priority": 0},
            {"id": "s2", "task": {"prompt": "code"}, "priority": 1,
             "depends_on": ["s1"]},
        ],
    })
    assert res["status"] == "complete"
    assert res["steps"]["s1"]["status"] == "done"
    assert res["steps"]["s2"]["status"] == "done"


def test_pipeline_skips_on_missing_dependency():
    q = TaskQueue()
    agents = _agents()
    runner = PipelineRunner(q, agents)
    res = runner.run_pipeline({
        "id": "p2",
        "steps": [
            {"id": "s2", "task": {"prompt": "x"}, "depends_on": ["s1"]},
        ],
    })
    assert res["steps"]["s2"]["status"] == "skipped"
