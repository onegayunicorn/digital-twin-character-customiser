# Task: EntityRegistryTask

> Capability #160 — **Entity Registry**

Atomic executable unit(s) for this capability.

### Task: RegisterEntityTask

```typescript
// task: RegisterEntityTask
const RegisterEntityTaskSpec: TaskSpecification = {
  taskId: 'RegisterEntityTask',
  operationRef: 'EntityRegistryProtocol',
  inputSchema: { capability: 'Entity Registry' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RegisterEntityTask

### Task: AddBeneficialOwnerTask

```typescript
// task: AddBeneficialOwnerTask
const AddBeneficialOwnerTaskSpec: TaskSpecification = {
  taskId: 'AddBeneficialOwnerTask',
  operationRef: 'EntityRegistryProtocol',
  inputSchema: { capability: 'Entity Registry' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AddBeneficialOwnerTask

## Related artifacts
- [Protocol](../protocols/EntityRegistryProtocol.md) · [Trigger(s)](../triggers/EntityRegistryTrigger.md) · [Workflow](../workflows/EntityRegistryWorkflow.md)
