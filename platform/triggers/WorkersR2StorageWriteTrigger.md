# Trigger: WorkersR2StorageWriteTrigger

> Capability #17 — **Workers R2 Storage Write**

Event source(s) that initiate execution for this capability.

### Trigger: ObjectUploadedTrigger

```typescript
// trigger: ObjectUploadedTrigger
const ObjectUploadedTriggerContract: TriggerContract = {
  triggerId: 'ObjectUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ObjectUploadedTrigger' },
  actionTarget: 'UploadR2ObjectTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: BucketConfigTrigger

```typescript
// trigger: BucketConfigTrigger
const BucketConfigTriggerContract: TriggerContract = {
  triggerId: 'BucketConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for BucketConfigTrigger' },
  actionTarget: 'UploadR2ObjectTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersR2StorageWriteProtocol.md) · [Tasks](../tasks/WorkersR2StorageWriteTask.md) · [Workflow](../workflows/WorkersR2StorageWriteWorkflow.md)
