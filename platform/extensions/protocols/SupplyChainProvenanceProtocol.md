# Protocol: SupplyChainProvenanceProtocol

> Capability #161 — **Supply Chain Provenance** · Domain: Access & Zero Trust · Access: `write`

## Purpose
SKU registry, serialisation, batch tracking, chain-of-custody with hash chaining.

## Interface contract
```typescript
// protocol: SupplyChainProvenanceProtocol
interface SupplyChainProvenanceProtocol extends BaseOperation {
  id: string;
  name: 'Supply Chain Provenance';
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
| Trigger(s) | [`UnitSerialisedTrigger`](../triggers/SupplyChainProvenanceTrigger.md), [`CustodyEventTrigger`](../triggers/SupplyChainProvenanceTrigger.md) |
| Task(s) | [`SerialiseUnitTask`](../tasks/SupplyChainProvenanceTask.md), [`AppendCustodyEventTask`](../tasks/SupplyChainProvenanceTask.md) |
| Workflow | [`SupplyChainProvenanceWorkflow`](../workflows/SupplyChainProvenanceWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register SKU -> Serialise -> Track -> Verify chain -> Report
