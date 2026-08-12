# Protocol: DexWriteProtocol

> Capability #127 — **DEX Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Digital experience monitoring, synthetic tests, and real-user monitoring.

## Interface contract
```typescript
// protocol: DexWriteProtocol
interface DexWriteProtocol extends BaseOperation {
  id: string;
  name: 'DEX Write';
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
| Trigger(s) | [`DEXTestTrigger`](../triggers/DexWriteTrigger.md) |
| Task(s) | [`ConfigureDEXTestTask`](../tasks/DexWriteTask.md) |
| Workflow | [`DexWriteWorkflow`](../workflows/DexWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define tests -> Deploy -> Collect -> Analyze -> Alert -> Report
