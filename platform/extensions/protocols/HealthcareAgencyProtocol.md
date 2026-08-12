# Protocol: HealthcareAgencyProtocol

> Capability #143 — **Healthcare Agency** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Hospital/doctor/researcher agent roster for medtech operations: triage, case review, literature matching, and audit-logged decision support.

## Interface contract
```typescript
// protocol: HealthcareAgencyProtocol
interface HealthcareAgencyProtocol extends BaseOperation {
  id: string;
  name: 'Healthcare Agency';
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
| Trigger(s) | [`AgencyRequestTrigger`](../triggers/HealthcareAgencyTrigger.md), [`AuditTrigger`](../triggers/HealthcareAgencyTrigger.md) |
| Task(s) | [`DispatchAgencyAgentTask`](../tasks/HealthcareAgencyTask.md), [`AuditHealthcareActionTask`](../tasks/HealthcareAgencyTask.md) |
| Workflow | [`HealthcareAgencyWorkflow`](../workflows/HealthcareAgencyWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Dispatch -> Execute -> Guardrail check -> Audit -> Report
