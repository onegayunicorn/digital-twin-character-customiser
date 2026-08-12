# Task: ChinaNetworkSteeringWriteTask

> Capability #86 — **China Network Steering Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureChinaSteeringTask

```typescript
// task: ConfigureChinaSteeringTask
const ConfigureChinaSteeringTaskSpec: TaskSpecification = {
  taskId: 'ConfigureChinaSteeringTask',
  operationRef: 'ChinaNetworkSteeringWriteProtocol',
  inputSchema: { capability: 'China Network Steering Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureChinaSteeringTask

## Related artifacts
- [Protocol](../protocols/ChinaNetworkSteeringWriteProtocol.md) · [Trigger(s)](../triggers/ChinaNetworkSteeringWriteTrigger.md) · [Workflow](../workflows/ChinaNetworkSteeringWriteWorkflow.md)
