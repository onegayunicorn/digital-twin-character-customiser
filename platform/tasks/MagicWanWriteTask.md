# Task: MagicWanWriteTask

> Capability #93 — **Magic WAN Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureMagicWANTask

```typescript
// task: ConfigureMagicWANTask
const ConfigureMagicWANTaskSpec: TaskSpecification = {
  taskId: 'ConfigureMagicWANTask',
  operationRef: 'MagicWanWriteProtocol',
  inputSchema: { capability: 'Magic WAN Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureMagicWANTask

## Related artifacts
- [Protocol](../protocols/MagicWanWriteProtocol.md) · [Trigger(s)](../triggers/MagicWanWriteTrigger.md) · [Workflow](../workflows/MagicWanWriteWorkflow.md)
