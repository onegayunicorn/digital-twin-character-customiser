# Protocol: OneConnectorWarpWriteProtocol

> Capability #123 — **One Connector: WARP Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Client configuration, encryption, split tunnel, and firewall for WARP.

## Interface contract
```typescript
// protocol: OneConnectorWarpWriteProtocol
interface OneConnectorWarpWriteProtocol extends BaseOperation {
  id: string;
  name: 'One Connector: WARP Write';
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
| Trigger(s) | [`WARPConfigUpdatedTrigger`](../triggers/OneConnectorWarpWriteTrigger.md) |
| Task(s) | [`ConfigureWARPConnectorTask`](../tasks/OneConnectorWarpWriteTask.md) |
| Workflow | [`OneConnectorWarpWriteWorkflow`](../workflows/OneConnectorWarpWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Install -> Configure -> Enable -> Connect -> Verify
