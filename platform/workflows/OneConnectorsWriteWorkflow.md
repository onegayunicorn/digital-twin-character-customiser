# Workflow: OneConnectorsWriteWorkflow

> Capability #124 — **One Connectors Write**

## Definition
```typescript
// workflow: OneConnectorsWriteWorkflow
const OneConnectorsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OneConnectorsWriteWorkflow',
  version: '1.0.0',
  description: 'One Connectors Write — Register -> Configure -> Deploy -> Update -> Monitor',
  trigger: { triggerId: 'ConnectorRegisteredTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Update'
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
Register -> Configure -> Deploy -> Update -> Monitor

## Related artifacts
- [Protocol](../protocols/OneConnectorsWriteProtocol.md) · [Trigger(s)](../triggers/OneConnectorsWriteTrigger.md) · [Tasks](../tasks/OneConnectorsWriteTask.md)
