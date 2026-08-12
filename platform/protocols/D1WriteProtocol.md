# Protocol: D1WriteProtocol

> Capability #15 — **D1 Write** · Domain: Storage & Data · Access: `write`

## Purpose
SQL schema, migrations, query patterns, and access controls for D1.

## Interface contract
```typescript
// protocol: D1WriteProtocol
interface D1WriteProtocol extends BaseOperation {
  id: string;
  name: 'D1 Write';
  accessLevel: 'write';
  category: 'Storage & Data';
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
| Trigger(s) | [`MigrationTrigger`](../triggers/D1WriteTrigger.md), [`WriteQueryTrigger`](../triggers/D1WriteTrigger.md) |
| Task(s) | [`ExecuteD1QueryTask`](../tasks/D1WriteTask.md), [`RunD1MigrationTask`](../tasks/D1WriteTask.md) |
| Workflow | [`D1WriteWorkflow`](../workflows/D1WriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate SQL -> Backup -> Apply migration -> Verify
