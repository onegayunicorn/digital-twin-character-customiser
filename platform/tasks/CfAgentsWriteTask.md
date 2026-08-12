# Task: CfAgentsWriteTask

> Capability #2 — **CF Agents Write**

Atomic executable unit(s) for this capability.

### Task: ProvisionUpdateAgentTask

```typescript
// task: ProvisionUpdateAgentTask
const ProvisionUpdateAgentTaskSpec: TaskSpecification = {
  taskId: 'ProvisionUpdateAgentTask',
  operationRef: 'CfAgentsWriteProtocol',
  inputSchema: { capability: 'CF Agents Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ProvisionUpdateAgentTask

## Related artifacts
- [Protocol](../protocols/CfAgentsWriteProtocol.md) · [Trigger(s)](../triggers/CfAgentsWriteTrigger.md) · [Workflow](../workflows/CfAgentsWriteWorkflow.md)
