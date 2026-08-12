# Protocol: MagicWanWriteProtocol

> Capability #93 — **Magic WAN Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Site-to-cloud, site-to-site, GRE/IPsec, and policies for Magic WAN.

## Interface contract
```typescript
// protocol: MagicWanWriteProtocol
interface MagicWanWriteProtocol extends BaseOperation {
  id: string;
  name: 'Magic WAN Write';
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
| Trigger(s) | [`WANConnectionTrigger`](../triggers/MagicWanWriteTrigger.md) |
| Task(s) | [`ConfigureMagicWANTask`](../tasks/MagicWanWriteTask.md) |
| Workflow | [`MagicWanWriteWorkflow`](../workflows/MagicWanWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create tunnels -> Establish -> Configure routing -> Activate
