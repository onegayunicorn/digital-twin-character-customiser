# Protocol: NfcEscrowProtocol

> Capability #162 — **NFC Escrow** · Domain: Access & Zero Trust · Access: `write`

## Purpose
NFC-tap conditional settlement bridge: tap -> hold -> verify condition -> release/refund (nfc-escrow-bridge integration).

## Interface contract
```typescript
// protocol: NfcEscrowProtocol
interface NfcEscrowProtocol extends BaseOperation {
  id: string;
  name: 'NFC Escrow';
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
| Trigger(s) | [`NfcTapTrigger`](../triggers/NfcEscrowTrigger.md), [`ConditionVerifiedTrigger`](../triggers/NfcEscrowTrigger.md) |
| Task(s) | [`TapHoldTask`](../tasks/NfcEscrowTask.md), [`ReleaseOrRefundTask`](../tasks/NfcEscrowTask.md) |
| Workflow | [`NfcEscrowWorkflow`](../workflows/NfcEscrowWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Tap -> Hold -> Verify -> Release/Refund -> Audit
