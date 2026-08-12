# Trigger: CfAgentsWriteTrigger

> Capability #2 — **CF Agents Write**

Event source(s) that initiate execution for this capability.

### Trigger: AgentDeploymentTrigger

```typescript
// trigger: AgentDeploymentTrigger
const AgentDeploymentTriggerContract: TriggerContract = {
  triggerId: 'AgentDeploymentTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AgentDeploymentTrigger' },
  actionTarget: 'ProvisionUpdateAgentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AgentConfigChangeTrigger

```typescript
// trigger: AgentConfigChangeTrigger
const AgentConfigChangeTriggerContract: TriggerContract = {
  triggerId: 'AgentConfigChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AgentConfigChangeTrigger' },
  actionTarget: 'ProvisionUpdateAgentTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CfAgentsWriteProtocol.md) · [Tasks](../tasks/CfAgentsWriteTask.md) · [Workflow](../workflows/CfAgentsWriteWorkflow.md)
