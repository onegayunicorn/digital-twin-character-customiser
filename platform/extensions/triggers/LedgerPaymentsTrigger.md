# Trigger: LedgerPaymentsTrigger

> Capability #157 — **Ledger & Payments**

Event source(s) that initiate execution for this capability.

### Trigger: PaymentInitiatedTrigger

```typescript
// trigger: PaymentInitiatedTrigger
const PaymentInitiatedTriggerContract: TriggerContract = {
  triggerId: 'PaymentInitiatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PaymentInitiatedTrigger' },
  actionTarget: 'PostLedgerEntryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: EscrowEventTrigger

```typescript
// trigger: EscrowEventTrigger
const EscrowEventTriggerContract: TriggerContract = {
  triggerId: 'EscrowEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EscrowEventTrigger' },
  actionTarget: 'PostLedgerEntryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/LedgerPaymentsProtocol.md) · [Tasks](../tasks/LedgerPaymentsTask.md) · [Workflow](../workflows/LedgerPaymentsWorkflow.md)
