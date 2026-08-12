# Task: LoadBalancersAccountWriteTask

> Capability #83 — **Load Balancers Account Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureLoadBalancerTask

```typescript
// task: ConfigureLoadBalancerTask
const ConfigureLoadBalancerTaskSpec: TaskSpecification = {
  taskId: 'ConfigureLoadBalancerTask',
  operationRef: 'LoadBalancersAccountWriteProtocol',
  inputSchema: { capability: 'Load Balancers Account Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureLoadBalancerTask

## Related artifacts
- [Protocol](../protocols/LoadBalancersAccountWriteProtocol.md) · [Trigger(s)](../triggers/LoadBalancersAccountWriteTrigger.md) · [Workflow](../workflows/LoadBalancersAccountWriteWorkflow.md)
