# Protocol: LoadBalancersAccountWriteProtocol

> Capability #83 — **Load Balancers Account Write** · Domain: Load Balancing & Traffic · Access: `write`

## Purpose
Pools, origins, steering, failover, and health checks for load balancers.

## Interface contract
```typescript
// protocol: LoadBalancersAccountWriteProtocol
interface LoadBalancersAccountWriteProtocol extends BaseOperation {
  id: string;
  name: 'Load Balancers Account Write';
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
| Trigger(s) | [`LoadBalancerConfigTrigger`](../triggers/LoadBalancersAccountWriteTrigger.md), [`PoolHealthChangeTrigger`](../triggers/LoadBalancersAccountWriteTrigger.md) |
| Task(s) | [`ConfigureLoadBalancerTask`](../tasks/LoadBalancersAccountWriteTask.md) |
| Workflow | [`LoadBalancersAccountWriteWorkflow`](../workflows/LoadBalancersAccountWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create LB -> Define pools -> Attach health checks -> Deploy -> Test
