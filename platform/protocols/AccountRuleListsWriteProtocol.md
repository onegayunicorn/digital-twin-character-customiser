# Protocol: AccountRuleListsWriteProtocol

> Capability #57 — **Account Rule Lists Write** · Domain: Security & Edge · Access: `write`

## Purpose
IPs, patterns, strings, bulk import/export, and versioning for rule lists.

## Interface contract
```typescript
// protocol: AccountRuleListsWriteProtocol
interface AccountRuleListsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Rule Lists Write';
  accessLevel: 'write';
  category: 'Security & Edge';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`RuleListUpdatedTrigger`](../triggers/AccountRuleListsWriteTrigger.md) |
| Task(s) | [`ManageRuleListTask`](../tasks/AccountRuleListsWriteTask.md) |
| Workflow | [`AccountRuleListsWriteWorkflow`](../workflows/AccountRuleListsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Import items -> Attach -> Deploy -> Monitor
