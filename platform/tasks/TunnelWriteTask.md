# Task: TunnelWriteTask

> Capability #119 — **Tunnel Write**

Atomic executable unit(s) for this capability.

### Task: ManageTunnelTask

```typescript
// task: ManageTunnelTask
const ManageTunnelTaskSpec: TaskSpecification = {
  taskId: 'ManageTunnelTask',
  operationRef: 'TunnelWriteProtocol',
  inputSchema: { capability: 'Tunnel Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageTunnelTask

## Related artifacts
- [Protocol](../protocols/TunnelWriteProtocol.md) · [Trigger(s)](../triggers/TunnelWriteTrigger.md) · [Workflow](../workflows/TunnelWriteWorkflow.md)
