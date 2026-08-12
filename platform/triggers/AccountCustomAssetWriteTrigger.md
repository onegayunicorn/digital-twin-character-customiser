# Trigger: AccountCustomAssetWriteTrigger

> Capability #65 — **Account Custom Asset Write**

Event source(s) that initiate execution for this capability.

### Trigger: AssetUploadedTrigger

```typescript
// trigger: AssetUploadedTrigger
const AssetUploadedTriggerContract: TriggerContract = {
  triggerId: 'AssetUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AssetUploadedTrigger' },
  actionTarget: 'UploadCustomAssetTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountCustomAssetWriteProtocol.md) · [Tasks](../tasks/AccountCustomAssetWriteTask.md) · [Workflow](../workflows/AccountCustomAssetWriteWorkflow.md)
