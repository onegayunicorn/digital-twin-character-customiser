# Task: TrustAndSafetyWriteTask

> Capability #52 — **Trust and Safety Write**

Atomic executable unit(s) for this capability.

### Task: UpdateTrustSafetyPolicyTask

```typescript
// task: UpdateTrustSafetyPolicyTask
const UpdateTrustSafetyPolicyTaskSpec: TaskSpecification = {
  taskId: 'UpdateTrustSafetyPolicyTask',
  operationRef: 'TrustAndSafetyWriteProtocol',
  inputSchema: { capability: 'Trust and Safety Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateTrustSafetyPolicyTask

## Related artifacts
- [Protocol](../protocols/TrustAndSafetyWriteProtocol.md) · [Trigger(s)](../triggers/TrustAndSafetyWriteTrigger.md) · [Workflow](../workflows/TrustAndSafetyWriteWorkflow.md)
