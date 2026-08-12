import pytest

from digital_twin import (EventBus, HeartbeatMonitor, RealtimeHub,
                          TwinStateStore, interpolate, interpolate_vec)


def test_event_bus_delivery_and_unsubscribe():
    bus = EventBus()
    got = []
    cb = lambda e: got.append(e)  # noqa: E731
    bus.subscribe("sphere.state", cb)
    assert bus.publish("sphere.state", {"charge": 0.5}) == 1
    assert got == [{"charge": 0.5}]
    bus.unsubscribe("sphere.state", cb)
    assert bus.publish("sphere.state", {"charge": 0.6}) == 0


def test_state_store_versioning():
    s = TwinStateStore()
    assert s.version("sphere") == 0
    v1 = s.set("sphere", "charge", 0.4)
    v2 = s.set("sphere", "charge", 0.7)
    assert v2 == v1 + 1
    assert s.get("sphere") == {"charge": 0.7}
    assert s.get("missing") is None


def test_interpolate_midpoint():
    assert interpolate(0.0, 1.0, 0.5) == pytest.approx(0.5)
    assert interpolate(10.0, 20.0, 0.25) == pytest.approx(12.5)
    assert interpolate(0.0, 1.0, 5.0) == 1.0  # clamped
    assert interpolate_vec([0, 0], [10, 20], 0.5) == [5.0, 10.0]


def test_heartbeat_staleness():
    m = HeartbeatMonitor(stale_after_s=5.0)
    m.beat("twin-a", 100.0)
    assert not m.is_stale("twin-a", 103.0)
    assert m.is_stale("twin-a", 106.0)
    assert m.stale_entities(106.0) == ["twin-a"]
    assert m.is_stale("never-beat", 0.0)


def test_heartbeat_backoff_grows():
    m = HeartbeatMonitor(base_delay_s=1.0)
    d0 = m.next_reconnect_delay(0, jitter=0.0)
    d2 = m.next_reconnect_delay(2, jitter=0.0)
    assert d2 == pytest.approx(4.0)
    assert d2 > d0


def test_realtime_hub_snapshot_and_late_join():
    hub = RealtimeHub()
    got = []
    hub.subscribe("ips", lambda ch, st: got.append((ch, st)))
    hub.publish("ips", {"tension": 0.3})
    assert hub.snapshot("ips") == {"tension": 0.3}
    late = []
    hub.subscribe("ips", lambda ch, st: late.append(st))
    # late joiner gets snapshot on next publish, not retroactively
    hub.publish("ips", {"tension": 0.4})
    assert len(late) == 1
    assert hub.update_count == 2
