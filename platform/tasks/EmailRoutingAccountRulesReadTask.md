# Task: EmailRoutingAccountRulesReadTask

> Capability #75 — **Email Routing Account Rules Read**

Atomic executable unit(s) for this capability.

### Task: ReadEmailRoutingRuleTask

```typescript
// task: ReadEmailRoutingRuleTask
const ReadEmailRoutingRuleTaskSpec: TaskSpecification = {
  taskId: 'ReadEmailRoutingRuleTask',
  operationRef: 'EmailRoutingAccountRulesReadProtocol',
  inputSchema: { capability: 'Email Routing Account Rules Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadEmailRoutingRuleTask

## Related artifacts
- [Protocol](../protocols/EmailRoutingAccountRulesReadProtocol.md) · [Trigger(s)](../triggers/EmailRoutingAccountRulesReadTrigger.md) · [Workflow](../workflows/EmailRoutingAccountRulesReadWorkflow.md)
