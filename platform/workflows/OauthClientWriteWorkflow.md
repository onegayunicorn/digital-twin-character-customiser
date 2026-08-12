# Workflow: OauthClientWriteWorkflow

> Capability #70 — **OAuth Client Write**

## Definition
```typescript
// workflow: OauthClientWriteWorkflow
const OauthClientWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OauthClientWriteWorkflow',
  version: '1.0.0',
  description: 'OAuth Client Write — Register -> Configure -> Generate secret -> Whitelist -> Activate',
  trigger: { triggerId: 'OAuthClientCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Generate secret'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Whitelist'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Configure -> Generate secret -> Whitelist -> Activate

## Related artifacts
- [Protocol](../protocols/OauthClientWriteProtocol.md) · [Trigger(s)](../triggers/OauthClientWriteTrigger.md) · [Tasks](../tasks/OauthClientWriteTask.md)
