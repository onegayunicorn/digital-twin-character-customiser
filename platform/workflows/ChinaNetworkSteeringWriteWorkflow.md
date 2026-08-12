# Workflow: ChinaNetworkSteeringWriteWorkflow

> Capability #86 — **China Network Steering Write**

## Definition
```typescript
// workflow: ChinaNetworkSteeringWriteWorkflow
const ChinaNetworkSteeringWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ChinaNetworkSteeringWriteWorkflow',
  version: '1.0.0',
  description: 'China Network Steering Write — Verify compliance -> Configure routing -> Activate -> Test',
  trigger: { triggerId: 'SteeringConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Verify compliance'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure routing'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Verify compliance -> Configure routing -> Activate -> Test

## Related artifacts
- [Protocol](../protocols/ChinaNetworkSteeringWriteProtocol.md) · [Trigger(s)](../triggers/ChinaNetworkSteeringWriteTrigger.md) · [Tasks](../tasks/ChinaNetworkSteeringWriteTask.md)
