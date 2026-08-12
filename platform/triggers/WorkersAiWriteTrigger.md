# Trigger: WorkersAiWriteTrigger

> Capability #7 — **Workers AI Write**

Event source(s) that initiate execution for this capability.

### Trigger: AIInferenceRequestTrigger

```typescript
// trigger: AIInferenceRequestTrigger
const AIInferenceRequestTriggerContract: TriggerContract = {
  triggerId: 'AIInferenceRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AIInferenceRequestTrigger' },
  actionTarget: 'DeployWorkersAIModelTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ModelDeploymentTrigger

```typescript
// trigger: ModelDeploymentTrigger
const ModelDeploymentTriggerContract: TriggerContract = {
  triggerId: 'ModelDeploymentTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ModelDeploymentTrigger' },
  actionTarget: 'DeployWorkersAIModelTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersAiWriteProtocol.md) · [Tasks](../tasks/WorkersAiWriteTask.md) · [Workflow](../workflows/WorkersAiWriteWorkflow.md)
