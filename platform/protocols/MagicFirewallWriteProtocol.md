# Protocol: MagicFirewallWriteProtocol

> Capability #90 — **Magic Firewall Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Packet-level rules, L3/L4, stateful, and logging for Magic Firewall.

## Interface contract
```typescript
// protocol: MagicFirewallWriteProtocol
interface MagicFirewallWriteProtocol extends BaseOperation {
  id: string;
  name: 'Magic Firewall Write';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`MagicFirewallRuleChangeTrigger`](../triggers/MagicFirewallWriteTrigger.md) |
| Task(s) | [`ConfigureMagicFirewallTask`](../tasks/MagicFirewallWriteTask.md) |
| Workflow | [`MagicFirewallWriteWorkflow`](../workflows/MagicFirewallWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define rule -> Set action -> Order -> Deploy -> Test
