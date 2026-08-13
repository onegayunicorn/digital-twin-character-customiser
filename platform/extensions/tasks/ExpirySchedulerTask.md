# Task: ExpirySchedulerTask

> Capability #167 — **Expiry Scheduler**

Atomic executable unit(s) for this capability.

### Task: RegisterAuthorizationTask

```typescript
// task: RegisterAuthorizationTask
const RegisterAuthorizationTaskSpec: TaskSpecification = {
  taskId: 'RegisterAuthorizationTask',
  operationRef: 'ExpirySchedulerProtocol',
  inputSchema: { capability: 'Expiry Scheduler' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RegisterAuthorizationTask

### Task: RunExpiryTickTask

```typescript
// task: RunExpiryTickTask
const RunExpiryTickTaskSpec: TaskSpecification = {
  taskId: 'RunExpiryTickTask',
  operationRef: 'ExpirySchedulerProtocol',
  inputSchema: { capability: 'Expiry Scheduler' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunExpiryTickTask

## Related artifacts
- [Protocol](../protocols/ExpirySchedulerProtocol.md) · [Trigger(s)](../triggers/ExpirySchedulerTrigger.md) · [Workflow](../workflows/ExpirySchedulerWorkflow.md)
