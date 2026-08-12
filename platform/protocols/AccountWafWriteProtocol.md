# Protocol: AccountWafWriteProtocol

> Capability #38 — **Account WAF Write** · Domain: Security & Edge · Access: `write`

## Purpose
Managed rules, custom rules, paranoia level, sensitivity, and actions for WAF.

## Interface contract
```typescript
// protocol: AccountWafWriteProtocol
interface AccountWafWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account WAF Write';
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
| Trigger(s) | [`WAFRuleUpdatedTrigger`](../triggers/AccountWafWriteTrigger.md), [`AttackDetectedTrigger`](../triggers/AccountWafWriteTrigger.md) |
| Task(s) | [`ConfigureWAFTask`](../tasks/AccountWafWriteTask.md) |
| Workflow | [`AccountWafWriteWorkflow`](../workflows/AccountWafWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select ruleset -> Tune -> Test -> Enable -> Monitor
