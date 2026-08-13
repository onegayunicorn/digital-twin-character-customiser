# Task: ProcurementEngineTask

> Capability #158 — **Procurement Engine**

Atomic executable unit(s) for this capability.

### Task: EvaluateBidsTask

```typescript
// task: EvaluateBidsTask
const EvaluateBidsTaskSpec: TaskSpecification = {
  taskId: 'EvaluateBidsTask',
  operationRef: 'ProcurementEngineProtocol',
  inputSchema: { capability: 'Procurement Engine' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute EvaluateBidsTask

### Task: ThreeWayMatchTask

```typescript
// task: ThreeWayMatchTask
const ThreeWayMatchTaskSpec: TaskSpecification = {
  taskId: 'ThreeWayMatchTask',
  operationRef: 'ProcurementEngineProtocol',
  inputSchema: { capability: 'Procurement Engine' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ThreeWayMatchTask

## Related artifacts
- [Protocol](../protocols/ProcurementEngineProtocol.md) · [Trigger(s)](../triggers/ProcurementEngineTrigger.md) · [Workflow](../workflows/ProcurementEngineWorkflow.md)
