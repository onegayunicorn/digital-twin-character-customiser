# Protocol: DlsWriteProtocol

> Capability #126 — **DLS: Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Data loss prevention patterns, detection rules, and redaction.

## Interface contract
```typescript
// protocol: DlsWriteProtocol
interface DlsWriteProtocol extends BaseOperation {
  id: string;
  name: 'DLS: Write';
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
| Trigger(s) | [`DLPRuleUpdatedTrigger`](../triggers/DlsWriteTrigger.md), [`SensitiveDataDetectedTrigger`](../triggers/DlsWriteTrigger.md) |
| Task(s) | [`ConfigureDLSPolicyTask`](../tasks/DlsWriteTask.md) |
| Workflow | [`DlsWriteWorkflow`](../workflows/DlsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define patterns -> Scan -> Detect -> Redact/Block -> Log/Alert
