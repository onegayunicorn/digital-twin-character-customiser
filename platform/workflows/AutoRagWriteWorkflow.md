# Workflow: AutoRagWriteWorkflow

> Capability #5 — **Auto Rag Write**

## Definition
```typescript
// workflow: AutoRagWriteWorkflow
const AutoRagWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AutoRagWriteWorkflow',
  version: '1.0.0',
  description: 'Auto Rag Write — Connect source -> Chunk -> Embed -> Store -> Test query',
  trigger: { triggerId: 'NewDataSourceDetectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Connect source'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Chunk'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Embed'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Test query'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Connect source -> Chunk -> Embed -> Store -> Test query

## Related artifacts
- [Protocol](../protocols/AutoRagWriteProtocol.md) · [Trigger(s)](../triggers/AutoRagWriteTrigger.md) · [Tasks](../tasks/AutoRagWriteTask.md)
