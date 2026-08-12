# Workflow: DnsFirewallWriteWorkflow

> Capability #31 — **DNS Firewall Write**

## Definition
```typescript
// workflow: DnsFirewallWriteWorkflow
const DnsFirewallWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DnsFirewallWriteWorkflow',
  version: '1.0.0',
  description: 'DNS Firewall Write — Define rule -> Attach -> Test -> Activate',
  trigger: { triggerId: 'DNSQueryTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define rule'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Attach'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Test'
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
Define rule -> Attach -> Test -> Activate

## Related artifacts
- [Protocol](../protocols/DnsFirewallWriteProtocol.md) · [Trigger(s)](../triggers/DnsFirewallWriteTrigger.md) · [Tasks](../tasks/DnsFirewallWriteTask.md)
