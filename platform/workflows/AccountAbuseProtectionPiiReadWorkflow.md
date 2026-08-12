# Workflow: AccountAbuseProtectionPiiReadWorkflow

> Capability #35 — **Account Abuse Protection PII Read**

## Definition
```typescript
// workflow: AccountAbuseProtectionPiiReadWorkflow
const AccountAbuseProtectionPiiReadWorkflow: WorkflowDefinition = {
  workflowId: 'AccountAbuseProtectionPiiReadWorkflow',
  version: '1.0.0',
  description: 'Account Abuse Protection PII Read — Request -> Auth -> Redact -> Review -> Action -> Log',
  trigger: { triggerId: 'PIIAccessRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Request'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Redact'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Review'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Action'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Log'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Request -> Auth -> Redact -> Review -> Action -> Log

## Related artifacts
- [Protocol](../protocols/AccountAbuseProtectionPiiReadProtocol.md) · [Trigger(s)](../triggers/AccountAbuseProtectionPiiReadTrigger.md) · [Tasks](../tasks/AccountAbuseProtectionPiiReadTask.md)
