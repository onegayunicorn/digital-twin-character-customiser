# Workflow: MagicFirewallPacketCapturesWritePcapsApiWorkflow

> Capability #94 — **Magic Firewall Packet Captures - Write PCAPs API**

## Definition
```typescript
// workflow: MagicFirewallPacketCapturesWritePcapsApiWorkflow
const MagicFirewallPacketCapturesWritePcapsApiWorkflow: WorkflowDefinition = {
  workflowId: 'MagicFirewallPacketCapturesWritePcapsApiWorkflow',
  version: '1.0.0',
  description: 'Magic Firewall Packet Captures - Write PCAPs API — Define filter -> Start -> Capture -> Stop -> Export -> Analyze',
  trigger: { triggerId: 'PacketCaptureTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define filter'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Start'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Capture'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Stop'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Export'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define filter -> Start -> Capture -> Stop -> Export -> Analyze

## Related artifacts
- [Protocol](../protocols/MagicFirewallPacketCapturesWritePcapsApiProtocol.md) · [Trigger(s)](../triggers/MagicFirewallPacketCapturesWritePcapsApiTrigger.md) · [Tasks](../tasks/MagicFirewallPacketCapturesWritePcapsApiTask.md)
