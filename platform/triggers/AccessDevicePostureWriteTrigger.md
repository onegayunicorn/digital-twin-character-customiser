# Trigger: AccessDevicePostureWriteTrigger

> Capability #102 — **Access: Device Posture Write**

Event source(s) that initiate execution for this capability.

### Trigger: DevicePostureUpdatedTrigger

```typescript
// trigger: DevicePostureUpdatedTrigger
const DevicePostureUpdatedTriggerContract: TriggerContract = {
  triggerId: 'DevicePostureUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DevicePostureUpdatedTrigger' },
  actionTarget: 'ConfigureDevicePostureCheckTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessDevicePostureWriteProtocol.md) · [Tasks](../tasks/AccessDevicePostureWriteTask.md) · [Workflow](../workflows/AccessDevicePostureWriteWorkflow.md)
