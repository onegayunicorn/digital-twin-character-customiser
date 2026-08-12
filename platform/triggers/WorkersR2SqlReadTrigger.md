# Trigger: WorkersR2SqlReadTrigger

> Capability #18 — **Workers R2 SQL Read**

Event source(s) that initiate execution for this capability.

### Trigger: R2SQLQueryTrigger

```typescript
// trigger: R2SQLQueryTrigger
const R2SQLQueryTriggerContract: TriggerContract = {
  triggerId: 'R2SQLQueryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for R2SQLQueryTrigger' },
  actionTarget: 'ExecuteR2SQLQueryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersR2SqlReadProtocol.md) · [Tasks](../tasks/WorkersR2SqlReadTask.md) · [Workflow](../workflows/WorkersR2SqlReadWorkflow.md)
