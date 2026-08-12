# Trigger: WebsearchWriteTrigger

> Capability #6 — **Websearch Write**

Event source(s) that initiate execution for this capability.

### Trigger: SearchConfigUpdatedTrigger

```typescript
// trigger: SearchConfigUpdatedTrigger
const SearchConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'SearchConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SearchConfigUpdatedTrigger' },
  actionTarget: 'UpdateWebsearchConfigTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WebsearchWriteProtocol.md) · [Tasks](../tasks/WebsearchWriteTask.md) · [Workflow](../workflows/WebsearchWriteWorkflow.md)
