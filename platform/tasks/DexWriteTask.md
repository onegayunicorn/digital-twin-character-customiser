# Task: DexWriteTask

> Capability #127 — **DEX Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureDEXTestTask

```typescript
// task: ConfigureDEXTestTask
const ConfigureDEXTestTaskSpec: TaskSpecification = {
  taskId: 'ConfigureDEXTestTask',
  operationRef: 'DexWriteProtocol',
  inputSchema: { capability: 'DEX Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureDEXTestTask

## Related artifacts
- [Protocol](../protocols/DexWriteProtocol.md) · [Trigger(s)](../triggers/DexWriteTrigger.md) · [Workflow](../workflows/DexWriteWorkflow.md)
