# Trigger: SovereignKernelTrigger

> Capability #154 — **Sovereign Kernel**

Event source(s) that initiate execution for this capability.

### Trigger: PrimitiveAttachedTrigger

```typescript
// trigger: PrimitiveAttachedTrigger
const PrimitiveAttachedTriggerContract: TriggerContract = {
  triggerId: 'PrimitiveAttachedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PrimitiveAttachedTrigger' },
  actionTarget: 'RegisterPrimitiveTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/SovereignKernelProtocol.md) · [Tasks](../tasks/SovereignKernelTask.md) · [Workflow](../workflows/SovereignKernelWorkflow.md)
