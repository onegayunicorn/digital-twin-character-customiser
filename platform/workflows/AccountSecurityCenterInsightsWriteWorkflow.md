# Workflow: AccountSecurityCenterInsightsWriteWorkflow

> Capability #37 — **Account Security Center Insights Write**

## Definition
```typescript
// workflow: AccountSecurityCenterInsightsWriteWorkflow
const AccountSecurityCenterInsightsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountSecurityCenterInsightsWriteWorkflow',
  version: '1.0.0',
  description: 'Account Security Center Insights Write — Scan -> Analyze -> Generate insight -> Prioritize -> Notify',
  trigger: { triggerId: 'SecurityScanCompleteTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Generate insight'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Prioritize'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Notify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Scan -> Analyze -> Generate insight -> Prioritize -> Notify

## Related artifacts
- [Protocol](../protocols/AccountSecurityCenterInsightsWriteProtocol.md) · [Trigger(s)](../triggers/AccountSecurityCenterInsightsWriteTrigger.md) · [Tasks](../tasks/AccountSecurityCenterInsightsWriteTask.md)
