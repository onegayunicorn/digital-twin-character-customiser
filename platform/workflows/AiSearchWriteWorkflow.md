# Workflow: AiSearchWriteWorkflow

> Capability #4 — **AI Search Write**

## Definition
```typescript
// workflow: AiSearchWriteWorkflow
const AiSearchWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AiSearchWriteWorkflow',
  version: '1.0.0',
  description: 'AI Search Write — Extract -> Embed -> Index -> Optimize',
  trigger: { triggerId: 'DocumentIngestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Extract'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Embed'
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
Extract -> Embed -> Index -> Optimize

## Related artifacts
- [Protocol](../protocols/AiSearchWriteProtocol.md) · [Trigger(s)](../triggers/AiSearchWriteTrigger.md) · [Tasks](../tasks/AiSearchWriteTask.md)
