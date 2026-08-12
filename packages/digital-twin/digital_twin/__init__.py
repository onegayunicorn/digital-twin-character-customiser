"""Twin-engine core (stdlib-only) for the Invisible Pressure Platform.

Provides the event-sourced synchronization layer used by the Twin-State
dashboard, VRmemories scenes, and IPS fleet twins:

  EventBus        - typed pub/sub
  TwinStateStore  - versioned entity state
  interpolate     - linear state interpolation (late-join smoothing)
  HeartbeatMonitor- staleness detection + reconnect signal
  RealtimeHub     - in-process broadcast with late-join snapshots
"""
from .event_bus import EventBus
from .state_store import TwinStateStore
from .interpolation import interpolate, interpolate_vec
from .heartbeat import HeartbeatMonitor
from .hub import RealtimeHub

__all__ = ["EventBus", "TwinStateStore", "interpolate", "interpolate_vec",
           "HeartbeatMonitor", "RealtimeHub"]
