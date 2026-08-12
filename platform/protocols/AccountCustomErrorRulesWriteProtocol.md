# Protocol: AccountCustomErrorRulesWriteProtocol

> Capability #55 — **Account Custom Error Rules Write** · Domain: Security & Edge · Access: `write`

## Purpose
Status codes, response bodies, redirects, and caching for custom error rules.

## Interface contract
```typescript
// protocol: AccountCustomErrorRulesWriteProtocol
interface AccountCustomErrorRulesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Custom Error Rules Write';
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
| Trigger(s) | [`ErrorResponseTrigger`](../triggers/AccountCustomErrorRulesWriteTrigger.md), [`RuleConfigTrigger`](../triggers/AccountCustomErrorRulesWriteTrigger.md) |
| Task(s) | [`CreateCustomErrorRuleTask`](../tasks/AccountCustomErrorRulesWriteTask.md) |
| Workflow | [`AccountCustomErrorRulesWriteWorkflow`](../workflows/AccountCustomErrorRulesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define -> Test -> Order -> Activate
