# Workflow: LogsWriteWorkflow

> Capability #95 — **Logs Write**

## Definition
```typescript
// workflow: LogsWriteWorkflow
const LogsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'LogsWriteWorkflow',
  version: '1.0.0',
  description: 'Logs Write — Select fields -> Set destination -> Enable -> Verify delivery',
  trigger: { triggerId: 'LogConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select fields'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set destination'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify delivery'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select fields -> Set destination -> Enable -> Verify delivery

## Related artifacts
- [Protocol](../protocols/LogsWriteProtocol.md) · [Trigger(s)](../triggers/LogsWriteTrigger.md) · [Tasks](../tasks/LogsWriteTask.md)
