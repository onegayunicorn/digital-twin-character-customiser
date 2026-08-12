# Task: MessagingReadTask

> Capability #21 — **Messaging Read**

Atomic executable unit(s) for this capability.

### Task: ReadMessageTask

```typescript
// task: ReadMessageTask
const ReadMessageTaskSpec: TaskSpecification = {
  taskId: 'ReadMessageTask',
  operationRef: 'MessagingReadProtocol',
  inputSchema: { capability: 'Messaging Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadMessageTask

### Task: PollMessagesTask

```typescript
// task: PollMessagesTask
const PollMessagesTaskSpec: TaskSpecification = {
  taskId: 'PollMessagesTask',
  operationRef: 'MessagingReadProtocol',
  inputSchema: { capability: 'Messaging Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute PollMessagesTask

## Related artifacts
- [Protocol](../protocols/MessagingReadProtocol.md) · [Trigger(s)](../triggers/MessagingReadTrigger.md) · [Workflow](../workflows/MessagingReadWorkflow.md)
