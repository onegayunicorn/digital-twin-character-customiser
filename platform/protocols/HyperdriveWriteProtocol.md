# Protocol: HyperdriveWriteProtocol

> Capability #11 — **Hyperdrive Write** · Domain: Workers, Compute & Code · Access: `write`

## Purpose
Origin configuration, connection pooling, caching rules, and timeouts for Hyperdrive.

## Interface contract
```typescript
// protocol: HyperdriveWriteProtocol
interface HyperdriveWriteProtocol extends BaseOperation {
  id: string;
  name: 'Hyperdrive Write';
  accessLevel: 'write';
  category: 'Workers, Compute & Code';
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
| Trigger(s) | [`HyperdriveConfigUpdatedTrigger`](../triggers/HyperdriveWriteTrigger.md) |
| Task(s) | [`ConfigureHyperdriveTask`](../tasks/HyperdriveWriteTask.md) |
| Workflow | [`HyperdriveWriteWorkflow`](../workflows/HyperdriveWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register origin -> Set pool -> Apply caching -> Test connectivity
