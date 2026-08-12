# Trigger: LogsWriteTrigger

> Capability #95 — **Logs Write**

Event source(s) that initiate execution for this capability.

### Trigger: LogConfigUpdatedTrigger

```typescript
// trigger: LogConfigUpdatedTrigger
const LogConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'LogConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for LogConfigUpdatedTrigger' },
  actionTarget: 'ConfigureLogpushTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/LogsWriteProtocol.md) · [Tasks](../tasks/LogsWriteTask.md) · [Workflow](../workflows/LogsWriteWorkflow.md)
