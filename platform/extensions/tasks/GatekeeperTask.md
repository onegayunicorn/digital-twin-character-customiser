# Task: GatekeeperTask

> Capability #145 — **Gatekeeper**

Atomic executable unit(s) for this capability.

### Task: CheckClaimsTask

```typescript
// task: CheckClaimsTask
const CheckClaimsTaskSpec: TaskSpecification = {
  taskId: 'CheckClaimsTask',
  operationRef: 'GatekeeperProtocol',
  inputSchema: { capability: 'Gatekeeper' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CheckClaimsTask

### Task: CheckAclTask

```typescript
// task: CheckAclTask
const CheckAclTaskSpec: TaskSpecification = {
  taskId: 'CheckAclTask',
  operationRef: 'GatekeeperProtocol',
  inputSchema: { capability: 'Gatekeeper' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CheckAclTask

## Related artifacts
- [Protocol](../protocols/GatekeeperProtocol.md) · [Trigger(s)](../triggers/GatekeeperTrigger.md) · [Workflow](../workflows/GatekeeperWorkflow.md)
