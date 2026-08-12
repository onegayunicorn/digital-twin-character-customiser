# Trigger: HealthcareAgencyTrigger

> Capability #143 — **Healthcare Agency**

Event source(s) that initiate execution for this capability.

### Trigger: AgencyRequestTrigger

```typescript
// trigger: AgencyRequestTrigger
const AgencyRequestTriggerContract: TriggerContract = {
  triggerId: 'AgencyRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AgencyRequestTrigger' },
  actionTarget: 'DispatchAgencyAgentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AuditTrigger

```typescript
// trigger: AuditTrigger
const AuditTriggerContract: TriggerContract = {
  triggerId: 'AuditTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AuditTrigger' },
  actionTarget: 'DispatchAgencyAgentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/HealthcareAgencyProtocol.md) · [Tasks](../tasks/HealthcareAgencyTask.md) · [Workflow](../workflows/HealthcareAgencyWorkflow.md)
