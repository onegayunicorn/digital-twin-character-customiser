# Workflow: MagicFirewallWriteWorkflow

> Capability #90 — **Magic Firewall Write**

## Definition
```typescript
// workflow: MagicFirewallWriteWorkflow
const MagicFirewallWriteWorkflow: WorkflowDefinition = {
  workflowId: 'MagicFirewallWriteWorkflow',
  version: '1.0.0',
  description: 'Magic Firewall Write — Define rule -> Set action -> Order -> Deploy -> Test',
  trigger: { triggerId: 'MagicFirewallRuleChangeTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define rule'
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
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define rule -> Set action -> Order -> Deploy -> Test

## Related artifacts
- [Protocol](../protocols/MagicFirewallWriteProtocol.md) · [Trigger(s)](../triggers/MagicFirewallWriteTrigger.md) · [Tasks](../tasks/MagicFirewallWriteTask.md)
