# Workflow: AccountAnalyticsReadWorkflow

> Capability #98 — **Account Analytics Read**

## Definition
```typescript
// workflow: AccountAnalyticsReadWorkflow
const AccountAnalyticsReadWorkflow: WorkflowDefinition = {
  workflowId: 'AccountAnalyticsReadWorkflow',
  version: '1.0.0',
  description: 'Account Analytics Read — Select metrics -> Query -> Aggregate -> Generate -> Distribute',
  trigger: { triggerId: 'AnalyticsReportTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select metrics'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Query'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Aggregate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Generate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select metrics -> Query -> Aggregate -> Generate -> Distribute

## Related artifacts
- [Protocol](../protocols/AccountAnalyticsReadProtocol.md) · [Trigger(s)](../triggers/AccountAnalyticsReadTrigger.md) · [Tasks](../tasks/AccountAnalyticsReadTask.md)
