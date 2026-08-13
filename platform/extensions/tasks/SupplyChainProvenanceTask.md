# Task: SupplyChainProvenanceTask

> Capability #161 — **Supply Chain Provenance**

Atomic executable unit(s) for this capability.

### Task: SerialiseUnitTask

```typescript
// task: SerialiseUnitTask
const SerialiseUnitTaskSpec: TaskSpecification = {
  taskId: 'SerialiseUnitTask',
  operationRef: 'SupplyChainProvenanceProtocol',
  inputSchema: { capability: 'Supply Chain Provenance' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SerialiseUnitTask

### Task: AppendCustodyEventTask

```typescript
// task: AppendCustodyEventTask
const AppendCustodyEventTaskSpec: TaskSpecification = {
  taskId: 'AppendCustodyEventTask',
  operationRef: 'SupplyChainProvenanceProtocol',
  inputSchema: { capability: 'Supply Chain Provenance' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AppendCustodyEventTask

## Related artifacts
- [Protocol](../protocols/SupplyChainProvenanceProtocol.md) · [Trigger(s)](../triggers/SupplyChainProvenanceTrigger.md) · [Workflow](../workflows/SupplyChainProvenanceWorkflow.md)
