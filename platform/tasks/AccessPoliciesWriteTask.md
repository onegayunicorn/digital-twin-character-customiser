# Task: AccessPoliciesWriteTask

> Capability #110 — **Access: Policies Write**

Atomic executable unit(s) for this capability.

### Task: CreateAccessPolicyTask

```typescript
// task: CreateAccessPolicyTask
const CreateAccessPolicyTaskSpec: TaskSpecification = {
  taskId: 'CreateAccessPolicyTask',
  operationRef: 'AccessPoliciesWriteProtocol',
  inputSchema: { capability: 'Access: Policies Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CreateAccessPolicyTask

## Related artifacts
- [Protocol](../protocols/AccessPoliciesWriteProtocol.md) · [Trigger(s)](../triggers/AccessPoliciesWriteTrigger.md) · [Workflow](../workflows/AccessPoliciesWriteWorkflow.md)
