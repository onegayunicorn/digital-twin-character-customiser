# Protocol: L4DdosManagedRulesetWriteProtocol

> Capability #49 — **L4 DDoS Managed Ruleset Write** · Domain: Security & Edge · Access: `write`

## Purpose
Packet filtering, flood protection, and anomaly detection for L4 DDoS rulesets.

## Interface contract
```typescript
// protocol: L4DdosManagedRulesetWriteProtocol
interface L4DdosManagedRulesetWriteProtocol extends BaseOperation {
  id: string;
  name: 'L4 DDoS Managed Ruleset Write';
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
| Trigger(s) | [`L4DDoSRulesetUpdatedTrigger`](../triggers/L4DdosManagedRulesetWriteTrigger.md) |
| Task(s) | [`DeployL4DDoSRulesetTask`](../tasks/L4DdosManagedRulesetWriteTask.md) |
| Workflow | [`L4DdosManagedRulesetWriteWorkflow`](../workflows/L4DdosManagedRulesetWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select -> Tune -> Deploy -> Monitor -> Adjust
