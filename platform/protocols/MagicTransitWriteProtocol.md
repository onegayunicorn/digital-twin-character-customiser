# Protocol: MagicTransitWriteProtocol

> Capability #92 — **Magic Transit Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
IPs, prefixes, DDoS protection, traffic steering, and peering for Magic Transit.

## Interface contract
```typescript
// protocol: MagicTransitWriteProtocol
interface MagicTransitWriteProtocol extends BaseOperation {
  id: string;
  name: 'Magic Transit Write';
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
| Trigger(s) | [`MagicTransitConfigTrigger`](../triggers/MagicTransitWriteTrigger.md) |
| Task(s) | [`ProvisionMagicTransitTask`](../tasks/MagicTransitWriteTask.md) |
| Workflow | [`MagicTransitWriteWorkflow`](../workflows/MagicTransitWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Announce prefix -> Configure -> Activate -> Verify traffic
