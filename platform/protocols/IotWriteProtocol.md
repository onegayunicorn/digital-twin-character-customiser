# Protocol: IotWriteProtocol

> Capability #48 — **IOT Write** · Domain: Security & Edge · Access: `write`

## Purpose
Device registry, auth, message routing, and device shadows for IoT.

## Interface contract
```typescript
// protocol: IotWriteProtocol
interface IotWriteProtocol extends BaseOperation {
  id: string;
  name: 'IOT Write';
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
| Trigger(s) | [`DeviceConnectedTrigger`](../triggers/IotWriteTrigger.md), [`DeviceMessageTrigger`](../triggers/IotWriteTrigger.md) |
| Task(s) | [`ManageIoTDeviceTask`](../tasks/IotWriteTask.md) |
| Workflow | [`IotWriteWorkflow`](../workflows/IotWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Auth -> Provision -> Monitor -> Update
