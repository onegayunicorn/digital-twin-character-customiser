# Trigger: PipelinesWriteTrigger

> Capability #12 — **Pipelines Write**

Event source(s) that initiate execution for this capability.

### Trigger: PipelineEventTrigger

```typescript
// trigger: PipelineEventTrigger
const PipelineEventTriggerContract: TriggerContract = {
  triggerId: 'PipelineEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PipelineEventTrigger' },
  actionTarget: 'ManagePipelineTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SchedulePipelineTrigger

```typescript
// trigger: SchedulePipelineTrigger
const SchedulePipelineTriggerContract: TriggerContract = {
  triggerId: 'SchedulePipelineTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SchedulePipelineTrigger' },
  actionTarget: 'ManagePipelineTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/PipelinesWriteProtocol.md) · [Tasks](../tasks/PipelinesWriteTask.md) · [Workflow](../workflows/PipelinesWriteWorkflow.md)
