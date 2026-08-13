# Task: NfcEscrowTask

> Capability #162 — **NFC Escrow**

Atomic executable unit(s) for this capability.

### Task: TapHoldTask

```typescript
// task: TapHoldTask
const TapHoldTaskSpec: TaskSpecification = {
  taskId: 'TapHoldTask',
  operationRef: 'NfcEscrowProtocol',
  inputSchema: { capability: 'NFC Escrow' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute TapHoldTask

### Task: ReleaseOrRefundTask

```typescript
// task: ReleaseOrRefundTask
const ReleaseOrRefundTaskSpec: TaskSpecification = {
  taskId: 'ReleaseOrRefundTask',
  operationRef: 'NfcEscrowProtocol',
  inputSchema: { capability: 'NFC Escrow' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReleaseOrRefundTask

## Related artifacts
- [Protocol](../protocols/NfcEscrowProtocol.md) · [Trigger(s)](../triggers/NfcEscrowTrigger.md) · [Workflow](../workflows/NfcEscrowWorkflow.md)
