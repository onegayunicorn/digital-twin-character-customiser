# Workflow: DdosBotnetFeedWriteWorkflow

> Capability #42 — **DDoS Botnet Feed Write**

## Definition
```typescript
// workflow: DdosBotnetFeedWriteWorkflow
const DdosBotnetFeedWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DdosBotnetFeedWriteWorkflow',
  version: '1.0.0',
  description: 'DDoS Botnet Feed Write — Fetch -> Validate -> Merge -> Deploy to edge -> Activate',
  trigger: { triggerId: 'FeedUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Fetch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Merge'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy to edge'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Fetch -> Validate -> Merge -> Deploy to edge -> Activate

## Related artifacts
- [Protocol](../protocols/DdosBotnetFeedWriteProtocol.md) · [Trigger(s)](../triggers/DdosBotnetFeedWriteTrigger.md) · [Tasks](../tasks/DdosBotnetFeedWriteTask.md)
