# Protocol: UrlScannerWriteProtocol

> Capability #54 — **URL Scanner Write** · Domain: Security & Edge · Access: `write`

## Purpose
Scan targets, frequency, checks, and risk categories for URL scanning.

## Interface contract
```typescript
// protocol: UrlScannerWriteProtocol
interface UrlScannerWriteProtocol extends BaseOperation {
  id: string;
  name: 'URL Scanner Write';
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
| Trigger(s) | [`URLSubmittedTrigger`](../triggers/UrlScannerWriteTrigger.md), [`ScheduleScanTrigger`](../triggers/UrlScannerWriteTrigger.md) |
| Task(s) | [`ScanURLTask`](../tasks/UrlScannerWriteTask.md) |
| Workflow | [`UrlScannerWriteWorkflow`](../workflows/UrlScannerWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Submit -> Scan -> Analyze -> Score -> Flag/Report
