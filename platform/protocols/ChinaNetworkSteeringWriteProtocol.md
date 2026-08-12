# Protocol: ChinaNetworkSteeringWriteProtocol

> Capability #86 — **China Network Steering Write** · Domain: Load Balancing & Traffic · Access: `write`

## Purpose
Routing, ICP, acceleration, and compliance for China network steering.

## Interface contract
```typescript
// protocol: ChinaNetworkSteeringWriteProtocol
interface ChinaNetworkSteeringWriteProtocol extends BaseOperation {
  id: string;
  name: 'China Network Steering Write';
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
| Trigger(s) | [`SteeringConfigUpdatedTrigger`](../triggers/ChinaNetworkSteeringWriteTrigger.md) |
| Task(s) | [`ConfigureChinaSteeringTask`](../tasks/ChinaNetworkSteeringWriteTask.md) |
| Workflow | [`ChinaNetworkSteeringWriteWorkflow`](../workflows/ChinaNetworkSteeringWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Verify compliance -> Configure routing -> Activate -> Test
