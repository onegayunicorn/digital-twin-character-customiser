# Protocol: ComplianceOsProtocol

> Capability #156 — **Compliance OS** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Regulatory capability gates (jurisdiction -> classification -> registration -> AML -> KYC -> monitoring -> travel rule -> sanctions -> records -> evaluation -> ENABLE/BLOCK) with evidence log.

## Interface contract
```typescript
// protocol: ComplianceOsProtocol
interface ComplianceOsProtocol extends BaseOperation {
  id: string;
  name: 'Compliance OS';
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
| Trigger(s) | [`FeatureEnableRequestTrigger`](../triggers/ComplianceOsTrigger.md) |
| Task(s) | [`RunGateChainTask`](../tasks/ComplianceOsTask.md), [`LogComplianceEvidenceTask`](../tasks/ComplianceOsTask.md) |
| Workflow | [`ComplianceOsWorkflow`](../workflows/ComplianceOsWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Gate chain -> Evidence -> Allow/Block -> Audit
