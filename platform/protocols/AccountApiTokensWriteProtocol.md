# Protocol: AccountApiTokensWriteProtocol

> Capability #64 — **Account API Tokens Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Token creation, scopes, expiry, rotation, and revocation.

## Interface contract
```typescript
// protocol: AccountApiTokensWriteProtocol
interface AccountApiTokensWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account API Tokens Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`TokenCreatedTrigger`](../triggers/AccountApiTokensWriteTrigger.md), [`TokenExpiryTrigger`](../triggers/AccountApiTokensWriteTrigger.md) |
| Task(s) | [`IssueAPITokenTask`](../tasks/AccountApiTokensWriteTask.md), [`RevokeAPITokenTask`](../tasks/AccountApiTokensWriteTask.md) |
| Workflow | [`AccountApiTokensWriteWorkflow`](../workflows/AccountApiTokensWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Request -> Scope -> Create -> Issue -> Rotate -> Revoke
