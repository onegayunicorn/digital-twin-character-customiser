# Task: IotWriteTask

> Capability #48 — **IOT Write**

Atomic executable unit(s) for this capability.

### Task: ManageIoTDeviceTask

```typescript
// task: ManageIoTDeviceTask
const ManageIoTDeviceTaskSpec: TaskSpecification = {
  taskId: 'ManageIoTDeviceTask',
  operationRef: 'IotWriteProtocol',
  inputSchema: { capability: 'IOT Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageIoTDeviceTask

## Related artifacts
- [Protocol](../protocols/IotWriteProtocol.md) · [Trigger(s)](../triggers/IotWriteTrigger.md) · [Workflow](../workflows/IotWriteWorkflow.md)
