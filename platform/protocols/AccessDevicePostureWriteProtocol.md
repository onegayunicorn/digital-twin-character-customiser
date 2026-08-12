# Protocol: AccessDevicePostureWriteProtocol

> Capability #102 — **Access: Device Posture Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Checks, OS, disk encryption, firewall, and client version for device posture.

## Interface contract
```typescript
// protocol: AccessDevicePostureWriteProtocol
interface AccessDevicePostureWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Device Posture Write';
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
| Trigger(s) | [`DevicePostureUpdatedTrigger`](../triggers/AccessDevicePostureWriteTrigger.md) |
| Task(s) | [`ConfigureDevicePostureCheckTask`](../tasks/AccessDevicePostureWriteTask.md) |
| Workflow | [`AccessDevicePostureWriteWorkflow`](../workflows/AccessDevicePostureWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define checks -> Collect -> Evaluate -> Allow/Block
