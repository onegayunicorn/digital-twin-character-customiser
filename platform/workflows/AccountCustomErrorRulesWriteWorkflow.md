# Workflow: AccountCustomErrorRulesWriteWorkflow

> Capability #55 — **Account Custom Error Rules Write**

## Definition
```typescript
// workflow: AccountCustomErrorRulesWriteWorkflow
const AccountCustomErrorRulesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountCustomErrorRulesWriteWorkflow',
  version: '1.0.0',
  description: 'Account Custom Error Rules Write — Define -> Test -> Order -> Activate',
  trigger: { triggerId: 'ErrorResponseTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Order'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Define -> Test -> Order -> Activate

## Related artifacts
- [Protocol](../protocols/AccountCustomErrorRulesWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomErrorRulesWriteTrigger.md) · [Tasks](../tasks/AccountCustomErrorRulesWriteTask.md)
