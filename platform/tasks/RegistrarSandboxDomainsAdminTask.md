# Task: RegistrarSandboxDomainsAdminTask

> Capability #34 — **Registrar Sandbox Domains Admin**

Atomic executable unit(s) for this capability.

### Task: ProvisionSandboxDomainTask

```typescript
// task: ProvisionSandboxDomainTask
const ProvisionSandboxDomainTaskSpec: TaskSpecification = {
  taskId: 'ProvisionSandboxDomainTask',
  operationRef: 'RegistrarSandboxDomainsAdminProtocol',
  inputSchema: { capability: 'Registrar Sandbox Domains Admin' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ProvisionSandboxDomainTask

## Related artifacts
- [Protocol](../protocols/RegistrarSandboxDomainsAdminProtocol.md) · [Trigger(s)](../triggers/RegistrarSandboxDomainsAdminTrigger.md) · [Workflow](../workflows/RegistrarSandboxDomainsAdminWorkflow.md)
