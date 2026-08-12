# Workflow: IpPrefixesBgpOnDemandWriteWorkflow

> Capability #89 — **IP Prefixes: BGP On Demand Write**

## Definition
```typescript
// workflow: IpPrefixesBgpOnDemandWriteWorkflow
const IpPrefixesBgpOnDemandWriteWorkflow: WorkflowDefinition = {
  workflowId: 'IpPrefixesBgpOnDemandWriteWorkflow',
  version: '1.0.0',
  description: 'IP Prefixes: BGP On Demand Write — Request -> Validate -> Announce -> Maintain -> Withdraw',
  trigger: { triggerId: 'BGPTriggerEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Request'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Announce'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Maintain'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Withdraw'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Request -> Validate -> Announce -> Maintain -> Withdraw

## Related artifacts
- [Protocol](../protocols/IpPrefixesBgpOnDemandWriteProtocol.md) · [Trigger(s)](../triggers/IpPrefixesBgpOnDemandWriteTrigger.md) · [Tasks](../tasks/IpPrefixesBgpOnDemandWriteTask.md)
