# Protocol: AccessCustomPagesWriteProtocol

> Capability #103 — **Access: Custom Pages Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Login, denied, error, and consent pages with branding.

## Interface contract
```typescript
// protocol: AccessCustomPagesWriteProtocol
interface AccessCustomPagesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Custom Pages Write';
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
| Trigger(s) | [`AccessPageRequestedTrigger`](../triggers/AccessCustomPagesWriteTrigger.md) |
| Task(s) | [`UploadAccessCustomPageTask`](../tasks/AccessCustomPagesWriteTask.md) |
| Workflow | [`AccessCustomPagesWriteWorkflow`](../workflows/AccessCustomPagesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Design -> Upload -> Assign -> Activate
