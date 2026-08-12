# Protocol: DdosProtectionWriteProtocol

> Capability #43 — **DDoS Protection Write** · Domain: Security & Edge · Access: `write`

## Purpose
Detection thresholds, mitigation actions, and auto-mitigation for DDoS protection.

## Interface contract
```typescript
// protocol: DdosProtectionWriteProtocol
interface DdosProtectionWriteProtocol extends BaseOperation {
  id: string;
  name: 'DDoS Protection Write';
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
| Trigger(s) | [`DDoSEventDetectedTrigger`](../triggers/DdosProtectionWriteTrigger.md) |
| Task(s) | [`ConfigureDDoSProtectionTask`](../tasks/DdosProtectionWriteTask.md) |
| Workflow | [`DdosProtectionWriteWorkflow`](../workflows/DdosProtectionWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Detect -> Classify -> Activate mitigation -> Monitor -> Release
