# Protocol: AccessIdentityProvidersWriteProtocol

> Capability #104 — **Access: Identity Providers Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
SAML/OIDC, SCIM, authentication methods, and attribute mapping for IdPs.

## Interface contract
```typescript
// protocol: AccessIdentityProvidersWriteProtocol
interface AccessIdentityProvidersWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Identity Providers Write';
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
| Trigger(s) | [`IdPConfigUpdatedTrigger`](../triggers/AccessIdentityProvidersWriteTrigger.md) |
| Task(s) | [`RegisterIdentityProviderTask`](../tasks/AccessIdentityProvidersWriteTask.md) |
| Workflow | [`AccessIdentityProvidersWriteWorkflow`](../workflows/AccessIdentityProvidersWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Configure -> Map attributes -> Test -> Enable
