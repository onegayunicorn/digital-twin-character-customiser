# Protocol: AccessScimLogsReadProtocol

> Capability #115 — **Access: SCIM Logs Read** · Domain: Access & Zero Trust · Access: `read`

## Purpose
Sync events, errors, user changes, and timestamps for SCIM logs.

## Interface contract
```typescript
// protocol: AccessScimLogsReadProtocol
interface AccessScimLogsReadProtocol extends BaseOperation {
  id: string;
  name: 'Access: SCIM Logs Read';
  accessLevel: 'read';
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
| Trigger(s) | [`SCIMSyncCompletedTrigger`](../triggers/AccessScimLogsReadTrigger.md) |
| Task(s) | [`ReadSCIMLogTask`](../tasks/AccessScimLogsReadTask.md) |
| Workflow | [`AccessScimLogsReadWorkflow`](../workflows/AccessScimLogsReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Collect -> Review -> Troubleshoot -> Report
