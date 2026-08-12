# Protocol: AccessServiceTokensWriteProtocol

> Capability #114 — **Access: Service Tokens Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Non-human authentication, scoped, expiry, and rotation for service tokens.

## Interface contract
```typescript
// protocol: AccessServiceTokensWriteProtocol
interface AccessServiceTokensWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Service Tokens Write';
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
| Trigger(s) | [`ServiceTokenCreatedTrigger`](../triggers/AccessServiceTokensWriteTrigger.md) |
| Task(s) | [`IssueServiceTokenTask`](../tasks/AccessServiceTokensWriteTask.md) |
| Workflow | [`AccessServiceTokensWriteWorkflow`](../workflows/AccessServiceTokensWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Scope -> Issue -> Rotate -> Revoke
