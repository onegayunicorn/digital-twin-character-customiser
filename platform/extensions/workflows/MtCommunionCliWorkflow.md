# Workflow: MtCommunionCliWorkflow

> Capability #134 — **MT Communion CLI**

## Definition
```typescript
// workflow: MtCommunionCliWorkflow
const MtCommunionCliWorkflow: WorkflowDefinition = {
  workflowId: 'MtCommunionCliWorkflow',
  version: '1.0.0',
  description: 'MT Communion CLI — Intent -> Sentiment -> Route -> Reply -> Persist',
  trigger: { triggerId: 'IntentReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Intent'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Sentiment'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Route'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Reply'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Persist'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Intent -> Sentiment -> Route -> Reply -> Persist

## Related artifacts
- [Protocol](../protocols/MtCommunionCliProtocol.md) · [Trigger(s)](../triggers/MtCommunionCliTrigger.md) · [Tasks](../tasks/MtCommunionCliTask.md)
