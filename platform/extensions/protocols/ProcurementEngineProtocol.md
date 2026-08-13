# Protocol: ProcurementEngineProtocol

> Capability #158 — **Procurement Engine** · Domain: Access & Zero Trust · Access: `write`

## Purpose
RFQ/RFP/tender, bid evaluation (value-for-money), three-way matching (PO/GRN/invoice) with rules engine.

## Interface contract
```typescript
// protocol: ProcurementEngineProtocol
interface ProcurementEngineProtocol extends BaseOperation {
  id: string;
  name: 'Procurement Engine';
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
| Trigger(s) | [`TenderOpenedTrigger`](../triggers/ProcurementEngineTrigger.md), [`InvoiceSubmittedTrigger`](../triggers/ProcurementEngineTrigger.md) |
| Task(s) | [`EvaluateBidsTask`](../tasks/ProcurementEngineTask.md), [`ThreeWayMatchTask`](../tasks/ProcurementEngineTask.md) |
| Workflow | [`ProcurementEngineWorkflow`](../workflows/ProcurementEngineWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Tender -> Bids -> Evaluate -> PO -> GRN -> Invoice -> Match -> Pay
