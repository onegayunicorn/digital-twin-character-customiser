# Workflow: TurnstileSitesWriteWorkflow

> Capability #53 — **Turnstile Sites Write**

## Definition
```typescript
// workflow: TurnstileSitesWriteWorkflow
const TurnstileSitesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'TurnstileSitesWriteWorkflow',
  version: '1.0.0',
  description: 'Turnstile Sites Write — Register site -> Set challenge mode -> Install -> Verify',
  trigger: { triggerId: 'TurnstileConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register site'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set challenge mode'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Install'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register site -> Set challenge mode -> Install -> Verify

## Related artifacts
- [Protocol](../protocols/TurnstileSitesWriteProtocol.md) · [Trigger(s)](../triggers/TurnstileSitesWriteTrigger.md) · [Tasks](../tasks/TurnstileSitesWriteTask.md)
