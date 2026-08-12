# Protocol: MagicNetworkMonitoringAdminProtocol

> Capability #91 — **Magic Network Monitoring Admin** · Domain: Access & Zero Trust · Access: `admin`

## Purpose
Flow sampling, path analysis, latency, and loss for network monitoring.

## Interface contract
```typescript
// protocol: MagicNetworkMonitoringAdminProtocol
interface MagicNetworkMonitoringAdminProtocol extends BaseOperation {
  id: string;
  name: 'Magic Network Monitoring Admin';
  accessLevel: 'admin';
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
| Trigger(s) | [`NetworkAnomalyTrigger`](../triggers/MagicNetworkMonitoringAdminTrigger.md) |
| Task(s) | [`ManageNetworkMonitoringTask`](../tasks/MagicNetworkMonitoringAdminTask.md) |
| Workflow | [`MagicNetworkMonitoringAdminWorkflow`](../workflows/MagicNetworkMonitoringAdminWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Enable sampling -> Collect -> Analyze -> Alert -> Report
