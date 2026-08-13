# Task: IdentityPqcSigningTask

> Capability #163 — **Identity & PQC Signing**

Atomic executable unit(s) for this capability.

### Task: CreateDidTask

```typescript
// task: CreateDidTask
const CreateDidTaskSpec: TaskSpecification = {
  taskId: 'CreateDidTask',
  operationRef: 'IdentityPqcSigningProtocol',
  inputSchema: { capability: 'Identity & PQC Signing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CreateDidTask

### Task: SignPqcTask

```typescript
// task: SignPqcTask
const SignPqcTaskSpec: TaskSpecification = {
  taskId: 'SignPqcTask',
  operationRef: 'IdentityPqcSigningProtocol',
  inputSchema: { capability: 'Identity & PQC Signing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SignPqcTask

### Task: BindKnoxTask

```typescript
// task: BindKnoxTask
const BindKnoxTaskSpec: TaskSpecification = {
  taskId: 'BindKnoxTask',
  operationRef: 'IdentityPqcSigningProtocol',
  inputSchema: { capability: 'Identity & PQC Signing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute BindKnoxTask

## Related artifacts
- [Protocol](../protocols/IdentityPqcSigningProtocol.md) · [Trigger(s)](../triggers/IdentityPqcSigningTrigger.md) · [Workflow](../workflows/IdentityPqcSigningWorkflow.md)
