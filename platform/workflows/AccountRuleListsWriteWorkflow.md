# Workflow: AccountRuleListsWriteWorkflow

> Capability #57 — **Account Rule Lists Write**

## Definition
```typescript
// workflow: AccountRuleListsWriteWorkflow
const AccountRuleListsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountRuleListsWriteWorkflow',
  version: '1.0.0',
  description: 'Account Rule Lists Write — Create -> Import items -> Attach -> Deploy -> Monitor',
  trigger: { triggerId: 'RuleListUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Import items'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Attach'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
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
Create -> Import items -> Attach -> Deploy -> Monitor

## Related artifacts
- [Protocol](../protocols/AccountRuleListsWriteProtocol.md) · [Trigger(s)](../triggers/AccountRuleListsWriteTrigger.md) · [Tasks](../tasks/AccountRuleListsWriteTask.md)
