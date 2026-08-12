# Trigger: ZeroTrustWriteTrigger

> Capability #128 — **Zero Trust Write**

Event source(s) that initiate execution for this capability.

### Trigger: ZeroTrustConfigTrigger

```typescript
// trigger: ZeroTrustConfigTrigger
const ZeroTrustConfigTriggerContract: TriggerContract = {
  triggerId: 'ZeroTrustConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ZeroTrustConfigTrigger' },
  actionTarget: 'ConfigureZeroTrustTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ZeroTrustWriteProtocol.md) · [Tasks](../tasks/ZeroTrustWriteTask.md) · [Workflow](../workflows/ZeroTrustWriteWorkflow.md)
