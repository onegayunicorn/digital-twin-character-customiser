# Workflow: CasbWriteWorkflow

> Capability #120 — **CASB Write**

## Definition
```typescript
// workflow: CasbWriteWorkflow
const CasbWriteWorkflow: WorkflowDefinition = {
  workflowId: 'CasbWriteWorkflow',
  version: '1.0.0',
  description: 'CASB Write — Connect SaaS -> Scan -> Apply policies -> Monitor -> Remediate',
  trigger: { triggerId: 'CASBConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Connect SaaS'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Apply policies'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Remediate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Connect SaaS -> Scan -> Apply policies -> Monitor -> Remediate

## Related artifacts
- [Protocol](../protocols/CasbWriteProtocol.md) · [Trigger(s)](../triggers/CasbWriteTrigger.md) · [Tasks](../tasks/CasbWriteTask.md)
