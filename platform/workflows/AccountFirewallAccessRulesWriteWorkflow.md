# Workflow: AccountFirewallAccessRulesWriteWorkflow

> Capability #36 — **Account Firewall Access Rules Write**

## Definition
```typescript
// workflow: AccountFirewallAccessRulesWriteWorkflow
const AccountFirewallAccessRulesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountFirewallAccessRulesWriteWorkflow',
  version: '1.0.0',
  description: 'Account Firewall Access Rules Write — Define -> Validate -> Order -> Apply -> Test',
  trigger: { triggerId: 'FirewallRuleChangeTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Order'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Apply'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define -> Validate -> Order -> Apply -> Test

## Related artifacts
- [Protocol](../protocols/AccountFirewallAccessRulesWriteProtocol.md) · [Trigger(s)](../triggers/AccountFirewallAccessRulesWriteTrigger.md) · [Tasks](../tasks/AccountFirewallAccessRulesWriteTask.md)
