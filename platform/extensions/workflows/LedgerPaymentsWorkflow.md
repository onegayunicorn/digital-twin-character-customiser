# Workflow: LedgerPaymentsWorkflow

> Capability #157 — **Ledger & Payments**

## Definition
```typescript
// workflow: LedgerPaymentsWorkflow
const LedgerPaymentsWorkflow: WorkflowDefinition = {
  workflowId: 'LedgerPaymentsWorkflow',
  version: '1.0.0',
  description: 'Ledger & Payments — Gate -> Intent -> Hold -> Capture -> Release -> Reconcile',
  trigger: { triggerId: 'PaymentInitiatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Gate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Intent'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Hold'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Capture'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Release'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Reconcile'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Gate -> Intent -> Hold -> Capture -> Release -> Reconcile

## Related artifacts
- [Protocol](../protocols/LedgerPaymentsProtocol.md) · [Trigger(s)](../triggers/LedgerPaymentsTrigger.md) · [Tasks](../tasks/LedgerPaymentsTask.md)
