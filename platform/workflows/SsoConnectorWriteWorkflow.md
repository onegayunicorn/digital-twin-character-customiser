# Workflow: SsoConnectorWriteWorkflow

> Capability #72 — **SSO Connector Write**

## Definition
```typescript
// workflow: SsoConnectorWriteWorkflow
const SsoConnectorWriteWorkflow: WorkflowDefinition = {
  workflowId: 'SsoConnectorWriteWorkflow',
  version: '1.0.0',
  description: 'SSO Connector Write — Register -> Upload metadata -> Map claims -> Test -> Enable',
  trigger: { triggerId: 'SSOConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Upload metadata'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Map claims'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Upload metadata -> Map claims -> Test -> Enable

## Related artifacts
- [Protocol](../protocols/SsoConnectorWriteProtocol.md) · [Trigger(s)](../triggers/SsoConnectorWriteTrigger.md) · [Tasks](../tasks/SsoConnectorWriteTask.md)
