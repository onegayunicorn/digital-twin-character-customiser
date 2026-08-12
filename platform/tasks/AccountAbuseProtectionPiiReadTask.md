# Task: AccountAbuseProtectionPiiReadTask

> Capability #35 — **Account Abuse Protection PII Read**

Atomic executable unit(s) for this capability.

### Task: ReadAbusePIIRecordTask

```typescript
// task: ReadAbusePIIRecordTask
const ReadAbusePIIRecordTaskSpec: TaskSpecification = {
  taskId: 'ReadAbusePIIRecordTask',
  operationRef: 'AccountAbuseProtectionPiiReadProtocol',
  inputSchema: { capability: 'Account Abuse Protection PII Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadAbusePIIRecordTask

## Related artifacts
- [Protocol](../protocols/AccountAbuseProtectionPiiReadProtocol.md) · [Trigger(s)](../triggers/AccountAbuseProtectionPiiReadTrigger.md) · [Workflow](../workflows/AccountAbuseProtectionPiiReadWorkflow.md)
