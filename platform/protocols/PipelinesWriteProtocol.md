# Protocol: PipelinesWriteProtocol

> Capability #12 — **Pipelines Write** · Domain: Workers, Compute & Code · Access: `write`

## Purpose
Data pipeline definitions, transforms, sinks, and sources.

## Interface contract
```typescript
// protocol: PipelinesWriteProtocol
interface PipelinesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Pipelines Write';
  accessLevel: 'write';
  category: 'Workers, Compute & Code';
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
| Trigger(s) | [`PipelineEventTrigger`](../triggers/PipelinesWriteTrigger.md), [`SchedulePipelineTrigger`](../triggers/PipelinesWriteTrigger.md) |
| Task(s) | [`ManagePipelineTask`](../tasks/PipelinesWriteTask.md) |
| Workflow | [`PipelinesWriteWorkflow`](../workflows/PipelinesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define schema -> Build stages -> Connect sources/sinks -> Activate
