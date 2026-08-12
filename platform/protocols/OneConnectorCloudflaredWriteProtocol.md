# Protocol: OneConnectorCloudflaredWriteProtocol

> Capability #122 — **One Connector: cloudflared Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Installation, configuration, tunnels, metrics, and updates for cloudflared.

## Interface contract
```typescript
// protocol: OneConnectorCloudflaredWriteProtocol
interface OneConnectorCloudflaredWriteProtocol extends BaseOperation {
  id: string;
  name: 'One Connector: cloudflared Write';
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
| Trigger(s) | [`CloudflaredConfigUpdatedTrigger`](../triggers/OneConnectorCloudflaredWriteTrigger.md) |
| Task(s) | [`ConfigureCloudflaredTask`](../tasks/OneConnectorCloudflaredWriteTask.md) |
| Workflow | [`OneConnectorCloudflaredWriteWorkflow`](../workflows/OneConnectorCloudflaredWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Install -> Authenticate -> Create tunnel -> Run -> Monitor
