# Protocol: LedgerPaymentsProtocol

> Capability #157 — **Ledger & Payments** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Double-entry ledger, conditional settlement (escrow hold/release/refund), Stripe-style payment orchestration (test-mode).

## Interface contract
```typescript
// protocol: LedgerPaymentsProtocol
interface LedgerPaymentsProtocol extends BaseOperation {
  id: string;
  name: 'Ledger & Payments';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`PaymentInitiatedTrigger`](../triggers/LedgerPaymentsTrigger.md), [`EscrowEventTrigger`](../triggers/LedgerPaymentsTrigger.md) |
| Task(s) | [`PostLedgerEntryTask`](../tasks/LedgerPaymentsTask.md), [`RunPaymentFlowTask`](../tasks/LedgerPaymentsTask.md), [`HoldEscrowTask`](../tasks/LedgerPaymentsTask.md) |
| Workflow | [`LedgerPaymentsWorkflow`](../workflows/LedgerPaymentsWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Gate -> Intent -> Hold -> Capture -> Release -> Reconcile
