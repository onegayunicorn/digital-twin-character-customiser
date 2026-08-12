# Task: ScimProvisioningTask

> Capability #71 — **SCIM Provisioning**

Atomic executable unit(s) for this capability.

### Task: ProvisionSCIMResourceTask

```typescript
// task: ProvisionSCIMResourceTask
const ProvisionSCIMResourceTaskSpec: TaskSpecification = {
  taskId: 'ProvisionSCIMResourceTask',
  operationRef: 'ScimProvisioningProtocol',
  inputSchema: { capability: 'SCIM Provisioning' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ProvisionSCIMResourceTask

## Related artifacts
- [Protocol](../protocols/ScimProvisioningProtocol.md) · [Trigger(s)](../triggers/ScimProvisioningTrigger.md) · [Workflow](../workflows/ScimProvisioningWorkflow.md)
