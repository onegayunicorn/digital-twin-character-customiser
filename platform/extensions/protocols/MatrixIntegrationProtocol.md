# Protocol: MatrixIntegrationProtocol

> Capability #149 — **Matrix Integration** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Build adjacency matrices from repo inventories and dependency declarations; graph metrics (density, centrality).

## Interface contract
```typescript
// protocol: MatrixIntegrationProtocol
interface MatrixIntegrationProtocol extends BaseOperation {
  id: string;
  name: 'Matrix Integration';
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
| Trigger(s) | [`InventoryUpdatedTrigger`](../triggers/MatrixIntegrationTrigger.md) |
| Task(s) | [`BuildAdjacencyTask`](../tasks/MatrixIntegrationTask.md), [`ComputeGraphMetricsTask`](../tasks/MatrixIntegrationTask.md) |
| Workflow | [`MatrixIntegrationWorkflow`](../workflows/MatrixIntegrationWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Load inventory -> Build matrix -> Metrics -> Report
