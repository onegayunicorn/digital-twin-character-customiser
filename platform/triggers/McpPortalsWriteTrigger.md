# Trigger: McpPortalsWriteTrigger

> Capability #29 — **MCP Portals Write**

Event source(s) that initiate execution for this capability.

### Trigger: PortalConfigUpdatedTrigger

```typescript
// trigger: PortalConfigUpdatedTrigger
const PortalConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'PortalConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PortalConfigUpdatedTrigger' },
  actionTarget: 'ConfigureMCPPortalTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/McpPortalsWriteProtocol.md) · [Tasks](../tasks/McpPortalsWriteTask.md) · [Workflow](../workflows/McpPortalsWriteWorkflow.md)
