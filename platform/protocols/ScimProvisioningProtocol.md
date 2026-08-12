# Protocol: ScimProvisioningProtocol

> Capability #71 — **SCIM Provisioning** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
User/group sync, provisioning, deprovisioning, and attributes via SCIM.

## Interface contract
```typescript
// protocol: ScimProvisioningProtocol
interface ScimProvisioningProtocol extends BaseOperation {
  id: string;
  name: 'SCIM Provisioning';
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
| Trigger(s) | [`SCIMSyncTrigger`](../triggers/ScimProvisioningTrigger.md), [`IdentityProviderTrigger`](../triggers/ScimProvisioningTrigger.md) |
| Task(s) | [`ProvisionSCIMResourceTask`](../tasks/ScimProvisioningTask.md) |
| Workflow | [`ScimProvisioningWorkflow`](../workflows/ScimProvisioningWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Pull from IdP -> Map -> Create/Update -> Deprovision -> Report
