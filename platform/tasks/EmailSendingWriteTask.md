# Task: EmailSendingWriteTask

> Capability #78 — **Email Sending Write**

Atomic executable unit(s) for this capability.

### Task: SendEmailTask

```typescript
// task: SendEmailTask
const SendEmailTaskSpec: TaskSpecification = {
  taskId: 'SendEmailTask',
  operationRef: 'EmailSendingWriteProtocol',
  inputSchema: { capability: 'Email Sending Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SendEmailTask

### Task: ConfigureEmailSenderTask

```typescript
// task: ConfigureEmailSenderTask
const ConfigureEmailSenderTaskSpec: TaskSpecification = {
  taskId: 'ConfigureEmailSenderTask',
  operationRef: 'EmailSendingWriteProtocol',
  inputSchema: { capability: 'Email Sending Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureEmailSenderTask

## Related artifacts
- [Protocol](../protocols/EmailSendingWriteProtocol.md) · [Trigger(s)](../triggers/EmailSendingWriteTrigger.md) · [Workflow](../workflows/EmailSendingWriteWorkflow.md)
