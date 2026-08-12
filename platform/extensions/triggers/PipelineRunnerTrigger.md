# Trigger: PipelineRunnerTrigger

> Capability #153 — **Pipeline Runner**

Event source(s) that initiate execution for this capability.

### Trigger: PipelineSubmittedTrigger

```typescript
// trigger: PipelineSubmittedTrigger
const PipelineSubmittedTriggerContract: TriggerContract = {
  triggerId: 'PipelineSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PipelineSubmittedTrigger' },
  actionTarget: 'ExecutePipelineTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/PipelineRunnerProtocol.md) · [Tasks](../tasks/PipelineRunnerTask.md) · [Workflow](../workflows/PipelineRunnerWorkflow.md)
