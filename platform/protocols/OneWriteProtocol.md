# Protocol: OneWriteProtocol

> Capability #41 — **One Write** · Domain: Security & Edge · Access: `write`

## Purpose
Unified platform configuration and single-pane settings for Cloudflare One.

## Interface contract
```typescript
// protocol: OneWriteProtocol
interface OneWriteProtocol extends BaseOperation {
  id: string;
  name: 'One Write';
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
| Trigger(s) | [`OneConfigChangeTrigger`](../triggers/OneWriteTrigger.md) |
| Task(s) | [`UpdateCloudflareOneConfigTask`](../tasks/OneWriteTask.md) |
| Workflow | [`OneWriteWorkflow`](../workflows/OneWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Update -> Sync across services -> Validate -> Notify
