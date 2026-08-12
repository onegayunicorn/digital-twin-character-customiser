# Workflow: OneConnectorCloudflaredWriteWorkflow

> Capability #122 — **One Connector: cloudflared Write**

## Definition
```typescript
// workflow: OneConnectorCloudflaredWriteWorkflow
const OneConnectorCloudflaredWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OneConnectorCloudflaredWriteWorkflow',
  version: '1.0.0',
  description: 'One Connector: cloudflared Write — Install -> Authenticate -> Create tunnel -> Run -> Monitor',
  trigger: { triggerId: 'CloudflaredConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Install'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Authenticate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Create tunnel'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Run'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Install -> Authenticate -> Create tunnel -> Run -> Monitor

## Related artifacts
- [Protocol](../protocols/OneConnectorCloudflaredWriteProtocol.md) · [Trigger(s)](../triggers/OneConnectorCloudflaredWriteTrigger.md) · [Tasks](../tasks/OneConnectorCloudflaredWriteTask.md)
