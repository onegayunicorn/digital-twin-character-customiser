import pytest

from bridge.registry import BridgeRegistry


def _echo(**kw):
    return {"echo": kw}


def test_register_and_route():
    b = BridgeRegistry()
    b.register("medgen", "dmd_repair", _echo)
    route = b.route("dmd_repair")
    assert route["module"] == "medgen"
    assert b.call("dmd_repair", x=1) == {"echo": {"x": 1}}


def test_unknown_capability_raises():
    b = BridgeRegistry()
    with pytest.raises(KeyError):
        b.route("nope")


def test_health_report():
    b = BridgeRegistry()
    b.register("sonar-5d", "crystal_mesh", _echo)
    b.register("genesis", "optimizer", _echo)
    h = b.health()
    assert h["capabilities"] == 2
    assert set(h["modules"]) == {"sonar-5d", "genesis"}


def test_handshake_via_sovereign():
    b = BridgeRegistry()
    ack = b.handshake.hello("bridge-1", "bridge")
    assert ack["ack"] == "ok"
    assert b.handshake.beat("bridge-1", ack["token"])
