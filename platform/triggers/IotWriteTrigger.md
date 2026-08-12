# Trigger: IotWriteTrigger

> Capability #48 — **IOT Write**

Event source(s) that initiate execution for this capability.

### Trigger: DeviceConnectedTrigger

```typescript
// trigger: DeviceConnectedTrigger
const DeviceConnectedTriggerContract: TriggerContract = {
  triggerId: 'DeviceConnectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DeviceConnectedTrigger' },
  actionTarget: 'ManageIoTDeviceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: DeviceMessageTrigger

```typescript
// trigger: DeviceMessageTrigger
const DeviceMessageTriggerContract: TriggerContract = {
  triggerId: 'DeviceMessageTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DeviceMessageTrigger' },
  actionTarget: 'ManageIoTDeviceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IotWriteProtocol.md) · [Tasks](../tasks/IotWriteTask.md) · [Workflow](../workflows/IotWriteWorkflow.md)
