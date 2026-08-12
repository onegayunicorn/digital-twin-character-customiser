# Protocol: ConstellationWriteProtocol

> Capability #27 — **Constellation Write** · Domain: Observability & Telemetry · Access: `write`

## Purpose
Distributed graph nodes, edges, discovery, and state sync for Constellation.

## Interface contract
```typescript
// protocol: ConstellationWriteProtocol
interface ConstellationWriteProtocol extends BaseOperation {
  id: string;
  name: 'Constellation Write';
  accessLevel: 'write';
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
| Trigger(s) | [`NodeJoinTrigger`](../triggers/ConstellationWriteTrigger.md), [`GraphUpdateTrigger`](../triggers/ConstellationWriteTrigger.md) |
| Task(s) | [`UpdateConstellationGraphTask`](../tasks/ConstellationWriteTask.md) |
| Workflow | [`ConstellationWriteWorkflow`](../workflows/ConstellationWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register node -> Sync state -> Reconcile -> Broadcast
