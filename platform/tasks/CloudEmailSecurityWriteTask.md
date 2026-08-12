# Task: CloudEmailSecurityWriteTask

> Capability #74 — **Cloud Email Security: Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureEmailSecurityPolicyTask

```typescript
// task: ConfigureEmailSecurityPolicyTask
const ConfigureEmailSecurityPolicyTaskSpec: TaskSpecification = {
  taskId: 'ConfigureEmailSecurityPolicyTask',
  operationRef: 'CloudEmailSecurityWriteProtocol',
  inputSchema: { capability: 'Cloud Email Security: Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureEmailSecurityPolicyTask

## Related artifacts
- [Protocol](../protocols/CloudEmailSecurityWriteProtocol.md) · [Trigger(s)](../triggers/CloudEmailSecurityWriteTrigger.md) · [Workflow](../workflows/CloudEmailSecurityWriteWorkflow.md)
