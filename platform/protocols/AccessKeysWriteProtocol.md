# Protocol: AccessKeysWriteProtocol

> Capability #106 — **Access: Keys Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Service auth keys, expiry, scope, and revocation.

## Interface contract
```typescript
// protocol: AccessKeysWriteProtocol
interface AccessKeysWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Keys Write';
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
| Trigger(s) | [`AccessKeyCreatedTrigger`](../triggers/AccessKeysWriteTrigger.md) |
| Task(s) | [`ManageAccessKeyTask`](../tasks/AccessKeysWriteTask.md) |
| Workflow | [`AccessKeysWriteWorkflow`](../workflows/AccessKeysWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Scope -> Distribute -> Rotate -> Revoke
