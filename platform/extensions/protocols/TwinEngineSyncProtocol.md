# Protocol: TwinEngineSyncProtocol

> Capability #132 — **Twin Engine Sync** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Event-sourced digital-twin synchronization: typed event bus, versioned state store, interpolation, heartbeat staleness.

## Interface contract
```typescript
// protocol: TwinEngineSyncProtocol
interface TwinEngineSyncProtocol extends BaseOperation {
  id: string;
  name: 'Twin Engine Sync';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`TwinStateChangedTrigger (on state update)`](../triggers/TwinEngineSyncTrigger.md), [`HeartbeatTimeoutTrigger`](../triggers/TwinEngineSyncTrigger.md) |
| Task(s) | [`SyncTwinStateTask`](../tasks/TwinEngineSyncTask.md), [`DetectStaleTwinTask`](../tasks/TwinEngineSyncTask.md) |
| Workflow | [`TwinEngineSyncWorkflow`](../workflows/TwinEngineSyncWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Capture -> Version -> Broadcast -> Reconcile -> Verify
