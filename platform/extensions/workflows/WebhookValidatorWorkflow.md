# Workflow: WebhookValidatorWorkflow

> Capability #166 — **Webhook Validator**

## Definition
```typescript
// workflow: WebhookValidatorWorkflow
const WebhookValidatorWorkflow: WorkflowDefinition = {
  workflowId: 'WebhookValidatorWorkflow',
  version: '1.0.0',
  description: 'Webhook Validator — Receive -> Validate HMAC -> Accept/Reject -> Log',
  trigger: { triggerId: 'WebhookReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Receive'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate HMAC'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Accept/Reject'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Log'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Receive -> Validate HMAC -> Accept/Reject -> Log

## Related artifacts
- [Protocol](../protocols/WebhookValidatorProtocol.md) · [Trigger(s)](../triggers/WebhookValidatorTrigger.md) · [Tasks](../tasks/WebhookValidatorTask.md)
