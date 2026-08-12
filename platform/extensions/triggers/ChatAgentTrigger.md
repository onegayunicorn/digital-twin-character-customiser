# Trigger: ChatAgentTrigger

> Capability #148 — **Chat Agent**

Event source(s) that initiate execution for this capability.

### Trigger: MessageReceivedTrigger

```typescript
// trigger: MessageReceivedTrigger
const MessageReceivedTriggerContract: TriggerContract = {
  triggerId: 'MessageReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MessageReceivedTrigger' },
  actionTarget: 'RouteIntentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ChatAgentProtocol.md) · [Tasks](../tasks/ChatAgentTask.md) · [Workflow](../workflows/ChatAgentWorkflow.md)
