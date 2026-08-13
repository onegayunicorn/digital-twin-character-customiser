# Trigger: IdentityPqcSigningTrigger

> Capability #163 — **Identity & PQC Signing**

Event source(s) that initiate execution for this capability.

### Trigger: DidVerifiedTrigger

```typescript
// trigger: DidVerifiedTrigger
const DidVerifiedTriggerContract: TriggerContract = {
  triggerId: 'DidVerifiedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DidVerifiedTrigger' },
  actionTarget: 'CreateDidTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: KnoxAttestedTrigger

```typescript
// trigger: KnoxAttestedTrigger
const KnoxAttestedTriggerContract: TriggerContract = {
  triggerId: 'KnoxAttestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for KnoxAttestedTrigger' },
  actionTarget: 'CreateDidTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IdentityPqcSigningProtocol.md) · [Tasks](../tasks/IdentityPqcSigningTask.md) · [Workflow](../workflows/IdentityPqcSigningWorkflow.md)
