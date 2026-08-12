# Task: ZeroTrustPiiReadTask

> Capability #131 — **Zero Trust: PII Read**

Atomic executable unit(s) for this capability.

### Task: ReadZeroTrustPIITask

```typescript
// task: ReadZeroTrustPIITask
const ReadZeroTrustPIITaskSpec: TaskSpecification = {
  taskId: 'ReadZeroTrustPIITask',
  operationRef: 'ZeroTrustPiiReadProtocol',
  inputSchema: { capability: 'Zero Trust: PII Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadZeroTrustPIITask

## Related artifacts
- [Protocol](../protocols/ZeroTrustPiiReadProtocol.md) · [Trigger(s)](../triggers/ZeroTrustPiiReadTrigger.md) · [Workflow](../workflows/ZeroTrustPiiReadWorkflow.md)
