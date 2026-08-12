# Workflow: TransformRulesWriteWorkflow

> Capability #59 — **Transform Rules Write**

## Definition
```typescript
// workflow: TransformRulesWriteWorkflow
const TransformRulesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'TransformRulesWriteWorkflow',
  version: '1.0.0',
  description: 'Transform Rules Write — Define match -> Set action -> Order -> Test -> Apply',
  trigger: { triggerId: 'TransformRuleUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define match'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set action'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Order'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Apply'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define match -> Set action -> Order -> Test -> Apply

## Related artifacts
- [Protocol](../protocols/TransformRulesWriteProtocol.md) · [Trigger(s)](../triggers/TransformRulesWriteTrigger.md) · [Tasks](../tasks/TransformRulesWriteTask.md)
