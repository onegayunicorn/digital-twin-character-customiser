# Protocol: AccessGroupsWriteProtocol

> Capability #105 — **Access: Groups Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
User grouping, dynamic criteria, and membership sync.

## Interface contract
```typescript
// protocol: AccessGroupsWriteProtocol
interface AccessGroupsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Groups Write';
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
| Trigger(s) | [`GroupMembershipChangedTrigger`](../triggers/AccessGroupsWriteTrigger.md) |
| Task(s) | [`ManageAccessGroupTask`](../tasks/AccessGroupsWriteTask.md) |
| Workflow | [`AccessGroupsWriteWorkflow`](../workflows/AccessGroupsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Add members -> Assign policies -> Sync
