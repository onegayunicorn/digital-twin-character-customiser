# Workflow: GatekeeperWorkflow

> Capability #145 — **Gatekeeper**

## Definition
```typescript
// workflow: GatekeeperWorkflow
const GatekeeperWorkflow: WorkflowDefinition = {
  workflowId: 'GatekeeperWorkflow',
  version: '1.0.0',
  description: 'Gatekeeper — Submit -> Check claims -> Check ACL -> Allow/Block -> Log',
  trigger: { triggerId: 'ContentSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Submit'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Check claims'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Check ACL'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Allow/Block'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Submit -> Check claims -> Check ACL -> Allow/Block -> Log

## Related artifacts
- [Protocol](../protocols/GatekeeperProtocol.md) · [Trigger(s)](../triggers/GatekeeperTrigger.md) · [Tasks](../tasks/GatekeeperTask.md)
