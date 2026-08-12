# Workflow: BillingWriteWorkflow

> Capability #67 — **Billing Write**

## Definition
```typescript
// workflow: BillingWriteWorkflow
const BillingWriteWorkflow: WorkflowDefinition = {
  workflowId: 'BillingWriteWorkflow',
  version: '1.0.0',
  description: 'Billing Write — Calculate usage -> Generate invoice -> Charge -> Receipt -> Notify',
  trigger: { triggerId: 'UsageThresholdTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Calculate usage'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Generate invoice'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Charge'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Receipt'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Notify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Calculate usage -> Generate invoice -> Charge -> Receipt -> Notify

## Related artifacts
- [Protocol](../protocols/BillingWriteProtocol.md) · [Trigger(s)](../triggers/BillingWriteTrigger.md) · [Tasks](../tasks/BillingWriteTask.md)
