# Task: AccountAnalyticsReadTask

> Capability #98 — **Account Analytics Read**

Atomic executable unit(s) for this capability.

### Task: QueryAnalyticsTask

```typescript
// task: QueryAnalyticsTask
const QueryAnalyticsTaskSpec: TaskSpecification = {
  taskId: 'QueryAnalyticsTask',
  operationRef: 'AccountAnalyticsReadProtocol',
  inputSchema: { capability: 'Account Analytics Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute QueryAnalyticsTask

## Related artifacts
- [Protocol](../protocols/AccountAnalyticsReadProtocol.md) · [Trigger(s)](../triggers/AccountAnalyticsReadTrigger.md) · [Workflow](../workflows/AccountAnalyticsReadWorkflow.md)
