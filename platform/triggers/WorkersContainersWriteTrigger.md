# Trigger: WorkersContainersWriteTrigger

> Capability #9 — **Workers Containers Write**

Event source(s) that initiate execution for this capability.

### Trigger: ContainerImagePushedTrigger

```typescript
// trigger: ContainerImagePushedTrigger
const ContainerImagePushedTriggerContract: TriggerContract = {
  triggerId: 'ContainerImagePushedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ContainerImagePushedTrigger' },
  actionTarget: 'DeployWorkerContainerTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScaleEventTrigger

```typescript
// trigger: ScaleEventTrigger
const ScaleEventTriggerContract: TriggerContract = {
  triggerId: 'ScaleEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScaleEventTrigger' },
  actionTarget: 'DeployWorkerContainerTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersContainersWriteProtocol.md) · [Tasks](../tasks/WorkersContainersWriteTask.md) · [Workflow](../workflows/WorkersContainersWriteWorkflow.md)
