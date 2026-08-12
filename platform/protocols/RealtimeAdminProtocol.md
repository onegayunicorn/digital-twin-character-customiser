# Protocol: RealtimeAdminProtocol

> Capability #26 — **Realtime Admin** · Domain: Observability & Telemetry · Access: `admin`

## Purpose
Presence, rooms, connections, events, and auth for realtime sessions.

## Interface contract
```typescript
// protocol: RealtimeAdminProtocol
interface RealtimeAdminProtocol extends BaseOperation {
  id: string;
  name: 'Realtime Admin';
  accessLevel: 'admin';
  category: 'Observability & Telemetry';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`ClientConnectedTrigger`](../triggers/RealtimeAdminTrigger.md), [`RoomEventTrigger`](../triggers/RealtimeAdminTrigger.md) |
| Task(s) | [`ManageRealtimeSessionTask`](../tasks/RealtimeAdminTask.md) |
| Workflow | [`RealtimeAdminWorkflow`](../workflows/RealtimeAdminWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Auth -> Join room -> Broadcast -> Monitor -> Disconnect
