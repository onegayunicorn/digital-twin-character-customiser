# Workflow: EmailRoutingAccountRulesReadWorkflow

> Capability #75 — **Email Routing Account Rules Read**

## Definition
```typescript
// workflow: EmailRoutingAccountRulesReadWorkflow
const EmailRoutingAccountRulesReadWorkflow: WorkflowDefinition = {
  workflowId: 'EmailRoutingAccountRulesReadWorkflow',
  version: '1.0.0',
  description: 'Email Routing Account Rules Read — List -> Validate -> Audit -> Report',
  trigger: { triggerId: 'EmailRoutingConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'List'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
List -> Validate -> Audit -> Report

## Related artifacts
- [Protocol](../protocols/EmailRoutingAccountRulesReadProtocol.md) · [Trigger(s)](../triggers/EmailRoutingAccountRulesReadTrigger.md) · [Tasks](../tasks/EmailRoutingAccountRulesReadTask.md)
