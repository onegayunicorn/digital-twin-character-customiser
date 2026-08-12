# Workflow: AccountRulesetsWriteWorkflow

> Capability #58 — **Account Rulesets Write**

## Definition
```typescript
// workflow: AccountRulesetsWriteWorkflow
const AccountRulesetsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountRulesetsWriteWorkflow',
  version: '1.0.0',
  description: 'Account Rulesets Write — Compose -> Validate -> Test -> Deploy -> Activate',
  trigger: { triggerId: 'RulesetDeployedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Compose'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Compose -> Validate -> Test -> Deploy -> Activate

## Related artifacts
- [Protocol](../protocols/AccountRulesetsWriteProtocol.md) · [Trigger(s)](../triggers/AccountRulesetsWriteTrigger.md) · [Tasks](../tasks/AccountRulesetsWriteTask.md)
