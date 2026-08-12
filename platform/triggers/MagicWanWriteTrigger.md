# Trigger: MagicWanWriteTrigger

> Capability #93 — **Magic WAN Write**

Event source(s) that initiate execution for this capability.

### Trigger: WANConnectionTrigger

```typescript
// trigger: WANConnectionTrigger
const WANConnectionTriggerContract: TriggerContract = {
  triggerId: 'WANConnectionTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WANConnectionTrigger' },
  actionTarget: 'ConfigureMagicWANTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MagicWanWriteProtocol.md) · [Tasks](../tasks/MagicWanWriteTask.md) · [Workflow](../workflows/MagicWanWriteWorkflow.md)
