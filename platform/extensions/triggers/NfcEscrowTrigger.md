# Trigger: NfcEscrowTrigger

> Capability #162 — **NFC Escrow**

Event source(s) that initiate execution for this capability.

### Trigger: NfcTapTrigger

```typescript
// trigger: NfcTapTrigger
const NfcTapTriggerContract: TriggerContract = {
  triggerId: 'NfcTapTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NfcTapTrigger' },
  actionTarget: 'TapHoldTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ConditionVerifiedTrigger

```typescript
// trigger: ConditionVerifiedTrigger
const ConditionVerifiedTriggerContract: TriggerContract = {
  triggerId: 'ConditionVerifiedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ConditionVerifiedTrigger' },
  actionTarget: 'TapHoldTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/NfcEscrowProtocol.md) · [Tasks](../tasks/NfcEscrowTask.md) · [Workflow](../workflows/NfcEscrowWorkflow.md)
