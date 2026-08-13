# Trigger: EntityRegistryTrigger

> Capability #160 — **Entity Registry**

Event source(s) that initiate execution for this capability.

### Trigger: EntityRegisteredTrigger

```typescript
// trigger: EntityRegisteredTrigger
const EntityRegisteredTriggerContract: TriggerContract = {
  triggerId: 'EntityRegisteredTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EntityRegisteredTrigger' },
  actionTarget: 'RegisterEntityTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/EntityRegistryProtocol.md) · [Tasks](../tasks/EntityRegistryTask.md) · [Workflow](../workflows/EntityRegistryWorkflow.md)
