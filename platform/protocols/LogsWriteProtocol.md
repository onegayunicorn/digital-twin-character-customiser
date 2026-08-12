# Protocol: LogsWriteProtocol

> Capability #95 — **Logs Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Log retention, sampling, destinations, fields, and exports.

## Interface contract
```typescript
// protocol: LogsWriteProtocol
interface LogsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Logs Write';
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
| Trigger(s) | [`LogConfigUpdatedTrigger`](../triggers/LogsWriteTrigger.md) |
| Task(s) | [`ConfigureLogpushTask`](../tasks/LogsWriteTask.md) |
| Workflow | [`LogsWriteWorkflow`](../workflows/LogsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select fields -> Set destination -> Enable -> Verify delivery
