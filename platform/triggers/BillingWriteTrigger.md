# Trigger: BillingWriteTrigger

> Capability #67 — **Billing Write**

Event source(s) that initiate execution for this capability.

### Trigger: UsageThresholdTrigger

```typescript
// trigger: UsageThresholdTrigger
const UsageThresholdTriggerContract: TriggerContract = {
  triggerId: 'UsageThresholdTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for UsageThresholdTrigger' },
  actionTarget: 'UpdateBillingPlanTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: InvoiceIssuedTrigger

```typescript
// trigger: InvoiceIssuedTrigger
const InvoiceIssuedTriggerContract: TriggerContract = {
  triggerId: 'InvoiceIssuedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for InvoiceIssuedTrigger' },
  actionTarget: 'UpdateBillingPlanTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PaymentDueTrigger

```typescript
// trigger: PaymentDueTrigger
const PaymentDueTriggerContract: TriggerContract = {
  triggerId: 'PaymentDueTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PaymentDueTrigger' },
  actionTarget: 'UpdateBillingPlanTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/BillingWriteProtocol.md) · [Tasks](../tasks/BillingWriteTask.md) · [Workflow](../workflows/BillingWriteWorkflow.md)
