# Protocol: FieldExtractorsWriteProtocol

> Capability #44 — **Field Extractors Write** · Domain: Security & Edge · Access: `write`

## Purpose
Regex, JSON, XPath, request/response fields, and transforms for field extraction.

## Interface contract
```typescript
// protocol: FieldExtractorsWriteProtocol
interface FieldExtractorsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Field Extractors Write';
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
| Trigger(s) | [`ExtractorConfigTrigger`](../triggers/FieldExtractorsWriteTrigger.md) |
| Task(s) | [`CreateFieldExtractorTask`](../tasks/FieldExtractorsWriteTask.md) |
| Workflow | [`FieldExtractorsWriteWorkflow`](../workflows/FieldExtractorsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define pattern -> Test -> Attach to rule -> Deploy
