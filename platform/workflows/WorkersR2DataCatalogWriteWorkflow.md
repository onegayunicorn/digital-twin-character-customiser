# Workflow: WorkersR2DataCatalogWriteWorkflow

> Capability #19 — **Workers R2 Data Catalog Write**

## Definition
```typescript
// workflow: WorkersR2DataCatalogWriteWorkflow
const WorkersR2DataCatalogWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersR2DataCatalogWriteWorkflow',
  version: '1.0.0',
  description: 'Workers R2 Data Catalog Write — Register schema -> Index -> Tag -> Publish',
  trigger: { triggerId: 'CatalogEntryUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register schema'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Index'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Tag'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Publish'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register schema -> Index -> Tag -> Publish

## Related artifacts
- [Protocol](../protocols/WorkersR2DataCatalogWriteProtocol.md) · [Trigger(s)](../triggers/WorkersR2DataCatalogWriteTrigger.md) · [Tasks](../tasks/WorkersR2DataCatalogWriteTask.md)
