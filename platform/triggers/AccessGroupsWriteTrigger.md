# Trigger: AccessGroupsWriteTrigger

> Capability #105 — **Access: Groups Write**

Event source(s) that initiate execution for this capability.

### Trigger: GroupMembershipChangedTrigger

```typescript
// trigger: GroupMembershipChangedTrigger
const GroupMembershipChangedTriggerContract: TriggerContract = {
  triggerId: 'GroupMembershipChangedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for GroupMembershipChangedTrigger' },
  actionTarget: 'ManageAccessGroupTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessGroupsWriteProtocol.md) · [Tasks](../tasks/AccessGroupsWriteTask.md) · [Workflow](../workflows/AccessGroupsWriteWorkflow.md)
