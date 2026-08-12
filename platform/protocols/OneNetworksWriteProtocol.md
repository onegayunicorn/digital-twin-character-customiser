# Protocol: OneNetworksWriteProtocol

> Capability #125 — **One Networks Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Private networks, routes, CIDR, and VPC peering.

## Interface contract
```typescript
// protocol: OneNetworksWriteProtocol
interface OneNetworksWriteProtocol extends BaseOperation {
  id: string;
  name: 'One Networks Write';
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
| Trigger(s) | [`NetworkConfigUpdatedTrigger`](../triggers/OneNetworksWriteTrigger.md) |
| Task(s) | [`ManageOneNetworkTask`](../tasks/OneNetworksWriteTask.md) |
| Workflow | [`OneNetworksWriteWorkflow`](../workflows/OneNetworksWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define CIDR -> Create routes -> Connect -> Verify reachability
