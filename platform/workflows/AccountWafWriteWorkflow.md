# Workflow: AccountWafWriteWorkflow

> Capability #38 — **Account WAF Write**

## Definition
```typescript
// workflow: AccountWafWriteWorkflow
const AccountWafWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountWafWriteWorkflow',
  version: '1.0.0',
  description: 'Account WAF Write — Select ruleset -> Tune -> Test -> Enable -> Monitor',
  trigger: { triggerId: 'WAFRuleUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select ruleset'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Tune'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Enable'
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
Select ruleset -> Tune -> Test -> Enable -> Monitor

## Related artifacts
- [Protocol](../protocols/AccountWafWriteProtocol.md) · [Trigger(s)](../triggers/AccountWafWriteTrigger.md) · [Tasks](../tasks/AccountWafWriteTask.md)
