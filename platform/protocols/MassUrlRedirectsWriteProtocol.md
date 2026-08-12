# Protocol: MassUrlRedirectsWriteProtocol

> Capability #60 — **Mass URL Redirects Write** · Domain: Security & Edge · Access: `write`

## Purpose
Bulk mappings, status codes, preserve-query, and priority for mass redirects.

## Interface contract
```typescript
// protocol: MassUrlRedirectsWriteProtocol
interface MassUrlRedirectsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Mass URL Redirects Write';
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
| Trigger(s) | [`RedirectConfigUpdatedTrigger`](../triggers/MassUrlRedirectsWriteTrigger.md), [`BulkImportTrigger`](../triggers/MassUrlRedirectsWriteTrigger.md) |
| Task(s) | [`ImportRedirectsTask`](../tasks/MassUrlRedirectsWriteTask.md) |
| Workflow | [`MassUrlRedirectsWriteWorkflow`](../workflows/MassUrlRedirectsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Import CSV -> Validate -> Deploy -> Test -> Verify
