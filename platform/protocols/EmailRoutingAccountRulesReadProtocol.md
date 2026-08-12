# Protocol: EmailRoutingAccountRulesReadProtocol

> Capability #75 — **Email Routing Account Rules Read** · Domain: Account, Auth, Email & Billing · Access: `read`

## Purpose
Match conditions, actions, forwarding, and aliases for email routing rules.

## Interface contract
```typescript
// protocol: EmailRoutingAccountRulesReadProtocol
interface EmailRoutingAccountRulesReadProtocol extends BaseOperation {
  id: string;
  name: 'Email Routing Account Rules Read';
  accessLevel: 'read';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`EmailRoutingConfigTrigger`](../triggers/EmailRoutingAccountRulesReadTrigger.md) |
| Task(s) | [`ReadEmailRoutingRuleTask`](../tasks/EmailRoutingAccountRulesReadTask.md) |
| Workflow | [`EmailRoutingAccountRulesReadWorkflow`](../workflows/EmailRoutingAccountRulesReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
List -> Validate -> Audit -> Report
