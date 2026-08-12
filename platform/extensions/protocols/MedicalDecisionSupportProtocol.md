# Protocol: MedicalDecisionSupportProtocol

> Capability #138 — **Medical Decision Support** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Healthcare agency agents (hospital triage, doctor case review, researcher matching) — decision-support only, never autonomous treatment; every output carries clinical_claim_level=none.

## Interface contract
```typescript
// protocol: MedicalDecisionSupportProtocol
interface MedicalDecisionSupportProtocol extends BaseOperation {
  id: string;
  name: 'Medical Decision Support';
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
| Trigger(s) | [`VitalsReceivedTrigger`](../triggers/MedicalDecisionSupportTrigger.md), [`CaseSubmittedTrigger`](../triggers/MedicalDecisionSupportTrigger.md) |
| Task(s) | [`RunTriageTask`](../tasks/MedicalDecisionSupportTask.md), [`ReviewCaseTask`](../tasks/MedicalDecisionSupportTask.md), [`MatchLiteratureTask`](../tasks/MedicalDecisionSupportTask.md) |
| Workflow | [`MedicalDecisionSupportWorkflow`](../workflows/MedicalDecisionSupportWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Ingest -> Score -> Present -> Log -> Escalate
