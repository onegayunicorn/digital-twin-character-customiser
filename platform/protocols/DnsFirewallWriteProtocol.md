# Protocol: DnsFirewallWriteProtocol

> Capability #31 — **DNS Firewall Write** · Domain: Domain, DNS & Networking · Access: `write`

## Purpose
Allowlists/blocklists, response filtering, and rate limits for DNS firewall.

## Interface contract
```typescript
// protocol: DnsFirewallWriteProtocol
interface DnsFirewallWriteProtocol extends BaseOperation {
  id: string;
  name: 'DNS Firewall Write';
  accessLevel: 'write';
  category: 'Domain, DNS & Networking';
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
| Trigger(s) | [`DNSQueryTrigger`](../triggers/DnsFirewallWriteTrigger.md), [`DNSFirewallRuleChangeTrigger`](../triggers/DnsFirewallWriteTrigger.md) |
| Task(s) | [`ManageDNSFirewallRuleTask`](../tasks/DnsFirewallWriteTask.md) |
| Workflow | [`DnsFirewallWriteWorkflow`](../workflows/DnsFirewallWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define rule -> Attach -> Test -> Activate
