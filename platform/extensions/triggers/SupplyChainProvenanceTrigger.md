# Trigger: SupplyChainProvenanceTrigger

> Capability #161 — **Supply Chain Provenance**

Event source(s) that initiate execution for this capability.

### Trigger: UnitSerialisedTrigger

```typescript
// trigger: UnitSerialisedTrigger
const UnitSerialisedTriggerContract: TriggerContract = {
  triggerId: 'UnitSerialisedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for UnitSerialisedTrigger' },
  actionTarget: 'SerialiseUnitTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: CustodyEventTrigger

```typescript
// trigger: CustodyEventTrigger
const CustodyEventTriggerContract: TriggerContract = {
  triggerId: 'CustodyEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CustodyEventTrigger' },
  actionTarget: 'SerialiseUnitTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/SupplyChainProvenanceProtocol.md) · [Tasks](../tasks/SupplyChainProvenanceTask.md) · [Workflow](../workflows/SupplyChainProvenanceWorkflow.md)
