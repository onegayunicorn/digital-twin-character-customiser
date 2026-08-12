# Trigger: ConstellationWriteTrigger

> Capability #27 — **Constellation Write**

Event source(s) that initiate execution for this capability.

### Trigger: NodeJoinTrigger

```typescript
// trigger: NodeJoinTrigger
const NodeJoinTriggerContract: TriggerContract = {
  triggerId: 'NodeJoinTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NodeJoinTrigger' },
  actionTarget: 'UpdateConstellationGraphTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: GraphUpdateTrigger

```typescript
// trigger: GraphUpdateTrigger
const GraphUpdateTriggerContract: TriggerContract = {
  triggerId: 'GraphUpdateTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for GraphUpdateTrigger' },
  actionTarget: 'UpdateConstellationGraphTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ConstellationWriteProtocol.md) · [Tasks](../tasks/ConstellationWriteTask.md) · [Workflow](../workflows/ConstellationWriteWorkflow.md)
