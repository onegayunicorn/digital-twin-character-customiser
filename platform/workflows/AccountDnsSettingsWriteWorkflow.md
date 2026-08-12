# Workflow: AccountDnsSettingsWriteWorkflow

> Capability #30 — **Account DNS Settings Write**

## Definition
```typescript
// workflow: AccountDnsSettingsWriteWorkflow
const AccountDnsSettingsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountDnsSettingsWriteWorkflow',
  version: '1.0.0',
  description: 'Account DNS Settings Write — Validate -> Apply -> Propagate -> Verify',
  trigger: { triggerId: 'DNSConfigChangeTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Apply'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Propagate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Validate -> Apply -> Propagate -> Verify

## Related artifacts
- [Protocol](../protocols/AccountDnsSettingsWriteProtocol.md) · [Trigger(s)](../triggers/AccountDnsSettingsWriteTrigger.md) · [Tasks](../tasks/AccountDnsSettingsWriteTask.md)
