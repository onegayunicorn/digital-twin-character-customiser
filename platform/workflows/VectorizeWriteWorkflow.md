# Workflow: VectorizeWriteWorkflow

> Capability #20 — **Vectorize Write**

## Definition
```typescript
// workflow: VectorizeWriteWorkflow
const VectorizeWriteWorkflow: WorkflowDefinition = {
  workflowId: 'VectorizeWriteWorkflow',
  version: '1.0.0',
  description: 'Vectorize Write — Generate embeddings -> Insert -> Index -> Optimize',
  trigger: { triggerId: 'VectorBatchTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Generate embeddings'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Insert'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Index'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Optimize'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Generate embeddings -> Insert -> Index -> Optimize

## Related artifacts
- [Protocol](../protocols/VectorizeWriteProtocol.md) · [Trigger(s)](../triggers/VectorizeWriteTrigger.md) · [Tasks](../tasks/VectorizeWriteTask.md)
