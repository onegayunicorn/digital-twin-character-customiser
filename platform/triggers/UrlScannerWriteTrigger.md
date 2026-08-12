# Trigger: UrlScannerWriteTrigger

> Capability #54 — **URL Scanner Write**

Event source(s) that initiate execution for this capability.

### Trigger: URLSubmittedTrigger

```typescript
// trigger: URLSubmittedTrigger
const URLSubmittedTriggerContract: TriggerContract = {
  triggerId: 'URLSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for URLSubmittedTrigger' },
  actionTarget: 'ScanURLTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleScanTrigger

```typescript
// trigger: ScheduleScanTrigger
const ScheduleScanTriggerContract: TriggerContract = {
  triggerId: 'ScheduleScanTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleScanTrigger' },
  actionTarget: 'ScanURLTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/UrlScannerWriteProtocol.md) · [Tasks](../tasks/UrlScannerWriteTask.md) · [Workflow](../workflows/UrlScannerWriteWorkflow.md)
