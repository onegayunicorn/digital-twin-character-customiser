# Task: IntelWriteTask

> Capability #96 — **Intel Write**

Atomic executable unit(s) for this capability.

### Task: UpdateThreatIntelTask

```typescript
// task: UpdateThreatIntelTask
const UpdateThreatIntelTaskSpec: TaskSpecification = {
  taskId: 'UpdateThreatIntelTask',
  operationRef: 'IntelWriteProtocol',
  inputSchema: { capability: 'Intel Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateThreatIntelTask

## Related artifacts
- [Protocol](../protocols/IntelWriteProtocol.md) · [Trigger(s)](../triggers/IntelWriteTrigger.md) · [Workflow](../workflows/IntelWriteWorkflow.md)
