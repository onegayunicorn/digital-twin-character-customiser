# Trigger: RepoSandboxTrigger

> Capability #152 — **Repo Sandbox**

Event source(s) that initiate execution for this capability.

### Trigger: RepoInventoriedTrigger

```typescript
// trigger: RepoInventoriedTrigger
const RepoInventoriedTriggerContract: TriggerContract = {
  triggerId: 'RepoInventoriedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RepoInventoriedTrigger' },
  actionTarget: 'GenerateSandboxTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/RepoSandboxProtocol.md) · [Tasks](../tasks/RepoSandboxTask.md) · [Workflow](../workflows/RepoSandboxWorkflow.md)
