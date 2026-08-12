# Task: AccountFirewallAccessRulesWriteTask

> Capability #36 — **Account Firewall Access Rules Write**

Atomic executable unit(s) for this capability.

### Task: CreateFirewallRuleTask

```typescript
// task: CreateFirewallRuleTask
const CreateFirewallRuleTaskSpec: TaskSpecification = {
  taskId: 'CreateFirewallRuleTask',
  operationRef: 'AccountFirewallAccessRulesWriteProtocol',
  inputSchema: { capability: 'Account Firewall Access Rules Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CreateFirewallRuleTask

## Related artifacts
- [Protocol](../protocols/AccountFirewallAccessRulesWriteProtocol.md) · [Trigger(s)](../triggers/AccountFirewallAccessRulesWriteTrigger.md) · [Workflow](../workflows/AccountFirewallAccessRulesWriteWorkflow.md)
