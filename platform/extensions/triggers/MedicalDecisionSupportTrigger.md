# Trigger: MedicalDecisionSupportTrigger

> Capability #138 — **Medical Decision Support**

Event source(s) that initiate execution for this capability.

### Trigger: VitalsReceivedTrigger

```typescript
// trigger: VitalsReceivedTrigger
const VitalsReceivedTriggerContract: TriggerContract = {
  triggerId: 'VitalsReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for VitalsReceivedTrigger' },
  actionTarget: 'RunTriageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: CaseSubmittedTrigger

```typescript
// trigger: CaseSubmittedTrigger
const CaseSubmittedTriggerContract: TriggerContract = {
  triggerId: 'CaseSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CaseSubmittedTrigger' },
  actionTarget: 'RunTriageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MedicalDecisionSupportProtocol.md) · [Tasks](../tasks/MedicalDecisionSupportTask.md) · [Workflow](../workflows/MedicalDecisionSupportWorkflow.md)
