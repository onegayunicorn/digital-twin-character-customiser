# Protocol: SovereignKernelProtocol

> Capability #154 — **Sovereign Kernel** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Twelve shared primitives (identity, trust, policy, permissions, ledger, events, payments, contracts, compliance, audit, ai-agents, interoperability) used by every vertical.

## Interface contract
```typescript
// protocol: SovereignKernelProtocol
interface SovereignKernelProtocol extends BaseOperation {
  id: string;
  name: 'Sovereign Kernel';
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
| Trigger(s) | [`PrimitiveAttachedTrigger`](../triggers/SovereignKernelTrigger.md) |
| Task(s) | [`RegisterPrimitiveTask`](../tasks/SovereignKernelTask.md), [`AttachPrimitiveTask`](../tasks/SovereignKernelTask.md) |
| Workflow | [`SovereignKernelWorkflow`](../workflows/SovereignKernelWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Attach -> Health check -> Report
