# Workflow: ConnectivityDirectoryAdminWorkflow

> Capability #87 — **Connectivity Directory Admin**

## Definition
```typescript
// workflow: ConnectivityDirectoryAdminWorkflow
const ConnectivityDirectoryAdminWorkflow: WorkflowDefinition = {
  workflowId: 'ConnectivityDirectoryAdminWorkflow',
  version: '1.0.0',
  description: 'Connectivity Directory Admin — Register -> Verify -> Peer -> Activate -> Monitor',
  trigger: { triggerId: 'ConnectivityUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Peer'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Activate'
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
Register -> Verify -> Peer -> Activate -> Monitor

## Related artifacts
- [Protocol](../protocols/ConnectivityDirectoryAdminProtocol.md) · [Trigger(s)](../triggers/ConnectivityDirectoryAdminTrigger.md) · [Tasks](../tasks/ConnectivityDirectoryAdminTask.md)
