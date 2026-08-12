import json

import pytest

from ipai_cli.router import TransceivingRouter, resonance_pulse
from ipai_cli.sentiment import sentiment_score
from ipai_cli.twin import mirror_twin_reply, sentiment_key


def test_sentiment_positive_negative():
    assert sentiment_score("joy fairness hope bloom") > 0.5
    assert sentiment_score("sorrow ache shadow void") < -0.5
    assert sentiment_score("the bind holds steady") == pytest.approx(0.0, abs=0.3)


def test_sentiment_deterministic():
    a = sentiment_score("weave the fair stand")
    b = sentiment_score("weave the fair stand")
    assert a == b


def test_router_evolves_frequency_with_emotion():
    r = TransceivingRouter()
    e_pos, f_pos = r.route_intent("joy fairness hope")
    r2 = TransceivingRouter()
    e_neg, f_neg = r2.route_intent("sorrow ache shadow")
    assert e_pos > 0 and e_neg < 0
    # positive emotion raises the evolved twin freq above the negative case
    assert f_pos > 1.0
    assert f_pos > f_neg


def test_router_cells_store_engrams():
    r = TransceivingRouter()
    r.route_intent("birth equity from light")
    for cell in r.cells.values():
        assert cell.retrieve_engram() is not None
        assert "emotion" in cell.retrieve_engram()


def test_resonance_pulse_bounds():
    assert resonance_pulse(1.0) == pytest.approx(1.0)
    assert resonance_pulse(-1.0) == pytest.approx(0.0)
    assert resonance_pulse(0.0) == pytest.approx(0.5)


def test_mirror_twin_reply_keys():
    assert sentiment_key(0.8) == "joy"
    assert sentiment_key(-0.8) == "sorrow"
    assert sentiment_key(0.1) == "neutral"
    reply = mirror_twin_reply(0.8, 1.08, 0.9)
    assert "Resonance pulse" in reply


def test_cli_engram_persist(tmp_path):
    from ipai_cli.__main__ import main
    out = tmp_path / "engram.json"
    rc = main(["--intent", "birth equity from light", "--persist", str(out), "--quiet"])
    assert rc == 0
    data = json.loads(out.read_text())
    assert data["intent"] == "birth equity from light"
    assert "cells" in data and "resonance" in data["cells"]
