# Protocol: AccessTagsWriteProtocol

> Capability #117 — **Access: Tags Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Resource tagging, policy-based, and RBAC grouping for Access tags.

## Interface contract
```typescript
// protocol: AccessTagsWriteProtocol
interface AccessTagsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Tags Write';
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
| Trigger(s) | [`AccessTagUpdatedTrigger`](../triggers/AccessTagsWriteTrigger.md) |
| Task(s) | [`ApplyAccessTagTask`](../tasks/AccessTagsWriteTask.md) |
| Workflow | [`AccessTagsWriteWorkflow`](../workflows/AccessTagsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define -> Assign -> Enforce -> Report
