# Trigger: MtCommunionCliTrigger

> Capability #134 — **MT Communion CLI**

Event source(s) that initiate execution for this capability.

### Trigger: IntentReceivedTrigger

```typescript
// trigger: IntentReceivedTrigger
const IntentReceivedTriggerContract: TriggerContract = {
  triggerId: 'IntentReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IntentReceivedTrigger' },
  actionTarget: 'RouteIntentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MtCommunionCliProtocol.md) · [Tasks](../tasks/MtCommunionCliTask.md) · [Workflow](../workflows/MtCommunionCliWorkflow.md)
