# Protocol: WatcherProtocol

> Capability #146 — **Watcher** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Health monitoring: heartbeat staleness, spec integrity counts, test status; flags attention items.

## Interface contract
```typescript
// protocol: WatcherProtocol
interface WatcherProtocol extends BaseOperation {
  id: string;
  name: 'Watcher';
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
| Trigger(s) | [`HealthCheckTrigger`](../triggers/WatcherTrigger.md), [`SpecDriftTrigger`](../triggers/WatcherTrigger.md) |
| Task(s) | [`ScanHeartbeatsTask`](../tasks/WatcherTask.md), [`VerifySpecCountsTask`](../tasks/WatcherTask.md) |
| Workflow | [`WatcherWorkflow`](../workflows/WatcherWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Collect -> Compare -> Flag -> Report
