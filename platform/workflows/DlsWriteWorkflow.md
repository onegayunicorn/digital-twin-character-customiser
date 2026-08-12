# Workflow: DlsWriteWorkflow

> Capability #126 — **DLS: Write**

## Definition
```typescript
// workflow: DlsWriteWorkflow
const DlsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DlsWriteWorkflow',
  version: '1.0.0',
  description: 'DLS: Write — Define patterns -> Scan -> Detect -> Redact/Block -> Log/Alert',
  trigger: { triggerId: 'DLPRuleUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define patterns'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Detect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Redact/Block'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Log/Alert'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define patterns -> Scan -> Detect -> Redact/Block -> Log/Alert

## Related artifacts
- [Protocol](../protocols/DlsWriteProtocol.md) · [Trigger(s)](../triggers/DlsWriteTrigger.md) · [Tasks](../tasks/DlsWriteTask.md)
