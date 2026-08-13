# Task: SovereignKernelTask

> Capability #154 — **Sovereign Kernel**

Atomic executable unit(s) for this capability.

### Task: RegisterPrimitiveTask

```typescript
// task: RegisterPrimitiveTask
const RegisterPrimitiveTaskSpec: TaskSpecification = {
  taskId: 'RegisterPrimitiveTask',
  operationRef: 'SovereignKernelProtocol',
  inputSchema: { capability: 'Sovereign Kernel' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RegisterPrimitiveTask

### Task: AttachPrimitiveTask

```typescript
// task: AttachPrimitiveTask
const AttachPrimitiveTaskSpec: TaskSpecification = {
  taskId: 'AttachPrimitiveTask',
  operationRef: 'SovereignKernelProtocol',
  inputSchema: { capability: 'Sovereign Kernel' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AttachPrimitiveTask

## Related artifacts
- [Protocol](../protocols/SovereignKernelProtocol.md) · [Trigger(s)](../triggers/SovereignKernelTrigger.md) · [Workflow](../workflows/SovereignKernelWorkflow.md)
