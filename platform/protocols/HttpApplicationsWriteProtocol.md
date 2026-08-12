# Protocol: HttpApplicationsWriteProtocol

> Capability #47 — **HTTP Applications Write** · Domain: Security & Edge · Access: `write`

## Purpose
Origin, routing, protocol, headers, timeouts, and keepalive for HTTP applications.

## Interface contract
```typescript
// protocol: HttpApplicationsWriteProtocol
interface HttpApplicationsWriteProtocol extends BaseOperation {
  id: string;
  name: 'HTTP Applications Write';
  accessLevel: 'write';
  category: 'Security & Edge';
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
| Trigger(s) | [`HTTPAppConfigTrigger`](../triggers/HttpApplicationsWriteTrigger.md) |
| Task(s) | [`ManageHTTPApplicationTask`](../tasks/HttpApplicationsWriteTask.md) |
| Workflow | [`HttpApplicationsWriteWorkflow`](../workflows/HttpApplicationsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define origin -> Set routing -> Configure headers -> Deploy -> Test
