# Task: DnsFirewallWriteTask

> Capability #31 — **DNS Firewall Write**

Atomic executable unit(s) for this capability.

### Task: ManageDNSFirewallRuleTask

```typescript
// task: ManageDNSFirewallRuleTask
const ManageDNSFirewallRuleTaskSpec: TaskSpecification = {
  taskId: 'ManageDNSFirewallRuleTask',
  operationRef: 'DnsFirewallWriteProtocol',
  inputSchema: { capability: 'DNS Firewall Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageDNSFirewallRuleTask

## Related artifacts
- [Protocol](../protocols/DnsFirewallWriteProtocol.md) · [Trigger(s)](../triggers/DnsFirewallWriteTrigger.md) · [Workflow](../workflows/DnsFirewallWriteWorkflow.md)
