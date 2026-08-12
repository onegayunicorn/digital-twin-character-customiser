# Protocol: OauthClientWriteProtocol

> Capability #70 — **OAuth Client Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Client registration, redirect URIs, scopes, and secrets for OAuth clients.

## Interface contract
```typescript
// protocol: OauthClientWriteProtocol
interface OauthClientWriteProtocol extends BaseOperation {
  id: string;
  name: 'OAuth Client Write';
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
| Trigger(s) | [`OAuthClientCreatedTrigger`](../triggers/OauthClientWriteTrigger.md) |
| Task(s) | [`RegisterOAuthClientTask`](../tasks/OauthClientWriteTask.md) |
| Workflow | [`OauthClientWriteWorkflow`](../workflows/OauthClientWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Configure -> Generate secret -> Whitelist -> Activate
