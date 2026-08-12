# Trigger: WorkersKvStorageWriteTrigger

> Capability #16 — **Workers KV Storage Write**

Event source(s) that initiate execution for this capability.

### Trigger: KVKeyWrittenTrigger

```typescript
// trigger: KVKeyWrittenTrigger
const KVKeyWrittenTriggerContract: TriggerContract = {
  triggerId: 'KVKeyWrittenTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for KVKeyWrittenTrigger' },
  actionTarget: 'WriteKVEntryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: KVExpiryTrigger

```typescript
// trigger: KVExpiryTrigger
const KVExpiryTriggerContract: TriggerContract = {
  triggerId: 'KVExpiryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for KVExpiryTrigger' },
  actionTarget: 'WriteKVEntryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersKvStorageWriteProtocol.md) · [Tasks](../tasks/WorkersKvStorageWriteTask.md) · [Workflow](../workflows/WorkersKvStorageWriteWorkflow.md)
