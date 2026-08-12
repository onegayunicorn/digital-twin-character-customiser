# Workflow: AccountWaitingRoomsReadWorkflow

> Capability #85 — **Account Waiting Rooms Read**

## Definition
```typescript
// workflow: AccountWaitingRoomsReadWorkflow
const AccountWaitingRoomsReadWorkflow: WorkflowDefinition = {
  workflowId: 'AccountWaitingRoomsReadWorkflow',
  version: '1.0.0',
  description: 'Account Waiting Rooms Read — Poll -> Calculate -> Report -> Alert',
  trigger: { triggerId: 'WaitingRoomEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Poll'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Calculate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Alert'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Poll -> Calculate -> Report -> Alert

## Related artifacts
- [Protocol](../protocols/AccountWaitingRoomsReadProtocol.md) · [Trigger(s)](../triggers/AccountWaitingRoomsReadTrigger.md) · [Tasks](../tasks/AccountWaitingRoomsReadTask.md)
