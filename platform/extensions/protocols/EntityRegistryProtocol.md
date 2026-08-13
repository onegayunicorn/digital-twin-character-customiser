# Protocol: EntityRegistryProtocol

> Capability #160 — **Entity Registry** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Legal entity registry (person..DAO), beneficial ownership, governance requirements per entity type.

## Interface contract
```typescript
// protocol: EntityRegistryProtocol
interface EntityRegistryProtocol extends BaseOperation {
  id: string;
  name: 'Entity Registry';
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
| Trigger(s) | [`EntityRegisteredTrigger`](../triggers/EntityRegistryTrigger.md) |
| Task(s) | [`RegisterEntityTask`](../tasks/EntityRegistryTask.md), [`AddBeneficialOwnerTask`](../tasks/EntityRegistryTask.md) |
| Workflow | [`EntityRegistryWorkflow`](../workflows/EntityRegistryWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Verify type -> Ownership -> Governance -> Report
