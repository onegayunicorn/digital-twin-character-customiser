# Trigger: WorkersScriptsWriteTrigger

> Capability #8 — **Workers Scripts Write**

Event source(s) that initiate execution for this capability.

### Trigger: ScriptUploadedTrigger

```typescript
// trigger: ScriptUploadedTrigger
const ScriptUploadedTriggerContract: TriggerContract = {
  triggerId: 'ScriptUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScriptUploadedTrigger' },
  actionTarget: 'UploadUpdateWorkerScriptTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: GitPushTrigger

```typescript
// trigger: GitPushTrigger
const GitPushTriggerContract: TriggerContract = {
  triggerId: 'GitPushTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for GitPushTrigger' },
  actionTarget: 'UploadUpdateWorkerScriptTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersScriptsWriteProtocol.md) · [Tasks](../tasks/WorkersScriptsWriteTask.md) · [Workflow](../workflows/WorkersScriptsWriteWorkflow.md)
