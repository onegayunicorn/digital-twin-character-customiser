# Task: DnsViewWriteTask

> Capability #32 — **DNS View Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureDNSViewTask

```typescript
// task: ConfigureDNSViewTask
const ConfigureDNSViewTaskSpec: TaskSpecification = {
  taskId: 'ConfigureDNSViewTask',
  operationRef: 'DnsViewWriteProtocol',
  inputSchema: { capability: 'DNS View Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureDNSViewTask

## Related artifacts
- [Protocol](../protocols/DnsViewWriteProtocol.md) · [Trigger(s)](../triggers/DnsViewWriteTrigger.md) · [Workflow](../workflows/DnsViewWriteWorkflow.md)
