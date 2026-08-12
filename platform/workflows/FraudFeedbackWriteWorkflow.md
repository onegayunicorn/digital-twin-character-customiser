# Workflow: FraudFeedbackWriteWorkflow

> Capability #46 — **Fraud Feedback Write**

## Definition
```typescript
// workflow: FraudFeedbackWriteWorkflow
const FraudFeedbackWriteWorkflow: WorkflowDefinition = {
  workflowId: 'FraudFeedbackWriteWorkflow',
  version: '1.0.0',
  description: 'Fraud Feedback Write — Accept -> Validate -> Store -> Retrain model -> Update rules',
  trigger: { triggerId: 'FraudFeedbackSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Accept'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Retrain model'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Update rules'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Accept -> Validate -> Store -> Retrain model -> Update rules

## Related artifacts
- [Protocol](../protocols/FraudFeedbackWriteProtocol.md) · [Trigger(s)](../triggers/FraudFeedbackWriteTrigger.md) · [Tasks](../tasks/FraudFeedbackWriteTask.md)
