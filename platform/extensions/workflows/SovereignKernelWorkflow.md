# Workflow: SovereignKernelWorkflow

> Capability #154 — **Sovereign Kernel**

## Definition
```typescript
// workflow: SovereignKernelWorkflow
const SovereignKernelWorkflow: WorkflowDefinition = {
  workflowId: 'SovereignKernelWorkflow',
  version: '1.0.0',
  description: 'Sovereign Kernel — Register -> Attach -> Health check -> Report',
  trigger: { triggerId: 'PrimitiveAttachedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Attach'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Health check'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Attach -> Health check -> Report

## Related artifacts
- [Protocol](../protocols/SovereignKernelProtocol.md) · [Trigger(s)](../triggers/SovereignKernelTrigger.md) · [Tasks](../tasks/SovereignKernelTask.md)
