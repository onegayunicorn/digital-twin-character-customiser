# Trigger: CallsWriteTrigger

> Capability #79 — **Calls Write**

Event source(s) that initiate execution for this capability.

### Trigger: CallInitiatedTrigger

```typescript
// trigger: CallInitiatedTrigger
const CallInitiatedTriggerContract: TriggerContract = {
  triggerId: 'CallInitiatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CallInitiatedTrigger' },
  actionTarget: 'ManageCallSessionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ParticipantJoinTrigger

```typescript
// trigger: ParticipantJoinTrigger
const ParticipantJoinTriggerContract: TriggerContract = {
  triggerId: 'ParticipantJoinTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ParticipantJoinTrigger' },
  actionTarget: 'ManageCallSessionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CallsWriteProtocol.md) · [Tasks](../tasks/CallsWriteTask.md) · [Workflow](../workflows/CallsWriteWorkflow.md)
