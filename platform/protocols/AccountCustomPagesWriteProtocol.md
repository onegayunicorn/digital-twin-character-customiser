# Protocol: AccountCustomPagesWriteProtocol

> Capability #56 — **Account Custom Pages Write** · Domain: Security & Edge · Access: `write`

## Purpose
Error, challenge, and maintenance pages with hosting for custom pages.

## Interface contract
```typescript
// protocol: AccountCustomPagesWriteProtocol
interface AccountCustomPagesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Custom Pages Write';
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
| Trigger(s) | [`CustomPageRequestedTrigger`](../triggers/AccountCustomPagesWriteTrigger.md), [`PageUpdatedTrigger`](../triggers/AccountCustomPagesWriteTrigger.md) |
| Task(s) | [`UploadCustomPageTask`](../tasks/AccountCustomPagesWriteTask.md) |
| Workflow | [`AccountCustomPagesWriteWorkflow`](../workflows/AccountCustomPagesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Design -> Upload -> Assign -> Activate -> Verify
