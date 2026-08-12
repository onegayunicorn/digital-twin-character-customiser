# Trigger: TunnelWriteTrigger

> Capability #119 — **Tunnel Write**

Event source(s) that initiate execution for this capability.

### Trigger: TunnelConfigTrigger

```typescript
// trigger: TunnelConfigTrigger
const TunnelConfigTriggerContract: TriggerContract = {
  triggerId: 'TunnelConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TunnelConfigTrigger' },
  actionTarget: 'ManageTunnelTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: TunnelConnectedTrigger

```typescript
// trigger: TunnelConnectedTrigger
const TunnelConnectedTriggerContract: TriggerContract = {
  triggerId: 'TunnelConnectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TunnelConnectedTrigger' },
  actionTarget: 'ManageTunnelTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TunnelWriteProtocol.md) · [Tasks](../tasks/TunnelWriteTask.md) · [Workflow](../workflows/TunnelWriteWorkflow.md)
