# Workflow: AccountCustomAssetWriteWorkflow

> Capability #65 — **Account Custom Asset Write**

## Definition
```typescript
// workflow: AccountCustomAssetWriteWorkflow
const AccountCustomAssetWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountCustomAssetWriteWorkflow',
  version: '1.0.0',
  description: 'Account Custom Asset Write — Upload -> Validate -> Hash -> Distribute -> Purge cache',
  trigger: { triggerId: 'AssetUploadedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Hash'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Purge cache'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Upload -> Validate -> Hash -> Distribute -> Purge cache

## Related artifacts
- [Protocol](../protocols/AccountCustomAssetWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomAssetWriteTrigger.md) · [Tasks](../tasks/AccountCustomAssetWriteTask.md)
