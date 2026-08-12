# Protocol: ZeroTrustWriteProtocol

> Capability #128 — **Zero Trust Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Assume-breach, least-privilege, identity-centric, and micro-perimeter principles.

## Interface contract
```typescript
// protocol: ZeroTrustWriteProtocol
interface ZeroTrustWriteProtocol extends BaseOperation {
  id: string;
  name: 'Zero Trust Write';
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
| Trigger(s) | [`ZeroTrustConfigTrigger`](../triggers/ZeroTrustWriteTrigger.md) |
| Task(s) | [`ConfigureZeroTrustTask`](../tasks/ZeroTrustWriteTask.md) |
| Workflow | [`ZeroTrustWriteWorkflow`](../workflows/ZeroTrustWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Identify assets -> Classify -> Design policies -> Deploy -> Validate -> Iterate
