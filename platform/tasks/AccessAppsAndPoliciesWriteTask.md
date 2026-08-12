# Task: AccessAppsAndPoliciesWriteTask

> Capability #99 — **Access: Apps and Policies Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessAppAndPolicyTask

```typescript
// task: ManageAccessAppAndPolicyTask
const ManageAccessAppAndPolicyTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessAppAndPolicyTask',
  operationRef: 'AccessAppsAndPoliciesWriteProtocol',
  inputSchema: { capability: 'Access: Apps and Policies Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessAppAndPolicyTask

## Related artifacts
- [Protocol](../protocols/AccessAppsAndPoliciesWriteProtocol.md) · [Trigger(s)](../triggers/AccessAppsAndPoliciesWriteTrigger.md) · [Workflow](../workflows/AccessAppsAndPoliciesWriteWorkflow.md)
