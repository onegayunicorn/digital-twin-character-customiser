# Trigger: MagicFirewallPacketCapturesWritePcapsApiTrigger

> Capability #94 — **Magic Firewall Packet Captures - Write PCAPs API**

Event source(s) that initiate execution for this capability.

### Trigger: PacketCaptureTrigger

```typescript
// trigger: PacketCaptureTrigger
const PacketCaptureTriggerContract: TriggerContract = {
  triggerId: 'PacketCaptureTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PacketCaptureTrigger' },
  actionTarget: 'CapturePacketsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SecurityEventTrigger

```typescript
// trigger: SecurityEventTrigger
const SecurityEventTriggerContract: TriggerContract = {
  triggerId: 'SecurityEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecurityEventTrigger' },
  actionTarget: 'CapturePacketsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MagicFirewallPacketCapturesWritePcapsApiProtocol.md) · [Tasks](../tasks/MagicFirewallPacketCapturesWritePcapsApiTask.md) · [Workflow](../workflows/MagicFirewallPacketCapturesWritePcapsApiWorkflow.md)
