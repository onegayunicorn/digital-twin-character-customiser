# Trigger: RegistrarDomainsAdminTrigger

> Capability #33 — **Registrar Domains Admin**

Event source(s) that initiate execution for this capability.

### Trigger: DomainEventTrigger

```typescript
// trigger: DomainEventTrigger
const DomainEventTriggerContract: TriggerContract = {
  triggerId: 'DomainEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DomainEventTrigger' },
  actionTarget: 'ManageDomainTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ExpiryWarningTrigger

```typescript
// trigger: ExpiryWarningTrigger
const ExpiryWarningTriggerContract: TriggerContract = {
  triggerId: 'ExpiryWarningTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ExpiryWarningTrigger' },
  actionTarget: 'ManageDomainTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/RegistrarDomainsAdminProtocol.md) · [Tasks](../tasks/RegistrarDomainsAdminTask.md) · [Workflow](../workflows/RegistrarDomainsAdminWorkflow.md)
