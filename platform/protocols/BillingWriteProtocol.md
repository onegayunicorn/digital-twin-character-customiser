# Protocol: BillingWriteProtocol

> Capability #67 — **Billing Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Subscriptions, usage, invoices, payments, credits, and alerts for billing.

## Interface contract
```typescript
// protocol: BillingWriteProtocol
interface BillingWriteProtocol extends BaseOperation {
  id: string;
  name: 'Billing Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`UsageThresholdTrigger`](../triggers/BillingWriteTrigger.md), [`InvoiceIssuedTrigger`](../triggers/BillingWriteTrigger.md), [`PaymentDueTrigger`](../triggers/BillingWriteTrigger.md) |
| Task(s) | [`UpdateBillingPlanTask`](../tasks/BillingWriteTask.md), [`ProcessPaymentTask`](../tasks/BillingWriteTask.md) |
| Workflow | [`BillingWriteWorkflow`](../workflows/BillingWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Calculate usage -> Generate invoice -> Charge -> Receipt -> Notify
