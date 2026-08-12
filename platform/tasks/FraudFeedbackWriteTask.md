# Task: FraudFeedbackWriteTask

> Capability #46 — **Fraud Feedback Write**

Atomic executable unit(s) for this capability.

### Task: SubmitFraudFeedbackTask

```typescript
// task: SubmitFraudFeedbackTask
const SubmitFraudFeedbackTaskSpec: TaskSpecification = {
  taskId: 'SubmitFraudFeedbackTask',
  operationRef: 'FraudFeedbackWriteProtocol',
  inputSchema: { capability: 'Fraud Feedback Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SubmitFraudFeedbackTask

## Related artifacts
- [Protocol](../protocols/FraudFeedbackWriteProtocol.md) · [Trigger(s)](../triggers/FraudFeedbackWriteTrigger.md) · [Workflow](../workflows/FraudFeedbackWriteWorkflow.md)
