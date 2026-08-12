# Workflow: AgentMemoryWriteWorkflow

> Capability #1 — **Agent Memory Write**

## Definition
```typescript
// workflow: AgentMemoryWriteWorkflow
const AgentMemoryWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AgentMemoryWriteWorkflow',
  version: '1.0.0',
  description: 'Agent Memory Write — Validate -> Write -> Replicate -> Notify',
  trigger: { triggerId: 'AgentMemoryUpdatedTrigger (on memory entry created/updated/expired)' },
  steps: [
  - stepId: 'step1'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Write'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Replicate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Validate -> Write -> Replicate -> Notify

## Related artifacts
- [Protocol](../protocols/AgentMemoryWriteProtocol.md) · [Trigger(s)](../triggers/AgentMemoryWriteTrigger.md) · [Tasks](../tasks/AgentMemoryWriteTask.md)
