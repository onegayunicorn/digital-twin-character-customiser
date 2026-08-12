# Workflow: CfAgentsWriteWorkflow

> Capability #2 — **CF Agents Write**

## Definition
```typescript
// workflow: CfAgentsWriteWorkflow
const CfAgentsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'CfAgentsWriteWorkflow',
  version: '1.0.0',
  description: 'CF Agents Write — Validate spec -> Deploy -> Health check -> Activate',
  trigger: { triggerId: 'AgentDeploymentTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate spec'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Health check'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Validate spec -> Deploy -> Health check -> Activate

## Related artifacts
- [Protocol](../protocols/CfAgentsWriteProtocol.md) · [Trigger(s)](../triggers/CfAgentsWriteTrigger.md) · [Tasks](../tasks/CfAgentsWriteTask.md)
