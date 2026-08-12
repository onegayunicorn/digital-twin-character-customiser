# Protocol: WorkersR2SqlReadProtocol

> Capability #18 — **Workers R2 SQL Read** · Domain: Storage & Data · Access: `read`

## Purpose
Query syntax, catalog mapping, permissions, and pagination for R2 SQL.

## Interface contract
```typescript
// protocol: WorkersR2SqlReadProtocol
interface WorkersR2SqlReadProtocol extends BaseOperation {
  id: string;
  name: 'Workers R2 SQL Read';
  accessLevel: 'read';
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
| Trigger(s) | [`R2SQLQueryTrigger`](../triggers/WorkersR2SqlReadTrigger.md) |
| Task(s) | [`ExecuteR2SQLQueryTask`](../tasks/WorkersR2SqlReadTask.md) |
| Workflow | [`WorkersR2SqlReadWorkflow`](../workflows/WorkersR2SqlReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Auth -> Parse -> Plan -> Execute -> Return results
