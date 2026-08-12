# Workflow: IntelWriteWorkflow

> Capability #96 — **Intel Write**

## Definition
```typescript
// workflow: IntelWriteWorkflow
const IntelWriteWorkflow: WorkflowDefinition = {
  workflowId: 'IntelWriteWorkflow',
  version: '1.0.0',
  description: 'Intel Write — Fetch -> Process -> Enrich -> Deploy -> Block/Alert',
  trigger: { triggerId: 'IntelFeedUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Fetch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Process'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Enrich'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Block/Alert'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Fetch -> Process -> Enrich -> Deploy -> Block/Alert

## Related artifacts
- [Protocol](../protocols/IntelWriteProtocol.md) · [Trigger(s)](../triggers/IntelWriteTrigger.md) · [Tasks](../tasks/IntelWriteTask.md)
