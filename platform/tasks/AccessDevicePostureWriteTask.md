# Task: AccessDevicePostureWriteTask

> Capability #102 — **Access: Device Posture Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureDevicePostureCheckTask

```typescript
// task: ConfigureDevicePostureCheckTask
const ConfigureDevicePostureCheckTaskSpec: TaskSpecification = {
  taskId: 'ConfigureDevicePostureCheckTask',
  operationRef: 'AccessDevicePostureWriteProtocol',
  inputSchema: { capability: 'Access: Device Posture Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureDevicePostureCheckTask

## Related artifacts
- [Protocol](../protocols/AccessDevicePostureWriteProtocol.md) · [Trigger(s)](../triggers/AccessDevicePostureWriteTrigger.md) · [Workflow](../workflows/AccessDevicePostureWriteWorkflow.md)
