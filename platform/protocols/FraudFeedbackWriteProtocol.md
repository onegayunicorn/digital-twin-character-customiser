# Protocol: FraudFeedbackWriteProtocol

> Capability #46 — **Fraud Feedback Write** · Domain: Security & Edge · Access: `write`

## Purpose
Labels, corrections, and model retraining loop for fraud feedback.

## Interface contract
```typescript
// protocol: FraudFeedbackWriteProtocol
interface FraudFeedbackWriteProtocol extends BaseOperation {
  id: string;
  name: 'Fraud Feedback Write';
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
| Trigger(s) | [`FraudFeedbackSubmittedTrigger`](../triggers/FraudFeedbackWriteTrigger.md) |
| Task(s) | [`SubmitFraudFeedbackTask`](../tasks/FraudFeedbackWriteTask.md) |
| Workflow | [`FraudFeedbackWriteWorkflow`](../workflows/FraudFeedbackWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Accept -> Validate -> Store -> Retrain model -> Update rules
