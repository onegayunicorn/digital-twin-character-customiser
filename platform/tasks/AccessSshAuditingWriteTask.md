# Task: AccessSshAuditingWriteTask

> Capability #116 — **Access: SSH Auditing Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureSSHAuditingTask

```typescript
// task: ConfigureSSHAuditingTask
const ConfigureSSHAuditingTaskSpec: TaskSpecification = {
  taskId: 'ConfigureSSHAuditingTask',
  operationRef: 'AccessSshAuditingWriteProtocol',
  inputSchema: { capability: 'Access: SSH Auditing Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureSSHAuditingTask

## Related artifacts
- [Protocol](../protocols/AccessSshAuditingWriteProtocol.md) · [Trigger(s)](../triggers/AccessSshAuditingWriteTrigger.md) · [Workflow](../workflows/AccessSshAuditingWriteWorkflow.md)
