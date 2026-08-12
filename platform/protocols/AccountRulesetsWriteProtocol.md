# Protocol: AccountRulesetsWriteProtocol

> Capability #58 — **Account Rulesets Write** · Domain: Security & Edge · Access: `write`

## Purpose
Rule composition, execution order, phase, and expression language for rulesets.

## Interface contract
```typescript
// protocol: AccountRulesetsWriteProtocol
interface AccountRulesetsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Rulesets Write';
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
| Trigger(s) | [`RulesetDeployedTrigger`](../triggers/AccountRulesetsWriteTrigger.md) |
| Task(s) | [`DeployRulesetTask`](../tasks/AccountRulesetsWriteTask.md) |
| Workflow | [`AccountRulesetsWriteWorkflow`](../workflows/AccountRulesetsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Compose -> Validate -> Test -> Deploy -> Activate
