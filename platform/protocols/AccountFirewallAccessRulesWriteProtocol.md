# Protocol: AccountFirewallAccessRulesWriteProtocol

> Capability #36 — **Account Firewall Access Rules Write** · Domain: Security & Edge · Access: `write`

## Purpose
IP, ASN, country, URI, and user-agent matching with actions for access rules.

## Interface contract
```typescript
// protocol: AccountFirewallAccessRulesWriteProtocol
interface AccountFirewallAccessRulesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Firewall Access Rules Write';
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
| Trigger(s) | [`FirewallRuleChangeTrigger`](../triggers/AccountFirewallAccessRulesWriteTrigger.md), [`AttackDetectedTrigger`](../triggers/AccountFirewallAccessRulesWriteTrigger.md) |
| Task(s) | [`CreateFirewallRuleTask`](../tasks/AccountFirewallAccessRulesWriteTask.md) |
| Workflow | [`AccountFirewallAccessRulesWriteWorkflow`](../workflows/AccountFirewallAccessRulesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define -> Validate -> Order -> Apply -> Test
