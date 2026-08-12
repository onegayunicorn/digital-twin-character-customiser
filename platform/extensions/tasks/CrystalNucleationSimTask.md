# Task: CrystalNucleationSimTask

> Capability #135 — **Crystal Nucleation Sim**

Atomic executable unit(s) for this capability.

### Task: NucleateCrystalTask

```typescript
// task: NucleateCrystalTask
const NucleateCrystalTaskSpec: TaskSpecification = {
  taskId: 'NucleateCrystalTask',
  operationRef: 'CrystalNucleationSimProtocol',
  inputSchema: { capability: 'Crystal Nucleation Sim' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute NucleateCrystalTask

### Task: AccreteMassTask

```typescript
// task: AccreteMassTask
const AccreteMassTaskSpec: TaskSpecification = {
  taskId: 'AccreteMassTask',
  operationRef: 'CrystalNucleationSimProtocol',
  inputSchema: { capability: 'Crystal Nucleation Sim' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AccreteMassTask

## Related artifacts
- [Protocol](../protocols/CrystalNucleationSimProtocol.md) · [Trigger(s)](../triggers/CrystalNucleationSimTrigger.md) · [Workflow](../workflows/CrystalNucleationSimWorkflow.md)
