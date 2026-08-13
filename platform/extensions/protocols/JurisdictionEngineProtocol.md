# Protocol: JurisdictionEngineProtocol

> Capability #155 — **Jurisdiction Engine** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Six-dimension jurisdiction classification (user/entity/transaction/asset/service/data) -> regulatory profile -> policy check.

## Interface contract
```typescript
// protocol: JurisdictionEngineProtocol
interface JurisdictionEngineProtocol extends BaseOperation {
  id: string;
  name: 'Jurisdiction Engine';
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
| Trigger(s) | [`TransactionSubmittedTrigger`](../triggers/JurisdictionEngineTrigger.md) |
| Task(s) | [`ClassifyJurisdictionTask`](../tasks/JurisdictionEngineTask.md), [`ResolveProfileTask`](../tasks/JurisdictionEngineTask.md) |
| Workflow | [`JurisdictionEngineWorkflow`](../workflows/JurisdictionEngineWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Classify -> Profile -> Check -> Warn -> Report
