# Protocol: OneConnectorsWriteProtocol

> Capability #124 — **One Connectors Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Unified connector management, fleet, and versions.

## Interface contract
```typescript
// protocol: OneConnectorsWriteProtocol
interface OneConnectorsWriteProtocol extends BaseOperation {
  id: string;
  name: 'One Connectors Write';
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
| Trigger(s) | [`ConnectorRegisteredTrigger`](../triggers/OneConnectorsWriteTrigger.md) |
| Task(s) | [`ManageOneConnectorTask`](../tasks/OneConnectorsWriteTask.md) |
| Workflow | [`OneConnectorsWriteWorkflow`](../workflows/OneConnectorsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Configure -> Deploy -> Update -> Monitor
