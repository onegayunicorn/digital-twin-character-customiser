# Protocol: WorkersContainersWriteProtocol

> Capability #9 — **Workers Containers Write** · Domain: Workers, Compute & Code · Access: `write`

## Purpose
OCI artifacts, registry auth, resource allocation, and scaling for container workloads.

## Interface contract
```typescript
// protocol: WorkersContainersWriteProtocol
interface WorkersContainersWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers Containers Write';
  accessLevel: 'write';
  category: 'Workers, Compute & Code';
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
| Trigger(s) | [`ContainerImagePushedTrigger`](../triggers/WorkersContainersWriteTrigger.md), [`ScaleEventTrigger`](../triggers/WorkersContainersWriteTrigger.md) |
| Task(s) | [`DeployWorkerContainerTask`](../tasks/WorkersContainersWriteTask.md) |
| Workflow | [`WorkersContainersWriteWorkflow`](../workflows/WorkersContainersWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Pull image -> Validate -> Deploy -> Start -> Health check
