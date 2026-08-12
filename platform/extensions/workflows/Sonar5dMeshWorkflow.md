# Workflow: Sonar5dMeshWorkflow

> Capability #141 — **Sonar 5D Mesh**

## Definition
```typescript
// workflow: Sonar5dMeshWorkflow
const Sonar5dMeshWorkflow: WorkflowDefinition = {
  workflowId: 'Sonar5dMeshWorkflow',
  version: '1.0.0',
  description: 'Sonar 5D Mesh — Generate -> Invariants -> Sweep -> Export -> Visualize',
  trigger: { triggerId: 'MeshRequestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Generate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Invariants'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Sweep'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Export'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Visualize'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Generate -> Invariants -> Sweep -> Export -> Visualize

## Related artifacts
- [Protocol](../protocols/Sonar5dMeshProtocol.md) · [Trigger(s)](../triggers/Sonar5dMeshTrigger.md) · [Tasks](../tasks/Sonar5dMeshTask.md)
