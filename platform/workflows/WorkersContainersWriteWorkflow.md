# Workflow: WorkersContainersWriteWorkflow

> Capability #9 — **Workers Containers Write**

## Definition
```typescript
// workflow: WorkersContainersWriteWorkflow
const WorkersContainersWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersContainersWriteWorkflow',
  version: '1.0.0',
  description: 'Workers Containers Write — Pull image -> Validate -> Deploy -> Start -> Health check',
  trigger: { triggerId: 'ContainerImagePushedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Pull image'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Start'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Health check'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Pull image -> Validate -> Deploy -> Start -> Health check

## Related artifacts
- [Protocol](../protocols/WorkersContainersWriteProtocol.md) · [Trigger(s)](../triggers/WorkersContainersWriteTrigger.md) · [Tasks](../tasks/WorkersContainersWriteTask.md)
