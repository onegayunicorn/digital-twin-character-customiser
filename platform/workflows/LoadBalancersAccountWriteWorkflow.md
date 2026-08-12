# Workflow: LoadBalancersAccountWriteWorkflow

> Capability #83 — **Load Balancers Account Write**

## Definition
```typescript
// workflow: LoadBalancersAccountWriteWorkflow
const LoadBalancersAccountWriteWorkflow: WorkflowDefinition = {
  workflowId: 'LoadBalancersAccountWriteWorkflow',
  version: '1.0.0',
  description: 'Load Balancers Account Write — Create LB -> Define pools -> Attach health checks -> Deploy -> Test',
  trigger: { triggerId: 'LoadBalancerConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create LB'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Define pools'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Attach health checks'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Create LB -> Define pools -> Attach health checks -> Deploy -> Test

## Related artifacts
- [Protocol](../protocols/LoadBalancersAccountWriteProtocol.md) · [Trigger(s)](../triggers/LoadBalancersAccountWriteTrigger.md) · [Tasks](../tasks/LoadBalancersAccountWriteTask.md)
