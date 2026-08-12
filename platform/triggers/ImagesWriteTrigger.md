# Trigger: ImagesWriteTrigger

> Capability #80 — **Images Write**

Event source(s) that initiate execution for this capability.

### Trigger: ImageUploadedTrigger

```typescript
// trigger: ImageUploadedTrigger
const ImageUploadedTriggerContract: TriggerContract = {
  triggerId: 'ImageUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ImageUploadedTrigger' },
  actionTarget: 'UploadTransformImageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ImagesWriteProtocol.md) · [Tasks](../tasks/ImagesWriteTask.md) · [Workflow](../workflows/ImagesWriteWorkflow.md)
