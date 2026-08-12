# Trigger: ZeroTrustSeatsWriteTrigger

> Capability #130 — **Zero Trust: Seats Write**

Event source(s) that initiate execution for this capability.

### Trigger: SeatAssignmentTrigger

```typescript
// trigger: SeatAssignmentTrigger
const SeatAssignmentTriggerContract: TriggerContract = {
  triggerId: 'SeatAssignmentTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SeatAssignmentTrigger' },
  actionTarget: 'ManageZeroTrustSeatTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ZeroTrustSeatsWriteProtocol.md) · [Tasks](../tasks/ZeroTrustSeatsWriteTask.md) · [Workflow](../workflows/ZeroTrustSeatsWriteWorkflow.md)
