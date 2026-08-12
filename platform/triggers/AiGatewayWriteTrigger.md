# Trigger: AiGatewayWriteTrigger

> Capability #3 — **AI Gateway Write**

Event source(s) that initiate execution for this capability.

### Trigger: AIRequestReceivedTrigger

```typescript
// trigger: AIRequestReceivedTrigger
const AIRequestReceivedTriggerContract: TriggerContract = {
  triggerId: 'AIRequestReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AIRequestReceivedTrigger' },
  actionTarget: 'ConfigureAIGatewayTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AIMetricThresholdTrigger

```typescript
// trigger: AIMetricThresholdTrigger
const AIMetricThresholdTriggerContract: TriggerContract = {
  triggerId: 'AIMetricThresholdTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AIMetricThresholdTrigger' },
  actionTarget: 'ConfigureAIGatewayTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AiGatewayWriteProtocol.md) · [Tasks](../tasks/AiGatewayWriteTask.md) · [Workflow](../workflows/AiGatewayWriteWorkflow.md)
