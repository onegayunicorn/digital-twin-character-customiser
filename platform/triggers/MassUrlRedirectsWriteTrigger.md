# Trigger: MassUrlRedirectsWriteTrigger

> Capability #60 — **Mass URL Redirects Write**

Event source(s) that initiate execution for this capability.

### Trigger: RedirectConfigUpdatedTrigger

```typescript
// trigger: RedirectConfigUpdatedTrigger
const RedirectConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'RedirectConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RedirectConfigUpdatedTrigger' },
  actionTarget: 'ImportRedirectsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: BulkImportTrigger

```typescript
// trigger: BulkImportTrigger
const BulkImportTriggerContract: TriggerContract = {
  triggerId: 'BulkImportTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for BulkImportTrigger' },
  actionTarget: 'ImportRedirectsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MassUrlRedirectsWriteProtocol.md) · [Tasks](../tasks/MassUrlRedirectsWriteTask.md) · [Workflow](../workflows/MassUrlRedirectsWriteWorkflow.md)
