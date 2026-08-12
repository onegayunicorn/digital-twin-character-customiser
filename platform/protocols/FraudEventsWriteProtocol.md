# Protocol: FraudEventsWriteProtocol

> Capability #45 — **Fraud Events Write** · Domain: Security & Edge · Access: `write`

## Purpose
Event schema, risk scoring, detection rules, and thresholds for fraud events.

## Interface contract
```typescript
// protocol: FraudEventsWriteProtocol
interface FraudEventsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Fraud Events Write';
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
| Trigger(s) | [`FraudEventDetectedTrigger`](../triggers/FraudEventsWriteTrigger.md) |
| Task(s) | [`LogFraudEventTask`](../tasks/FraudEventsWriteTask.md), [`ScoreFraudRiskTask`](../tasks/FraudEventsWriteTask.md) |
| Workflow | [`FraudEventsWriteWorkflow`](../workflows/FraudEventsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Collect -> Score -> Flag -> Action -> Report
