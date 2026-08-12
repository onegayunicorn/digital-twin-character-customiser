# Workflow: RealtimeAdminWorkflow

> Capability #26 — **Realtime Admin**

## Definition
```typescript
// workflow: RealtimeAdminWorkflow
const RealtimeAdminWorkflow: WorkflowDefinition = {
  workflowId: 'RealtimeAdminWorkflow',
  version: '1.0.0',
  description: 'Realtime Admin — Auth -> Join room -> Broadcast -> Monitor -> Disconnect',
  trigger: { triggerId: 'ClientConnectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Join room'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Broadcast'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Disconnect'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Auth -> Join room -> Broadcast -> Monitor -> Disconnect

## Related artifacts
- [Protocol](../protocols/RealtimeAdminProtocol.md) · [Trigger(s)](../triggers/RealtimeAdminTrigger.md) · [Tasks](../tasks/RealtimeAdminTask.md)
