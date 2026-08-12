# Workflow: TunnelWriteWorkflow

> Capability #119 — **Tunnel Write**

## Definition
```typescript
// workflow: TunnelWriteWorkflow
const TunnelWriteWorkflow: WorkflowDefinition = {
  workflowId: 'TunnelWriteWorkflow',
  version: '1.0.0',
  description: 'Tunnel Write — Create -> Install connector -> Configure ingress -> Run -> Verify',
  trigger: { triggerId: 'TunnelConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Install connector'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Configure ingress'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Run'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Create -> Install connector -> Configure ingress -> Run -> Verify

## Related artifacts
- [Protocol](../protocols/TunnelWriteProtocol.md) · [Trigger(s)](../triggers/TunnelWriteTrigger.md) · [Tasks](../tasks/TunnelWriteTask.md)
