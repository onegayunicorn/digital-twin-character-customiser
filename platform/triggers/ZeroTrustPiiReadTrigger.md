# Trigger: ZeroTrustPiiReadTrigger

> Capability #131 — **Zero Trust: PII Read**

Event source(s) that initiate execution for this capability.

### Trigger: PIIAccessRequestTrigger

```typescript
// trigger: PIIAccessRequestTrigger
const PIIAccessRequestTriggerContract: TriggerContract = {
  triggerId: 'PIIAccessRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PIIAccessRequestTrigger' },
  actionTarget: 'ReadZeroTrustPIITask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ZeroTrustPiiReadProtocol.md) · [Tasks](../tasks/ZeroTrustPiiReadTask.md) · [Workflow](../workflows/ZeroTrustPiiReadWorkflow.md)
