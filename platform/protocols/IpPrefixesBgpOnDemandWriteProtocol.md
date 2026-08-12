# Protocol: IpPrefixesBgpOnDemandWriteProtocol

> Capability #89 — **IP Prefixes: BGP On Demand Write** · Domain: Load Balancing & Traffic · Access: `write`

## Purpose
Dynamic route advertisement, withdrawal, and scheduling.

## Interface contract
```typescript
// protocol: IpPrefixesBgpOnDemandWriteProtocol
interface IpPrefixesBgpOnDemandWriteProtocol extends BaseOperation {
  id: string;
  name: 'IP Prefixes: BGP On Demand Write';
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
| Trigger(s) | [`BGPTriggerEventTrigger`](../triggers/IpPrefixesBgpOnDemandWriteTrigger.md) |
| Task(s) | [`ControlBGPAnnouncementTask`](../tasks/IpPrefixesBgpOnDemandWriteTask.md) |
| Workflow | [`IpPrefixesBgpOnDemandWriteWorkflow`](../workflows/IpPrefixesBgpOnDemandWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Request -> Validate -> Announce -> Maintain -> Withdraw
