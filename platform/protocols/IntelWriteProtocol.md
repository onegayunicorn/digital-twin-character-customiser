# Protocol: IntelWriteProtocol

> Capability #96 — **Intel Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Threat feeds, IOCs, domain/IP reputation, and signatures.

## Interface contract
```typescript
// protocol: IntelWriteProtocol
interface IntelWriteProtocol extends BaseOperation {
  id: string;
  name: 'Intel Write';
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
| Trigger(s) | [`IntelFeedUpdatedTrigger`](../triggers/IntelWriteTrigger.md) |
| Task(s) | [`UpdateThreatIntelTask`](../tasks/IntelWriteTask.md) |
| Workflow | [`IntelWriteWorkflow`](../workflows/IntelWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Fetch -> Process -> Enrich -> Deploy -> Block/Alert
