# Protocol: IpPrefixesWriteProtocol

> Capability #88 — **IP Prefixes: Write** · Domain: Load Balancing & Traffic · Access: `write`

## Purpose
Announced prefixes, origins, ASNs, RPKI, and authorization.

## Interface contract
```typescript
// protocol: IpPrefixesWriteProtocol
interface IpPrefixesWriteProtocol extends BaseOperation {
  id: string;
  name: 'IP Prefixes: Write';
  accessLevel: 'write';
  category: 'Load Balancing & Traffic';
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
| Trigger(s) | [`PrefixAnnouncementTrigger`](../triggers/IpPrefixesWriteTrigger.md) |
| Task(s) | [`ManageIPPrefixTask`](../tasks/IpPrefixesWriteTask.md) |
| Workflow | [`IpPrefixesWriteWorkflow`](../workflows/IpPrefixesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Authorize -> Announce -> Validate -> Monitor
