# Protocol: PipelineRunnerProtocol

> Capability #153 — **Pipeline Runner** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Declarative pipelines: ordered steps referencing queue tasks with dependency gating and audit.

## Interface contract
```typescript
// protocol: PipelineRunnerProtocol
interface PipelineRunnerProtocol extends BaseOperation {
  id: string;
  name: 'Pipeline Runner';
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
| Trigger(s) | [`PipelineSubmittedTrigger`](../triggers/PipelineRunnerTrigger.md) |
| Task(s) | [`ExecutePipelineTask`](../tasks/PipelineRunnerTask.md), [`GateDependenciesTask`](../tasks/PipelineRunnerTask.md) |
| Workflow | [`PipelineRunnerWorkflow`](../workflows/PipelineRunnerWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Enqueue steps -> Dispatch -> Audit -> Report
