# Trigger: AgentTriggerBusTrigger

> Capability #168 — **Agent Trigger Bus**

Event source(s) that initiate execution for this capability.

### Trigger: AnyPlatformEventTrigger

```typescript
// trigger: AnyPlatformEventTrigger
const AnyPlatformEventTriggerContract: TriggerContract = {
  triggerId: 'AnyPlatformEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AnyPlatformEventTrigger' },
  actionTarget: 'RouteTriggerTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AgentTriggerBusProtocol.md) · [Tasks](../tasks/AgentTriggerBusTask.md) · [Workflow](../workflows/AgentTriggerBusWorkflow.md)
