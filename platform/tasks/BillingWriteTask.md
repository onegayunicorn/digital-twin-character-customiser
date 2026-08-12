# Task: BillingWriteTask

> Capability #67 — **Billing Write**

Atomic executable unit(s) for this capability.

### Task: UpdateBillingPlanTask

```typescript
// task: UpdateBillingPlanTask
const UpdateBillingPlanTaskSpec: TaskSpecification = {
  taskId: 'UpdateBillingPlanTask',
  operationRef: 'BillingWriteProtocol',
  inputSchema: { capability: 'Billing Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateBillingPlanTask

### Task: ProcessPaymentTask

```typescript
// task: ProcessPaymentTask
const ProcessPaymentTaskSpec: TaskSpecification = {
  taskId: 'ProcessPaymentTask',
  operationRef: 'BillingWriteProtocol',
  inputSchema: { capability: 'Billing Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ProcessPaymentTask

## Related artifacts
- [Protocol](../protocols/BillingWriteProtocol.md) · [Trigger(s)](../triggers/BillingWriteTrigger.md) · [Workflow](../workflows/BillingWriteWorkflow.md)
