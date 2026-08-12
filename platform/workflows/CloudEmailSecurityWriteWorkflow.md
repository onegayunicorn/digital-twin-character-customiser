# Workflow: CloudEmailSecurityWriteWorkflow

> Capability #74 — **Cloud Email Security: Write**

## Definition
```typescript
// workflow: CloudEmailSecurityWriteWorkflow
const CloudEmailSecurityWriteWorkflow: WorkflowDefinition = {
  workflowId: 'CloudEmailSecurityWriteWorkflow',
  version: '1.0.0',
  description: 'Cloud Email Security: Write — Scan -> Classify -> Filter -> Quarantine -> Notify',
  trigger: { triggerId: 'EmailReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Filter'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Quarantine'
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
Scan -> Classify -> Filter -> Quarantine -> Notify

## Related artifacts
- [Protocol](../protocols/CloudEmailSecurityWriteProtocol.md) · [Trigger(s)](../triggers/CloudEmailSecurityWriteTrigger.md) · [Tasks](../tasks/CloudEmailSecurityWriteTask.md)
