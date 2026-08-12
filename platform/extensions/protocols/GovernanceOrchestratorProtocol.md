# Protocol: GovernanceOrchestratorProtocol

> Capability #144 — **Governance Orchestrator** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Dispatch-coordination agent: routes task batches to agents by role with audit logging.

## Interface contract
```typescript
// protocol: GovernanceOrchestratorProtocol
interface GovernanceOrchestratorProtocol extends BaseOperation {
  id: string;
  name: 'Governance Orchestrator';
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
| Trigger(s) | [`BatchReceivedTrigger`](../triggers/GovernanceOrchestratorTrigger.md) |
| Task(s) | [`RouteBatchTask`](../tasks/GovernanceOrchestratorTask.md), [`LogDispatchTask`](../tasks/GovernanceOrchestratorTask.md) |
| Workflow | [`GovernanceOrchestratorWorkflow`](../workflows/GovernanceOrchestratorWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Ingest -> Route -> Dispatch -> Audit
