# Task: McpPortalsWriteTask

> Capability #29 — **MCP Portals Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureMCPPortalTask

```typescript
// task: ConfigureMCPPortalTask
const ConfigureMCPPortalTaskSpec: TaskSpecification = {
  taskId: 'ConfigureMCPPortalTask',
  operationRef: 'McpPortalsWriteProtocol',
  inputSchema: { capability: 'MCP Portals Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureMCPPortalTask

## Related artifacts
- [Protocol](../protocols/McpPortalsWriteProtocol.md) · [Trigger(s)](../triggers/McpPortalsWriteTrigger.md) · [Workflow](../workflows/McpPortalsWriteWorkflow.md)
