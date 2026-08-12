# Protocol: TunnelWriteProtocol

> Capability #119 — **Tunnel Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
cloudflared ingress, configuration, warp-routing, and HA for tunnels.

## Interface contract
```typescript
// protocol: TunnelWriteProtocol
interface TunnelWriteProtocol extends BaseOperation {
  id: string;
  name: 'Tunnel Write';
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
| Trigger(s) | [`TunnelConfigTrigger`](../triggers/TunnelWriteTrigger.md), [`TunnelConnectedTrigger`](../triggers/TunnelWriteTrigger.md) |
| Task(s) | [`ManageTunnelTask`](../tasks/TunnelWriteTask.md) |
| Workflow | [`TunnelWriteWorkflow`](../workflows/TunnelWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Install connector -> Configure ingress -> Run -> Verify
