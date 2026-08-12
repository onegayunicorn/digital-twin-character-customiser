# Workflow: TagWriteWorkflow

> Capability #51 — **Tag Write**

## Definition
```typescript
// workflow: TagWriteWorkflow
const TagWriteWorkflow: WorkflowDefinition = {
  workflowId: 'TagWriteWorkflow',
  version: '1.0.0',
  description: 'Tag Write — Define taxonomy -> Assign -> Propagate -> Enforce policies',
  trigger: { triggerId: 'TagAddedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define taxonomy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Propagate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Enforce policies'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define taxonomy -> Assign -> Propagate -> Enforce policies

## Related artifacts
- [Protocol](../protocols/TagWriteProtocol.md) · [Trigger(s)](../triggers/TagWriteTrigger.md) · [Tasks](../tasks/TagWriteTask.md)
