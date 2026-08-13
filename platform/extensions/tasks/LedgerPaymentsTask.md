# Task: LedgerPaymentsTask

> Capability #157 — **Ledger & Payments**

Atomic executable unit(s) for this capability.

### Task: PostLedgerEntryTask

```typescript
// task: PostLedgerEntryTask
const PostLedgerEntryTaskSpec: TaskSpecification = {
  taskId: 'PostLedgerEntryTask',
  operationRef: 'LedgerPaymentsProtocol',
  inputSchema: { capability: 'Ledger & Payments' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute PostLedgerEntryTask

### Task: RunPaymentFlowTask

```typescript
// task: RunPaymentFlowTask
const RunPaymentFlowTaskSpec: TaskSpecification = {
  taskId: 'RunPaymentFlowTask',
  operationRef: 'LedgerPaymentsProtocol',
  inputSchema: { capability: 'Ledger & Payments' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunPaymentFlowTask

### Task: HoldEscrowTask

```typescript
// task: HoldEscrowTask
const HoldEscrowTaskSpec: TaskSpecification = {
  taskId: 'HoldEscrowTask',
  operationRef: 'LedgerPaymentsProtocol',
  inputSchema: { capability: 'Ledger & Payments' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute HoldEscrowTask

## Related artifacts
- [Protocol](../protocols/LedgerPaymentsProtocol.md) · [Trigger(s)](../triggers/LedgerPaymentsTrigger.md) · [Workflow](../workflows/LedgerPaymentsWorkflow.md)
