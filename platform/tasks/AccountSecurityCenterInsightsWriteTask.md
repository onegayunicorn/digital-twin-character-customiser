# Task: AccountSecurityCenterInsightsWriteTask

> Capability #37 — **Account Security Center Insights Write**

Atomic executable unit(s) for this capability.

### Task: UpdateSecurityInsightTask

```typescript
// task: UpdateSecurityInsightTask
const UpdateSecurityInsightTaskSpec: TaskSpecification = {
  taskId: 'UpdateSecurityInsightTask',
  operationRef: 'AccountSecurityCenterInsightsWriteProtocol',
  inputSchema: { capability: 'Account Security Center Insights Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateSecurityInsightTask

## Related artifacts
- [Protocol](../protocols/AccountSecurityCenterInsightsWriteProtocol.md) · [Trigger(s)](../triggers/AccountSecurityCenterInsightsWriteTrigger.md) · [Workflow](../workflows/AccountSecurityCenterInsightsWriteWorkflow.md)
