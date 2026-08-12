# Protocol: CasbWriteProtocol

> Capability #120 — **CASB Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
SaaS app connectors, data policies, DLP, and access controls for CASB.

## Interface contract
```typescript
// protocol: CasbWriteProtocol
interface CasbWriteProtocol extends BaseOperation {
  id: string;
  name: 'CASB Write';
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
| Trigger(s) | [`CASBConfigUpdatedTrigger`](../triggers/CasbWriteTrigger.md) |
| Task(s) | [`ConfigureCASBIntegrationTask`](../tasks/CasbWriteTask.md) |
| Workflow | [`CasbWriteWorkflow`](../workflows/CasbWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Connect SaaS -> Scan -> Apply policies -> Monitor -> Remediate
