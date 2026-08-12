# Task: L4DdosManagedRulesetWriteTask

> Capability #49 — **L4 DDoS Managed Ruleset Write**

Atomic executable unit(s) for this capability.

### Task: DeployL4DDoSRulesetTask

```typescript
// task: DeployL4DDoSRulesetTask
const DeployL4DDoSRulesetTaskSpec: TaskSpecification = {
  taskId: 'DeployL4DDoSRulesetTask',
  operationRef: 'L4DdosManagedRulesetWriteProtocol',
  inputSchema: { capability: 'L4 DDoS Managed Ruleset Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DeployL4DDoSRulesetTask

## Related artifacts
- [Protocol](../protocols/L4DdosManagedRulesetWriteProtocol.md) · [Trigger(s)](../triggers/L4DdosManagedRulesetWriteTrigger.md) · [Workflow](../workflows/L4DdosManagedRulesetWriteWorkflow.md)
