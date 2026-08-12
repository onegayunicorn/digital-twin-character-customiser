# Protocol: TagWriteProtocol

> Capability #51 — **Tag Write** · Domain: Security & Edge · Access: `write`

## Purpose
Resource tagging, taxonomy, and policy-based assignment.

## Interface contract
```typescript
// protocol: TagWriteProtocol
interface TagWriteProtocol extends BaseOperation {
  id: string;
  name: 'Tag Write';
  accessLevel: 'write';
  category: 'Security & Edge';
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
| Trigger(s) | [`TagAddedTrigger`](../triggers/TagWriteTrigger.md), [`TagUpdatedTrigger`](../triggers/TagWriteTrigger.md) |
| Task(s) | [`ApplyResourceTagTask`](../tasks/TagWriteTask.md) |
| Workflow | [`TagWriteWorkflow`](../workflows/TagWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define taxonomy -> Assign -> Propagate -> Enforce policies
