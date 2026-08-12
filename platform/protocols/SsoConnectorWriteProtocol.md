# Protocol: SsoConnectorWriteProtocol

> Capability #72 — **SSO Connector Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
SAML/OIDC, IdP configuration, claims mapping, and sign-on URL.

## Interface contract
```typescript
// protocol: SsoConnectorWriteProtocol
interface SsoConnectorWriteProtocol extends BaseOperation {
  id: string;
  name: 'SSO Connector Write';
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
| Trigger(s) | [`SSOConfigUpdatedTrigger`](../triggers/SsoConnectorWriteTrigger.md) |
| Task(s) | [`ConfigureSSOConnectorTask`](../tasks/SsoConnectorWriteTask.md) |
| Workflow | [`SsoConnectorWriteWorkflow`](../workflows/SsoConnectorWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Upload metadata -> Map claims -> Test -> Enable
