# Trigger: DexWriteTrigger

> Capability #127 — **DEX Write**

Event source(s) that initiate execution for this capability.

### Trigger: DEXTestTrigger

```typescript
// trigger: DEXTestTrigger
const DEXTestTriggerContract: TriggerContract = {
  triggerId: 'DEXTestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DEXTestTrigger' },
  actionTarget: 'ConfigureDEXTestTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DexWriteProtocol.md) · [Tasks](../tasks/DexWriteTask.md) · [Workflow](../workflows/DexWriteWorkflow.md)
