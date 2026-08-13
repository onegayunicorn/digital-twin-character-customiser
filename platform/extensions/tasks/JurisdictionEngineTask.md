# Task: JurisdictionEngineTask

> Capability #155 — **Jurisdiction Engine**

Atomic executable unit(s) for this capability.

### Task: ClassifyJurisdictionTask

```typescript
// task: ClassifyJurisdictionTask
const ClassifyJurisdictionTaskSpec: TaskSpecification = {
  taskId: 'ClassifyJurisdictionTask',
  operationRef: 'JurisdictionEngineProtocol',
  inputSchema: { capability: 'Jurisdiction Engine' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ClassifyJurisdictionTask

### Task: ResolveProfileTask

```typescript
// task: ResolveProfileTask
const ResolveProfileTaskSpec: TaskSpecification = {
  taskId: 'ResolveProfileTask',
  operationRef: 'JurisdictionEngineProtocol',
  inputSchema: { capability: 'Jurisdiction Engine' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ResolveProfileTask

## Related artifacts
- [Protocol](../protocols/JurisdictionEngineProtocol.md) · [Trigger(s)](../triggers/JurisdictionEngineTrigger.md) · [Workflow](../workflows/JurisdictionEngineWorkflow.md)
