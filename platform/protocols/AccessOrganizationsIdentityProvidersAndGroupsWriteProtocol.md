# Protocol: AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol

> Capability #109 — **Access: Organizations, Identity Providers, and Groups Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Unified provisioning, relationships, and mappings across org, IdP, and groups.

## Interface contract
```typescript
// protocol: AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol
interface AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Organizations, Identity Providers, and Groups Write';
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
| Trigger(s) | [`OrgStructureUpdatedTrigger`](../triggers/AccessOrganizationsIdentityProvidersAndGroupsWriteTrigger.md) |
| Task(s) | [`SyncOrgIdPGroupTask`](../tasks/AccessOrganizationsIdentityProvidersAndGroupsWriteTask.md) |
| Workflow | [`AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow`](../workflows/AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Sync IdP -> Map groups -> Assign org -> Provision users
