# Trigger: TurnstileSitesWriteTrigger

> Capability #53 — **Turnstile Sites Write**

Event source(s) that initiate execution for this capability.

### Trigger: TurnstileConfigUpdatedTrigger

```typescript
// trigger: TurnstileConfigUpdatedTrigger
const TurnstileConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'TurnstileConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TurnstileConfigUpdatedTrigger' },
  actionTarget: 'ConfigureTurnstileSiteTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TurnstileSitesWriteProtocol.md) · [Tasks](../tasks/TurnstileSitesWriteTask.md) · [Workflow](../workflows/TurnstileSitesWriteWorkflow.md)
