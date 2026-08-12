# Task: OneConnectorCloudflaredWriteTask

> Capability #122 — **One Connector: cloudflared Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureCloudflaredTask

```typescript
// task: ConfigureCloudflaredTask
const ConfigureCloudflaredTaskSpec: TaskSpecification = {
  taskId: 'ConfigureCloudflaredTask',
  operationRef: 'OneConnectorCloudflaredWriteProtocol',
  inputSchema: { capability: 'One Connector: cloudflared Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureCloudflaredTask

## Related artifacts
- [Protocol](../protocols/OneConnectorCloudflaredWriteProtocol.md) · [Trigger(s)](../triggers/OneConnectorCloudflaredWriteTrigger.md) · [Workflow](../workflows/OneConnectorCloudflaredWriteWorkflow.md)
