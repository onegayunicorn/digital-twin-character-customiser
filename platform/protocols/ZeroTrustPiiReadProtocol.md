# Protocol: ZeroTrustPiiReadProtocol

> Capability #131 — **Zero Trust: PII Read** · Domain: Access & Zero Trust · Access: `read`

## Purpose
PII access, minimization, consent, export, and deletion.

## Interface contract
```typescript
// protocol: ZeroTrustPiiReadProtocol
interface ZeroTrustPiiReadProtocol extends BaseOperation {
  id: string;
  name: 'Zero Trust: PII Read';
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
| Trigger(s) | [`PIIAccessRequestTrigger`](../triggers/ZeroTrustPiiReadTrigger.md) |
| Task(s) | [`ReadZeroTrustPIITask`](../tasks/ZeroTrustPiiReadTask.md) |
| Workflow | [`ZeroTrustPiiReadWorkflow`](../workflows/ZeroTrustPiiReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Request -> Auth -> Minimize -> Access -> Export/Delete -> Audit
