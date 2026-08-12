# Workflow: AccountApiGatewayWorkflow

> Capability #63 — **Account API Gateway**

## Definition
```typescript
// workflow: AccountApiGatewayWorkflow
const AccountApiGatewayWorkflow: WorkflowDefinition = {
  workflowId: 'AccountApiGatewayWorkflow',
  version: '1.0.0',
  description: 'Account API Gateway — Define API -> Set auth -> Attach policies -> Deploy -> Test',
  trigger: { triggerId: 'APIRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define API'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Attach policies'
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
Define API -> Set auth -> Attach policies -> Deploy -> Test

## Related artifacts
- [Protocol](../protocols/AccountApiGatewayProtocol.md) · [Trigger(s)](../triggers/AccountApiGatewayTrigger.md) · [Tasks](../tasks/AccountApiGatewayTask.md)
