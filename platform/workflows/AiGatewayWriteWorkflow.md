# Workflow: AiGatewayWriteWorkflow

> Capability #3 — **AI Gateway Write**

## Definition
```typescript
// workflow: AiGatewayWriteWorkflow
const AiGatewayWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AiGatewayWriteWorkflow',
  version: '1.0.0',
  description: 'AI Gateway Write — Define routes -> Attach models -> Set policies -> Deploy',
  trigger: { triggerId: 'AIRequestReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define routes'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Attach models'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Set policies'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define routes -> Attach models -> Set policies -> Deploy

## Related artifacts
- [Protocol](../protocols/AiGatewayWriteProtocol.md) · [Trigger(s)](../triggers/AiGatewayWriteTrigger.md) · [Tasks](../tasks/AiGatewayWriteTask.md)
