# Workflow: OneNetworksWriteWorkflow

> Capability #125 — **One Networks Write**

## Definition
```typescript
// workflow: OneNetworksWriteWorkflow
const OneNetworksWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OneNetworksWriteWorkflow',
  version: '1.0.0',
  description: 'One Networks Write — Define CIDR -> Create routes -> Connect -> Verify reachability',
  trigger: { triggerId: 'NetworkConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define CIDR'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Create routes'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Connect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify reachability'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define CIDR -> Create routes -> Connect -> Verify reachability

## Related artifacts
- [Protocol](../protocols/OneNetworksWriteProtocol.md) · [Trigger(s)](../triggers/OneNetworksWriteTrigger.md) · [Tasks](../tasks/OneNetworksWriteTask.md)
