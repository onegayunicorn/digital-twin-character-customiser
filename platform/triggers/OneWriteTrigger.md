# Trigger: OneWriteTrigger

> Capability #41 — **One Write**

Event source(s) that initiate execution for this capability.

### Trigger: OneConfigChangeTrigger

```typescript
// trigger: OneConfigChangeTrigger
const OneConfigChangeTriggerContract: TriggerContract = {
  triggerId: 'OneConfigChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OneConfigChangeTrigger' },
  actionTarget: 'UpdateCloudflareOneConfigTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OneWriteProtocol.md) · [Tasks](../tasks/OneWriteTask.md) · [Workflow](../workflows/OneWriteWorkflow.md)
