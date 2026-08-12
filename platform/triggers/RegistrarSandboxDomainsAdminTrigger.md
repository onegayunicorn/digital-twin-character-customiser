# Trigger: RegistrarSandboxDomainsAdminTrigger

> Capability #34 — **Registrar Sandbox Domains Admin**

Event source(s) that initiate execution for this capability.

### Trigger: SandboxDomainCreatedTrigger

```typescript
// trigger: SandboxDomainCreatedTrigger
const SandboxDomainCreatedTriggerContract: TriggerContract = {
  triggerId: 'SandboxDomainCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SandboxDomainCreatedTrigger' },
  actionTarget: 'ProvisionSandboxDomainTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/RegistrarSandboxDomainsAdminProtocol.md) · [Tasks](../tasks/RegistrarSandboxDomainsAdminTask.md) · [Workflow](../workflows/RegistrarSandboxDomainsAdminWorkflow.md)
