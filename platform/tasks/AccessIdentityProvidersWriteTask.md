# Task: AccessIdentityProvidersWriteTask

> Capability #104 — **Access: Identity Providers Write**

Atomic executable unit(s) for this capability.

### Task: RegisterIdentityProviderTask

```typescript
// task: RegisterIdentityProviderTask
const RegisterIdentityProviderTaskSpec: TaskSpecification = {
  taskId: 'RegisterIdentityProviderTask',
  operationRef: 'AccessIdentityProvidersWriteProtocol',
  inputSchema: { capability: 'Access: Identity Providers Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RegisterIdentityProviderTask

## Related artifacts
- [Protocol](../protocols/AccessIdentityProvidersWriteProtocol.md) · [Trigger(s)](../triggers/AccessIdentityProvidersWriteTrigger.md) · [Workflow](../workflows/AccessIdentityProvidersWriteWorkflow.md)
