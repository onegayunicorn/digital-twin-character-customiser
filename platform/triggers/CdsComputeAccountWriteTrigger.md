# Trigger: CdsComputeAccountWriteTrigger

> Capability #121 — **CDS Compute Account Write**

Event source(s) that initiate execution for this capability.

### Trigger: CDSJobTrigger

```typescript
// trigger: CDSJobTrigger
const CDSJobTriggerContract: TriggerContract = {
  triggerId: 'CDSJobTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CDSJobTrigger' },
  actionTarget: 'DeployCDSComputeTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CdsComputeAccountWriteProtocol.md) · [Tasks](../tasks/CdsComputeAccountWriteTask.md) · [Workflow](../workflows/CdsComputeAccountWriteWorkflow.md)
