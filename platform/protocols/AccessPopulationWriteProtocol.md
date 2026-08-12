# Protocol: AccessPopulationWriteProtocol

> Capability #112 — **Access: Population Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
User directory, scope, sync, and filters for populations.

## Interface contract
```typescript
// protocol: AccessPopulationWriteProtocol
interface AccessPopulationWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Population Write';
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
| Trigger(s) | [`PopulationUpdatedTrigger`](../triggers/AccessPopulationWriteTrigger.md) |
| Task(s) | [`ManageAccessPopulationTask`](../tasks/AccessPopulationWriteTask.md) |
| Workflow | [`AccessPopulationWriteWorkflow`](../workflows/AccessPopulationWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Sync source -> Filter -> Store -> Update policies
