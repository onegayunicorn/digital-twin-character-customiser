# Protocol: WorkersAiWriteProtocol

> Capability #7 — **Workers AI Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Model bindings, inference endpoints, and usage quotas for Workers AI.

## Interface contract
```typescript
// protocol: WorkersAiWriteProtocol
interface WorkersAiWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers AI Write';
  accessLevel: 'write';
  category: 'Agents & AI / Automation';
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
| Trigger(s) | [`AIInferenceRequestTrigger`](../triggers/WorkersAiWriteTrigger.md), [`ModelDeploymentTrigger`](../triggers/WorkersAiWriteTrigger.md) |
| Task(s) | [`DeployWorkersAIModelTask`](../tasks/WorkersAiWriteTask.md) |
| Workflow | [`WorkersAiWriteWorkflow`](../workflows/WorkersAiWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select model -> Bind worker -> Set limits -> Deploy endpoint
