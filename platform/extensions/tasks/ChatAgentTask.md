# Task: ChatAgentTask

> Capability #148 — **Chat Agent**

Atomic executable unit(s) for this capability.

### Task: RouteIntentTask

```typescript
// task: RouteIntentTask
const RouteIntentTaskSpec: TaskSpecification = {
  taskId: 'RouteIntentTask',
  operationRef: 'ChatAgentProtocol',
  inputSchema: { capability: 'Chat Agent' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RouteIntentTask

### Task: RefuseQuarantinedTask

```typescript
// task: RefuseQuarantinedTask
const RefuseQuarantinedTaskSpec: TaskSpecification = {
  taskId: 'RefuseQuarantinedTask',
  operationRef: 'ChatAgentProtocol',
  inputSchema: { capability: 'Chat Agent' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RefuseQuarantinedTask

## Related artifacts
- [Protocol](../protocols/ChatAgentProtocol.md) · [Trigger(s)](../triggers/ChatAgentTrigger.md) · [Workflow](../workflows/ChatAgentWorkflow.md)
