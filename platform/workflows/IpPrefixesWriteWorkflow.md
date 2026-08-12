# Workflow: IpPrefixesWriteWorkflow

> Capability #88 — **IP Prefixes: Write**

## Definition
```typescript
// workflow: IpPrefixesWriteWorkflow
const IpPrefixesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'IpPrefixesWriteWorkflow',
  version: '1.0.0',
  description: 'IP Prefixes: Write — Register -> Authorize -> Announce -> Validate -> Monitor',
  trigger: { triggerId: 'PrefixAnnouncementTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Authorize'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Announce'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Validate'
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
Register -> Authorize -> Announce -> Validate -> Monitor

## Related artifacts
- [Protocol](../protocols/IpPrefixesWriteProtocol.md) · [Trigger(s)](../triggers/IpPrefixesWriteTrigger.md) · [Tasks](../tasks/IpPrefixesWriteTask.md)
