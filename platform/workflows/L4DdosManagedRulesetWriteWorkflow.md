# Workflow: L4DdosManagedRulesetWriteWorkflow

> Capability #49 — **L4 DDoS Managed Ruleset Write**

## Definition
```typescript
// workflow: L4DdosManagedRulesetWriteWorkflow
const L4DdosManagedRulesetWriteWorkflow: WorkflowDefinition = {
  workflowId: 'L4DdosManagedRulesetWriteWorkflow',
  version: '1.0.0',
  description: 'L4 DDoS Managed Ruleset Write — Select -> Tune -> Deploy -> Monitor -> Adjust',
  trigger: { triggerId: 'L4DDoSRulesetUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Tune'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Adjust'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select -> Tune -> Deploy -> Monitor -> Adjust

## Related artifacts
- [Protocol](../protocols/L4DdosManagedRulesetWriteProtocol.md) · [Trigger(s)](../triggers/L4DdosManagedRulesetWriteTrigger.md) · [Tasks](../tasks/L4DdosManagedRulesetWriteTask.md)
