# Trigger: TrustAndSafetyWriteTrigger

> Capability #52 — **Trust and Safety Write**

Event source(s) that initiate execution for this capability.

### Trigger: ContentReportedTrigger

```typescript
// trigger: ContentReportedTrigger
const ContentReportedTriggerContract: TriggerContract = {
  triggerId: 'ContentReportedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ContentReportedTrigger' },
  actionTarget: 'UpdateTrustSafetyPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PolicyUpdatedTrigger

```typescript
// trigger: PolicyUpdatedTrigger
const PolicyUpdatedTriggerContract: TriggerContract = {
  triggerId: 'PolicyUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PolicyUpdatedTrigger' },
  actionTarget: 'UpdateTrustSafetyPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TrustAndSafetyWriteProtocol.md) · [Tasks](../tasks/TrustAndSafetyWriteTask.md) · [Workflow](../workflows/TrustAndSafetyWriteWorkflow.md)
