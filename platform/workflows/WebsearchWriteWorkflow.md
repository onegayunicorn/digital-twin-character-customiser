# Workflow: WebsearchWriteWorkflow

> Capability #6 — **Websearch Write**

## Definition
```typescript
// workflow: WebsearchWriteWorkflow
const WebsearchWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WebsearchWriteWorkflow',
  version: '1.0.0',
  description: 'Websearch Write — Validate -> Apply -> Test -> Audit',
  trigger: { triggerId: 'SearchConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Apply'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Validate -> Apply -> Test -> Audit

## Related artifacts
- [Protocol](../protocols/WebsearchWriteProtocol.md) · [Trigger(s)](../triggers/WebsearchWriteTrigger.md) · [Tasks](../tasks/WebsearchWriteTask.md)
