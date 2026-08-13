# Workflow: NfcEscrowWorkflow

> Capability #162 — **NFC Escrow**

## Definition
```typescript
// workflow: NfcEscrowWorkflow
const NfcEscrowWorkflow: WorkflowDefinition = {
  workflowId: 'NfcEscrowWorkflow',
  version: '1.0.0',
  description: 'NFC Escrow — Tap -> Hold -> Verify -> Release/Refund -> Audit',
  trigger: { triggerId: 'NfcTapTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Tap'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Hold'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Release/Refund'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Tap -> Hold -> Verify -> Release/Refund -> Audit

## Related artifacts
- [Protocol](../protocols/NfcEscrowProtocol.md) · [Trigger(s)](../triggers/NfcEscrowTrigger.md) · [Tasks](../tasks/NfcEscrowTask.md)
