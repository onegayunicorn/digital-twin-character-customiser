# Workflow: OneConnectorWarpWriteWorkflow

> Capability #123 — **One Connector: WARP Write**

## Definition
```typescript
// workflow: OneConnectorWarpWriteWorkflow
const OneConnectorWarpWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OneConnectorWarpWriteWorkflow',
  version: '1.0.0',
  description: 'One Connector: WARP Write — Install -> Configure -> Enable -> Connect -> Verify',
  trigger: { triggerId: 'WARPConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Install'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Connect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Install -> Configure -> Enable -> Connect -> Verify

## Related artifacts
- [Protocol](../protocols/OneConnectorWarpWriteProtocol.md) · [Trigger(s)](../triggers/OneConnectorWarpWriteTrigger.md) · [Tasks](../tasks/OneConnectorWarpWriteTask.md)
