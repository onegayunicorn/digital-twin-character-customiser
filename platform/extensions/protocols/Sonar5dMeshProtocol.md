# Protocol: Sonar5dMeshProtocol

> Capability #141 — **Sonar 5D Mesh** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Crystal-mesh geometry (diamond-cubic lattice, OBJ export) + 5D sonar sweep (x,y,z,time,intensity echo field).

## Interface contract
```typescript
// protocol: Sonar5dMeshProtocol
interface Sonar5dMeshProtocol extends BaseOperation {
  id: string;
  name: 'Sonar 5D Mesh';
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
| Trigger(s) | [`MeshRequestedTrigger`](../triggers/Sonar5dMeshTrigger.md), [`SweepTrigger`](../triggers/Sonar5dMeshTrigger.md) |
| Task(s) | [`GenerateMeshTask`](../tasks/Sonar5dMeshTask.md), [`RunSweepTask`](../tasks/Sonar5dMeshTask.md), [`ExportObjTask`](../tasks/Sonar5dMeshTask.md) |
| Workflow | [`Sonar5dMeshWorkflow`](../workflows/Sonar5dMeshWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Generate -> Invariants -> Sweep -> Export -> Visualize
