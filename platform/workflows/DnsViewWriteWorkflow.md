# Workflow: DnsViewWriteWorkflow

> Capability #32 — **DNS View Write**

## Definition
```typescript
// workflow: DnsViewWriteWorkflow
const DnsViewWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DnsViewWriteWorkflow',
  version: '1.0.0',
  description: 'DNS View Write — Define view -> Assign zones -> Set match -> Deploy',
  trigger: { triggerId: 'DNSViewConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define view'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign zones'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Set match'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define view -> Assign zones -> Set match -> Deploy

## Related artifacts
- [Protocol](../protocols/DnsViewWriteProtocol.md) · [Trigger(s)](../triggers/DnsViewWriteTrigger.md) · [Tasks](../tasks/DnsViewWriteTask.md)
