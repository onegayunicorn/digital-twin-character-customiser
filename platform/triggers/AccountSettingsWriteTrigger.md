# Trigger: AccountSettingsWriteTrigger

> Capability #66 — **Account Settings Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccountSettingsUpdatedTrigger

```typescript
// trigger: AccountSettingsUpdatedTrigger
const AccountSettingsUpdatedTriggerContract: TriggerContract = {
  triggerId: 'AccountSettingsUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccountSettingsUpdatedTrigger' },
  actionTarget: 'UpdateAccountSettingTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountSettingsWriteProtocol.md) · [Tasks](../tasks/AccountSettingsWriteTask.md) · [Workflow](../workflows/AccountSettingsWriteWorkflow.md)
