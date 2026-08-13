# Task: WebhookValidatorTask

> Capability #166 — **Webhook Validator**

Atomic executable unit(s) for this capability.

### Task: ValidateSignatureTask

```typescript
// task: ValidateSignatureTask
const ValidateSignatureTaskSpec: TaskSpecification = {
  taskId: 'ValidateSignatureTask',
  operationRef: 'WebhookValidatorProtocol',
  inputSchema: { capability: 'Webhook Validator' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ValidateSignatureTask

### Task: LogWebhookTask

```typescript
// task: LogWebhookTask
const LogWebhookTaskSpec: TaskSpecification = {
  taskId: 'LogWebhookTask',
  operationRef: 'WebhookValidatorProtocol',
  inputSchema: { capability: 'Webhook Validator' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute LogWebhookTask

## Related artifacts
- [Protocol](../protocols/WebhookValidatorProtocol.md) · [Trigger(s)](../triggers/WebhookValidatorTrigger.md) · [Workflow](../workflows/WebhookValidatorWorkflow.md)
