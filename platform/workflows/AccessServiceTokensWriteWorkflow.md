# Workflow: AccessServiceTokensWriteWorkflow

> Capability #114 — **Access: Service Tokens Write**

## Definition
```typescript
// workflow: AccessServiceTokensWriteWorkflow
const AccessServiceTokensWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessServiceTokensWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Service Tokens Write — Create -> Scope -> Issue -> Rotate -> Revoke',
  trigger: { triggerId: 'ServiceTokenCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scope'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Issue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Rotate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Revoke'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Scope -> Issue -> Rotate -> Revoke

## Related artifacts
- [Protocol](../protocols/AccessServiceTokensWriteProtocol.md) · [Trigger(s)](../triggers/AccessServiceTokensWriteTrigger.md) · [Tasks](../tasks/AccessServiceTokensWriteTask.md)
